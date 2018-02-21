#encoding=utf-8
import jieba
import jieba.analyse
import jieba.posseg as pseg
import csv

newfilepath = "E:\PycharmProjects\PythonProject\SubjectBasedEmotionalAnalysis\CCFCompetition\Data\\NewAddEmotionalword\\NewUserDic.txt"
file = open(newfilepath,"r")
lines = file.readlines() #读取全部内容
list = []
for line in lines:
    list.append(line)

morethanfour = []
four = []
three = []
two = []
one = []

for word in list:
    if(len(word)>=6):
        morethanfour.append(word)
    elif(len(word)==5):
        four.append(word)
    elif(len(word)==4):
        three.append(word)
    elif(len(word)==3):
        two.append(word)
    elif(len(word)==2):
        one.append(word)

result = []
for word in morethanfour:
    result.append(word)
for word in four:
    result.append(word)
for word in three:
    result.append(word)
for word in two:
    result.append(word)
for word in one:
    result.append(word)

for word in result:
    print(word)

writefile = open("USERDIC.txt", 'w', encoding='gb18030')      #打开正面词文件，准备写入正面词
for word in result:
    writefile.writelines(word)
writefile.close()