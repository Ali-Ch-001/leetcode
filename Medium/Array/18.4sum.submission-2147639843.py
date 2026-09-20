class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        if n < 4:
            return res

        for i in range(n - 3):
            # Skip duplicate first values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Pruning 1: Smallest possible sum starting with nums[i] exceeds target
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break

            # Pruning 2: Largest possible sum starting with nums[i] cannot reach target
            if nums[i] + nums[-3] + nums[-2] + nums[-1] < target:
                continue

            for j in range(i + 1, n - 2):
                # Skip duplicate second values
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Pruning 3: Smallest sum with nums[i] and nums[j] exceeds target
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break

                # Pruning 4: Largest sum with nums[i] and nums[j] cannot reach target
                if nums[i] + nums[j] + nums[-2] + nums[-1] < target:
                    continue

                # Two-pointer sweep for the final two elements
                left, right = j + 1, n - 1
                remain = target - nums[i] - nums[j]

                while left < right:
                    two_sum = nums[left] + nums[right]
                    if two_sum == remain:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif two_sum < remain:
                        left += 1
                    else:
                        right -= 1

        return res