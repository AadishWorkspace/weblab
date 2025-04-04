import math

def calculate_statistics(numbers):
    n = len(numbers)
    if n == 0:
        print("No numbers entered. Exiting.")
        return
    
    mean = sum(numbers) / n
    variance = 0
    for x in numbers:
        variance += (x - mean) ** 2
    variance = variance / n

    std_dev = math.sqrt(variance)
    
    print(f"Mean: {mean:.2f}")
    print(f"Variance: {variance:.2f}")
    print(f"Standard Deviation: {std_dev:.2f}")

# Read input
try:
    N = int(input("Enter the number of elements: "))
    numbers = []
    for i in range(N):
        num = float(input(f"Enter number {i+1}: "))
        numbers.append(num)

    calculate_statistics(numbers)
except ValueError:
    print("Invalid input. Please enter numeric values.")
