# 从数组 nums 中读取下标为 i 的数据元素值
def value(nums, i):
    if 0 <= i <= len(nums) - 1:
        print(nums[i])


arr = [0, 5, 2, 3, 7, 1, 6]
value(arr, 3)

# 从数组 nums 中查找元素值为 val 的数据元素第一次出现的位置
def find(nums, val):
    for i in range(len(nums)):
        if nums[i] == val:
            return i
    return -1

arr = [0, 5, 2, 3, 7, 1, 6]
print(find(arr, 5))

# append尾部插入
arr = [0, 5, 2, 3, 7, 1, 6]
val = 4
arr.append(val)
print(arr)

# insert插入
arr = [0, 5, 2, 3, 7, 1, 6]
i, val = 2, 4
arr.insert(i, val)
print(arr)


# change更改元素
def change(nums, i, val):
    if 0 <= i <= len(nums) - 1:
        nums[i] = val
        
arr = [0, 5, 2, 3, 7, 1, 6]
i, val = 2, 4
change(arr, i, val)
print(arr)

# pop删除
arr = [0, 5, 2, 3, 7, 1, 6]
arr.pop()
print(arr)

# pop指定删除
arr = [0, 5, 2, 3, 7, 1, 6]
i = 3
arr.pop(i)
print(arr)

# remove删除指定元素
arr = [0, 5, 2, 3, 7, 1, 6]
i = 3
arr.remove(5)
print(arr)



