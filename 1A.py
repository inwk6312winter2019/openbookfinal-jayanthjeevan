

#An Integer that counts the total number of words that are in the list


def count_the_article():
 file=open("Book1.txt","r+")
 wordcount={}
 for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
 print (word,wordcount)
 file.close();
count_the_article()
