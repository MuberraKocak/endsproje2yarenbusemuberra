#YAREN BUSE SEMERCİ
#kayıt olmak isteyenler için

akademik= ("genel not ortalamasi","yabanci diliniz var mi","bilimsel projede yarismada kazanilmis odulunuz var mı")
genelnotortalamasiagirlik=0.50
yabancidilagirlik=0.40
bilimselprojeagirlik=0.20

sosyal_sanat= ("sosyal projede kazanilmis odulunuz var mi")
sosyalprojeagirlik=0.20

spor=("profosyonel sporcu lisansina sahip misiniz")
sporculisansiagirlik=0.25


kisi=1
while <=10;
  tckimliknumarasi=int(input("tc kimlik numarasi : "))
  ad=str(input("ad : "))
  soyad=str(input("soyad : "))
  print(kisi{kisi}  tckimliknumarasi{tc kimlik numarasi}  soyad{soyad})
  kisi+1
  
genelnotortalamasi=float(input("genel not ortalamaniz : "))
  if(genelnototralamasi 3.50 > and genelnotortalamasi <= 4.00):
genelnotortalamasipuani=100
  elif(genelnotortalamasi 3.00 > and genelnotortalamasi <= 3.50):
genelnotortalamasipuani=85
  elif(genelnotortalamasi 2.50 > and genelnotortalamasi <= 3.00):
genelnotortalamasipuani=70
  elif(genelnotortalamasi 2.00 > and genelnotortlamasi <= 2.50):
genelnotortalamasipuani=55
  elif(genelnotortalamasi 1.50 > and genelnotortalamasi <= 2.00):
genelnotortalamasipuani=40
  elif(genelnotortalamasi 1.00 > and genelnotortalamasi <= 1.50):
genelnotortalamasipuani=25
  else:
    print("Giridiginiz ortalamayi kontrol ediniz: ")
    print(f'Genel Not Ortalamasi Puaniniz={genelnotortalamasipuani}')
    
    
yabancidil=str(input("yabanci diliniz var mi : "))
   if (yabancidil== "EVET"):
    yabancidilpuani=100
  print(f'İngilizcesi mevcut={yabancidilpuani}')
  else (yabancidil== "HAYİR"):
    yabancidilpuani=0
  print(f'İngilizcesi mevcut değil={yabancidilpuani}')
  

bilimselproje=str(input("bilimsel projede yarismada kazanilmis odulunuz var mi : "))
   if (bilimselproje== "EVET"):
    bilimselprojepuani=100
    print(f'Bilimsel projede yarismada kazanilmis odulu mevcut={bilimselprojepuani}')
   else (bilimselproje== "HAYIR"):
    bilimselprojepuani=0
    print(f'Bilimsel projede yarismada kazanilmis odulu mevcut degil={bilimselprojepuani}')
    
    akademiktab= (genelnotortalamasiagirlik*genelnotortalamasipuani) + (yabancidilagirlik*yabancidilpuani) + (bilimselprojeagirlik*bilimselprojepuani)
    print(f'Akademik Yetelilik Puani={akademiktab}')
    


sosyalproje=str(input("sosyal projede yarismada kazanilmis odulunuz var mi : "))
    if (sosyalproje== "EVET"):
    sosyalprojepuani=100
    print(f'Sosyal projede yarismada kazanilmis odulunuz mevcut={sosyalprojepuani}')
    else :
      sosyalprojepuani=0
      print(f'Sosyal projede yarismada kazilmis odulunuz mevcut degil={sosyalprojepuani}')
      
      sosyal_sanattab=(sosyalprojeagirlik*sosyalprojepuani)
      print(f' Sosyal ve Sanatsal Yeterlilik Puani={sosyal_sanattab}')
      
     
      
sporculisansi=str(input("profosyonel sporcu lisansina sahip misiniz : "))
    if (sporculisansi== "EVET"):
    sporculisansipuani=100
    print(f'Profosyonel sporcu lisansiniz mevcut={sporculisansipuani}')
    else:
      sporculisansipuani=0
    print(f'Profosyonel sporcu lisansiniz mevcut degil={sporculisansipuani}')
    
    sportab=(sporculisansiagirlik*sporculisansipuani)
    print(f' Spor Yeterlilik Puani={sportab}')
          
          
    print(f'{kisi} kisi tc kimlik numarasi: {tckimliknumarasi} ad:{ad} soyad: {soyad} akademik yeterlilik puani: {akademiktab} sosyal sanatsal yeterlilik puani: {sosyal_sanattab} spor yeterlilik puani: {sportab}')
    kisi+1
