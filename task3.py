with open(r'C:\Users\zlunn\OneDrive\Рабочий стол\Files hw\1.txt',encoding="utf8") as f:
    txt1 = f.readlines()

with open(r'C:\Users\zlunn\OneDrive\Рабочий стол\Files hw\2.txt',encoding="utf8") as f:
    txt2 = f.readlines()

with open(r'C:\Users\zlunn\OneDrive\Рабочий стол\Files hw\3.txt',encoding="utf8") as f:
    txt3 = f.readlines()
files= [txt1,txt2,txt3]
files_=dict()
for i,t in enumerate(files):
    files_.setdefault(str(i+1)+'.txt', t)
files_=sorted(files_.items(), key=lambda x: x[1], reverse=True)
with open(r'C:\Users\zlunn\OneDrive\Рабочий стол\Files hw\4.txt','w', encoding="utf8") as f:
    for file in files_:
        f.write(file[0]+'\n')
        f.write(str(len(file[1]))+'\n')
        for i in file[1]:
            if i==0:
                f.write(i.lstrip())
            else:
                f.write(i)
        f.write('\n')

with open(r'C:\Users\zlunn\OneDrive\Рабочий стол\Files hw\4.txt', encoding="utf8") as f:
    txt = f.readlines()
print([i for i  in txt])
