class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            # Skip duplicate outer values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Optimization 1: Smallest possible sum with nums[i]
            min_sum = nums[i] + nums[i + 1] + nums[i + 2]
            if min_sum > target:
                if abs(min_sum - target) < abs(closest_sum - target):
                    closest_sum = min_sum
                # Any subsequent i will produce an even larger sum, so we can break early
                break

            # Optimization 2: Largest possible sum with nums[i]
            max_sum = nums[i] + nums[-2] + nums[-1]
            if max_sum < target:
                if abs(max_sum - target) < abs(closest_sum - target):
                    closest_sum = max_sum
                # No triplet starting with this nums[i] can get closer than max_sum
                continue

            # Standard two-pointer search
            left, right = i + 1, n - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                # Exact match found; impossible to get closer
                if curr_sum == target:
                    return target

                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum

                if curr_sum < target:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return closest_sum