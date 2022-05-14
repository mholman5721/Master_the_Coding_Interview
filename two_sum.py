# given:
nums = [0, 3, 4, 2, 7, 8]
target = 10

# find indices of the two numbers such that they add up to target

def two_sum1(nums, target):

    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j

    return -1, -1

def two_sum2(nums, target):
    compliments = {}

    for i in range(0, len(nums)):
        compliment = target - nums[i]
        if compliment in compliments:
            return i, compliments[compliment]
        else:
            compliments[nums[i]] = i

    return -1, -1

ind1, ind2 = two_sum1(nums, target)

print(ind1, ind2)

ind1, ind2 = two_sum2(nums, target)

print(ind1, ind2)