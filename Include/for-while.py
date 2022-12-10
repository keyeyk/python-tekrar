print("1 den başlayarak 10 a kadar yazdıran döngü modelini oluşturun.")
for i in range(1,10):
    print(i)

print(" ")

print("1 den başlayarak ikişer arttırarak 33 e kadar yazdıran programı modelleyin.")
for i in range(1,33,3):
    print(i)

print(" ")

print("20 den 10 a geri saydırarak gelen programı modelleyin.")
for i in reversed(range(10,20)):
    print(i)

print(" ")

print("metinsel ifade yazdıran programı modelleyin.")
for i in "for döngüsü calisiyoruz":
    print(i)

print(" ")

# dizilerle birlikte çalışma
a=[2,3,5,7,11,13]
for i in a:
    print(i)

print(" ")

print("*** While Döngüsü ***")
print("i değerimiz 10 a gelene kadar birer artacak ama 5 e gelince duracak.")
i=0
while i<10:
    print("%s.merhaba"%(i))
    i+=1
    if i==5:
        break