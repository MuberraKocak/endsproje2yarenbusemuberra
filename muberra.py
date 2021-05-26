#endustri projesi
'''
AŞAMA-1: Yeterlilik alan göstergelerinden 5 tanesi seçilir.
AŞAMA-2: Belirlenen kriterlere ait -varsa- alt kriterler belirlenir.
AŞAMA-3: Kriterlerin/Alt kriterlerin her biri için ağırlık belirlenir.
AŞAMA-4: Aday numarası 1'den başlatılır.
AŞAMA-5: Adayların TC kimlik no alınır, 
         eğer karakter sayısı doğru değilse (11 rakam) adayın bilgisini kontrol edip düzeltmesi 
         için uyarı mesajı yazdırılır.
AŞAMA-6: Adayların isim ve soyisim bilgileri alınır,
        eğer bu sorulara yanıt verilmezse adayın ilgili alan için geçerli bir bilgi girmesi için 
        uyarı mesajı yazdırılır.
AŞAMA-7: Adaylardan genel not ortalaması bilgisini girmesi istenir. Alınan bilgi float tipine dönüştürülür.
         Not ortalaması için belirlenene sınırlara göre if-elif-else koşulları kullanılarak adayın 
         girdiği notun bulunduğu aralık tespit edilir.
         İlgili aralık için tanımlanan puan adayın not ortalaması puanı olarak kaydedilir.
AŞAMA-8: Adaylara bilimsel projelerden/yarışmalardan ödül alıp almadığı sorulur,
         "evet/hayır" biçiminde cevap vermediyse adayın ilgili alana geçerli bir bilgi girmesi 
         için uyarı mesajı yazdırılır.           
AŞAMA-9: Adaylardan ingilizce seviyesini sayısal olarak belirtmesi isternir 
         (1:Yok, 2:Başlangıç, 3:Orta, 4:İyi, 5:Çok İyi)
        eğer girilen bilgi doğru değilse adaya bilgisini kontrol edip düzeltmesi
        için uyarı mesajı yazdırılır.
AŞAMA-10: Adaylara sanatsal/sosyal projelerden/yarışmalardan ödül alıp almadığı sorulur,
         "evet/hayır" biçiminde cevap vermediyse adayın ilgili alana geçerli bir bilgi girmesi 
         için uyarı mesajı yazdırılır.
AŞAMA-11: Adaylara profesyonel sporcu lisansının olup olmadığı sorulur,
         "evet/hayır" biçiminde cevap vermediyse adayın ilgili alana geçerli bir bilgi girmesi 
         için uyarı mesajı yazdırılır.
AŞAMA-12: Yeni aday listesine adayın bilgileri kaydedilir.
AŞAMA-13: Aday bilgileri listesine de yeni aday listesi kaydedilir.'''

#yeterlilik alan göstergeleri
akademik_mesleki_yeterlilikler =  ("Genel not ortalaması", "Bilimsel projelerden/yarışmalar kazanılmış ödüller", "Yabacı dil")
notOrtAgirlik = 0.50
bilimselOdulAgirlik = 0.20
ingilizceSeviyesiAgirlik = 0.30
akademikYeterlilikAgirlik = 0.6

sanatsal_sosyal_yeterlilikler = ("Sosyal projelerden/yarışmalardan kazanılmış ödüller")
sosyalOdulAgirlik = 0.2

sportif_yeterlilikler = ("Profesyonel sporcu lisansına sahip olmak")
sportifOdulAgirlik = 0.2

#kullanıcıdan bilgilerin alınması ve puan hesaplamaları
aday = 1
adayBilgileri = [ ]
while aday <= 2:
  TCbilgi = False
  while TCbilgi == False:
    TCKimlikNumarasi = input("TC kimlik numaranızı giriniz: ")
    TCuzunluk = len(TCKimlikNumarasi)
    if TCuzunluk == 11:
      TCbilgi = True
    else:
      TCbilgi = False
      print("Lütfen girdiğiniz bilgiyi kontrol edip tekrar giriniz!")

  # TCno = input("TC kimlik numaranızı giriniz: ")
  # TCuzunluk = len(TCno)
  # if  TCuzunluk == 11:
  #   TCno = int(TCno)
  # elif TCuzunluk!=11:
  #   print("Lütfen girdiğiniz bilgiyi kontrol edip tekrar giriniz!")
  #   TCno = int(input("TC kimlik numaranızı giriniz: "))
  #   if  TCuzunluk == 11:
  #     TCno = int(TCno)
  #   elif TCuzunluk!=11:
  #     print("Lütfen girdiğiniz bilgiyi kontrol edip tekrar giriniz!")
  #     TCno = int(input("TC kimlik numaranızı giriniz: "))

  isim = input("İsminiz: ")
  while (isim == ""):
     print("Lütfen girdiğiniz bilgiyi kontrol edip tekrar giriniz!")
     isim = input("İsminiz: ")

  soyisim = input("Soyisminiz: ")
  while(soyisim == ""):
     print("Lütfen girdiğiniz bilgiyi kontrol edip tekrar giriniz!")
     soyisim = input("Soyisminiz: ")

  notOrt = float(input("Genel not ortalamanızı giriniz: "))
  if (notOrt > 3.49 and notOrt <= 4.00) or (notOrt > 87.25 and notOrt <= 100.00):
    notOrtPuan = 100
  elif (notOrt > 2.99 and notOrt <= 3.49) or (notOrt > 74.75 and notOrt <= 87.25):
    notOrtPuan = 85
  elif (notOrt > 2.50 and notOrt <= 2.99) or (notOrt > 62.50 and notOrt <= 74.75):
    notOrtPuan = 70
  elif (notOrt > 2.00 and notOrt <= 2.50) or (notOrt > 50.00 and notOrt <= 62.50):
    notOrtPuan = 55
  elif (notOrt >= 1.00 and notOrt <= 2.00) or (notOrt >= 25 and notOrt <= 50.00):
    notOrtPuan = 20
  else:
    print("Lütfen girdiğiniz not ortalamasını kontrol edip tekrar giriniz!")
    notOrt = float(input("Genel not ortalamanızı giriniz: "))
    if (notOrt > 3.49 and notOrt <= 4.00) or (notOrt > 87.25 and notOrt <= 100.00):
      notOrtPuan = 100
    elif (notOrt > 2.99 and notOrt <= 3.49) or (notOrt > 74.75 and notOrt <= 87.25):
      notOrtPuan = 85
    elif (notOrt > 2.50 and notOrt <= 2.99) or (notOrt > 62.50 and notOrt <= 74.75):
      notOrtPuan = 70
    elif (notOrt > 2.00 and notOrt <= 2.50) or (notOrt > 50.00 and notOrt <= 62.50):
      notOrtPuan = 55
    elif (notOrt >= 1.00 and notOrt <= 2.00) or (notOrt >= 25 and notOrt <= 50.00):
      notOrtPuan = 20
  print(f'Genel not ortalaması puanı={notOrtPuan}')

  bilimselOdul = (input("Bilimsel projelerden/yarışmalardan ödül aldınız mı?: "))
  if (bilimselOdul.upper() == "EVET"):
    bilimselOdulPuan = 100
  elif (bilimselOdul.upper() == "HAYIR"):
    bilimselOdulPuan = 0
  else:
    print("Lütfen girdiğiniz bilgiyi kontrol edip tekrar giriniz!(Evet/Hayır sorusu)") 
    bilimselOdul = (input("Bilimsel projelerden/yarışmalardan ödül aldınız mı?: "))
    if (bilimselOdul.upper() == "EVET"):
      bilimselOdulPuan = 100
    elif (bilimselOdul.upper() == "HAYIR"):
      bilimselOdulPuan = 0
  print(f'Bilimsel ödül puanı={bilimselOdulPuan}')
  
  ingilizceSeviyesi = int(input("ingilizce seviyenizi sayısal olarak belirtiniz (1:Yok, 2:Başlangıç, 3:Orta, 4:İyi, 5:Çok İyi): "))
  if ingilizceSeviyesi == 5:
    ingilizceSeviyesiPuan = 100
  elif ingilizceSeviyesi == 4:
    ingilizceSeviyesiPuan = 80
  elif ingilizceSeviyesi == 3:
    ingilizceSeviyesiPuan = 60
  elif ingilizceSeviyesi == 2:
    ingilizceSeviyesiPuan = 40
  elif ingilizceSeviyesi == 1:
    ingilizceSeviyesiPuan = 20
  elif ingilizceSeviyesi == 0:
    ingilizceSeviyesiPuan = 0
  elif ingilizceSeviyesi < 0 or ingilizceSeviyesi > 5:
    print("Lütfen girdiğiniz değeri kontrol ederek geçerli bir değer giriniz!")
    ingilizceSeviyesi = int(input("ingilizce seviyenizi sayısal olarak belirtiniz (1:Yok, 2:Başlangıç, 3:Orta, 4:İyi, 5:Çok İyi): "))
    if ingilizceSeviyesi == 5:
      ingilizceSeviyesiPuan = 100
    elif ingilizceSeviyesi == 4:
      ingilizceSeviyesiPuan = 80
    elif ingilizceSeviyesi == 3:
      ingilizceSeviyesiPuan = 60
    elif ingilizceSeviyesi == 2:
      ingilizceSeviyesiPuan = 40
    elif ingilizceSeviyesi == 1:
      ingilizceSeviyesiPuan = 20
    elif ingilizceSeviyesi == 0:
      ingilizceSeviyesiPuan = 0
  print(f'İngilizce seviyesi puanı = {ingilizceSeviyesiPuan}')
  akademik_mesleki_yeterlilikTAP = (notOrtAgirlik*notOrtPuan)+(bilimselOdulAgirlik*bilimselOdulPuan)+(ingilizceSeviyesiAgirlik*ingilizceSeviyesiPuan)
  print(f'Akademik/Mesleki Yeterlilik Puanı = {akademik_mesleki_yeterlilikTAP}')
  akademik = ["Akademik/Mesleki Yeterlilik Puanı", {akademik_mesleki_yeterlilikTAP}]

  sosyalOdul = (input("Sosyal projelerden/yarışmalardan ödül aldınız mı?: "))
  if sosyalOdul.upper() == "EVET":
    sosyalOdulPuan = 100
  elif (sosyalOdul.upper() == "HAYIR"):
    sosyalOdulPuan = 0
  elif sosyalOdul.upper() != "EVET" and (sosyalOdul.upper() != "HAYIR"):
    print("Lütfen girdiğiniz bilgiyi kontrol edip tekrar giriniz!(Evet/Hayır sorusu)")
    sosyalOdul = (input("Sosyal projelerden/yarışmalardan ödül aldınız mı?: "))
    if sosyalOdul.upper() == "EVET":
      sosyalOdulPuan = 100
    elif (sosyalOdul.upper() == "HAYIR"):
      sosyalOdulPuan = 0
  sanatsal_sosyal_yeterlilikTAP = (sosyalOdulAgirlik*sosyalOdulPuan)
  print(f'Sanatsal/Sosyal Yeterlilik Puanı = {sanatsal_sosyal_yeterlilikTAP}')
  sosyal = ["Sanatsal/Sosyal Yeterlilik Puanı", {sanatsal_sosyal_yeterlilikTAP}]

  sportifOdul = (input("Profesyonel sporcu lisansınız bulunuyor mu?: "))
  if sportifOdul.upper() == "EVET":
    sportifOdulPuan = 100
  elif (sportifOdul.upper() == "HAYIR"):
    sportifOdulPuan = 0
  elif sportifOdul.upper() != "EVET" and (sportifOdul.upper() != "HAYIR"):  
    print("Lütfen girdiğiniz bilgiyi kontrol edip tekrar giriniz!(Evet/Hayır sorusu)")
    sportifOdul = (input("Profesyonel sporcu lisansınız bulunuyor mu?: "))
    if sportifOdul.upper() == "EVET":
      sportifOdulPuan = 100
    elif (sportifOdul.upper() == "HAYIR"):
      sportifOdulPuan = 0
  sportif_yeterlilikTAP = (sportifOdulAgirlik*sportifOdulPuan)
  print(f'Sportif Yeterlilik Puanı = {sportif_yeterlilikTAP}')
  sportif = ["Sportif Yeterlilik Puanı", {sportif_yeterlilikTAP}]
  
  print(f'\n{aday}.aday \nTC Kimlik Numarası:{TCKimlikNumarasi} \nİsim:{isim.capitalize()} \nSoyisim:{soyisim.upper()} \nAkademik/Mesleki Yeterlilik Puanı={akademik_mesleki_yeterlilikTAP} \nSanatsal/Sosyal Yeterlilik Puanı={sanatsal_sosyal_yeterlilikTAP} \nSportif Yeterlilik Puanı={sportif_yeterlilikTAP}\n')
  
  aday_kimlik_bilgi = f'{aday}. Aday TC Kimlik Numarası:{TCKimlikNumarasi} İsim:{isim.capitalize()} Soyisim:{soyisim.upper()}'.split()
  yeniAday = [aday_kimlik_bilgi[0], aday_kimlik_bilgi[1], aday_kimlik_bilgi[2], aday_kimlik_bilgi[3], akademik, sosyal, sportif]
  adayBilgileri.append(yeniAday)
  #print(yeniAday)
  aday += 1
print(adayBilgileri)




#bu kısım henüz hazır değil

#ağırlıklı toplam seçme puanı (atsp) hesaplanması......................................................................
# minakademik_mesleki_yeterlilikTAP = 
# agirlikliToplamSecmePuani = 100 + 400 * (()) 

