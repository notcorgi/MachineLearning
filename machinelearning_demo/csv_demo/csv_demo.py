import pandas as pd
import numpy as np

path = r"C:\Users\lishubin\Desktop\文本\twitter数据处理\final.csv"
csv_data = pd.read_csv(path, usecols=[1, 2], header=0)  # 读取csv文件，usecols为列索引号,header为列名所在行号
print("原始数据\n", csv_data.head(10))  # 显示前十行
print(type(csv_data['time']), type(np.array(csv_data['time'])))  # 输出单列的数据，可以转换为数组类型
print('---------------------------------------------')
dataarray = csv_data.head(10).values  # 矩阵转化为数组类型
print(dataarray, '数据类型是：', type(dataarray))
print('--------------------------------------------\n', '转化为矩阵类型:')
dataframe = pd.DataFrame(dataarray, columns=["用户id", "时间"])  # 转化为矩阵，指定列名
dataframe['标签'] = ['1', '2', '3', '4', '5', '6', '7']   # 添加一列，加入矩阵中
print(dataframe, '数据类型是:', type(dataframe))
dataframe.to_csv('test.csv', mode='a', index=False,
                 header=False)  # index=False去掉行号，写入csv文件,mode='a'追加写，header=False为省略表名（用于追加）
