#include <algorithm>
#include <string>
#include <unordered_set>
#include <vector>

using namespace std;

namespace {
struct FastSet {
    vector<unsigned __int128> t;
    vector<size_t> used;
    size_t mask;
    size_t count;

    FastSet() : t((size_t)1 << 20, 0), mask(((size_t)1 << 20) - 1), count(0) {}

    static size_t h(unsigned __int128 x) {
        unsigned long long lo = (unsigned long long)x;
        unsigned long long hi = (unsigned long long)(x >> 64);
        unsigned long long v = lo ^ (hi * 0x9e3779b97f4a7c15ULL);
        v ^= v >> 33;
        v *= 0xff51afd7ed558ccdULL;
        v ^= v >> 29;
        return (size_t)v;
    }

    void clear() {
        for (size_t i : used) t[i] = 0;
        used.clear();
        count = 0;
    }

    void rehash() {
        vector<unsigned __int128> old;
        old.swap(t);
        t.assign(old.size() * 2, 0);
        mask = t.size() - 1;
        used.clear();
        for (unsigned __int128 x : old) {
            if (!x) continue;
            size_t i = h(x) & mask;
            while (t[i]) i = (i + 1) & mask;
            t[i] = x;
            used.push_back(i);
        }
    }

    bool insert(unsigned __int128 x) {
        if ((count + 1) * 10 >= t.size() * 7) rehash();
        size_t i = h(x) & mask;
        while (t[i]) {
            if (t[i] == x) return false;
            i = (i + 1) & mask;
        }
        t[i] = x;
        used.push_back(i);
        ++count;
        return true;
    }
};
}

class Solution {
public:
    int findMinStep(string board, string hand) {
        unsigned char tbl[256];
        for (int i = 0; i < 256; ++i) tbl[i] = 255;
        unsigned char next_digit = 0;
        vector<char> palette;
        for (char c : board) {
            if (tbl[(unsigned char)c] == 255) {
                tbl[(unsigned char)c] = (unsigned char)next_digit++;
                palette.push_back(c);
            }
        }
        for (char c : hand) {
            if (tbl[(unsigned char)c] == 255) {
                tbl[(unsigned char)c] = (unsigned char)next_digit++;
                palette.push_back(c);
            }
        }

        auto board_code = [&](const string &s) -> unsigned __int128 {
            unsigned __int128 code = 1;
            for (char c : s) code = (code << 3) | tbl[(unsigned char)c];
            return code;
        };

        shrink(board);
        sort(hand.begin(), hand.end());

        int hcnt0[8] = {0};
        for (char c : hand) hcnt0[tbl[(unsigned char)c]]++;
        unsigned __int128 hid0 = 0;
        for (int i = 0; i < 8; ++i) hid0 += (unsigned __int128)hcnt0[i] << (3 * i);

        static FastSet seen;
        seen.clear();
        vector<unsigned __int128> level;
        level.push_back((board_code(board) << 15) | hid0);
        seen.insert(level[0]);

        string b, h;
        for (int steps = 0; !level.empty(); ++steps) {
            vector<unsigned __int128> next;
            next.reserve(1u << 12);
            for (unsigned __int128 state : level) {
                unsigned __int128 code0 = state >> 15;
                unsigned __int128 hid = state & 0x7FFFULL;

                b.clear();
                {
                    unsigned __int128 v = code0;
                    int len = 0;
                    while (v > 1) {
                        v >>= 3;
                        ++len;
                    }
                    b.resize(len);
                    v = code0;
                    for (int i = len - 1; i >= 0; --i) {
                        b[i] = palette[(size_t)(v & 7)];
                        v >>= 3;
                    }
                }
                if (b.empty()) return steps;
                h.clear();
                for (int i = 0; i < 8; ++i) {
                    int cnt = (int)((hid >> (3 * i)) & 7);
                    for (int j = 0; j < cnt; ++j) h.push_back(palette[i]);
                }
                sort(h.begin(), h.end());

                int bcnt[8] = {0};
                for (char c : b) bcnt[tbl[(unsigned char)c]]++;
                int hcnt[8] = {0};
                for (char c : h) hcnt[tbl[(unsigned char)c]]++;

                bool dead = false;
                for (char c : b) {
                    unsigned char d = tbl[(unsigned char)c];
                    if (bcnt[d] + hcnt[d] < 3) {
                        dead = true;
                        break;
                    }
                }
                if (dead) continue;

                int n = (int)b.size();
                int dg[32];
                unsigned __int128 pre[33], suf[33];
                pre[0] = 1;
                for (int i = 0; i < n; ++i) {
                    dg[i] = tbl[(unsigned char)b[i]];
                    pre[i + 1] = (pre[i] << 3) | (unsigned)dg[i];
                }
                suf[n] = 0;
                for (int i = n - 1; i >= 0; --i) {
                    suf[i] = suf[i + 1] | ((unsigned __int128)(unsigned)dg[i] << (3 * (n - 1 - i)));
                }

                for (size_t i = 0; i < h.size(); ++i) {
                    if (i && h[i] == h[i - 1]) continue;
                    char c = h[i];
                    unsigned char cd = tbl[(unsigned char)c];
                    if (!bcnt[cd] && hcnt[cd] < 3) continue;
                    unsigned __int128 nhid = hid - ((unsigned __int128)1 << (3 * cd));

                    for (int p = 0; p <= n; ++p) {
                        if (p > 0 && b[p - 1] == c) continue;
                        unsigned __int128 code;
                        if (p + 1 < n && b[p] == c && b[p + 1] == c) {
                            string cand;
                            cand.reserve(n + 1);
                            cand.assign(b, 0, p);
                            cand.push_back(c);
                            cand.append(b, p, n - p);
                            shrink(cand);
                            if (cand == b) continue;
                            code = board_code(cand);
                        } else {
                            code = (pre[p] << (3 * (n - p + 1))) |
                                   ((unsigned __int128)(unsigned)cd << (3 * (n - p))) |
                                   suf[p];
                        }
                        if (nhid == 0 && code != 1) continue;
                        unsigned __int128 key = (code << 15) | nhid;
                        if (seen.insert(key)) next.push_back(key);
                    }
                }
            }
            level.swap(next);
        }
        return -1;
    }

private:
    static void shrink(string &s) {
        for (;;) {
            string out;
            size_t n = s.size(), i = 0;
            while (i < n) {
                size_t j = i;
                while (j < n && s[j] == s[i]) ++j;
                if (j - i < 3) out.append(s, i, j - i);
                i = j;
            }
            if (out == s || out.empty()) {
                s = out;
                return;
            }
            s = out;
        }
    }
};

#ifdef LOCAL_TEST
#include <chrono>
#include <cstdio>
#include <utility>

int main() {
    struct Case {
        const char *board;
        const char *hand;
        int want;
    };
    Case cases[] = {
        {"WRRBBW", "RB", -1},
        {"WWRRBBWW", "WRBRW", 2},
        {"RBYYBBRRB", "YRBGB", 3},
        {"RRWWRRBBRR", "WB", 2},
        {"RRGGBBYYWWRRGGBB", "RGBYW", -1},
        {"RRYGGYYRRYYGGYRR", "GGBBB", 5},
        {"G", "GGGGG", 2},
        {"GWRBGYWGWGWYGRYW", "BRGGW", -1},
        {"YYRGWRBYGGBGBGWY", "BWGRY", -1},
        {"WWRBBWWGGBBRRGWB", "WGGBB", -1},
    };
    bool ok = true;
    double total = 0.0;
    for (auto &c : cases) {
        Solution sol;
        auto t0 = std::chrono::steady_clock::now();
        int got = sol.findMinStep(c.board, c.hand);
        auto t1 = std::chrono::steady_clock::now();
        double ms = std::chrono::duration<double, std::milli>(t1 - t0).count();
        total += ms;
        bool good = got == c.want;
        ok = ok && good;
        printf("%s %-18s %-6s -> %d (%.0f ms)\n", good ? "OK " : "FAIL", c.board, c.hand, got, ms);
    }
    printf("%s | total %.0f ms\n", ok ? "ALL OK" : "SOME FAILED", total);
    return ok ? 0 : 1;
}
#endif
