
file_dict = {}   # ключ - имя файла, значение - количество строк в файле
full_file_dict = {}    # ключ - имя файла, значение - содержание файла

f_1 = open('1.txt', encoding='utf-8')
text_1 = f_1.readlines()
dict_1 = {'1.txt': len(text_1)}
file_dict.update(dict_1)
f_1.close()

f_1 = open('1.txt', encoding='utf-8')
r_text_1 = f_1.read()
f_dict_1 = {'1.txt': r_text_1}
full_file_dict.update(f_dict_1)
f_1.close()

f_2 = open('2.txt', encoding='utf-8')
text_2 = f_2.readlines()
dict_2 = {'2.txt': len(text_2)}
file_dict.update(dict_2)
f_2.close()

f_2 = open('2.txt', encoding='utf-8')
r_text_2 = f_2.read()
f_dict_2 = {'2.txt': r_text_2}
full_file_dict.update(f_dict_2)
f_2.close()

f_3 = open('3.txt', encoding='utf-8')
r_text_3 = f_3.read()
f_dict_3 = {'3.txt': r_text_3}
full_file_dict.update(f_dict_3)
f_3.close()

f_3 = open('3.txt', encoding='utf-8')
text_3 = f_3.readlines()
dict_3 = {'3.txt': len(text_3)}
file_dict.update(dict_3)
f_3.close()

for i in range(100):  # взял производное число(число строк в файлах изначально не известно)
    if i in file_dict.values():
        res = list(file_dict.keys())[list(file_dict.values()).index(i)]
        with open('4.txt', 'a', encoding='utf-8') as file:
            file.write(f'{res}\n')
            file.write(f'{file_dict[res]}\n')
            file.write(f'{full_file_dict[res]}\n')
