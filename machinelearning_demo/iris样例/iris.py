from sklearn import datasets  # 引入数据集,sklearn包含众多数据集
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split  # 将数据分为测试集和训练集
from sklearn.neighbors import KNeighborsClassifier  # 利用邻近点方式训练数据
from sklearn import preprocessing as pre
from sklearn.preprocessing import StandardScaler
import numpy as np

###引入数据###
# iris = datasets.load_iris()  # 引入iris鸢尾花数据,iris数据包含4个特征变量
# iris_X = iris.data  # 特征变量
# iris_y = iris.target  # 标签值
# print("+++++++++++++++++++++++++++++++++++")
iris_X = np.array(
    [[1, 2, 3], [1, 2, 2], [2, 1, 3], [1, 3, 2], [2, 3, 2], [1, 2, 3], [3, 2, 1], [1, 2, 3], [1, 2, 1],
     [3, 2, 1]])  # 原始数据10*3特征
iris_y = np.array([1, 1, 2, 3, 1, 1, 2, 3, 2, 1])  # 十个标签
print("开始数据预处理\n+++++++++++++++++++++++++++++++++++")
x_binary = pre.binarize(iris_X, threshold=1.5)  # 数据预处理，数据2值化，阈值为1.5
print(x_binary)
print("+++++++++++++++++++++++++++++++++++")
x_scale = pre.scale(iris_X)  # 数据预处理 使得数据的均值维0，方差为1
print(x_scale, '\n', x_scale.std(axis=1), '\n', x_scale.shape, '\n', type(x_scale))
print("+++++++++++++++++++++++++++++++++++")
x_standard_scale = StandardScaler()  # 创建标准化转换对象
x_standard_scale.fit(iris_X)  # 用于计算训练数据的均值和方差， 后面就会用均值和方差来转换训练数据
x_traffic_feature = x_standard_scale.transform(iris_X)  # 转换数据集,把训练数据转换成标准的正态分布
print(x_traffic_feature)
print("+++++++++++++++++++++++++++++++++++")
X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y,
                                                    test_size=0.3)  # 利用train_test_split进行将训练集和测试集进行分开，test_size占30%
###训练数据###
knn = KNeighborsClassifier()  # 引入训练方法
knn.fit(X_train, y_train)  # 进行填充测试数据进行训练
###预测数据###
pre = knn.predict(X_test)  # 预测的标签
print(accuracy_score(pre, y_test))
print("+++++++++++++++++++++++++++++++++++")
conf_mat = confusion_matrix(y_test, pre)
print(conf_mat)
print("+++++++++++++++++++++++++++++++++++")
print(classification_report(y_test, pre))
