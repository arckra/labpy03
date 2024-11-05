
# 1. Algoritma Program Bilangan Random (latihan1-P7.py)
![hasil code latihan1](https://github.com/user-attachments/assets/5e58f9a5-61c4-49d8-91f7-df5c6bcb7ff7)

## Tujuan Program:
Menghasilkan sejumlah N bilangan acak yang nilainya lebih kecil dari 0.5

## Alur Program:
1. **Inisialisasi**
   - Import fungsi random dari modul random
   - Buat fungsi generate_numbers yang menerima parameter n (jumlah bilangan yang diinginkan)
   - Inisialisasi counter (count = 1)

2. **Input**
   - Program meminta input dari user berupa nilai N
   - Input divalidasi harus berupa angka integer

3. **Proses Utama**
   - Loop WHILE akan berjalan selama count <= N
   - Dalam setiap iterasi:
     a. Generate bilangan random antara 0-1 menggunakan random()
     b. Cek apakah bilangan < 0.5
     c. Jika ya: 
        - Tampilkan bilangan
        - Increment counter
     d. Jika tidak: 
        - Skip dan generate bilangan baru
   - Loop berlanjut sampai mendapatkan N bilangan yang memenuhi syarat

4. **Output**
   - Menampilkan setiap bilangan yang memenuhi syarat dengan format:
     "data ke: [urutan] => [bilangan random]"
   - Menampilkan "Selesai" ketika program berakhir
  


# 2. Algoritma Program Hitung Laba (latihan2-P7.py)
![hasil code latihan2](https://github.com/user-attachments/assets/236f9cd7-55c0-4237-a3dc-62381176f572)

## Tujuan Program:
Menghitung total keuntungan usaha selama 8 bulan dengan persentase laba yang berbeda-beda

## Alur Program:
1. **Inisialisasi**
   - Set modal awal = 100 juta
   - Inisialisasi total_laba = 0
   - Buat list kosong untuk menyimpan laba per bulan

2. **Proses Perhitungan**
   - Loop FOR untuk 8 bulan (range 1-9)
   - Untuk setiap bulan, hitung laba berdasarkan kondisi:
     a. Bulan 1-2: Laba = 0 (belum dapat untung)
     b. Bulan 3-4: Laba = 1% dari modal (modal * 0.01)
     c. Bulan 5-7: Laba = 5% dari modal (modal * 0.05)
     d. Bulan 8: Laba = 3% dari modal (modal * 0.03)
   - Setiap laba bulanan:
     a. Ditambahkan ke total_laba
     b. Disimpan ke dalam list laba_per_bulan
     c. Ditampilkan ke layar

3. **Output**
   - Menampilkan laba setiap bulan
   - Menampilkan total laba keseluruhan
  


# 3. Algoritma Program ATM (latihan3-P7.py)
![hasil code latihan3](https://github.com/user-attachments/assets/73d101a7-18f1-4c1f-89a7-e30ac6370478)

## Tujuan Program:
Mensimulasikan mesin ATM sederhana dengan fitur cek saldo dan penarikan uang

## Alur Program:
1. **Inisialisasi**
   - Set saldo awal = Rp 1.000.000
   - Program berjalan dalam infinite loop (while True)

2. **Menu Utama**
   - Tampilkan saldo saat ini
   - Tampilkan menu pilihan:
     1. Tarik Uang
     2. Keluar
   - Minta input pilihan dari user

3. **Proses Berdasarkan Pilihan**
   - Jika pilihan = 1 (Tarik Uang):
     a. Minta input jumlah penarikan
     b. Validasi input:
        - Harus berupa angka (try-except untuk ValueError)
        - Jumlah penarikan harus <= saldo
        - Jumlah penarikan harus > 0
     c. Jika valid:
        - Kurangi saldo dengan jumlah penarikan
        - Tampilkan pesan sukses
     d. Jika tidak valid:
        - Tampilkan pesan error yang sesuai
   
   - Jika pilihan = 2 (Keluar):
     a. Tampilkan pesan terima kasih
     b. Break dari loop (program selesai)
   
   - Jika pilihan tidak valid:
     a. Tampilkan pesan error
     b. Kembali ke menu utama

4. **Fitur Keamanan**
   - Validasi input harus berupa angka
   - Validasi saldo mencukupi
   - Validasi jumlah penarikan positif
   - Error handling untuk input tidak valid

5. **Output**
   - Menampilkan saldo terkini setiap kali menu ditampilkan
   - Menampilkan pesan sukses/error sesuai dengan aksi yang dilakukan
   - Menampilkan pesan terima kasih saat keluar
