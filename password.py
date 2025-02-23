import time
import secrets
import string
import os


download_folger = os.path.join(os.path.expanduser("~"), "Downloads")

file_path = os.path.join(download_folger, 'passwords.txt')

resolved_symbols_for_code_of_all_symbols = string.digits + \
    string.ascii_letters + string.punctuation

def smooth_text(text, delay=0.008):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

# Генерация пароля

def password_generator(length):
    password = ''.join(secrets.choice(resolved_symbols_for_code_of_all_symbols)
                        for _ in range(length))
    return password 
while True:
    # Человек дает название паролю
    smooth_text("\nВведите название пароля: ")
    password_name = input()
    

    while True:
        # Ввод длины пароля в количесве символов
        smooth_text("\nВведите длину пароля: ")

        try:
            length = int(input())
            if length > 64:
                smooth_text(
                    "Длинна пароля не должна быть больше 64 символов\n")
                smooth_text("Вы уверены что хотите сохранить длинну? да/нет\n")
                save_length = input().lower()

                if save_length == 'да':
                    time.sleep(0.7)
                    break

                else:
                    continue

            else:
                break

        except ValueError:
            smooth_text("Ошибка! Введите только числа\n")
            time.sleep(2)

    # Сохранить пароль или нет
    smooth_text("Сохранить пароль в файле? да/нет: ")
    save_password = input().lower()

    # Сохранение рехультата функции password_generator
    password = password_generator(length)

    # Сохранение пароля в файл passwords.txt
    if save_password == "да":
        with open(file_path, 'w') as file:
            file.write(f"{password_name}: {password}\n")

        smooth_text("Пароль был успешно сохранен в файле password.txt\n")
        time.sleep(0.5)

        smooth_text("Хотите вывести пароль на экран? да/нет: ")
        password_output = input().lower()

        if password_output == 'да':
            smooth_text(f"{password_name}: {password}\n")
            time.sleep(2)

        else:
            break

    else:
        smooth_text(f"{password_name}: {password}\n")

    smooth_text("\nХотите выйти из программы? да/нет: ")
    exit = input().lower()

    if exit == 'да':
        break

    else:
        continue
