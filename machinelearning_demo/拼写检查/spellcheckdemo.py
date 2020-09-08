import enchant
from enchant.checker import SpellChecker  # 对长文本进行拼写检查

d = enchant.Dict('en_US')  # 指定语言
print(d.check("helo"))  # 对指定单词拼写检查
print(d.suggest("helloo"))  #对错误单词的推想
print(d.check("hello"))
print(d.tag)  #指定的语言
print('--------------------------------------')
chkr = SpellChecker("en_US")
chkr.set_text("This is sme sample txt with erors.")
for err in chkr:
    print("error:", err.word)
