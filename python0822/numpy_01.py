

import numpy as np

# 创建一维数组
# arr1 = np.array([1, 2, 3, 4])
#
# print(type(arr1))
# print(arr1)
# print(arr1.shape)   # 查看是几喂数组
# print(arr1.dtype)
#
# arr2 = np.array(['1', 3, 4, 5])
# print(arr2)
d=np.array([[10,11,12],[20,21,22],[30,31,32]])
# print(d)
# print(d.ndim)

# 创建二维数组
arr3 = np.array(((1,2,3),(5,6,7)))
# print(arr3)
# print(arr3.shape)   # 查看数组的长度
# print(arr3.ndim)   # 查看是几维的数组


# 其他方法创建数组
# zeros()函数可以创建全0数组
# ones()函数可以创建全1数组
# empty()函数可以创建空数组


arr17 = np.zeros(5)    # 创建全0的1维数组
# print(arr3)
# print(arr3.dtype)

arr4 = np.zeros((3, 4), dtype='int32')   # 创建一个全0的2维3行4列的数组
# print(arr4)
# print(arr4.ndim)
# arr40=np.zeros([1,2,3],dtype='int32')
# print(arr40)
# print(arr40.ndim)

arr5 = np.ones(5)   # 创建全1的1维数组
# print(arr5)

arr6 = np.ones((2, 3, 5), dtype='int32')   # 创建一个全1的2维2行3列的数组
# print(arr6)


# 创建一个等差数组
arr7 = np.arange(5, 10, 2)
# print(arr7)
# 创建一个等分数组
arr8 = np.arange(0, 8, 2).reshape(2, 2)
# print(arr8)

# 对角线创建
arr9 = np.eye(8, 5)
# print(arr9.ndim)
# print(arr9)


# 数组的运算/比较
# 同尺寸
arr01 = np.array([1, 2, 3, 4])
arr02 = np.array([4, 5, 6, 7])
# print(arr01*5)
# print(arr01<arr02)

# 不同尺寸
arr03 = np.array(((0,0,0),(1,1,1),(2,2,2),(3,3,3),(4,4,4)))
# print(arr03)
arr04 = np.array((0,1,2,3))
# print(arr04)
arr05 =np.array((0,1,2,5))


arr06 = np.add(arr05,arr04)
print(arr06)

