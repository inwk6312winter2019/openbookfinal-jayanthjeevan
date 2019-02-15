# A Dicionary containing words in the book as key and the character count as the values.


task = open("Book1.txt",'r')
task = task.readlines()


def character_word_count(task):
  dict1=dict()
  for line in task:
    line=line.strip()
    line=line.lower()
    line=line.split()
    for word in line:
      if word not in dict1:
             dict1[word]=1
      elif word in dict1:
             dict1[word]+=1
  print(dict1)

character_word_count(task)
