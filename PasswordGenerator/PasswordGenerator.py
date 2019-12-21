from random import randint
numbers = '0123456789'
big_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small_letters = 'abcdefghijklmnopqrstuvwxyz'
symbols = '!#$%&()*+,-.:;<=>?@[]^_{|}~'
password_pattern_dict = {"1": big_letters + small_letters,
                         "2": big_letters + small_letters + numbers,
                         "3": big_letters + small_letters + numbers + symbols}


def get_settings():
    print("Choose password's length (enter a number from 10 to 20):")
    n = int(input())
    print("Choose password's complexity (enter a number: 1 - only letters, 2 - add numbers, 3 - add symbols ):")
    level = input()
    return n, password_pattern_dict[level]


def generator():
    password = ""
    length, pattern = get_settings()
    for i in range(length):
        password += pattern[randint(0, len(pattern)) - 1]
    print(password)


if __name__ == '__main__':
    generator()
