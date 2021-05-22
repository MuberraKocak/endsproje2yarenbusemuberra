#MÜBERRA KOÇAK

#Bahsedilen kriterlerin sınırlarını belirleyeceğiz.
#TC no ile başvurulan sistemden yukarıda bahsedilen kriterlere ait bilgileri sistemden çekeceğiz.
#Aday bilgilerini dosyaya kaydedeceğiz. (her aday için bir aday/başvuru no atanacak)
#Her adayın puanını hesaplayacağız.
#and, or, if, elif, else kullanarak değerlendirme yapacağız.

#yeterlilik alan göstergeleri
akademik_mesleki_yeterlilikler =  ("genel not ortalaması", "Bilimsel projelerden/yarışmalardan ödül kazandınız mı?", "ingilizce seviyenizi sayısal olarak belirtiniz (1:Yok, 2:Başlangıç, 3:Orta, 4:İyi, 5:Çok İyi): ")
notOrtAgirlik = 0.50
bilimselOdulAgirlik = 0.20
ingilizceSeviyesiAgirlik = 0.30
akademikYeterlilikAgirlik = 0.6

sanatsal_sosyal_yeterlilikler = ("sosyal projelerden/yarışmalardan kazanılmış ödüller")
sosyalOdulAgirlik = 0.2

sportif_yeterlilikler = ("profesyonel sporcu lisansına sahip olmak")
sportifOdulAgirlik = 0.2

#ağırlıklı toplam seçme puanı (atsp) hesaplanması......................................................................

#kullanıcıdan bilgilerin alınması ve puan hesaplamaları
aday=1
while aday<=10:
  TCno=int(input("TC kimlik numaranızı giriniz: "))
  isim=input("İsminiz: ")
  soyisim=input("Soyisminiz: ")

  notOrt=float(input("Genel not ortalamanızı giriniz: "))
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
  print(f'Genel not ortalaması puanı={notOrtPuan}')
  
  bilimselOdul = (input("Bilimsel projelerden/yarışmalardan ödül aldınız mı?: "))
  if (bilimselOdul == "evet"):
    bilimselOdulPuan = 100
  elif (bilimselOdul == "hayır"):
    bilimselOdulPuan = 0
  else:
    print("Lütfen girdiğiniz bilgiyi kontrol edip tekrar giriniz!")  
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
  print(f'İngilizce seviyesi puanı = {ingilizceSeviyesiPuan}')
  akademik_mesleki_yeterlilikTAP = (notOrtAgirlik*notOrtPuan)+(bilimselOdulAgirlik*bilimselOdulPuan)+(ingilizceSeviyesiAgirlik*ingilizceSeviyesiPuan)
  print(f'Akademik/Mesleki Yeterlilik Puanı = {akademik_mesleki_yeterlilikTAP}')

  sosyalOdul = (input("Sosyal projelerden/yarışmalardan ödül aldınız mı?: "))
  if sosyalOdul == "evet":
    sosyalOdulPuan = 100
  else:
    sosyalOdulPuan = 0
  sanatsal_sosyal_yeterlilikTAP=(sosyalOdulAgirlik*sosyalOdulPuan)
  print(f'Sanatsal/Sosyal Yeterlilik Puanı = {sanatsal_sosyal_yeterlilikTAP}')

  sportifOdul = (input("Profesyonel sporcu lisansınız bulunuyor mu?: "))
  if sportifOdul == "evet":
    sportifOdulPuan = 100
  else:
    sportifOdulPuan = 0
  sportif_yeterlilikTAP=(sportifOdulAgirlik*sportifOdulPuan)
  print(f'Sportif Yeterlilik Puanı = {sportif_yeterlilikTAP}')

  print(f'{aday} aday TC No: {TCno} isim: {isim} soyisim: {soyisim}, akademik mesleki yeterlilik puanı={akademik_mesleki_yeterlilikTAP}, sanatsal sosyal yeterlilik puanı={sanatsal_sosyal_yeterlilikTAP}, sportif yeterlilik puanı={sportif_yeterlilikTAP}')

aday +=1
