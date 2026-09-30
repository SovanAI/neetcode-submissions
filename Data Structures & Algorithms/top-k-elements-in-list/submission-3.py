class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for i in range(k):
            max_freq = max(count.values())

            for num in count:
                if count[num] == max_freq:
                    result.append(num)
                    del count[num]
                    break

        return result