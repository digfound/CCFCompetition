#encoding=utf-8
import jieba
import jieba.analyse
import jieba.posseg as pseg
import csv

TrainingDataSetPath = "E:\PycharmProjects\PythonProject\SubjectBasedEmotionalAnalysis\CCFCompetition\Data\TrainingData\TrainingDataSet.csv"
csv_reader = csv.reader(open(TrainingDataSetPath,encoding='gb18030'))
wordlist = []
for row in csv_reader:
    if(len(row[2]) != 0):
        list = []
        list = row[2].split(";")
        for word in list:
            if(word != "NULL" and  word != ""):
                if word not in wordlist:
                    wordlist.append(word)
print(len(wordlist),wordlist)

"""
writefile = open("TrainingTheme.txt", 'w', encoding='gb18030')      #打开正面词文件，准备写入正面词
for theme in wordlist:
    theme = theme + " " + "n" + "\n"
    writefile.writelines(theme)
writefile.close()
"""

userDicPath = "E:\PycharmProjects\PythonProject\SubjectBasedEmotionalAnalysis\CCFCompetition\Data\\NewAddEmotionalword\\NewUserDic.txt"
file = open(userDicPath,"r")
lines = file.readlines() #读取全部内容

userDiclist = []
for line in lines:
    userDiclist.append(line[:-1])
print(userDiclist)

InuserDiclist = []
OutuserDiclist = []

for word in wordlist:
    if word not in userDiclist:
        OutuserDiclist.append(word)
    else:
        InuserDiclist.append(word)
print(len(OutuserDiclist),OutuserDiclist)
print(len(InuserDiclist),InuserDiclist)

print("---------")
four = []
three = []
two = []
one = []

for word in OutuserDiclist:
    if(len(word)>=4):
        four.append(word)
    elif(len(word)==3):
        three.append(word)
    elif(len(word)==2):
        two.append(word)
    else:
        one.append(word)

result = []
for word in four:
    result.append(word)
for word in three:
    result.append(word)
for word in two:
    result.append(word)
for word in one:
    result.append(word)

print(len(result),result)

writefile = open("OutuserDiclist.txt", 'w', encoding='gb18030')      #打开正面词文件，准备写入正面词
for theme in result:
    theme = theme + " " + "n" + "\n"
    writefile.writelines(theme)
writefile.close()

writefile = open("InuserDiclist.txt", 'w', encoding='gb18030')      #打开正面词文件，准备写入正面词
for theme in InuserDiclist:
    theme = theme + " " + "n" + "\n"
    writefile.writelines(theme)
writefile.close()