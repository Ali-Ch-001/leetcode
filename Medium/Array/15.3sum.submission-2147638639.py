class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        counts = collections.Counter(nums)
        
        # Partition numbers into unique sorted negative and positive lists
        neg = sorted([x for x in counts if x < 0])
        pos = sorted([x for x in counts if x > 0])
        neg_set = set(neg)
        pos_set = set(pos)

        # Case 1: Three zeros [0, 0, 0]
        if counts[0] >= 3:
            res.append([0, 0, 0])

        # Case 2: One zero, one negative, one positive [-x, 0, x]
        if counts[0] >= 1:
            for x in pos:
                if -x in neg_set:
                    res.append([-x, 0, x])

        # Case 3: Two negatives, one positive (n1 + n2 + pos = 0)
        for i, n1 in enumerate(neg):
            # Duplicate negative: [n1, n1, -(2*n1)]
            if counts[n1] >= 2 and -(2 * n1) in pos_set:
                res.append([n1, n1, -(2 * n1)])
            # Distinct negatives
            for j in range(i + 1, len(neg)):
                n2 = neg[j]
                target = -(n1 + n2)
                if target in pos_set:
                    res.append([n1, n2, target])

        # Case 4: Two positives, one negative (neg + p1 + p2 = 0)
        for i, p1 in enumerate(pos):
            # Duplicate positive: [-(2*p1), p1, p1]
            if counts[p1] >= 2 and -(2 * p1) in neg_set:
                res.append([-(2 * p1), p1, p1])
            # Distinct positives
            for j in range(i + 1, len(pos)):
                p2 = pos[j]
                target = -(p1 + p2)
                if target in neg_set:
                    res.append([target, p1, p2])

        return res