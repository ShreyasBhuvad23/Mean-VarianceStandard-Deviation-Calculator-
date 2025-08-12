import math

def calculate_stats(numbers):
    n = len(numbers)
    mean = sum(numbers) / n
    variance = sum((x - mean) ** 2 for x in numbers) / n
    stddev = math.sqrt(variance)
    return mean, variance, stddev

if __name__ == "__main__":
    input_str = input("Enter numbers separated by spaces: ")
    numbers = list(map(float, input_str.strip().split()))
    mean, variance, stddev = calculate_stats(numbers)
    print(f"Mean: {mean}")
    print(f"Variance: {variance}")
    print(f"Standard Deviation: {stddev}")