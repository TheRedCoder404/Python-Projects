class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        countI = 0
        countX = 0
        solution = []

        for i in nums:
            for x in nums:
                if i + x == target and not countI == countX:
                    solution.append(countI)
                    solution.append(countX)
                    break
                countX += 1
            if solution:
                break
            countI += 1
            countX = 0
        return solution
