
import time


def time_it(func):
    print("FOUR")


    def wrapper(*args, **kwargs):
        print("FIVE")
        start = time.time()
        print("Starting Timing")
        print("SIX")
        print(nums[1])
        func(*args, **kwargs)
        print("SEVEN")
        end = time.time()
        print("End Timing")
        print("EIGHT")
        print("It took " + str(end - start) + " seconds")
        print("NINE")
    return wrapper
    print("TEN")


nums = range(1, 1000000)


@time_it
def squared(nums):
    print("ONE")
    result = []
    print("TWO")
    for num in nums:
        result.append(num * num)
    print("squared finished!")
    print("THREE")
    print('what')


squared(nums)
