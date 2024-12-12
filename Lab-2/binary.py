def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        
        if arr[mid] == x:
            return mid
        
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        
        else:
            return binary_search(arr, mid + 1, high, x)
    
    return -1
def test_binary_search(self):
    for unsorted_list, sorted_list in self.test_data:
        sorted_list = sorted(unsorted_list)
        for element in sorted_list:
            index = binary_search(sorted_list, 0, len(sorted_list) - 1, element)
            self.assertEqual(sorted_list[index], element)
