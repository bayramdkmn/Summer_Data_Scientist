# -------------------------- 1- VERI TIPLERI ------------------------------

'''
#1. soru

name = input("Lutfen adinizi giriniz: ")
if name != "":    
    age = int(input("Lutfen yasinizi giriniz: "))
    if age != "":
        height = float(input("Lutfen boyunuzu giriniz, (Ornek: 1.75): "))
        if(height != ""):
            print("Isim: ",name)
            print("Yas: ",age)
            print("Boy: ",height)
else:
    print("Eksik ya da yanlis bilgi girdiniz. Lutfen programı bastan baslatin!")
'''

'''
#2. soru

matematik = int(input("Lutfen matematik dersi sinav sonucunuzu giriniz: "))
fizik = int(input("Lutfen fizik dersi sinav sonucunuzu giriniz: "))
kimya = int(input("Lutfen kimya dersi sinav sonucunuzu giriniz: "))
if matematik and fizik and kimya >= 0 and matematik and fizik and kimya <=100 :
    sum = matematik + fizik + kimya
    avg = float(sum / 3)
    print("Derslerin ortalaması: ",avg )
else:
    print("Sınav degerlerini referans disi degerler girdiniz. Lutfen tekrar deneyin")
'''

'''
#3. soru

metin = "Data Scientist"

print("Ilk karakter: ", metin[0])
print("Son karakter: ", metin[-1])
print("Uzunluk: ", len(metin))
print("Ters cevrilmis hali: ", metin[::-1])
'''

# -------------------------- 2- OPERATORLER ------------------------------
'''
#4. soru

firstNum = int(input("Lutfen birinci sayiyi giriniz: "))
secondNum = int(input("Lutfen ikinci sayiyi giriniz: "))

print("Iki sayinin toplami: ", firstNum + secondNum)
print("Iki sayinin cikarimi: ", firstNum - secondNum)
print("Iki sayinin carpimi: ", firstNum * secondNum)
print("Iki sayinin bolumu: ", firstNum / secondNum)
print("Iki sayinin modu: ", firstNum % secondNum)
'''

'''
#5. soru

avg= int(input("Lutfen ortalamanizi giriniz: "))
if avg >= 0 and avg <= 100:
    if avg > 50:
        print("Tebrikler, dersi gectiniz, ortalamaniz: ", avg)
    else:
        print("Dersten kaldiniz, ortalamaniz: ", avg)
else:
    print("Gecerli deger araligi girmediniz. Lutfen programi bastan baslatin")
'''

'''
#6. soru

age = int(input("Lutfen yasinizi giriniz: "))
if age >= 18:
    print("Ehliyet alabilirsiniz")
elif age >0 and age<18:
    print("Ehliyet alamazsiniz")
else:
    print("Gecerli deger girmediginiz icin program sonlandirilmistir.")
'''

'''
#7. soru

price = float(input("Lutfen urunun fiyatini giriniz:"))
if price != "":
    discount = int(input("Lutfen indirim oranini giriniz: %"))
    if discount != "":
        newPrice = price - (price * discount / 100)
        print("Urunun eski fiyati: ",price, " Urunun yeni fiyati: ", newPrice)
else:
    print("Gecerli deger girmediginiz icin program sonlandirilmistir.")
'''

'''
#8. soru

a= True
b = False

print("a AND b: ", a and b)
print("a OR b: ", a or b)
print("NOT a", not a)
print("NOT b", not b)
print("(a and b) or a: " ,(a and b) or a)
'''


# -------------------------- 3- MINI PROJE ------------------------------

'''
#9. Soru

print("Hosgeldiniz! 200 TL uzeri alisverisinize %10 indirim uygulanacaktir.")
firstProduct= float(input("Birinci urunun fiyatini giriniz: "))
secondProduct = float(input("Ikinci urunun fiyatini giriniz: "))
thirdProduct = float(input("Ucuncu urunun fiyatini giriniz: "))

if firstProduct != "" and secondProduct != "" and thirdProduct != "":
    sum = firstProduct + secondProduct + thirdProduct
    if sum > 200:
        newPrice = sum - (sum * 0.1)
        print("Urunlerin toplam tutari 200TL'yi astigi icin %10 indirim uygulanmistir. Yeni fiyat: ", newPrice," TL")
    else:
        print("Aldiginiz urunlerin toplam fiyati ", sum, " TL. 200 TL üzeri alisverisinize %10 indirim uygulanacaktir.")
else:
    print("Gecerli deger girmediginiz icin program sonlandirilmistir.")
'''

'''
#10. Soru

from datetime import datetime

now = datetime.now().year
bornDate = int(input("Lutfen dogum yilinizi giriniz: "))

if bornDate <= now and bornDate > 0:    
    age = now - bornDate

    if 0 <= age <= 12:
        print("Cocuksunuz, yasiniz: ",age)
    elif 13 <= age <= 17:
        print("Ergensiniz, yasiniz: ", age)
    elif age >=18:
        print("Yetiskinsiniz, yasiniz: ", age)
    else:
        print("Gecersiz dogum yili girdiniz.")
else:
    print("Lutfen dogum yilinizi kontrol ediniz. Program sonlandiriliyor.")
'''
