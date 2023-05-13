#Baraj doluluk oranı
h = float(input("Yükseklik verisi: "))
critical_h_start = 20       # Suyun
total_h = float(input("Barajın yüksekliği: "))    # Barajın Total Yüksekliği
kapak1 = 0      # Kapak Kapalı
kapak2 = 0      # Kapak Kapalı
kapak3 = 0      # Kapak Kapalı
kapak4 = 0      # Kapak Kapalı
if h >= total_h*0.89:
    if h in range(int(total_h*0.89),int(total_h*0.92)):
        kapak1 = 1
        print("{kapak1} numaralı kapak doluluk oranına bağlı olarak tek başına açıldı.")
    elif h in range(int(total_h*0.91),int(total_h*0.94)):
        kapak1 = 1
        kapak2 = 1
        print("{kapak1} ve {kapak2} numaralı kapaklar doluluk oranına bağlı olarak açıldı.")
    elif h in range(int(total_h*0.93),int(total_h*0.97)):
        kapak1 = 1
        kapak2 = 1
        kapak3 = 1
        print("{kapak1},{kapak2} ve {kapak3} numaralı kapaklar doluluk oranına bağlı olarak açıldı")
    else:
        kapak1 = 1
        kapak2 = 1
        kapak3 = 1
        kapak4 = 1
        print("Su tehlikede seviyede. Lütfen çevre yerleşkeleri boşaltın. Tüm kapaklar açılıyor.")
elif h < 6:
    print("Doluluk oranı kritik durumda!")


#Ph değeri
try:
    ph = float(input("Lütfen suyun pH değerini girin (0-14 aralığında): "))
    if ph < 0 or ph > 14:
        raise ValueError
    elif ph > 10:
        print("Suyun pH değeri çok yüksek, deriyle temas etmemelisiniz. Ayrıca bakteriyel olabilir.")
    elif 6.5 <= ph <= 8.5:
        print("Suyun pH değeri uygun, içilebilir.")
    elif ph < 6.5:
        print("Suyun pH değeri çok asidik, tahriş edici olabilir.")
    elif ph > 8.5:
        print("Suyun pH değeri çok bazik, içilmesi tavsiye edilmez.")
except ValueError:
    print("Hatalı giriş! Lütfen 0-14 aralığında bir sayı girin.")


