from random import randit

title = "PERMAINAN GUNTING BATU KERTAS"
print(title)
print(f"{'=' * len(title)}")

alat = ("gunting","batu","kertas")
player = input("Pilih alatnya!(gunting | batu | kertas):")
computer = alat[randit(0,2)]

if player == computer:
    print("Musuh:", computer)
    print("Kamu:", player)
    print("SERI COY! COBA LAGI!")

elif player == "batu":
    if computer == "kertas":
        print("Musuh:", computer)
        print("Kamu:", player)
        print("YAH KALAH...")
    elif computer == "gunting":
        print("Musuh:", computer)
        print("Kamu:", player)
        print("KAMU MENAG!!!")

elif player == "gunting":
    if computer == "batu":
        print("Musuh:", computer)
        print("Kamu:", player)
        print("YAH KALAH...")
    elif computer == "kertas":
        print("Musuh:", computer)
        print("Kamu:", player)
        print("KAMU MENAG!!!")

elif player == "kertas":
    if computer == "gunting":
        print("Musuh:", computer)
        print("Kamu:", player)
        print("YAH KALAH...")
    elif computer == "batu":
        print("Musuh:", computer)
        print("Kamu:", player)
        print("KAMU MENAG!!!")

else:
    print("SALAH NULIS TUH")





