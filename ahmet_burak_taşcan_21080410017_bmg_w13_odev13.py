sinav_sonuc = {'isimler':['Ayşe K.','Ahmet M.','Nuri C.','Nawar T.','Suzan T.','Ala B.'],'cinsiyet':['K','E','E','E','K','K'],'matematik':[60,40,97,45,56,95],'turkce':[70,30,23,80,78,46]}

def yeni_ogrenci(isim, cinsiyet, matematik, turkce):
    sinav_sonuc["isimler"].append(isim)
    sinav_sonuc['cinsiyet'].append(cinsiyet)
    sinav_sonuc['matematik'].append(matematik)
    sinav_sonuc['turkce'].append(turkce)


for i in range (2) :
    isim = input("isim giriniz : ")
    cinsiyet = input("cinsiyet giriniz : ")
    matematik = input("matematik notunu giriniz : ")
    turkce = input ("turkce notunu giriniz : ")
    yeni_ogrenci(isim, cinsiyet, matematik, turkce)

print(sinav_sonuc)