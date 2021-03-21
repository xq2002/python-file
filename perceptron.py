# coding: utf-8
import numpy as np
from sklearn import datasets  # 导入scikit-learn库
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler  # 标准化工具

breast_cancer_data = datasets.load_breast_cancer()
features = breast_cancer_data.data  # 特征
targets = breast_cancer_data.target  # 类别

scaler = StandardScaler()
features = scaler.fit_transform(features)

train_X, test_X, train_y, test_y = train_test_split(features, targets, test_size=0.3, random_state=5)#数据集划分训练和测试数据

w0 = []  # 初始化w0
for i in range(30):
    w0.append(0)
w0 = np.array(w0)
num = 1
b0 = 0  # 初始化b0
m = 0.1  # 学习率
tag = 0  # 判断是否已经进行完训练
while 1:
    tag = 0
    for a, b in zip(train_X, train_y):
        if b == 0:
            b = -1
        if (a @ w0 + b0) * b <= 0:
            num = num + 1
            tag = 1
            w0 = w0 + m * b * a
            b0 = b0 + m * b
    if num > 5000:  # 限制迭代次数
        break
    if tag == 0:
        break

print(w0)
print(b0)
right = 0
for a, b in zip(test_X, test_y):
    if b == 0:
        b = -1
    if (a @ w0 + b0) * b > 0:
        right = right + 1

print("正确率：", right/len(test_X))


