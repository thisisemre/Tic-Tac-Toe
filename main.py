kordinat_sistemi = [["   " for x in range(3)] for y in range(3)]
oyun_sira = [0]
x_eksenleri = {
    "A": 0,
    "B": 1,
    "C": 2,
    "a": 0,
    "b": 1,
    "c": 2
}
x_indexleri = [f" {x} " for x in x_eksenleri if x <= "C"]
KILITLENME_DURUMU = ["X","O","X"]
def sablon():
    print("0",end=" ")
    print(x_indexleri)
    for i in range(3):
        print(i+1,end=" ")
        print(kordinat_sistemi[i])


def tas_kordinat_iste():
    if oyun_sira[0] % 2 == 0:
        tas_kordinat = input("Lütfen X koymak istediğiniz yerin kordinatlarını yazınız ")
    else:
        tas_kordinat = input("Lütfen O koymak istediğiniz yerin kordinatlarını yazınız ")
    while tas_kordinat[0] not in ["1","2","3"] and tas_kordinat[1].upper() not in x_indexleri:
        tas_kordinat = input("Tahtada olmayan bir konum girdiniz lütfen tekrar yazınız ")
    while kordinat_sistemi[int(tas_kordinat[0])-1][x_eksenleri[tas_kordinat[1]]] != "   ":
        tas_kordinat = input("İlgili konumda başka bir taş var lütfen tekrar giriniz ")
    
    return tas_kordinat

def tas_koy(tas_kordinat):
    if oyun_sira[0] % 2 == 0:
        kordinat_sistemi[int(tas_kordinat[0])-1][x_eksenleri[tas_kordinat[1]]] = "X"
    else:
        kordinat_sistemi[int(tas_kordinat[0])-1][x_eksenleri[tas_kordinat[1]]] = "O"
    oyun_sira[0] += 1

def oyun_bitti():
    if oyun_sira[0]%2==1:
        print("X oyunu kazandı. ")
    else:
        print("O oyunu kazandı. ")


def kilitlenme():
    for i in range(3):
        kilitli_mi_dikey = []
        kilitli_mi_çapraz = []
        kilitli_mi_çapraz_1=[]

        if kordinat_sistemi[i] == KILITLENME_DURUMU:#yatay
            oyun_bitti()
            return False
        for n in range(3):
            kilitli_mi_dikey.append(kordinat_sistemi[n][i])
            kilitli_mi_çapraz.append(kordinat_sistemi[n][n])

            for _ in range(2,-1,-1):
                kilitli_mi_çapraz_1.append(kordinat_sistemi[n][_])

        if kilitli_mi_dikey == KILITLENME_DURUMU:#dikey
            oyun_bitti()
            return False
        elif kilitli_mi_çapraz == KILITLENME_DURUMU or kilitli_mi_çapraz_1==KILITLENME_DURUMU:#çapraz
            oyun_bitti()
            return False
    return True

on = True
while on:
    sablon()
    tas_koy(tas_kordinat_iste())
    on = kilitlenme()
sablon()