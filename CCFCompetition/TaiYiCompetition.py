#encoding=utf-8
import jieba
import jieba.analyse
import jieba.posseg as pseg
import csv

"""
userDic = "E:\PycharmProjects\PythonProject\SubjectBasedEmotionalAnalysis\CCFCompetition\Data\\userDic.txt"
jieba.load_userdict(userDic)    #载入用户字典
"""
#载入新的用户词典
userDic = "E:\PycharmProjects\PythonProject\SubjectBasedEmotionalAnalysis\CCFCompetition\Data\\NewAddEmotionalword\\NewUserDic.txt"
jieba.load_userdict(userDic)    #载入新的用户字典


"""
从训练集中获取负面情感词作为用户字典，同时也获取正面情感词文件和中性情感词文件
"""
def getUserDicFromTrainingDataSet(TrainingDataSetPath):
    negativePath = "negative.txt"     #生成负面词集合文件
    Positivetxt = "positive.txt"    #生成正面词集合文件
    Neutraltxt = "Neutral.txt"      #生成中性词集合文件
    """
    negativefile = open(negativePath, 'w', encoding='gb18030')     #打开负面词文件，准备写入负面词
    positivefile = open(Positivetxt, 'w', encoding='gb18030')      #打开正面词文件，准备写入正面词
    neutralfile = open(Neutraltxt, 'w', encoding='gb18030')        #打开中性词文件，准备写入中性词
    """
    csv_reader = csv.reader(open(TrainingDataSetPath,encoding='gb18030'))
    negativewords = []      #负面词集合
    positivewords = []      #正面词集合
    Neutralwords = []       #中性词集合
    for row in csv_reader:
        listword=[]       #每一行的情感词
        listanls=[]       #每一行的情感值
        words = row[3]    #情感关键词
        anls = row[4]     #情感值
        listword = words.split(";")    #将情感词按;划分成集合
        listanls = anls.split(";")     #将情感值按;划分成集合
        Index = 0
        for word in listword:
            if(listanls[Index] == '-1'):
                if word not in negativewords:   #如果负面词没有在列表中，添加进列表
                    negativewords.append(word)
            if (listanls[Index] == '1'):
                if word not in positivewords:  # 如果正向词没有在列表中，添加进列表
                    positivewords.append(word)
            if (listanls[Index] == '0'):
                if word not in Neutralwords:  # 如果中性词没有在列表中，添加进列表
                    Neutralwords.append(word)
            Index += 1
    """
    #将negativewords列表中的负面词写入到我们的用户字典
    for word in negativewords:
        word += '\n'
        negativefile.writelines(word)
    negativefile.close()  #关闭文件
    for word in positivewords:
        word += '\n'
        positivefile.writelines(word)
    positivefile.close()  #关闭文件
    for word in Neutralwords:
        word += '\n'
        neutralfile.writelines(word)
    neutralfile.close()  #关闭文件
    """
    return negativewords,positivewords,Neutralwords   #返回负向词、正向词、中性词列表


"""
读取我们新生成的正面词、负面词和中性词，传递给对应的列表
"""

def getNewEmotionWords():
    negativefilepath = "E:\PycharmProjects\PythonProject\SubjectBasedEmotionalAnalysis\CCFCompetition\Data\\NewAddEmotionalword\\NewNegative.txt"
    negativecsv_reader = csv.reader(open(negativefilepath, encoding='gb18030'))
    negativewords = []
    for word in negativecsv_reader:
        negativewords.append(str(word[0]))

    positivefilepath = "E:\PycharmProjects\PythonProject\SubjectBasedEmotionalAnalysis\CCFCompetition\Data\\NewAddEmotionalword\\NewPositive.txt"
    positivecsv_reader = csv.reader(open(positivefilepath, encoding='gb18030'))
    positivewords = []
    for word in positivecsv_reader:
        positivewords.append(str(word[0]))

    neutralfilepath = "E:\PycharmProjects\PythonProject\SubjectBasedEmotionalAnalysis\CCFCompetition\Data\\NewAddEmotionalword\\NewNeutral.txt"
    neutralcsv_reader = csv.reader(open(neutralfilepath, encoding='gb18030'))
    Neutralwords = []
    for word in neutralcsv_reader:
        Neutralwords.append(str(word[0]))
    return negativewords,positivewords,Neutralwords

"""
测试集，先对评论进行切词，切词时引入前面建好的用户词典（也即负面词），然后依次判断切分的词是否在训练集中的正面词、中性词、
负面词列表中，如果再，标注其为情感词，并加上相应的标签。此时情感词已经获取到，在通过情感词推出其主题，过程是：
情感词之前带有名词特点的词一般为主题词，根据这个原则寻找主题词
基于上述仍未找到主题词，则主题词为NULL;
"""

def getThemeAndEmotionalWords(TestingDataSetPath,stopwordsPath,negativewords,positivewords,Neutralwords):
    out = open("result1.csv",'w',newline='')
    csv_writer = csv.writer(out, dialect='excel')     #待写入的csv文件

    csv_reader = csv.reader(open(TestingDataSetPath, encoding='gb18030'))
    stopwords = stopwords = [line.strip() for line in open(stopwordsPath, 'r').readlines()]
    for row in csv_reader:
        words = pseg.cut(row[1])
        cutwordAndTagging = []     #保存切分好的词及其词性
        emotionwordsAndtag = []    #保存情感词及其词性和情感值
        themewords = []            #情感词对应的主题词
        for word,flag in words:
            if word not in stopwords:    #去除停用词之后切好的词，现在需要筛选出情感词
                cutwordAndTagging.append([word,flag])
        for wordAndtag in cutwordAndTagging:
            if wordAndtag[0] in positivewords:    #如果在正向词内
                list = wordAndtag
                list.append(1)
                emotionwordsAndtag.append(list)
            elif wordAndtag[0] in negativewords:    #如果在负向词内
                list = wordAndtag
                list.append(-1)
                emotionwordsAndtag.append(list)
            elif wordAndtag[0] in Neutralwords:    #如果在中性词内
                list = wordAndtag
                list.append(0)
                emotionwordsAndtag.append(list)
        #情感词emotionwordsAndtag已经获取到，现在，需要抠出主题词
        print(cutwordAndTagging)
        print(emotionwordsAndtag)
        for word in emotionwordsAndtag:
            count = 0
            for wordlist in cutwordAndTagging:
                if(word[0] == wordlist[0]):
                    break
                count += 1
            if(count == 0):    #第一个情感词，主题为null
                themewords.append("NULL")
            else:        #找到该情感词前面一个n或者nr或者nt或者vn或者ns的词作为主题词
                if (cutwordAndTagging[count - 1][1] == 'n' or cutwordAndTagging[count - 1][1] == 'nt' or cutwordAndTagging[count - 1][1] == 'nr'
                    or cutwordAndTagging[count - 1][1] == 'vn' or cutwordAndTagging[count - 1][1] == 'ns' or cutwordAndTagging[count - 1][1] == 'nz' or cutwordAndTagging[count-1][1] == 'nrt'):
                    themewords.append(cutwordAndTagging[count - 1][0])
                else:
                    themewords.append("NULL")
            """
                if( (cutwordAndTagging[count][1]=='x' or cutwordAndTagging[count][1]=='v') and count+1<len(cutwordAndTagging)):
                    if(cutwordAndTagging[count+1][1]=='n' or cutwordAndTagging[count+1][1]=='nt'or cutwordAndTagging[count+1][1]=='nr'
                        or cutwordAndTagging[count+1][1]=='vn' or cutwordAndTagging[count+1][1]=='ns'or cutwordAndTagging[count+1][1]=='nz'):
                        themewords.append(cutwordAndTagging[count + 1][0])
                    elif(cutwordAndTagging[count-1][1]=='n' or cutwordAndTagging[count-1][1]=='nt'or cutwordAndTagging[count-1][1]=='nr'
                        or cutwordAndTagging[count-1][1]=='vn' or cutwordAndTagging[count-1][1]=='ns'or cutwordAndTagging[count-1][1]=='nz'):
                        themewords.append(cutwordAndTagging[count - 1][0])
                    else:
                        themewords.append("NULL")
                elif(cutwordAndTagging[count-1][1]=='n' or cutwordAndTagging[count-1][1]=='nt'or cutwordAndTagging[count-1][1]=='nr'
                   or cutwordAndTagging[count-1][1]=='vn' or cutwordAndTagging[count-1][1]=='ns'or cutwordAndTagging[count-1][1]=='nz'):
                   themewords.append(cutwordAndTagging[count-1][0])
                else:
                   themewords.append("NULL")
            """
        # 以上抠出了主题词themewords
        print(themewords)
        """
        至此，我们已经得到了主题词themewords、情感词及其情感值emotionwordsAndtag，接下来，把这些信息写到一个list中，
        最终，将该list写到csv文件中的某一行中
        """
        list = []
        list.append(row[0])   #row_id
        list.append(row[1])   #content

        """
        Theme = ""
        for theme in themewords:
            Theme = Theme + theme + ";"
        list.append(Theme)   #Theme
        sentimentwords = ""
        sentimentanls = ""
        for wordanls in emotionwordsAndtag:
            sentimentwords = sentimentwords + str(wordanls[0]) + ";"
            sentimentanls = sentimentanls + str(wordanls[2]) + ";"
        list.append(sentimentwords)    #sentiment_word
        list.append(sentimentanls)     #sentiment_anls

        """
        # themewords emotionwordsAndtag 列表都已经获取好
        newthemewords = ""
        newsentimentwords = ""
        newsentimentanls = ""
        tem = []
        for i in range(len(themewords)):
            themeAndsentimentword = []
            themeAndsentimentword.append(themewords[i])   #主题词
            themeAndsentimentword.append(emotionwordsAndtag[i][0])  #情感词
            themeAndsentimentword.append(emotionwordsAndtag[i][2])  #情感值
            if themeAndsentimentword not in tem:
                tem.append(themeAndsentimentword)
        #print(tem)
        for line in tem:
            newthemewords = newthemewords + str(line[0]) + ";"
            newsentimentwords = newsentimentwords + str(line[1]) + ";"
            newsentimentanls = newsentimentanls + str(line[2]) + ";"
        list.append(newthemewords)
        list.append(newsentimentwords)
        list.append(newsentimentanls)

        print(list)
        csv_writer.writerow(list)

if __name__ == "__main__":
    TrainingDataSetPath = "E:\PycharmProjects\PythonProject\SubjectBasedEmotionalAnalysis\CCFCompetition\Data\TrainingData\TrainingDataSet.csv"
    TestingDataSetPath = "E:\PycharmProjects\PythonProject\SubjectBasedEmotionalAnalysis\CCFCompetition\Data\TestingData\TestingDataSet.csv"
    stopwordsPath = "E:\PycharmProjects\PythonProject\SubjectBasedEmotionalAnalysis\CCFCompetition\Data\stopword.txt"
    #negativewords, positivewords, Neutralwords = getUserDicFromTrainingDataSet(TrainingDataSetPath) #获取到正面词、中性词、负面词
    negativewords, positivewords, Neutralwords = getNewEmotionWords()
    getThemeAndEmotionalWords(TestingDataSetPath,stopwordsPath,negativewords, positivewords, Neutralwords)




