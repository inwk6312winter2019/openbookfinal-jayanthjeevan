task= open('Book2.txt','r')
task = task.readlines()
def unique_words(task):
  result = []
  for line in task:
    line=line.strip()
    line=line.split()
    for word in line:
      if word not in result:
        result.append(word)
  print(result)
