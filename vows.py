#- Returns: An Integer In each book count the total number of words that start with this following collection tuple.

task = open("Book3.txt")
task = task.readlines()

def starts_with_vow(task):
  count=0
  vow=("a","e","i","o","u")
  for line in task:
    line=line.strip()
    line=line.lower()
    line=line.split()
    for word in line:
      if word[0] in vow:
        count+=1
  print(count)

starts_with_vow(task)
