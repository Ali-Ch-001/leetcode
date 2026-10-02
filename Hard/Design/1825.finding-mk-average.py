"""
1825. Finding MK Average
Difficulty: Hard
https://leetcode.com/problems/finding-mk-average/

──────────────────────────────────────────────────

You are given two integers, m and k, and a stream of integers. You
are tasked to implement a data structure that calculates the MKAverage
for the stream.

The MKAverage can be calculated using these steps:

• If the number of the elements in the stream is less than m you
should consider the MKAverage to be -1. Otherwise, copy the last m
elements of the stream to a separate container.

• Remove the smallest k elements and the largest k elements from the
container.

• Calculate the average value for the rest of the elements rounded
down to the nearest integer.

Implement the MKAverage class:

• MKAverage(int m, int k) Initializes the MKAverage object with an
empty stream and the two integers m and k.

	• void addElement(int num) Inserts a new element num into the stream.

• int calculateMKAverage() Calculates and returns the MKAverage for
the current stream rounded down to the nearest integer.

 

Example 1:

Input
["MKAverage", "addElement", "addElement", "calculateMKAverage",
"addElement", "calculateMKAverage", "addElement", "addElement",
"addElement", "calculateMKAverage"]
[[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]
Output
[null, null, null, -1, null, 3, null, null, null, 5]

Explanation
MKAverage obj = new MKAverage(3, 1); 
obj.addElement(3);        // current elements are [3]
obj.addElement(1);        // current elements are [3,1]
obj.calculateMKAverage(); // return -1, because m = 3 and only 2
elements exist.
obj.addElement(10);       // current elements are [3,1,10]
obj.calculateMKAverage(); // The last 3 elements are [3,1,10].
// After removing smallest and largest 1
element the container will be [3].
// The average of [3] equals 3/1 = 3,
return 3
obj.addElement(5);        // current elements are [3,1,10,5]
obj.addElement(5);        // current elements are [3,1,10,5,5]
obj.addElement(5);        // current elements are [3,1,10,5,5,5]
obj.calculateMKAverage(); // The last 3 elements are [5,5,5].
// After removing smallest and largest 1
element the container will be [5].
// The average of [5] equals 5/1 = 5,
return 5

 

Constraints:

	• 3 <= m <= 10^5

	• 1 < k*2 < m

	• 1 <= num <= 10^5

• At most 10^5 calls will be made to addElement and
calculateMKAverage.
"""

class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.n = 100001
        self.cnt = [0] * (self.n + 1)
        self.sm = [0] * (self.n + 1)
        self.q = []
        self.head = 0
        self.total = 0

    def _add(self, i, dc, ds):
        n = self.n
        while i <= n:
            self.cnt[i] += dc
            self.sm[i] += ds
            i += i & (-i)

    def _kth(self, k):
        idx = 0
        bit = 1 << 20
        while bit:
            nxt = idx + bit
            if nxt <= self.n and self.cnt[nxt] < k:
                idx = nxt
                k -= self.cnt[nxt]
            bit >>= 1
        return idx + 1

    def _prefix(self, i):
        c = s = 0
        while i > 0:
            c += self.cnt[i]
            s += self.sm[i]
            i -= i & (-i)
        return c, s

    def _sum_smallest(self, t):
        if t <= 0:
            return 0
        v = self._kth(t)
        c, s = self._prefix(v - 1)
        return s + (t - c) * v

    def addElement(self, num: int) -> None:
        self.q.append(num)
        self.total += num
        self._add(num, 1, num)
        if len(self.q) - self.head > self.m:
            old = self.q[self.head]
            self.head += 1
            self.total -= old
            self._add(old, -1, -old)

    def calculateMKAverage(self) -> int:
        if len(self.q) - self.head < self.m:
            return -1
        lo = self._sum_smallest(self.k)
        hi = self._sum_smallest(self.m - self.k)
        return (hi - lo) // (self.m - 2 * self.k)


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
