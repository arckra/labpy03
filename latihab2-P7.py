def hitung_laba():
    modal = 100000000
    total_laba = 0
    laba_per_bulan = []
    
    for bulan in range(1, 9):
        if bulan < 3:
            laba = 0
        elif bulan < 5:
            laba = modal * 0.01
        elif bulan < 8:
            laba = modal * 0.05
        else:
            laba = modal * 0.02
            
        total_laba += laba
        laba_per_bulan.append(laba)
        print(f"laba bulan ke- {bulan} sebesar: {laba}")
    
    print(f"Total laba adalah: {total_laba}")

if __name__ == "__main__":
    hitung_laba()