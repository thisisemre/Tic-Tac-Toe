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

def sablon():
    print(x_indexleri)
    for i in range(3):
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
    

