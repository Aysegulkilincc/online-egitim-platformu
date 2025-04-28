class Kurs:
     # Kurs sınıfı kurs bilgilerini tutar
    def __init__(self, kurs_id, ad, kontenjan):
        self.kurs_id = kurs_id
        self.ad = ad
        self.kontenjan = kontenjan

    def bilgileri_goster(self):
         # Kurs bilgilerini ekrana yazdırır
        return f"Kurs ID: {self.kurs_id}, Ad: {self.ad}, Kontenjan: {self.kontenjan}"

    def kontenjan_guncelle(self, miktar):
         # Kursun kontenjanını günceller
        self.kontenjan += miktar
        print(f"Kontenjan güncellendi. Yeni kontenjan: {self.kontenjan}")

class Kayit:
    #Kayit sınıfı öğrencilerin kurslara kayıtlarını tutar
    def __init__(self, kayit_id, kurs, ogrenci_adi):
        self.kayit_id = kayit_id
        self.kurs = kurs
        self.ogrenci_adi = ogrenci_adi

    def kayit_detaylari(self):
         # Kayıt detaylarını ekrana yazdırır
        return f"Kayıt ID: {self.kayit_id}, Kurs: {self.kurs.ad}, Öğrenci: {self.ogrenci_adi}"

class EgitimPlatformu:
    def __init__(self):
        self.kurslar = []
        self.kayitlar = []
        self.kayit_sayaci = 1

    def kurs_ekle(self, kurs):
        # yeni kurs ekler
        self.kurslar.append(kurs)

    def kurslari_listele(self):
        # tüm kursları ekrana yazdırır
        for kurs in self.kurslar:
            print(kurs.bilgileri_goster())

    def kayit_olustur(self, kurs_id, ogrenci_adi):
        # öğrenciyi bir kursa kaydeder
        kurs = self.kurs_bul(kurs_id)
        if kurs:
            if kurs.kontenjan > 0:
                kurs.kontenjan -= 1
                kayit = Kayit(self.kayit_sayaci, kurs, ogrenci_adi)
                self.kayitlar.append(kayit)
                self.kayit_sayaci += 1
                print("Kayıt başarıyla gerçekleşti")
            else:
                print("Kurs kontenjanı dolu")
        else:
            print("Kurs bulunamadı")

    def kontenjan_guncelle(self, kurs_id, miktar):
        #bir kursun kontenjanını günceller.
        kurs = self.kurs_bul(kurs_id)
        if kurs:
            kurs.kontenjan_guncelle(miktar)
        else:
            print("Kurs bulunamadı")

    def kayitlari_listele(self):
        # bu zamana kadar yapılan tüm kayıtları listeler
        for kayit in self.kayitlar:
            print(kayit.kayit_detaylari())

    def kurs_bul(self, kurs_id):
         # Kurs ID'sine göre kursu arar
        for kurs in self.kurslar:
            if kurs.kurs_id == kurs_id:
                return kurs
        return None

    def menu(self):
        # Kullanıcıya menü sunar
        while True:
            print("\n    ONLINE EĞİTİM PLATFORMU   ")
            print("1 - Kursları Listele")
            print("2 - Yeni Kurs Ekle")
            print("3 - Kontenjan Güncelle")
            print("4 - Kursa Kayıt Ol")
            print("5 - Kayıtları Listele")
            print("6 - Çıkış Yap")
            
            try:
                secim = int(input("Ne yapmak istersin? (Seçim yap: 1-6): "))
            except ValueError:
                print(" Sadece rakam kullan")
                continue

            if secim == 1:
                self.kurslari_listele()
            elif secim == 2:
                kurs_id = int(input("Kurs ID gir: "))
                ad = input("Kurs adını yaz: ")
                kontenjan = int(input("Başlangıç kontenjanı gir: "))
                kurs = Kurs(kurs_id, ad, kontenjan)
                self.kurs_ekle(kurs)
                print(f"{ad} kursu başarıyla eklendi")
            elif secim == 3:
                kurs_id = int(input("Kontenjan güncellemesi için Kurs ID gir: "))
                miktar = int(input("Eklenecek kontenjan miktarı: "))
                self.kontenjan_guncelle(kurs_id, miktar)
            elif secim == 4:
                kurs_id = int(input("Kayıt için Kurs ID gir: "))
                ogrenci_adi = input("Öğrenci adını yaz: ")
                self.kayit_olustur(kurs_id, ogrenci_adi)
            elif secim == 5:
                self.kayitlari_listele()
            elif secim == 6:
                print("Çıkış yapılıyor")
                break
            else:
                print("Yanlış seçim yaptın.")

egitim_platformu = EgitimPlatformu()

egitim_platformu.kurs_ekle(Kurs(1, "Günlük Meditasyon", 20))
egitim_platformu.kurs_ekle(Kurs(2, "Fotoğrafçılık", 15))
egitim_platformu.kurs_ekle(Kurs(3, "Yemek Yaparken Püf Noktalar", 32))
egitim_platformu.kurs_ekle(Kurs(4, "Basit Tamirat", 45))
egitim_platformu.kurs_ekle(Kurs(5, "Bilgisayar'a Giriş", 29))

egitim_platformu.menu()

