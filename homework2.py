'''
# 1. soru - Kullanıcıdan bir sayı alıp, bu sayının tek mi çift mi olduğunu kontrol eden bir program yazın.

num = int(input("Lutfen bir sayi giriniz: "))

if num % 2 == 0:
    print(f"{num} sayisi cift sayidir.")
else:
    print(f"{num} sayisi tek sayidir.")
'''
    
'''
# 2. soru - Kullanıcıdan bir kelime alıp hangi harften kac tane oldugunu dictionary kullanarak bulan bir program yazın.
word = input("Lutfen bir kelime giriniz: ")
char_count = {}
for char in word:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)
'''

'''
#3. soru kullanicidan sifre alin, sifre en az 8 karakter, en az 1 buyuk harf ve en az 1 rakam icermeli
password = input("Lutfen bir sifre giriniz: ")
if len(password) < 8:
    print("Sifre en az 8 karakter olmalidir.")
elif not any(char.isupper() for char in password):
    print("Sifre en az 1 buyuk harf icermelidir.")
elif not any(char.isdigit() for char in password):
    print("Sifre en az 1 rakam icermelidir.")
else:
    print("Sifre olusturuldu.")    
'''

'''
#4. soru - [12,4,9,25,30,7,18] listesinin ortalamasini bulun ve ortalamadan buyuk sayilari ayri bir listeye atayin

numbers = [12,4,9,25,30,7,18]
new_list = []
average = sum(numbers) / len(numbers)
for num in numbers:
    if num> average:
        new_list.append(num)
print(f"Ortalama: {average}, Ortalamadan buyuk sayilar: {new_list}")
'''

'''
#5. soru - ucgen deseni yazdirin

rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print("")
'''

'''
#6. soru while ile kullanicidan sayi al, sayilari topla, kullanici 0 girince islemi bitir ve toplami yazdir
total = 0
while True:
    num = int(input("Lutfen bir sayi giriniz (bitirmek icin 0 giriniz): "))
    if num == 0:
        break
    total += num
print(f"Girilen sayilarin toplami: {total}")
'''

'''
#7. soru palindrom kontrolu yapin
word = input("Lutfen bir kelime giriniz: ")
if word == word[::-1]:
    print(f"{word} kelimesi palindromdur.")
else:
    print(f"{word} kelimesi palindrom degildir.")
'''

'''
#8. soru 1'den 100'e kadar olan sayilardan 3 ve 5'e bolunebilen sayilarin karelerini listeye alin ve yazdirin

list_squares = []
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        list_squares.append(i**2)
print(list_squares)
'''

'''
#9. soru - kullanicidan bir cumle al ve split() kullanarak cumlenin her kelimesinin bas harfini buyuk yapip yazdir 

sentence = input("Lutfen bir cumle giriniz: ")
words = sentence.split()
new_sentence = ""
for word in words:
    if len(word) > 0:
        new_word = word[0].upper() + word[1:]
        new_sentence += new_word + " "
    else:
        new_sentence += " "
print(new_sentence.strip())
'''

'''
#10. soru - kullanicidan 5 6 adet yorum alin, yorumlari bir listede saklayin, her yorumun karakter sayisini bulun, en uzun ve en kisa yorumu yazdirin, kac yorumda "iyi" kelimesinin gectigini bulun ve tum yorumlarin ortalama uzunlugunu hesaplayin
comments = []
for i in range(5):
    comment = input(f"Lutfen {i+1}. yorumu giriniz: ")
    comments.append(comment)
lengths = [len(comment) for comment in comments]
longest_comment = comments[lengths.index(max(lengths))]
shortest_comment = comments[lengths.index(min(lengths))]
good_count = sum(1 for comment in comments if "iyi" in comment.lower())
average_length = sum(lengths) / len(comments) 
print(f"En uzun yorum: {longest_comment}")
print(f"En kisa yorum: {shortest_comment}")
print(f"'iyi' kelimesi {good_count} yorumda gecti.")
print(f"Tum yorumlarin ortalama uzunlugu: {average_length}")
'''