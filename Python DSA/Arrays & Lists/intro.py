# Various array methods in python
nums = [1, 2, 3, 4, 5, 6, 7, 8]

# 1. Print array
print(len(nums))

# 2. Indexing array
nums[0]
nums[5]
nums[-2]
nums[-7]

# 3. Slicing
nums[1:5]
nums[:4]
nums[2:]
nums[::2]
nums[:]
nums[::-1]

# 4. Iterating
for x in nums:
    print(x)

for i in range(len(nums)):
    print(nums[i])

for i, x in enumerate(nums):
    print(i, x)

# 5. Other Array functions
nums.append(10)
nums.pop()
nums.insert(0, 9)
nums.insert(i, 8)
nums.remove(8)
nums.index(i)
nums + [2, 3]
nums.sort()
sorted(nums)
nums.copy()

# theres so much more