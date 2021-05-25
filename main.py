import os
def deletePrefix(path,prefix,aft,n):

	files = os.listdir(path)
	print(files)
	i = 0
	for file in files:
		
    	# old 旧名称的信息
		old = path + os.sep + files[i]
    	# new是新名称的信息
		new = path + os.sep + file.replace(prefix,aft,int(n))
    	#新旧替换
		os.rename(old,new)
		#print(file)
		i+=1
def printFileName(path):
        files = os.listdir(path)
        for file in files:
                print(file)
# 输入文件夹地址

#path 示例： "C:\\Users\\quercus\\Desktop\\观复嘟嘟第一季\\"
path=input('Please input your files address:')
prefix=input('Please input the prefix which you wanna delete:')
aft=input('And you wanna change that to?:')
n=input('Please input the number:')
deletePrefix(path,prefix,aft,n)
printFileName(path)
print('Success!')
