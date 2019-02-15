# A list containing the words in th book in descending order based on character count.
task = open("Book1.txt",'r')
task = task.readlines()


def sorted_words(task):
  result=[]
  list2=[]
  for line in task:
    line=line.strip()
    line=line.split()
    for word in line:
      if word not in result:
        result.append(word)
  print(sorted(result[::-1], key = len))

sorted_words(task)
