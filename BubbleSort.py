# _*_ coding utf-8 _*_
# @Time    : 2018/09/05 0005 20:50
# @Author  : pyx
# @File    : BubbleSort.py
'''
冒泡排序
1.外层循环负责帮忙递减内存循环的次数【len-1,1】
2.内层循环负责前后两两比较，index的取值范围【0，len-2】
'''
def bubble_sort(nums):
    for i in range(1,len(nums)-1):
        # [0,len-1-i]
        for j in range(len(nums)-i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums
if __name__ == '__main__':
    nums = [2,6,8,5,1,4,9,3,7]
    bubble_sort(nums)
    print('result:',nums)



