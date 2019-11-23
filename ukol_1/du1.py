# Výpočet Marinova, Lambertova, Braunova a Mercartorova zobrazení

from math import radians, sin, tan, log

# zadání zobrazení
# pokud uživetel zadá jiné písmeno, než tato definovaná, program ho upozorní a skončí
zobrazeni = input("Zadej písmeno zobrazení (A - Marinovo, B - Braunovo, L - Lambertovo, nebo M - Marcatorovo):")
if zobrazeni not in ["A", "B", "L", "M"]:
    print("Zadej správné písmeno zobrazení!")
    quit()

# volitelný poloměr Země
# vrací zadaný poloměr přepočtený na cm
# pokud uživatel zadá 0, je poloměr roven 6371,11 km
# zadání záporného poloměru není matematicky korektní, proto v tomto případě program skončí
polomer_km = float(input("Zadej poloměr Země v km (s desetinnou tečkou), nebo 0 pro poloměr 6371.11:"))
polomer_cm = polomer_km*100000
if polomer_cm == 0:
    polomer_cm = 637111000
elif polomer_cm < 0:
    print("Zadej správný poloměr Země!")
    quit()

# zadávání měřítka
# vrací zadané měřítko
# pokud uživatel zadá záporné nebo nulové měřítko, pogram skončí
meritko = int(input("Zadej měřítko (z tvaru 1:m pouze číslo m):"))
if meritko <= 0:
    print("Zadej správně měřítko!")
    quit()

seznam_rovnobezky = []
seznam_poledniky = []

# ošetření chybových hlášek při překročení vzdálenosti 1 m mezi přímkami sítě souřadnic
def prekroceni_delky_x(x):
    if x <= -100.0 or x >= 100.0:
        seznam_poledniky.append("-")
    else:
        seznam_poledniky.append(x)

def prekroceni_delky_y(y):
    if y <= -100.0 or y >= 100.0:
        seznam_rovnobezky.append("-")
    else:
        seznam_rovnobezky.append(y)

# výpočet poledníků je shodný pro všechna zobrazení
# vstupem je zadaný poloměr a měřítko
# vrací vypočtenou hodnotu s přesností na milimetry (proměnná x)
def vypocet_poledniky(polomer_cm, meritko):
    for zem_delka in range(-180, 190, 10):
        x = (round((polomer_cm*((radians(zem_delka)))/meritko),1)) # zaokrouhleno na 1 des. místo
        prekroceni_delky_x(x)


# 4 funkce na výpočet rovnoběžek dle zadaného zobrazení
# vstupem je zadané poloměr a měřítko
# výstupem je hodnota s přesností na milimetry (proměnná y)

def Marin_rovnobezky(polomer_cm, meritko):
    for zem_sirka in range(-90, 100, 10):
        y = (round((polomer_cm*((radians(zem_sirka)))/meritko), 1))
        prekroceni_delky_y(y)

def Lambert_rovnobezky(polomer_cm, meritko):
    for zem_sirka in range(-90, 100, 10):
        y = (round((polomer_cm*(sin(radians(zem_sirka)))/meritko), 1))
        prekroceni_delky_y(y)

def Braun_rovnobezky(polomer_cm, meritko):
    for zem_sirka in range(-90, 100, 10):
        y = (round((polomer_cm * (tan(((radians(zem_sirka)))/2))/meritko), 1))
        prekroceni_delky_y(y)

def Mercator_rovnobezky(polomer_cm, meritko):
    for zem_sirka in range(-90, 100, 10):
        d = 90 - zem_sirka
        if d == 0:
            return seznam_rovnobezky.append("-")
        elif d != 0:
            y = (round((polomer_cm*(log(1/(tan(radians((90-zem_sirka)/2)))))/meritko), 1))
            prekroceni_delky_y(y)

# funkce, která volá jednotlivé funkce na výpočet poledníků a rovnoběžek definované výše dle požadovaného zobrazení
# vstupem je zobrazení
def vypocti_zvolene_zobrazeni(zobrazeni):
    if zobrazeni == "A":
        Marin_rovnobezky(polomer_cm, meritko)
        return
    elif zobrazeni == "L":
        Lambert_rovnobezky(polomer_cm, meritko)
        return
    elif zobrazeni == "B":
        Braun_rovnobezky(polomer_cm, meritko)
        return
    elif zobrazeni == "M":
        Mercator_rovnobezky(polomer_cm, meritko)
        return
vypocti_zvolene_zobrazeni(zobrazeni)
vypocet_poledniky(polomer_cm, meritko)

# vypsání výsledků pomocí volání print()
# je zde ošetřen vstup poloměru 0 pro defaultně nastavený poloměr 6371.11 km

print("Zadané zobrazení:", zobrazeni)
# ošetřen výsledný výstup poloměru ve správných jednotkách
if polomer_km == 0:
    print("Zadaný poloměr Země je: 6371.11 km")
else:
    print("Zadaný poloměr Země je:", polomer_km, "km")
print("Zadané měřítko je: 1 :", meritko)
print("Rovnoběžky:", seznam_rovnobezky)
print("Poledníky:", seznam_poledniky)


# výpočet souřadnic libovolných bodů
# využívá zadané vstupy na začítku programu: zobrazení, poloměr a měřítko

# funkce, která dle zadaného zobrazení vypočte vzdálenost od bodu [0,0] po svislé ose
# vstupem je zeměpisná šířka, zobrazení, poloměr a měřítko
# řeší výpočet Mercatorova zobrazení při vstupu 90° nebo - 90° vypsáním "-", protože tato hodnota směřuje do nekonečna
def vypocti_zem_sirku_bodu(bod_zem_sirka, zobrazeni, polomer_cm, meritko):
    if zobrazeni == "A":
        y = (round((polomer_cm * ((radians(bod_zem_sirka))) / meritko), 1))
        souradnice_bodu.append(y)
    elif zobrazeni == "B":
        y = (round((polomer_cm * (sin(radians(bod_zem_sirka))) / meritko), 1))
        souradnice_bodu.append(y)
    elif zobrazeni == "L":
        y = (round((polomer_cm * (tan(((radians(bod_zem_sirka))) / 2)) / meritko), 1))
        souradnice_bodu.append(y)
    elif zobrazeni == "M":
        d = 90 - bod_zem_sirka
        if d == 0:
            souradnice_bodu.append("-")
        elif d == 180:
            souradnice_bodu.append("-")
        else:
            y = (round((polomer_cm * (log(1 / (tan((d) / 2))))) / meritko), 1)
            souradnice_bodu.append(y)

# funkce, která vypočte vzdálenost od bodu [0,0] po vodorovné ose
# vstupem je zeměpisná délka, poloměr a měřítko
def vypocti_zem_delku_bodu(bod_zem_delka, polomer_cm, meritko):
    x = (round((polomer_cm * ((radians(bod_zem_delka))) / meritko), 1))
    souradnice_bodu.append(x)

# volání výše definovaných funkcí a vypsání jejich výstupu v podobě seznamu
# program se ptá, dokud není zadán bod [0,0], po jeho zadání skončí
# řeší nesprávné vstupy - zadání větších stupňů než 90 a 180, respektive menších než -90° a -180°
while True:
    bod_zem_sirka = int(input("Zadej zeměpisnou šířku bodu:"))
    bod_zem_delka = int(input("Zadej zeměpisnou délku bodu:"))
    souradnice_bodu = []
    if bod_zem_sirka > 90 or bod_zem_sirka < -90:
        print("Zadaná nesprávná zeměpisná šířka! Zadej znovu.")
        continue
    elif bod_zem_delka > 180 or bod_zem_delka < -180:
        print("Zadaná nesprávná zeměpisná délka! Zadej znovu.")
        continue
    elif bod_zem_sirka == 0 and bod_zem_delka == 0:
        print("Zadaný bod [0,0], konec programu.")
        quit()
    vypocti_zem_sirku_bodu(bod_zem_sirka, zobrazeni, polomer_cm, meritko)
    vypocti_zem_delku_bodu(bod_zem_delka, polomer_cm, meritko)
    print("Souřadnice zadaného bodu jsou:", souradnice_bodu)