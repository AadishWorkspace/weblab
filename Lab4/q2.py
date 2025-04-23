class PairFinder:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
    
    def find_pair(self):
        num_map = {}
        for i, num in enumerate(self.nums):
            complement = self.target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return None  # Return None if no pair is found

# Get user input
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Enter target sum: "))

finder = PairFinder(nums, target)
result = finder.find_pair()
print("Pair indices:", result if result else "No pair found")
