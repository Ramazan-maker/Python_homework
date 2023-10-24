import time
import random
import hashlib

def generate_password(length):
    symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()_+-="
    password = ""
    for i in range(length):
        password += symbols[random.randint(0, len(symbols) - 1)]
    return password

def main():
    start_time = time.time()
    while True:
        password = generate_password(8)
        if hashlib.md5(password.encode("utf-8")).hexdigest() == "f232b847c44bd9992dd04efe19597ee6":
            break
    print("Пароль:", password)
    end_time = time.time()
    print("Время подбора пароля:", end_time - start_time, "секунд")

if __name__ == "__main__":
    main()
