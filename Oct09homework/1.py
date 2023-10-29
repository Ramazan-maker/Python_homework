import time
import hashlib
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def main():
    start_time = time.time()

    symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()_+-="

    for i in range(3**8):
        password = ""
        for j in range(8):
            password += symbols[i % len(symbols)]
            i //= len(symbols)

        if hash_password(password) == "f232b847c44bd9992dd04efe19597ee6":
            print("Найдено:", password)
            break

    end_time = time.time()
    print("Найдено:", password)

    print("Время подбора:", end_time - start_time, "секунд")

if __name__ == "__main__":
    main()
