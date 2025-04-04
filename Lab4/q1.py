class SubsetGenerator:
    def __init__(self, nums):
        self.nums = nums
    
    def get_subsets(self):
        result = [[]]
        for num in self.nums:
            result += [subset + [num] for subset in result]
        return result

# Example usage:
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
generator = SubsetGenerator(nums)
print(generator.get_subsets())
