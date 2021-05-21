#MÜBERRA KOÇAK

#Bahsedilen kriterlerin sınırlarını belirleyeceğiz.
#TC no ile başvurulan sistemden yukarıda bahsedilen kriterlere ait bilgileri sistemden çekeceğiz.
#Aday bilgilerini dosyaya kaydedeceğiz. (her aday için bir aday/başvuru no atanacak)
#Her adayın puanını hesaplayacağız.
#and, or, if, elif, else kullanarak değerlendirme yapacağız.

#kullanıcının kişisel bilgileri
aday=1
while aday<=10:
  TCno=int(input("TC No: "))
  isim=input("isim: ")
  soyisim=input("soyisim: ")
  print(f'aday {aday} TC No: {TCno} isim: {isim} soyisim: {soyisim}')
aday +=1
  
#yeterlilik alan göstergeleri
akademik_mesleki_yeterlilikler =  ("genel not ortalaması", "bilimsel projelerden/yarışmalardan kazanılmış ödüller", "yabancı dil")
sanatsal_sosyal_yeterlilikler = ("sosyal projelerden/yarışmalardan kazanılmış ödüller")
sportif_yeterlilikler = ("profesyonel sporcu lisansına sahip olmak")

#yeterlilik alanı cevapları
notort=float(input("not ortalamanız: "))



#toplam ağırlıklı puan (tap) hesaplaması



#ağırlıklı toplam seçme puanı (atsp) hesaplanması



