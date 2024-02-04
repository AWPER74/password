from random import randint

choice = int(input("Введите длину пароля: "))

choice_num_chr = input("Делать ли фильтрацию по цифрам (y, n): ")

if choice_num_chr.lower() == "y":
    choice_num_chr = True
elif choice_num_chr.lower() == "n":
    choice_num_chr = False
else:
    print("Необходимо вводить лишь у или п")
    exit()

password = ""