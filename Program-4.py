def count_multiples(nums):
    result = {i: 0 for i in range(1, 10)}
    for num in nums:
        for i in range(1, 10):
            if num % i == 0:
                result[i] += 1
    print(result)

# Example
count_multiples([1,2,8,9,12,46,76,82,15,20,30])
