# LeetCode Solutions

My LeetCode solutions, collected and re-synced to my current account.

**Profile:** https://leetcode.com/u/Ali01Ch/

## A note on the submission history

I've been solving LeetCode problems for years — first on an old account
whose password I lost. Since I couldn't recover it, I re-uploaded all of
those solutions to this new account so everything lives in one place and
nothing gets lost again.

That's why the submission history here is concentrated into just 1–2 days:
it's years of old work being synced at once, not new activity. The
solutions themselves are years of my own work from the old account, just
re-submitted in bulk during the migration.

## What's in here

Solutions are organized by difficulty and category (`Easy/`, `Medium/`,
`Hard/`), with one file per problem.

- `1.two-sum.submission-1293151396.py` — an accepted submission synced
  from my old account (the ID comes from the original submission).
- `20.valid-parentheses.py` — my current solution for the problem.

## Tooling

Problems are fetched, tested, and submitted with
[`@night-slayer18/leetcode-cli`](https://www.npmjs.com/package/@night-slayer18/leetcode-cli),
using Python 3 by default.

```bash
leetcode config -l python3 -w /Users/alich/Downloads/leetcode
leetcode login          # once; needs LEETCODE_SESSION + csrftoken from the browser
```

| Command                 | What it does                                |
| ----------------------- | ------------------------------------------- |
| `leetcode daily`        | Show today's challenge                      |
| `leetcode list -d easy` | Browse problems by difficulty               |
| `leetcode pick 1`       | Create the solution file for problem 1      |
| `leetcode show 1`       | Print the problem statement                 |
| `leetcode test 1`       | Run sample test cases against your solution |
| `leetcode submit 1`     | Submit to LeetCode                          |
| `leetcode reset 1`      | Restore the original stub (start over)      |
| `leetcode stat`         | Progress stats                              |

`test` and `submit` accept a problem ID, a filename, or a path, e.g.
`leetcode test ./Easy/Array/1.two-sum.py`.

## Notes

- Config lives in `~/.leetcode/workspaces/default/config.json`.
- `leetcode config -e "code"` sets VS Code as the editor for `leetcode pick`.
