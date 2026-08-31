class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total % k != 0:
            return False

        target = total // k

        nums.sort(reverse=True)

        if nums[0] > target:
            return False

        used = [False] * len(nums)

        def backtrack(start, k, curr_sum):
            if k == 1:
                return True

            if curr_sum == target:
                return backtrack(0, k - 1, 0)

            for j in range(start, len(nums)):
                if used[j]:
                    continue

                if curr_sum + nums[j] > target:
                    continue

                # Avoid trying the same value in the same position.
                if j > start and nums[j] == nums[j - 1] and not used[j - 1]:
                    continue

                used[j] = True

                if backtrack(j + 1, k, curr_sum + nums[j]):
                    return True

                used[j] = False

            return False

        return backtrack(0, k, 0)