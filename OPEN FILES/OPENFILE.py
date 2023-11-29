# import sys
# import os

# FILENAME = sys.argv[1]
# text = sys.argv[2:]

# if os.path.exists(FILENAME):
#     with open(FILENAME, "w") as file:
#         file.write(" ".join(text))
#         print("If block")
#         print("The file exists")
#         file.close()
# else:
#     with open(FILENAME, "x") as file:
#         file.write(" ".join(text))
#         print("Else block")
#         print("The file exists")
#         file.close()

# with open(FILENAME, "r") as file:
#     print(file.read())
#     file.close()






# СОЗДАТЬ ФАЙЛ
# Чтобы создать несуществующий файл, мы используем режим «x»
# Кроме того, если файл НАЙДЕН, он возвращает ошибку
# ex: 
# open("myfile.txt", "x") # =>  x режим позволяет создать#файл, если он не существует, иначе выдается ошибка.
# если мы не хотим получить ошибку, нам нужно использовать os
# if os.path.exists("myfile.txt"):
#   print("The file exists")
# ===========================================================
# Когда мы открываем файл, мы всегда должны не забывать его закрывать
# Если мы не закроем его, мы не сможем открыть его снова, пока не перезапустим программу
# Для чтения файла мы используем режим «r»
# Кроме того, если файл НЕ НАЙДЕН, возвращается ошибка
# ===========================================================
# 1. read()      => читает весь файл (мы также можем указать, сколько символов читать)
# 2. readline    => читает только одну строку
# 3. readlines() => читает файл построчно (все строки)
# 4. перебирать файл построчно
# ===========================================================
# FILENAME = "test.txt"
# with open(FILENAME, 'r+') as f:
#     f.write("\nThis is new line")
#     for line in f.readlines():
#         print(line)
# ===========================================================
# ex:
#   f = open("myfile.txt", "r")
#       print(f.read())
# ===========================================================

# -_--_--_--_--_--_--_--_--_-   ПИСАТЬ ОТСЮДА   -_--_--_--_--_--_--_--_--_--_--_--_-

# Чтобы обновить существующий файл, мы используем режим «a» или режим «w».
# --- (w) режим записи заменяет содержимое файла
# --- (a) режим добавления добавляет содержимое в конец файла
# ex:  
#   f = open("myfile.txt", "a")
#   f.write("Now the file has more content!")
#   ----------------------------
#   используя ключевое слово WITH 
#   with open("myfile.txt", "a") as f:
#       f.write("Now the file has more content!")
# ===========================================================
# DELETE A FILE
# Чтобы удалить файл, мы используем функцию os.remove().
# ex:
#   import os
#   os.remove("myfile.txt")
# ===========================================================
# "r" - Read - Значение по умолчанию. Открывает файл для чтения, ошибка, если файл не существует
# "a" - Append - Открывает файл для добавления, создает файл, если он не существует.
# "w" - Write - Открывает файл для записи, создает файл, если он не существует.
# "x" - Create - Создает указанный файл, возвращает ошибку, если файл существует.
# "t" - Text - Значение по умолчанию. Текстовый режим
# "b" - Binary - Двоичный режим (например, изображения)
# ===========================================================
# Комбинации режимов:
# "a+" - Read and Append - Открывает файл для чтения и добавления, создает файл, если он не существует.
# "w+" - Write and Read - Открывает файл для записи и чтения, создает файл, если он не существует.
# "r+" - Read and Write - Открывает файл для чтения и записи, ошибка, если файл не существует
# ===========================================================
# WORKING WITH DIRECTORIES and os
# РАБОТА С СПРАВОЧНИКАМИ и os
# import os
# os.mkdir("myfolder") # => создает папку
# os.rmdir("myfolder") # => удаляет папку
# os.rename("oldname", "newname") # => переименовывает папку
# os.getcwd() # => возвращает текущий рабочий каталог
# os.path.exists("myfolder") # => проверяет, существует ли папка
# os.path.isdir("myfolder") # => проверяет, существует ли папка
# os.path.isfile("myfile.txt") # => проверяет, существует ли файл
# os.path.join("myfolder", "myfile.txt") # => объединяет папку и файл
# ===========================================================


file = open("file.txt", "w")
file.write("Пример текста для записи в файл")
file = open("file.txt", "r")
file.close()
print(file)



































# import os 

# FILENAME = 'test.txt'
# if os.path.exists(FILENAME):
#     with open('test.txt', 'r') as file:
#             print(file.read())
# else:
#     print(f'The file {FILENAME=} does not exist')

# def read_names():
#     names_dict = {}
#     try:
#         with open("names.txt", "r") as file:
#             for line in file:
#                 name = line.strip()
#                 if name in names_dict:
#                     names_dict[name] += 1
#                 else:
#                     names_dict[name] = 1
#     except FileNotFoundError:
#         print("Файл не найден.")
#     for name, count in names_dict.items():
#         print(f"{name}: {count}")

# def create_names(names):
#     try:
#         with open("names.txt", "w") as file:
#             for name in names:
#                 file.write(name + "\n")
#     except:
#         print("Ошибка при создании файла.")

# names = [
#     "Oliver", "George", "Harry", "Jack", "Jacob", "Noah",
#     "Charlie", "Muhammad", "Thomas", "Oscar", "William",
#     "James", "Leo", "Alfie", "Henry", "Archie", "Ethan",
#     "Charlie", "Muhammad", "Thomas", "Oscar", "William",
#     "Joseph", "Freddie", "Samuel", "Alexander", "Logan"
# ]

# create_names(names)
# read_names()