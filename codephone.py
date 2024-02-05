import os

def add_new_user(name: str, phone: str, filename: str):
#Добавление нового пользователя.
    with open(filename,'r+t', encoding='utf-8') as wrtbl:
       lines_count = len(wrtbl.readlines())
       wrtbl.write(f"{lines_count +1};{name};{phone}\n")


def read_all(filename: str) -> str:
#Возвращает все содержимое телефонной книги.
    with open(filename,'r',encoding='utf-8') as data:
        result = data.read()
    return result
    #pass


def search_user(data: str, filename: str) -> str:
#Поиск записи по критерию data.
    #pass
    with open(filename,'r',encoding='utf-8') as content:
       text = content.readlines()
       res = [item for item in text if data.lower() in item.lower()]
    return (''.join(res)).replace(':', ' ') if res else ' Контакта в справочнике не обнаружено'  


def check_directory(filename: str)-> bool:
   if filename  not in os.listdir():
     with open(filename,'w',encoding='utf-8') as data:
        data.write("")

def copy_line(filename: str,newfilename: str, line_num) -> str:
    #pass
   with open(filename,'r',encoding='utf-8') as data:
     lines = data.readlines()
     if line_num<1 or line_num>len(lines):
        print('Некорректный номер строки')
        return 
   with open(newfilename, 'a', encoding='utf-8') as data:
      
     data.write(lines[line_num-1])


INFO_STRING = """
Выберите режим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск
4 - скопировать строку в новый файл
"""


DATASOURCE = 'phone.txt'

NEWFile = 'copyphone.txt'

check_directory(DATASOURCE)

while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        print(read_all(DATASOURCE))
    elif mode == 2:
       user =  input("Введите ФИО :" )
       phone = input("Введите № телефона : " )
       add_new_user(name =user,phone=phone, filename=DATASOURCE)
    elif mode == 3:
       search = input("введите строку для поиска :" ) 
       print(search_user(search, DATASOURCE))
    elif mode == 4:
       line_num = int(input('введите номер стоки: '))
       copy_line(DATASOURCE, NEWFile, line_num)
