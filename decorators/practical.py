# Speed test practical
from time import time

def speedDecorator(func):

    def wrapper(nums):

        start = time()
        func(nums)
        end = time()

        print(f"Execution time: {end - start}")

    return wrapper

@speedDecorator
def sumNumbers(nums):
    sum = 0
    for num in nums:
        sum += num

    print(f"Sum is :{sum}")


sumNumbers(list(range(1,2000000)))