# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np

list_1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
list_2 = [2, 4, 6, 8, 10, 9, 8, 7, 6, 5]
array_1 = np.array(list_1)
array_2 = np.array(list_2)
plt.figure()
plt.plot(array_1, array_2, color='r', label='test')
# plt.plot(list_1, list_2, color='r', label='test')   直接放入列表也可绘图
plt.plot(array_2, array_1, ls=':', color='b', label='test2')  # ls代表线类型，：为虚线，默认是实线
plt.legend()  # 显示右上角label标志，可调label位置
plt.xlabel("X")
plt.ylabel("Y")
plt.title("test_demo")
plt.show()
