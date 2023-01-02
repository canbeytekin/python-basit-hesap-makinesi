print("""***************************************
HESAP MAKİNESİ

1.Toplama İşlemi
2.Çıkarma İşlemi
3.Çarpma İşlemi
4.Bölme İşlemi
***************************************""")

#kullanıcıdan tam sayı girmesini istedik ve bunlar a,b olarak iki değere atadık.

a = int(input("Birinci Sayıyı Giriniz:"))                                                
b = int(input("İkinci Sayıyı Giriniz:"))

#kullanıcıdan yapmak istediği işlemi yukarıda belirtilen işlemlerin karşılığı olan sayıya göre seçmesini istedik.

islem = input("Yapmak İstediğiniz İşlemi Seçin:")                                      

#kullanıcının girdiği 4 işlem değerlerinin eşit olduğu koşullarda nasıl tepki vereceğine göre işlemleri sıraladık.

if islem == "1":                                                                         
    print("{} + {} = {}".format(a,b,a+b))                                                
    print("İşleminiz Sonlandı..")
elif islem == "2":
    print("{} - {} = {}".format(a,b,a-b))
    print("İşleminiz Sonlandı..")
elif islem == "3":
    print("{} x {} = {}".format(a,b,a*b))
    print("İşleminiz Sonlandı..")
elif islem == "4":
    print("{} / {} = {}".format(a,b,a/b))
    print("İşleminiz Sonlandı..")
else:
    print("Lütfen Geçerli Bir İşlem Seçiniz!!")
    print("İşleminiz Sonlandı..")

print("nacWARE")
