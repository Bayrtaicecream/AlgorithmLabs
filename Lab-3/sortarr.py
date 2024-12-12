class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:

        return self.merge_sort(nums)

    def merge_sort(self, arr: list[int]) -> list[int]:
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left_half = self.merge_sort(arr[:mid])
        right_half = self.merge_sort(arr[mid:])
        
        return self.merge(left_half, right_half)
        
    def merge(self, left: list[int], right: list[int]) -> list[int]:
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result