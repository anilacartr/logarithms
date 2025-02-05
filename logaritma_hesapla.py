import math


def logaritma_hesapla(taban, sayi):
    if taban <= 0 or sayi <= 0:
        return "Taban ve sayı pozitif olmalıdır."
    if taban == 1:
        return "Taban 1 olamaz."

    # logaritma hesaplama: log_taban(sayi) = ln(sayi) / ln(taban)
    sonuc = math.log(sayi) / math.log(taban)
    return sonuc


# Kullanıcıdan girdi alalım
taban = float(input("Logaritmanın tabanını girin: "))
sayi = float(input("Logaritması alınacak sayıyı girin: "))

# Logaritma hesapla ve sonucu göster
sonuc = logaritma_hesapla(taban, sayi)
print(f"log{taban}({sayi}) = {sonuc}")
