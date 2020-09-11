import pandas as pd
from nltk import word_tokenize, pos_tag, sent_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string

from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer


def read_data(data_path):
    csv_data = pd.read_csv(data_path, usecols=[1], header=0)  # 读取csv文件，usecols为列索引号,header为列名所在行号
    data_array = csv_data.values
    print(data_array.shape, type(data_array))
    return data_array


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


def preprocess(data_array):
    list = []
    for sentence in data_array:
        # print(data)
        sentence = " ".join(sentence)
        sentence = sentence.lower()  # 转化为小写
        # tokens2 = sent_tokenize(sentence)  # 按句分词样例,按句分词一定要在去标点前，否则句号将被去掉
        # print("按句分词样例：", tokens2)
        remove = str.maketrans('', '', string.punctuation)  # 引入英文标点集
        sentence = sentence.translate(remove)  # 去标点
        # print("转化为小写去标点：", sentence)
        tokens = word_tokenize(sentence)  # 分词
        # print("初步分词:", tokens)
        wordfilter = []
        stopWords = set(stopwords.words('english'))
        for w in tokens:
            if w not in stopWords:
                wordfilter.append(w)
        # print("去停用词后:", wordfilter)
        tagged_sent = pos_tag(wordfilter)  # 获取单词词性
        # print("获取词性后:", tagged_sent)

        wnl = WordNetLemmatizer()
        lemmas_sent = []
        for tag in tagged_sent:
            wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN  # 由于分词时有标点符号词性为None，故用or语句
            lemmas_sent.append(wnl.lemmatize(tag[0], pos=wordnet_pos))  # 词形还原，参数：单词，词性

        result = " ".join(lemmas_sent)
        print("最终结果：", result)  # 最终词形还原结果
        list.append(result)
    return list


def vectorization(data):
    tfidf = TfidfVectorizer()
    re = tfidf.fit_transform(data)
    print(type(re), re)
    return re, tfidf.get_feature_names()


def train(data):
    n_topics = 6
    lda = LatentDirichletAllocation(n_components=n_topics, max_iter=50,
                                    learning_method='online',
                                    learning_offset=50.,
                                    random_state=0)
    lda.fit(data)
    return lda


def print_top_words(model, feature_names, n_top_words):
    print(model.components_.shape, '\n', model.components_, '\n', feature_names, '\n', feature_names.__len__())
    print('------------')
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d:" % topic_idx)
        print(" ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))
    print()


if __name__ == '__main__':
    data_path = "test.csv"
    data_array = read_data(data_path)
    after_pre_data = preprocess(data_array)
    after_vec_data, feature_name = vectorization(after_pre_data)
    lda = train(after_vec_data)
    print_top_words(lda, feature_name, 30)
