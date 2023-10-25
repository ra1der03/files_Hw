#ЗАДАЧА 1:
with open(r'C:\Users\zlunn\OneDrive\Рабочий стол\Files hw\cook-book.txt',encoding="utf8") as f:
    dishes_list = f.readlines()

cook= dict()
def renew( dict, file, title ):
    key= title[:-1]+':'
    dict.setdefault(key, [])
    for i in range(int(file[file.index(title)+1])):
        value = [{'ingredient_name': file[file.index(title)+2+i].split('|')[0]},
                 {'quantity': file[file.index(title)+2+i].split('|')[1]},
                 {'measure': file[file.index(title)+2+i].split('|')[2][:-1]}]
        dict[key].append(value)

def counts(file):
    indexes=[]
    for line in file:
        if line[0].isdigit()==True:
            indexes.append(line)
    return indexes
def titles(file):
    title=[]
    for line in file:
        if line[0].isdigit()==False and '|' not in line and line!='\n':
            title.append(line)
    return title

for t in titles(dishes_list):
    renew( cook, dishes_list, t)
# for dish in cook.items():
#     print(dish)
#ЗАДАЧА 2:
def counting(index):
    count=0
    index+=2
    while '|' in dishes_list[index]:
        count+=1
        index+=1
    return count

def get_shop_list_by_dishes(dishes: list, person_count):
    dic= dict()
    for line in dishes_list:
        for dish in dishes:

            if line[:-1]==dish:
                for i in range(counting(dishes_list.index(dish+'\n'))):
                    key = dishes_list[dishes_list.index(dish+'\n')+2+i].split('|')[0] + ':'
                    value=[{'quantity': int(dishes_list[dishes_list.index(dish+'\n')+2+i].split('|')[1])*person_count},
                           {'measure':dishes_list[dishes_list.index(dish+'\n')+2+i].split('|')[2][:-1]}]
                    if key in dic:
                        dic.update({key: [{'quantity': int(dishes_list[dishes_list.index(dish+'\n')+2+i].split('|')[1])*person_count*2},
                           {'measure':dishes_list[dishes_list.index(dish+'\n')+2+i].split('|')[2][:-1]}]})
                    else:
                        dic.setdefault(key, value)
            else:
                continue
    print(dic)


cafe= get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
