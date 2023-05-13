while True:
    

    class Baraj:
    
        def __init__(self, yukseklik, baraj_alani, kapak_sayisi, turbin_sayisi):
            self.yukseklik = yukseklik
            self.baraj_alani = baraj_alani
            self.kapak_sayisi = kapak_sayisi
            self.turbin_sayisi = turbin_sayisi
            self.turbin_sayac = 0
            self.su_miktari = 0
            self.su_temizlik_orani = 0
            self.su_ph_degeri = 0
    
        def hesapla_hacim(self):
            self.hacim = self.yukseklik * self.baraj_alani
            return self.hacim
    
        def doluluk_orani_hesapla(self):
            doluluk_orani = self.su_miktari / self.hacim
            return doluluk_orani
    
        def anti_tasma(self, su_miktari):
            max_su_miktari = self.hacim() * 0.9 # barajın %90'ı dolduğunda kapaklar açılacak
            while su_miktari > max_su_miktari:
                kapak_acilacak_miktar = su_miktari - max_su_miktari
                kapak_sayisi = min(self.kapak_sayisi, int(kapak_acilacak_miktar / 10)) # her kapak en fazla 10 birim su boşaltabilir
                for i in range(self.kapak_sayisi):
                    # kapakları aç
                    print(f"Kapak {i+1} açıldı.")
                    print("Su tahliye ediliyor...")
                self.su_miktari = self.hacim
                self.doluluk_orani = self.doluluk_orani_hesapla()
                print("Su seviyesi kontrol edildi.")
    
        def ph_kontrol(self, ph_degeri):
            if ph_degeri < 6.5 or ph_degeri > 8.5:
                print("Su pH değeri uygun değil! pH değeri:", ph_degeri)
                
            
        def kuraklik_tahmini(self, yagis_miktari):
            baraj_alani = self.baraj_alani
            su_miktari = self.su_miktari()
            tahmini_sure = (baraj_alani * 0.7 - su_miktari) / yagis_miktari
            if tahmini_sure <= 0:
                print("Baraj dolu!")
            elif tahmini_sure <= 7:
                print("Yakında kuraklık olabilir, lütfen tasarruf yapın.")
            else:
                print("Kuraklık tehlikesi yok.")
        
        class Turbin:
            def __init__(self, basinc, sayac, verim=0.9):
                self.basinc = basinc
                self.sayac = sayac
                self.verim = verim
        
            def elektrik_uret(self, turbin_sayisi,sure):
                uretilecek_saatlik_enerji = self.basinc * turbin_sayisi * self.sayac / 980000 * 3600000 * self.verim # 1 kWh enerji için gereken su miktarı 3.67 m^3'tür
                print("{} turbin için saatlik üretilecek enerji miktarı: {:.2f} kWh".format(turbin_sayisi, uretilecek_saatlik_enerji / 1000))
                toplam_elektrik_uretimi = uretilecek_saatlik_enerji * sure
                return toplam_elektrik_uretimi
    if input("Devam etmek için herhangi bir tuşa, çıkmak için q'ya basın: ") == "q":
        break

