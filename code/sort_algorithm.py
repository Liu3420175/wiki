def maopao_sort(nums):
    """冒泡算法
   冒泡排序只会操作相邻的两个数据。每次冒泡操作都会对相邻的两个元素进行比较，看是否满足大小关系要求。如果不满足就让它俩互换。
   一次冒泡会让至少一个元素移动到它应该在的位置，重复 n 次，就完成了 n 个数据的排序工作
    """
    length = len(nums)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j+1], nums[j]


def charu_sort(nums):
    """
    插入算法
    数组中的数据分为两个区间，已排序区间和未排序区间。初始已排序区间只有一个元素，就是数组的第一个元素。
    插入算法的核心思想是取未排序区间中的元素，在已排序区间中找到合适的插入位置将其插入，并保证已排序区间数据一直有序。
    重复这个过程，直到未排序区间中元素为空，算法结束。
    """
    length = len(nums)
    for i in range(1, length):
        for j in range(i, 0, -1):
            if nums[j] < nums[j -1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
            else:
                break

def xuanzhe_sort(nums):
    """
    选择排序
    选择排序算法的实现思路有点类似插入排序，也分已排序区间和未排序区间。但是选择排序每次会从未排序区间中找到最小的元素，将其放到已排序区间的末尾。
    
    """
    length = len(nums)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if nums[j] < nums[min_index]:
                min_index = j
        if i != min_index:
            nums[i], nums[min_index] = nums[min_index], nums[i]


    


if __name__ == '__main__':
    a = random.sample(range(1000), 10)
    print(a)
    xuanzhe_sort(a)
    print(a)
