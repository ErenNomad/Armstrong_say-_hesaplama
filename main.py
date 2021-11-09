name = str(input("Adınızı giriniz :"))
surname = str(input("Soyadınızı giriniz :"))
N = input("Bir N değeri giriniz (N en az 1000 olmalı) : ")


def armstrongNum():
    global name
    global surname
    global N
    global h
    armstrongnums = []
    while True:
        if int(N) >= 1000:

            for i in range(1, int(N) + 1):
                y = str(i)
                total = 0
                for x in y:
                    total = total + (int(x) ** 3)

                    if total == i:
                        armstrongnums.append(i)
                        h = len(armstrongnums)


                        if int(i) % int(len(name)) == 0 or (int(i) % int(len(surname)) == 0):
                            print(f"{i} Armstrong sayı değildir")
                            armstrongnums.remove(i)
                        else:
                            print(f"{i} Armstrong sayıdır")
        print(armstrongnums)
        return
