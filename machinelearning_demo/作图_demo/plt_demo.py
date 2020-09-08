# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np

list_1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
array_1 = np.array(list_1)
array_2 = np.sin(array_1)
plt.figure()
# 建立 subplot 网格，高为 2，宽为 1
# 激活第一个 subplot
plt.subplot(2, 2, 1)
plt.plot(array_1, array_2, linestyle='--', marker='*', color='r', label='test')  # ls代表线类型，：为虚线，默认是实线
# plt.plot(list_1, list_2, color='r', label='test')   直接放入列表也可绘图
plt.plot(array_2, array_1, linestyle=':', marker='v', color='b', label='test2')  # ls代表线类型，：为虚线，默认是实线
plt.legend()  # 显示右上角label标志，可调label位置
plt.xlabel("X")
plt.ylabel("Y")
plt.title("test_demo")
# plt.show()   若有多个图，在最后只有一个show（）函数即可


print('-------------------------------')
# 将第二个 subplot 激活，并绘制第二个图像
plt.subplot(2, 2, 2)
x = [5, 8, 10]
y = [12, 16, 6]
x2 = [6, 9, 11]
y2 = [6, 15, 7]
plt.bar(x, y, color='r', align='center', label='test1')  # 条形的中心 “center”,"lege"边缘
plt.bar(x2, y2, color='g', align='center', label='test2')
plt.title('Bar graph')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()

print('-------------------------------')
plt.subplot(2, 2, 3)
plt.scatter(array_1, array_2, color='y', label="test1")
plt.xlabel("X")  # 设置横坐标
plt.ylabel("Y")
plt.legend()
plt.show()
