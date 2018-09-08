# _*_ coding utf-8 _*_
# @Time    : 2018/09/08 0008 9:44
# @Author  : pyx
# @File    : QuickSort.py

def quick_sort(nums, start, end):
    i = start
    j = end
    key = nums[i]
    # 结束排序
    if i >= j:
        return
    # 一次排序
    while i < j:
        # 从后向前，把小于key的数放在key的左边
        while i < j and nums[j] >= key:
            j -= 1
        nums[i] = nums[j]
        # 从前向后，把大于key的数放在key的右边
        while i < j and nums[i] < key:
            i += 1
        nums[j] = nums[i]
    nums[i] = key
    # 左排序
    quick_sort(nums, start, i - 1)
    # 右排序
    quick_sort(nums, i + 1, end)


if __name__ == '__main__':
    nums = [2, 6, 8, 5, 1, 4, 9, 3, 7]
    quick_sort(nums, 0, len(nums) - 1)
    print('result:', nums)
