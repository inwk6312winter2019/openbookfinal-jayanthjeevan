import string

def exlore(file):
	fin=open(file)
	count=0
	for line in fin:
		line=line.replace("-"," ")
		if "get" in line:
			fout=open("get.log","a")
			fout.write(line)
			fout.close()
		if "post" in line:
			fout=open("post.log","a")
			fout.write(line)
			fout.close()
		if "put" in line:
			fout=open("put.log","a")
			fout.write(line)
			fout.close()
		if "delete" in line:
			fout=open("delete.log","a")
			fout.write(line)
			fout.close()

file_read("access.log")
