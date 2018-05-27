
std_dct={}


def Read_From_File():
    with open("output_data.txt", "r")as f:
        for line in f.readlines():
            (id,name,tot)=line.split(',')
            std_dct.update({id: {'name': name, 'tot': tot}})
    f.close()

def Write_to_File():
    with open("output_data.txt", "w")as f:
        for id in std_dct:
            f.write(str(id)+','+str(std_dct[id]['name'])+','+str(std_dct[id]['tot']))

    f.close()


def Search_dict():
    id = input('enter ur id')
    print('name:', std_dct[id]['name'])
    print('tot:', std_dct[id]['tot'])

def print_all():
    for id in std_dct:
        print('id',id)
        print('name:', std_dct[id]['name'])
        print('Tot', std_dct[id]['tot'])

def add_dict():
    id = input('enter ur id')
    name = input('enter ur name')
    tot = input('enter ur tot')
    std_dct.update({id: {'name': name, 'tot': tot}})

def removekey():
    key=input("Enter the ID")
    std_dct.pop(key)
    print_all()

def removekey():
    key=input("Enter the ID")
    std_dct.pop(key)
    print_all()



while(True):
    Read_From_File()
    print('1. Search id','2. print all','3.add detais','4.save and exit','5.delete')
    ch=input('enter ur choices')

    if ch=='1':
       Search_dict()

    if ch =='2':
        print_all()

    if ch=='3':
        add_dict()

    if ch == '4':
        Write_to_File()
        break

    if ch == '5':
        removekey()
        Write_to_File()








