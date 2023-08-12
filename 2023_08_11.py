# 冒泡排序（小到大）
class Solution:
  def bubbleSort(self, arr):
        # 第 i 趟排序
        for i in range(len(arr)):
            # 从序列中前 n - i + 1 个元素的第 1 个元素开始，相邻两个元素进行比较
            for j in range(len(arr) - i - 1): # major point
                # 相邻两个元素进行比较，如果前者大于后者，则交换位置
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.bubbleSort(nums)

# 选择排序（小到大）
class Solution:
    def selectionSort(self, arr):
        for i in range(len(arr) - 1):
            # 记录未排序部分中最小值的位置
            min_i = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_i]:
                    min_i = j
            # 如果找到最小值的位置，将 i 位置上元素与最小值位置上的元素进行交换
            if i != min_i:
                arr[i], arr[min_i] = arr[min_i], arr[i]
        return arr

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.selectionSort(nums)

# 插入排序
class Solution:
    def insertionSort(self, arr):
        # 遍历无序序列
        for i in range(1, len(arr)):
            temp = arr[i]
            j = i
            # 从右至左遍历有序序列
            while j > 0 and arr[j - 1] > temp:
                # 将有序序列中插入位置右侧的元素依次右移一位
                arr[j] = arr[j - 1]
                j -= 1
            # 将该元素插入到适当位置
            arr[j] = temp

        return arr

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.insertionSort(nums)

# 归并排序
class Solution:
    def merge(self, left_arr, right_arr):           # 归并过程
        arr = []
        left_i, right_i = 0, 0
        while left_i < len(left_arr) and right_i < len(right_arr):
            # 将两个有序子序列中较小元素依次插入到结果数组中
            if left_arr[left_i] < right_arr[right_i]:
                arr.append(left_arr[left_i])
                left_i += 1
            else:
                arr.append(right_arr[right_i])
                right_i += 1
        
        while left_i < len(left_arr):
            # 如果左子序列有剩余元素，则将其插入到结果数组中
            arr.append(left_arr[left_i])
            left_i += 1
            
        while right_i < len(right_arr):
            # 如果右子序列有剩余元素，则将其插入到结果数组中
            arr.append(right_arr[right_i])
            right_i += 1
        
        return arr                                  # 返回排好序的结果数组

    def mergeSort(self, arr):                       # 分割过程
        if len(arr) <= 1:                           # 数组元素个数小于等于 1 时，直接返回原数组
            return arr
        
        mid = len(arr) // 2                         # 将数组从中间位置分为左右两个数组。
        left_arr = self.mergeSort(arr[0: mid])      # 递归将左子序列进行分割和排序
        right_arr =  self.mergeSort(arr[mid:])      # 递归将右子序列进行分割和排序
        return self.merge(left_arr, right_arr)      # 把当前序列组中有序子序列逐层向上，进行两两合并。

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)

# 希尔排序
class Solution:
    def shellSort(self, arr):
        size = len(arr)
        gap = size // 2
		# 按照 gap 分组
        while gap > 0:
            # 对每组元素进行插入排序
            for i in range(gap, size):
                # temp 为每组中无序序列第 1 个元素
                temp = arr[i]
                j = i
                # 从右至左遍历每组中的有序序列元素
                while j >= gap and arr[j - gap] > temp:
                    # 将每组有序序列中插入位置右侧的元素依次在组中右移一位
                    arr[j] = arr[j - gap]
                    j -= gap
                # 将该元素插入到适当位置
                arr[j] = temp
            # 缩小 gap 间隔
            gap = gap // 2
        return arr

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.shellSort(nums)

# 快速排序
import random

class Solution:
    # 从 arr[low: high + 1] 中随机挑选一个基准数，并进行移动排序
    def randomPartition(self, arr: [int], low: int, high: int):
        # 随机挑选一个基准数
        i = random.randint(low, high)
        # 将基准数与最低位互换
        arr[i], arr[low] = arr[low], arr[i]
        # 以最低位为基准数，然后将序列中比基准数大的元素移动到基准数右侧，比他小的元素移动到基准数左侧。最后将基准数放到正确位置上
        return self.partition(arr, low, high)
    
    # 以最低位为基准数，然后将序列中比基准数大的元素移动到基准数右侧，比他小的元素移动到基准数左侧。最后将基准数放到正确位置上
    def partition(self, arr: [int], low: int, high: int):
        pivot = arr[low]            # 以第 1 为为基准数
        i = low + 1                 # 从基准数后 1 位开始遍历，保证位置 i 之前的元素都小于基准数
        
        for j in range(i, high + 1):
            # 发现一个小于基准数的元素
            if arr[j] < pivot:
                # 将小于基准数的元素 arr[j] 与当前 arr[i] 进行换位，保证位置 i 之前的元素都小于基准数
                arr[i], arr[j] = arr[j], arr[i]
                # i 之前的元素都小于基准数，所以 i 向右移动一位
                i += 1
        # 将基准节点放到正确位置上
        arr[i - 1], arr[low] = arr[low], arr[i - 1]
        # 返回基准数位置
        return i - 1

    def quickSort(self, arr, low, high):
        if low < high:
            # 按照基准数的位置，将序列划分为左右两个子序列
            pi = self.randomPartition(arr, low, high)
            # 对左右两个子序列分别进行递归快速排序
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)

        return arr

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quickSort(nums, 0, len(nums) - 1)
