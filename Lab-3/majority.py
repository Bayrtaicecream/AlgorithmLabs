class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        # counts = {}
        # for num in nums:
        #     counts[num] = counts.get(num, 0) + 1
        #     if counts[num] > len(nums) // 2:
        #         return num
        return self.get_most_frequent_value(nums)[0]
    
    def merge_counts(self, left_counts, right_counts):
        merged_counts = {}
        for key in left_counts:
            if key in merged_counts:
                merged_counts[key] += left_counts[key]
            else:
                merged_counts[key] = left_counts[key]
        for key in right_counts:
            if key in merged_counts:
                merged_counts[key] += right_counts[key]
            else:
                merged_counts[key] = right_counts[key]
        
        return merged_counts

    def find_most_frequent(self, arr):
        if len(arr) == 1:
            return {arr[0]: 1}
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        left_counts = self.find_most_frequent(left_half)
        right_counts = self.find_most_frequent(right_half)
        combined_counts = self.merge_counts(left_counts, right_counts)
        
        return combined_counts

    def get_most_frequent_value(self, arr):
        counts = self.find_most_frequent(arr)
        most_frequent_value = None
        max_count = 0
        
        for key, value in counts.items():
            if value > max_count:
                most_frequent_value = key
                max_count = value
        
        return most_frequent_value, max_count