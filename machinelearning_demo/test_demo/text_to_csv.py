import os
import re
import pandas as pd

root = r"C:\Users\lishubin\Desktop\文本\第一阶段\database.mpqa.3.0\docs"
contentlist = []
dirlist = []
for file in os.listdir(root):
    if re.match(r"^\d", file):
        dirpath = os.path.join(root, file)
        for file in os.listdir(dirpath):
            filepath = os.path.join(dirpath, file)
            with open(filepath, "r") as f:
                data = f.read()
                # print('---------------' + filepath + '-----------------')
                contentlist.append(data)
                dirlist.append(filepath)

dataframe = pd.DataFrame(dirlist, columns=["filepath"])
dataframe["content"] = contentlist
dataframe.to_csv('test.csv', mode='w', index=False)
