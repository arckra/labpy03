from random import random

def generate_numbers(n):
    count = 1
    while count <= n:
        number = random()
        if number < 0.5:
            print(f"data ke: {count} => {number}")
            count += 1

def main():
    try:
        n = int(input("Masukkan nilai N: "))
        generate_numbers(n)
        print("Selesai")
    except ValueError:
        print("Mohon masukkan angka yang valid")

if __name__ == "__main__":
    main()