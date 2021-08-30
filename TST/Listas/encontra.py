n = int(input())
nums = [int(num) for num in input().split()]
verif = 'não'
for i in range(len(nums)):
    if n == nums[i]:
        verif = 'sim'
print(verif)
