nums = [1,1,1,2,2,3]
numeros = {}
for i in range(len(nums)):
    numeros[nums[i]] = 1 + numeros.get(nums[i], 0)
print(nums[1])
print(nums[2])
print(nums[3])