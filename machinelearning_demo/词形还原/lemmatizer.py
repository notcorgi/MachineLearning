from nltk import word_tokenize, pos_tag, sent_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk


# 对数据进行清洗，并放入TF-IDF模型

# 第一次运行需要下载这些包
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('punkt')
# 获取单词的词性
def get_wordnet_pos(tag):  # 变换表示形式使lemmatize（）函数能够识别词性参数  对应关系：https://www.jianshu.com/p/79255fe0c5b5
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None


sentence = 'New York #is a (family family) of team sports that involve. To varying degrees, kicking a ball to score a goal.'
sentence = sentence.lower()  # 转化为小写
# tokens2 = sent_tokenize(sentence)  # 按句分词样例,按句分词一定要在去标点前，否则句号将被去掉
# print("按句分词样例：", tokens2)
remove = str.maketrans('', '', string.punctuation)  # 引入英文标点集
sentence = sentence.translate(remove)  # 去标点
print("转化为小写去标点：", sentence)
tokens = word_tokenize(sentence)  # 分词
print("初步分词:", tokens)
wordfilter = []
stopWords = set(stopwords.words('english'))
for w in tokens:
    if w not in stopWords:
        wordfilter.append(w)
print("去停用词后:", wordfilter)
tagged_sent = pos_tag(wordfilter)  # 获取单词词性
print("获取词性后:", tagged_sent)

wnl = WordNetLemmatizer()
lemmas_sent = []
for tag in tagged_sent:
    wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN  # 由于分词时有标点符号词性为None，故用or语句
    lemmas_sent.append(wnl.lemmatize(tag[0], pos=wordnet_pos))  # 词形还原，参数：单词，词性

print("最终结果：", lemmas_sent)  # 最终词形还原结果
result = " ".join(lemmas_sent)
print(result)  # 将最终结果合并为不含标点，不含停用词，纯小写，词形还原的纯净的字符串
print('----------------------------------------')
list = []
list.append(result)  # 字符串转为列表形式
tfidf = TfidfVectorizer()
re = tfidf.fit_transform(list)
print(type(re), '\n',re)
re = re.toarray()  # 将结果转化为矩阵形式
print(type(re), '\n', re)
print(tfidf.get_feature_names())  # 获取各个特征的名字
