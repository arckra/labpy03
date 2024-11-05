def atm():
    saldo = 1000000  # Saldo awal Rp 1.000.000
    
    while True:
        print(f"\nSaldo saat ini: Rp {saldo}")
        print("1. Tarik Uang")
        print("2. Keluar")
        
        pilihan = input("Pilih menu (1/2): ")
        
        if pilihan == "1":
            try:
                jumlah = int(input("Masukkan jumlah penarikan: "))
                if jumlah > saldo:
                    print("Maaf, saldo tidak mencukupi!")
                elif jumlah <= 0:
                    print("Jumlah penarikan tidak valid!")
                else:
                    saldo -= jumlah
                    print("Penarikan berhasil!")
            except ValueError:
                print("Mohon masukkan angka yang valid")
                
        elif pilihan == "2":
            print("Terima kasih telah menggunakan ATM!")
            break
            
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    atm()