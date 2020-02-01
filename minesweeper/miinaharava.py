# Miinaharava Ari Lankinen
import pyglet
import time
import haravasto
import random

tila = {
    "pelikentta": [],''
                     ''
                     ''
    "tietokentta": [],
    "jaljella": [],
    "lopputulos": 0,
}
"""A sanakirja sisältää kaikki tilasoihin tarvittavat asiat. Arvot päivitetään pelin päätyttyä."""
A = {
    "kentan_korkeus": 10,
    "kentan_leveys": 10,
    "miinojen_maara": 10,
    "paivamaara": "1.1.2020 12.30",
    "minuutit": 0,
    "sekuntit": 0,
    "siirrot": 0,
    "lopputulos": "voitto",
    "aika_A": 0,
    "aika_B": 0
}            

def tilastotallennus(tiedosto):
    """funktio tallentaa päättyneen pelin tiedot tilastotiedostoon. Jos tiedostoa ei ole olemassa, funktio luo sen koneelle"""
    with open(tiedosto, "a") as kohde:
        kohde.write("{A},{B},{C},{D},{E},{F},{G},{H}\n".format(A=A["paivamaara"], B=A["minuutit"], C=A["sekuntit"], D=A["siirrot"], E=A["lopputulos"], F=A["kentan_leveys"], G=A["kentan_korkeus"], H=A["miinojen_maara"]))
            
def tilastolukija(tiedosto):
    """Kun käyttäjä valitsee alkuvalikossa tilastot, niin funktio lukee ne tiedostosta ja näyttää ne pelaajalle."""
    with open(tiedosto) as kohde:
        for rivi in kohde.readlines():
            T = rivi.rstrip("\n").split(",")
            print("{A}, pelin kesto: {B} minuuttia {C} sekuntia, siirrot: {D}, kentan koko: {F}x{G}, miinat: {H}, lopputulos: {E}".format(A=T[0], B=T[1], C=T[2], D=T[3], E=T[4], F=T[5], G=T[6], H=T[7]))
            
def valikko():
    """Valikko käynnistää main() funktion kun pelaaja valitsee uuden pelin."""
    try:
        operaatio = input("Valitse toiminto (1 = Uusi peli, 2 = Tilastot, 3 = Lopeta):")
    except ValueError:
        print("Anna luku 1-3")
    else:
        if operaatio == "1":
            main()
        elif operaatio == "2":
            tilastolukija("miinaharavatilastot.txt")   
            valikko()        
        elif operaatio == "3":
            haravasto.lopeta()
        else:
            valikko()
            
def kenttienluonti():
    """Funktio luo kaksi samankokoista 2-ulotteista listaa. Pelikenttä näytetään reaaliajassa pelaajalle. Tietokenttä
    sisältää myöhemmin tiedot jokaisen ruudun merkistä. Jaljella listaa käytetään apuna miinojen sijoittamisessa random
    paikkoihin ja että samaan ruutuun ei laiteta kahta miinaa."""
    tietokentta = [] 
    for rivi in range(A["kentan_korkeus"]):
        tietokentta.append([])
        for sarake in range(A["kentan_leveys"]):
            tietokentta[-1].append(" ")
    tila["tietokentta"] = tietokentta
    
    jaljella = []
    for x in range(A["kentan_leveys"]):
        for y in range(A["kentan_korkeus"]):
            jaljella.append((x, y))
    for i in range(A["miinojen_maara"]):
        x, y = random.choice(jaljella)
        tietokentta[y][x] = "x"
        jaljella.remove((x, y))
        
    pelikentta = []
    for rivi in range(A["kentan_korkeus"]):
        pelikentta.append([])
        for sarake in range(A["kentan_leveys"]):
            pelikentta[-1].append(" ")
    tila["pelikentta"] = pelikentta
    
def laskemiinat(x, y, tietokentta):
    """Laskee yksittäisen ruudun ympärillä olevat miinat"""
    pommit = 0
    for i in range(y - 1, y + 2):
        for j in range(x - 1, x + 2):
            if i >= 0 and j >= 0 and j < len(tila["tietokentta"][0]) and i < len(tila["tietokentta"]):
                if tila["tietokentta"][i][j] == 'x':
                    pommit += 1
    if tila["tietokentta"][y][x] == 'x':
        tila["tietokentta"][y][x] = 'x'
    else:
        tila["tietokentta"][y][x] = pommit
    
def tietokentanpaivitys():
    """Käy läpi yksitellen jokaisen ruudun tietokentässä ja kutsuu jokaisen ruudun kohdalla laskemiinat funktiota
    joka antaa kyseisen ruudn ympärillä olevien miinojen määrän. Miinojen määrä päivitetään tietokenttään arvona 1-8"""
    for y in range(A["kentan_korkeus"]):
        for x in range(A["kentan_leveys"]):
            laskemiinat(x, y, tila["tietokentta"])

def piirra_kentta():
    """Piirtää piirtää käyttäjän haluaman kokoisen ikkunan. Ikkunan koko on leveys on 40 kertaa kentän leveys. Korkeudella sama"""
    haravasto.tyhjaa_ikkuna()
    haravasto.piirra_tausta()  
    haravasto.aloita_ruutujen_piirto()
    for y, rivi in enumerate(tila["pelikentta"]):
        for x, avain in enumerate(tila["pelikentta"][y]):
            haravasto.lisaa_piirrettava_ruutu(avain, x * 40, y * 40)
    haravasto.piirra_ruudut()

def kasittele_hiiri(hiiriX, hiiriY, hiirenpainike, painetut_muokkausnappaimet):
    """Tunnistaa klikatun hiirenpainikkeen ja koordinaatin. Jos tietokentän kyseisessä ruudussa on x niin pelaaja häviää pelin
    ja tilastot tallennetaan A sanakirjaan. Jos 0, niin kutsutaan tulvatäyttöä. Muissa tapauksissa tietokenta ruutu 
    päivitetään samaan kohtaa pelikenttään. Jokaisella hiiren vasemmalla painalluksella tarkistetaan myös, onko lopputulos valmis.
    Jos on niin ikkuna suljetaan ja peli palaa valikkoon"""
    x = int(hiiriX // 40)
    y = int(hiiriY // 40)
    painallus = int(hiirenpainike)
    if painallus == haravasto.HIIRI_VASEN:
        if tila["lopputulos"] == "valmis":
            tila["lopputulos"] = " "
            haravasto.lopeta()
            valikko()
        elif tila["tietokentta"][y][x] == 0:
            A["siirrot"] = A["siirrot"] + 1
            tulvataytto(tila["tietokentta"], x, y)
        elif tila["tietokentta"][y][x] == 'x':
            A["siirrot"] = A["siirrot"] + 1
            A["lopputulos"] = "tappio"
            A["aika_B"] = time.time()
            A["minuutit"] = int(round((A["aika_B"] - A["aika_A"] - 30) / 60, 0))
            A["sekuntit"] = int(round(A["aika_B"] - A["aika_A"] - (A["minuutit"] * 60), 0))
            tilastotallennus("miinaharavatilastot.txt")
            print("Hävisit")
            tila["pelikentta"] = tila["tietokentta"]
            tila["lopputulos"] = "valmis"
        else:  
            A["siirrot"] = A["siirrot"] + 1
            tila["pelikentta"][y][x] = tila["tietokentta"][y][x]
    elif painallus == haravasto.HIIRI_OIKEA:
        tila["pelikentta"][y][x] = 'f'
    tarkastavoitto()

def tarkastavoitto():
    """Tämä funktio laskee kutsuttaessa, onko avaamattomia ja liputettuja ruutuja
    yhteensä saman verran kuin miinoja. Jos on niin peli päättyy ja tila["lopputulos"] saa arvon valmis ja muut tilastotiedot
    tallennetaan myös sanakirjaan A. Sum-lause löydetty netistä"""
    tulos_1 = sum([i.count(' ') for i in tila["pelikentta"]])
    tulos_2 = sum([i.count('f') for i in tila["pelikentta"]])
    avaamattomat_ruudut = tulos_1 + tulos_2
    if avaamattomat_ruudut == A["miinojen_maara"]:
        print("Voitit")
        A["lopputulos"] = "voitto"
        A["aika_B"] = time.time()
        A["minuutit"] = int(round((A["aika_B"] - A["aika_A"] - 30) / 60, 0))
        A["sekuntit"] = int(round(A["aika_B"] - A["aika_A"] - (A["minuutit"] * 60), 0))
        tilastotallennus("miinaharavatilastot.txt")
        tila["pelikentta"] = tila["tietokentta"]
        tila["lopputulos"] = "valmis"

        
def aloitusfunktio():
    """Tämä funktio luo peli-ikkunan ja käynnistää hiiren käsittelijän"""
    haravasto.lataa_kuvat("spritet")
    haravasto.luo_ikkuna(A["kentan_leveys"] * 40, A["kentan_korkeus"] * 40)
    haravasto.aseta_piirto_kasittelija(piirra_kentta)
    haravasto.aseta_hiiri_kasittelija(kasittele_hiiri)
    haravasto.aloita()
    
def tulvataytto(tietokentta, x_koordinaatti, y_koordinaatti):
    """Tulvatäyttöfunktiota kutsutaan jos pelaaja klikkaa ruutua, jossa on 0. Tulvatäyttö etsii ympärillä olevat tyhjät
    ruudut ja laajenee siihen asti kunnes vastaan tulee nollasta eroava ruutu. "Täyttää myös luvut 1-8 nollien ympärillä
    oleviin ruutuihin. Kaikki tulvatäytön avaamat luvut päivitetään pelikenttään ja näytetään pelaajalle."""
    aloituspiste = [(x_koordinaatti, y_koordinaatti)]
    while aloituspiste:
        muuttuja = aloituspiste.pop(-1)
        x = int(muuttuja[0])
        y = int(muuttuja[1])
        tila["pelikentta"][y][x] = tila["tietokentta"][y][x]
        if tila["tietokentta"][y][x] == 0:
            for i in range(y - 1, y + 2):
                for j in range(x - 1, x + 2):
                    if i >= 0 and j >= 0 and j < len(tila["tietokentta"][0]) and i < len(tila["tietokentta"]):
                        if tila["pelikentta"][i][j] == ' ':
                            aloituspiste.append((j, i))

def main():
    """Main funktio pyytää käyttäjältä kentän tiedot ja luo pelikentän kutsumalla kenttienluontifunktiota, sekä
    tietokentanpaivitysfunktiota."""
    while True:
        try:
            A["kentan_leveys"] = int(input("Anna kentän leveys(1-48):"))
            A["kentan_korkeus"] = int(input("Anna kentän korkeus(1-24):"))
            A["miinojen_maara"] = int(input("Anna miinojen määrä:"))
        except ValueError:
            print("Anna kokonaisluku:")
        else:
            if A["kentan_leveys"] > 48 or A["kentan_leveys"] <= 0:
                print("Kentän leveyden täytyy olla 1-48")
            elif A["kentan_korkeus"] > 24 or A["kentan_korkeus"] <= 0:
                print("Kentän korkeuden täytyy olla 1-24")
            elif A["miinojen_maara"] > A["kentan_korkeus"] * A["kentan_leveys"] or A["miinojen_maara"] < 0:
                print("Miinoja ei voi olla enemmän kuin ruutuja, eikä vähemmän kuin 0")
            else:
                break
    A["siirrot"] = 0
    A["paivamaara"] = "{A}.{B}.{C} {D}:{E}".format(A=time.localtime()[2], B=time.localtime()[1], C=time.localtime()[0], D=time.localtime()[3], E=format(time.localtime()[4], "02"))
    A["aika_A"] = time.time()
    kenttienluonti()
    tietokentanpaivitys()
    aloitusfunktio()
"""Valikkoa kutsutaan pelin alussa automaattisesti. Tästä seuraan loputon silmukka, kunnes käyttäjä lopettaa pelin"""
valikko()