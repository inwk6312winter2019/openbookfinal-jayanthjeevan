import string

jk=open('Book1.txt')
file1=jk.read()

def print_book(books):
	count=0
	mydict=dict()
	com_dict=dict()
	for line in books.split():
		word=line.strip(string.punctuation)
		myword=word.lower()
		count=count+1
		if myword not in mydict:
			mydict[myword]=1
		else:
			mydict[myword]+=1

	print(' Number  of words in the Book is:',count)
	mylist=[]
	for key,value in mydict.items():
		mylist.append((value,key))
	mylist.sort(reverse=True)
	print("commonly used  20 words in Book are:")
	for freq,word in mylist[:20]:
		print(word,freq,sep='\t')
	for char in mylist[:20]:
		com_dict[char]=com_dict.get(char,0)+1
	print("\nDictionery containing the most common 20 words:\n")
	print(com_dict)
jk1=open('Book1.txt')
file1=jk1.read()
jk2=open('Book2.txt')
file2=jk2.read()
jk3=open('Book3.txt')
file3=jk3.read()
print("conten in Book1")
print_book(file1)
print("content in Book2")
print_book(file2)
print("content in Book3")
print_book(file3)
