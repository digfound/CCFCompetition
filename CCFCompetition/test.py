#encoding=utf-8
import jieba
import jieba.analyse
import jieba.posseg as pseg
import csv

newfilepath = "E:\PycharmProjects\PythonProject\SubjectBasedEmotionalAnalysis\CCFCompetition\Data\\NewAddEmotionalword\\NewUserDic.txt"

oldfilepath = "E:\PycharmProjects\PythonProject\SubjectBasedEmotionalAnalysis\CCFCompetition\Data\\outsideUserDic.txt"
file = open(newfilepath,"r")
lines = file.readlines() #读取全部内容
list = []
for line in lines:
    list.append(line)


writefile = open("testtest.txt", 'w', encoding='gb18030')      #打开正面词文件，准备写入正面词
f = open(oldfilepath,"r")
lines = f.readlines()#读取全部内容
for line in lines:
    if line not in list:
        writefile.writelines(line)
        print(len(line),line)

writefile.close()
