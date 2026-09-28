"""
715. Range Module
Difficulty: Hard
https://leetcode.com/problems/range-module/

──────────────────────────────────────────────────

A Range Module is a module that tracks ranges of numbers. Design a
data structure to track the ranges represented as half-open intervals
and query about them.

A half-open interval [left, right) denotes all the real numbers x
where left <= x < right.

Implement the RangeModule class:

	• RangeModule() Initializes the object of the data structure.

• void addRange(int left, int right) Adds the half-open interval
[left, right), tracking every real number in that interval. Adding an
interval that partially overlaps with currently tracked numbers should
add any numbers in the interval [left, right) that are not already
tracked.

• boolean queryRange(int left, int right) Returns true if every real
number in the interval [left, right) is currently being tracked, and
false otherwise.

• void removeRange(int left, int right) Stops tracking every real
number currently being tracked in the half-open interval [left,
right).

 

Example 1:

Input
["RangeModule", "addRange", "removeRange", "queryRange",
"queryRange", "queryRange"]
[[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
Output
[null, null, null, true, false, true]

Explanation
RangeModule rangeModule = new RangeModule();
rangeModule.addRange(10, 20);
rangeModule.removeRange(14, 16);
rangeModule.queryRange(10, 14); // return True,(Every number in [10,
14) is being tracked)
rangeModule.queryRange(13, 15); // return False,(Numbers like 14,
14.03, 14.17 in [13, 15) are not being tracked)
rangeModule.queryRange(16, 17); // return True, (The number 16 in
[16, 17) is still being tracked, despite the remove operation)

 

Constraints:

	• 1 <= left < right <= 10^9

• At most 10^4 calls will be made to addRange, queryRange, and
removeRange.
"""

class RangeModule:

    def __init__(self):
        self.intervals = []

    def addRange(self, left: int, right: int) -> None:
        merged = []
        placed = False
        for start, end in self.intervals:
            if end < left:
                merged.append([start, end])
            elif start > right:
                if not placed:
                    merged.append([left, right])
                    placed = True
                merged.append([start, end])
            else:
                left = min(left, start)
                right = max(right, end)
        if not placed:
            merged.append([left, right])
        self.intervals = merged

    def queryRange(self, left: int, right: int) -> bool:
        for start, end in self.intervals:
            if start <= left and right <= end:
                return True
            if start > left:
                break
        return False

    def removeRange(self, left: int, right: int) -> None:
        merged = []
        for start, end in self.intervals:
            if end <= left or start >= right:
                merged.append([start, end])
            else:
                if start < left:
                    merged.append([start, left])
                if end > right:
                    merged.append([right, end])
        self.intervals = merged


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
