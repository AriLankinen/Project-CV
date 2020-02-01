from pprint import pprint
import pygame
import random
import time


kenttä = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]

jäljellä = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

A = {
    "ruutu": 0,
    "edellinen": "O",
    "siirrot": 0,
    "livedata": [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    "X": 0,
    "O": 0,
    "tasapelit": 0,
    "tilanne": "kesken",
    "pause": 0,
    "tallennus": 0,
    "jäljellä": [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    "AIdata": [],
    "musiikki": 1,
    "superäly": 0,
    "älykenttä": [],
    "ekaruutu": 10
}

tausta = pygame.image.load("ristinolla kuvat/tausta.png")
risti = pygame.image.load("ristinolla kuvat/risti.png")
nolla = pygame.image.load("ristinolla kuvat/nolla.png")
valikkotausta = pygame.image.load("ristinolla kuvat/valikko.png")
pygame.mixer.init()
pygame.mixer.music.load("ristinolla kuvat/black hole.wav")


def soitin():
    if A["musiikki"] == 1:
            while not pygame.mixer.music.get_busy():
                pygame.mixer.music.play(1)
    else:
        pygame.mixer.music.stop()


def siirto():
    A["jäljellä"][A["ruutu"]] = 'k'
    A["siirrot"] += 1
    if A["tallennus"] == 1:
        livedatanpäivittäjä()
    rivi = A["ruutu"] // 3
    sarake = divmod(A["ruutu"], 3)[1]
    if A["edellinen"] == "O":
        kenttä[rivi][sarake] = "X"
        A["edellinen"] = "X"
        ikkuna.blit(risti, (sarake * 200, rivi * 200 + 60))
    else:
        kenttä[rivi][sarake] = "O"
        A["edellinen"] = "O"
        ikkuna.blit(nolla, (sarake * 200, rivi * 200 + 60))
    pygame.display.update()
    pprint(kenttä[0])
    pprint(kenttä[1])
    pprint(kenttä[2])
    tarkistavoitto()


def tarkistavoitto():
    while True:
        for y in range(0, 3):
            if A["tilanne"] == "kesken":
                if kenttä[y][0] == kenttä[y][1] == kenttä[y][2] == A["edellinen"]:
                    voitto()
                    break
        for x in range(0, 3):
            if A["tilanne"] == "kesken":
                if kenttä[0][x] == kenttä[1][x] == kenttä[2][x] == A["edellinen"]:
                    voitto()
                    break
        if kenttä[0][0] == kenttä[1][1] == kenttä[2][2] == A["edellinen"]:
            voitto()
            break
        elif kenttä[0][2] == kenttä[1][1] == kenttä[2][0] == A["edellinen"]:
            voitto()
            break
        elif A["siirrot"] == 9 and A["tilanne"] == "kesken":
            print("tasapeli")
            A["tasapelit"] += 1
            A["tilanne"] = "valmis"
            fontti = pygame.font.SysFont("playbill", 130)
            voittaja = fontti.render(("Tasapeli"), False, (122, 0, 122))
            ikkuna.blit(voittaja, (170, 280))
            if A["tallennus"] == 1:
                tallentaja()
            break
        else:
            break
    pygame.display.update()


def voitto():
    pygame.font.init()
    fontti = pygame.font.SysFont("playbill", 160)
    if A["edellinen"] == "X":
        print("X voitti")
        A["X"] += 1
        voittaja = fontti.render(("X VOITTI!"), False, (0, 0, 255))
        A["tilanne"] = "valmis"
    elif A["edellinen"] == "O":
        print("O voitti")
        A["O"] += 1
        if A["tallennus"] == 1:
            tallentaja()
        A["tilanne"] = "valmis"
        voittaja = fontti.render(("O VOITTI!"), False, (255, 0, 0))
    ikkuna.blit(voittaja, (110, 280))


def nollaus():
    kenttä[0] = [' ', ' ', ' ']
    kenttä[1] = [' ', ' ', ' ']
    kenttä[2] = [' ', ' ', ' ']
    A["jäljellä"] = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    A["siirrot"] = 0
    A["livedata"] = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    print("Tilanne: X ({A} - {B}) O tasapelit: {C}". format(A=A["X"], B=A["O"], C=A["tasapelit"]))
    pprint(kenttä[0])
    pprint(kenttä[1])
    pprint(kenttä[2])
    ikkuna.fill((255, 255, 255))
    ikkuna.blit(tausta, (0, 60))
    tulostaulu()
    pygame.display.update()
    if A["tallennus"] == 1:
        if A["edellinen"] == "X":
            A["livedata"][0] = 0
        elif A["edellinen"] == "O":
            A["livedata"][0] = 1


def tulostaulu():
    pygame.font.init()
    fontti = pygame.font.SysFont("playbill", 50)
    valikko = fontti.render(("VALIKKO"), False, (30, 140, 20))
    tulos = fontti.render("{A} - {B}".format(A=A["X"], B=A["O"]), False, (0, 0, 0))
    risti = fontti.render(("risti"), False, (0, 0, 255))
    nolla = fontti.render(("nolla"), False, (255, 0, 0))
    tulostasapeli = fontti.render("tasapelit: {}".format(A["tasapelit"]), False, (122, 0, 122))
    ikkuna.blit(valikko, (20, 10))
    ikkuna.blit(risti, (190, 10))
    ikkuna.blit(tulos, (250, 10))
    ikkuna.blit(nolla, (340, 10))
    ikkuna.blit(tulostasapeli, (450, 10))


def classic():
    ikkuna.fill((255, 255, 255))
    ikkuna.blit(tausta, (0, 60))
    tulostaulu()
    tila = True
    pygame.display.update()
    while tila:
        for event in pygame.event.get():
            pygame.display.update()
            c = 12
            soitin()
            if event.type == pygame.QUIT:
                nollaus()
                valikko()
                tila = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                R = (y - 60) // 200
                S = x // 200
                if R == 0 and S == 0:
                    c = 0
                elif R == 0 and S == 1:
                    c = 1
                elif R == 0 and S == 2:
                    c = 2
                elif R == 1 and S == 0:
                    c = 3
                elif R == 1 and S == 1:
                    c = 4
                elif R == 1 and S == 2:
                    c = 5
                elif R == 2 and S == 0:
                    c = 6
                elif R == 2 and S == 1:
                    c = 7
                elif R == 2 and S == 2:
                    c = 8
                elif R == -1 and S == 0:
                    nollaus()
                    tila = False
                    valikko()
                if A["tilanne"] == "kesken":
                    if c < 9 and c >= 0:
                        if not A["jäljellä"][c] == "k":
                            A["ruutu"] = c
                            siirto()
                elif A["tilanne"] == "valmis":
                    A["tilanne"] = "kesken"
                    c = 10
                    tulostaulu()
                    nollaus()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    c = 0
                elif event.key == pygame.K_w:
                    c = 1
                elif event.key == pygame.K_e:
                    c = 2
                elif event.key == pygame.K_a:
                    c = 3
                elif event.key == pygame.K_s:
                    c = 4
                elif event.key == pygame.K_d:
                    c = 5
                elif event.key == pygame.K_z:
                    c = 6
                elif event.key == pygame.K_x:
                    c = 7
                elif event.key == pygame.K_c:
                    c = 8
                elif event.key == pygame.K_ESCAPE:
                    nollaus()
                    tila = False
                    valikko()
                if A["tilanne"] == "kesken":
                    if c < 9 and c >= 0:
                        if not A["jäljellä"][c] == "k":
                            A["ruutu"] = c
                            siirto()
                elif A["tilanne"] == "valmis":
                    A["tilanne"] = "kesken"
                    c = 10
                    nollaus()


def bottipeli():
    ikkuna.fill((255, 255, 255))
    ikkuna.blit(tausta, (0, 60))
    tulostaulu()
    tila = True
    pygame.display.update()
    while tila:
        for event in pygame.event.get():
            soitin()
            pygame.display.update()
            c = 12
            if event.type == pygame.QUIT:
                nollaus()
                valikko()
                tila = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if A["tilanne"] == "valmis":
                    A["tilanne"] = "kesken"
                    c = 10
                    tulostaulu()
                    nollaus()
                elif A["edellinen"] == "O":
                    x, y = event.pos
                    R = (y - 60) // 200
                    S = x // 200
                    if R == 0 and S == 0:
                        c = 0
                    elif R == 0 and S == 1:
                        c = 1
                    elif R == 0 and S == 2:
                        c = 2
                    elif R == 1 and S == 0:
                        c = 3
                    elif R == 1 and S == 1:
                        c = 4
                    elif R == 1 and S == 2:
                        c = 5
                    elif R == 2 and S == 0:
                        c = 6
                    elif R == 2 and S == 1:
                        c = 7
                    elif R == 2 and S == 2:
                        c = 8
                    elif R == -1 and S == 0:
                        nollaus()
                        tila = False
                        valikko()
                    if c < 9 and c >= 0:
                        if not A["jäljellä"][c] == "k":
                            A["ruutu"] = c
                            siirto()
                    if A["edellinen"] == "X" and A["tilanne"] == "kesken":
                        if A["tallennus"] == 1:
                            lukija()
                        arpoja()
                elif A["edellinen"] == "X" and A["tilanne"] == "kesken":
                    if A["tallennus"] == 1:
                        lukija()
                    arpoja()
            elif event.type == pygame.KEYDOWN:
                if A["tilanne"] == "valmis":
                    A["tilanne"] = "kesken"
                    c = 10
                    tulostaulu()
                    nollaus()
                elif A["edellinen"] == "O":
                    if event.key == pygame.K_q:
                        c = 0
                    elif event.key == pygame.K_w:
                        c = 1
                    elif event.key == pygame.K_e:
                        c = 2
                    elif event.key == pygame.K_a:
                        c = 3
                    elif event.key == pygame.K_s:
                        c = 4
                    elif event.key == pygame.K_d:
                        c = 5
                    elif event.key == pygame.K_z:
                        c = 6
                    elif event.key == pygame.K_x:
                        c = 7
                    elif event.key == pygame.K_c:
                        c = 8
                    elif event.key == pygame.K_ESCAPE:
                        nollaus()
                        tila = False
                        valikko()
                    if c < 9 and c >= 0:
                        if not A["jäljellä"][c] == "k":
                            A["ruutu"] = c
                            siirto()
                    if A["edellinen"] == "X" and A["tilanne"] == "kesken":
                        if A["tallennus"] == 1:
                            lukija()
                        arpoja()
                elif A["edellinen"] == "X" and A["tilanne"] == "kesken":
                    if A["tallennus"] == 1:
                        lukija()
                    arpoja()


def viisasbotti():
    A["tallennus"] = 1
    A["livedata"][0] = 1
    bottipeli()


def arpoja():
    if A["tallennus"] == 0:
        if not A["siirrot"] == 0:
            A["pause"] = 1
            time.sleep(0)
            A["pause"] = 0
        while True:
            c = random.randint(0, 8)
            if not A["jäljellä"][c] == "k":
                A["ruutu"] = c
                siirto()
                break
    elif A["tallennus"] == 1:
        if not A["siirrot"] == 0:
            A["pause"] = 1
            time.sleep(0)
            A["pause"] = 0
            yritykset = 0
            while True:
                c = random.randint(0, 8)
                if not A["jäljellä"][c] == "k":
                    yritykset += 1
                    if c in A["AIdata"]:
                        A["ruutu"] = c
                        siirto()
                        A["AIdata"] = []
                        break
                    elif yritykset == 100:
                        A["ruutu"] = c
                        siirto()
                        A["AIdata"] = []
                        break
        elif A["siirrot"] == 0:
            c = random.randint(0, 8)
            A["ruutu"] = c
            siirto()


def livedatanpäivittäjä():
    if A["siirrot"] == 1:
        A["ekaruutu"] = A["ruutu"]
        if A["ruutu"] == 4:
            A["livedata"][1] = 4
        else:
            A["livedata"][1] = 0
    elif A["ekaruutu"] == 0 or A["ekaruutu"] == 4:
        A["livedata"][A["siirrot"]] = A["ruutu"]
    else:
        if A["ekaruutu"] == 1:
            if A["ruutu"] == 0:
                A["livedata"][A["siirrot"]] = 3
            elif A["ruutu"] == 1:
                A["livedata"][A["siirrot"]] = 2
            elif A["ruutu"] == 2:
                A["livedata"][A["siirrot"]] = 1
            elif A["ruutu"] == 3:
                A["livedata"][A["siirrot"]] = 6
            elif A["ruutu"] == 5:
                A["livedata"][A["siirrot"]] = 2
            elif A["ruutu"] == 6:
                A["livedata"][A["siirrot"]] = 7
            elif A["ruutu"] == 7:
                A["livedata"][A["siirrot"]] = 8
            elif A["ruutu"] == 8:
                A["livedata"][A["siirrot"]] = 5
            elif A["ruutu"] == 4:
                A["livedata"][A["siirrot"]] = 4
        elif A["ekaruutu"] == 2:
            if A["ruutu"] == 0:
                A["livedata"][A["siirrot"]] = 6
            elif A["ruutu"] == 1:
                A["livedata"][A["siirrot"]] = 3
            elif A["ruutu"] == 2:
                A["livedata"][A["siirrot"]] = 0
            elif A["ruutu"] == 3:
                A["livedata"][A["siirrot"]] = 7
            elif A["ruutu"] == 5:
                A["livedata"][A["siirrot"]] = 1
            elif A["ruutu"] == 6:
                A["livedata"][A["siirrot"]] = 8
            elif A["ruutu"] == 7:
                A["livedata"][A["siirrot"]] = 5
            elif A["ruutu"] == 8:
                A["livedata"][A["siirrot"]] = 2
            elif A["ruutu"] == 4:
                A["livedata"][A["siirrot"]] = 4
        elif A["ekaruutu"] == 3:
            if A["ruutu"] == 0:
                A["livedata"][A["siirrot"]] = 1
            elif A["ruutu"] == 1:
                A["livedata"][A["siirrot"]] = 2
            elif A["ruutu"] == 2:
                A["livedata"][A["siirrot"]] = 5
            elif A["ruutu"] == 3:
                A["livedata"][A["siirrot"]] = 0
            elif A["ruutu"] == 5:
                A["livedata"][A["siirrot"]] = 8
            elif A["ruutu"] == 6:
                A["livedata"][A["siirrot"]] = 3
            elif A["ruutu"] == 7:
                A["livedata"][A["siirrot"]] = 6
            elif A["ruutu"] == 8:
                A["livedata"][A["siirrot"]] = 7
            elif A["ruutu"] == 4:
                A["livedata"][A["siirrot"]] = 4
        elif A["ekaruutu"] == 5:
            if A["ruutu"] == 0:
                A["livedata"][A["siirrot"]] = 7
            elif A["ruutu"] == 1:
                A["livedata"][A["siirrot"]] = 6
            elif A["ruutu"] == 2:
                A["livedata"][A["siirrot"]] = 3
            elif A["ruutu"] == 3:
                A["livedata"][A["siirrot"]] = 8
            elif A["ruutu"] == 5:
                A["livedata"][A["siirrot"]] = 0
            elif A["ruutu"] == 6:
                A["livedata"][A["siirrot"]] = 5
            elif A["ruutu"] == 7:
                A["livedata"][A["siirrot"]] = 2
            elif A["ruutu"] == 8:
                A["livedata"][A["siirrot"]] = 1
            elif A["ruutu"] == 4:
                A["livedata"][A["siirrot"]] = 4
        elif A["ekaruutu"] == 6:
            if A["ruutu"] == 0:
                A["livedata"][A["siirrot"]] = 2
            elif A["ruutu"] == 1:
                A["livedata"][A["siirrot"]] = 5
            elif A["ruutu"] == 2:
                A["livedata"][A["siirrot"]] = 8
            elif A["ruutu"] == 3:
                A["livedata"][A["siirrot"]] = 1
            elif A["ruutu"] == 5:
                A["livedata"][A["siirrot"]] = 7
            elif A["ruutu"] == 6:
                A["livedata"][A["siirrot"]] = 0
            elif A["ruutu"] == 7:
                A["livedata"][A["siirrot"]] = 3
            elif A["ruutu"] == 8:
                A["livedata"][A["siirrot"]] = 6
            elif A["ruutu"] == 4:
                A["livedata"][A["siirrot"]] = 4
        elif A["ekaruutu"] == 7:
            if A["ruutu"] == 0:
                A["livedata"][A["siirrot"]] = 5
            elif A["ruutu"] == 1:
                A["livedata"][A["siirrot"]] = 8
            elif A["ruutu"] == 2:
                A["livedata"][A["siirrot"]] = 7
            elif A["ruutu"] == 3:
                A["livedata"][A["siirrot"]] = 2
            elif A["ruutu"] == 5:
                A["livedata"][A["siirrot"]] = 6
            elif A["ruutu"] == 6:
                A["livedata"][A["siirrot"]] = 1
            elif A["ruutu"] == 7:
                A["livedata"][A["siirrot"]] = 0
            elif A["ruutu"] == 8:
                A["livedata"][A["siirrot"]] = 3
            elif A["ruutu"] == 4:
                A["livedata"][A["siirrot"]] = 4
        elif A["ekaruutu"] == 8:
            if A["ruutu"] == 0:
                A["livedata"][A["siirrot"]] = 8
            elif A["ruutu"] == 1:
                A["livedata"][A["siirrot"]] = 7
            elif A["ruutu"] == 2:
                A["livedata"][A["siirrot"]] = 6
            elif A["ruutu"] == 3:
                A["livedata"][A["siirrot"]] = 3
            elif A["ruutu"] == 5:
                A["livedata"][A["siirrot"]] = 0
            elif A["ruutu"] == 6:
                A["livedata"][A["siirrot"]] = 1
            elif A["ruutu"] == 7:
                A["livedata"][A["siirrot"]] = 2
            elif A["ruutu"] == 8:
                A["livedata"][A["siirrot"]] = 5
            elif A["ruutu"] == 4:
                A["livedata"][A["siirrot"]] = 4


def lukija():
    if A["superäly"] == 0:
        with open("ristinollaAI.txt", "r") as kohde:
            for rivi in kohde.readlines():
                apudata = rivi.rstrip("\n").split(",")
                apulaskuri = 0
                luku = (A["siirrot"] + 1)
                for i in range(luku):
                    if int(apudata[i]) == int(A["livedata"][i]):
                        apulaskuri += 1
                if apulaskuri == luku:
                        A["ruutu"] = int(apudata[(luku)])
                        if A["ekaruutu"] == 0 or A["ekaruutu"] == 4:
                            B = A["ruutu"]
                        elif A["ekaruutu"] == 1:
                            if A["ruutu"] == 0:
                                B = 3
                            elif A["ruutu"] == 1:
                                B = 2
                            elif A["ruutu"] == 2:
                                B = 1
                            elif A["ruutu"] == 3:
                                B = 6
                            elif A["ruutu"] == 5:
                                B = 2
                            elif A["ruutu"] == 6:
                                B = 7
                            elif A["ruutu"] == 7:
                                B = 8
                            elif A["ruutu"] == 8:
                                B = 5
                            elif A["ruutu"] == 4:
                                B = 4
                        elif A["ekaruutu"] == 2:
                            if A["ruutu"] == 0:
                                B = 6
                            elif A["ruutu"] == 1:
                                B = 3
                            elif A["ruutu"] == 2:
                                B = 0
                            elif A["ruutu"] == 3:
                                B = 7
                            elif A["ruutu"] == 5:
                                B = 1
                            elif A["ruutu"] == 6:
                                B = 8
                            elif A["ruutu"] == 7:
                                B = 5
                            elif A["ruutu"] == 8:
                                B = 2
                            elif A["ruutu"] == 4:
                                B = 4
                        elif A["ekaruutu"] == 3:
                            if A["ruutu"] == 0:
                                B = 1
                            elif A["ruutu"] == 1:
                                B = 2
                            elif A["ruutu"] == 2:
                                B = 5
                            elif A["ruutu"] == 3:
                                B = 0
                            elif A["ruutu"] == 5:
                                B = 8
                            elif A["ruutu"] == 6:
                                B = 3
                            elif A["ruutu"] == 7:
                                B = 6
                            elif A["ruutu"] == 8:
                                B = 7
                            elif A["ruutu"] == 4:
                                B = 4
                        elif A["ekaruutu"] == 5:
                            if A["ruutu"] == 0:
                                B = 7
                            elif A["ruutu"] == 1:
                                B = 6
                            elif A["ruutu"] == 2:
                                B = 3
                            elif A["ruutu"] == 3:
                                B = 8
                            elif A["ruutu"] == 5:
                                B = 0
                            elif A["ruutu"] == 6:
                                B = 5
                            elif A["ruutu"] == 7:
                                B = 2
                            elif A["ruutu"] == 8:
                                B = 1
                            elif A["ruutu"] == 4:
                                B = 4
                        elif A["ekaruutu"] == 6:
                            if A["ruutu"] == 0:
                                B = 2
                            elif A["ruutu"] == 1:
                                B = 5
                            elif A["ruutu"] == 2:
                                B = 8
                            elif A["ruutu"] == 3:
                                B = 1
                            elif A["ruutu"] == 5:
                                B = 7
                            elif A["ruutu"] == 6:
                                B = 0
                            elif A["ruutu"] == 7:
                                B = 3
                            elif A["ruutu"] == 8:
                                B = 6
                            elif A["ruutu"] == 4:
                                B = 4
                        elif A["ekaruutu"] == 7:
                            if A["ruutu"] == 0:
                                B = 5
                            elif A["ruutu"] == 1:
                                B = 8
                            elif A["ruutu"] == 2:
                                B = 7
                            elif A["ruutu"] == 3:
                                B = 2
                            elif A["ruutu"] == 5:
                                B = 6
                            elif A["ruutu"] == 6:
                                B = 1
                            elif A["ruutu"] == 7:
                                B = 0
                            elif A["ruutu"] == 8:
                                B = 3
                            elif A["ruutu"] == 4:
                                B = 4
                        if A["ekaruutu"] == 8:
                            if A["ruutu"] == 0:
                                B = 8
                            elif A["ruutu"] == 1:
                                B = 7
                            elif A["ruutu"] == 2:
                                B = 6
                            elif A["ruutu"] == 3:
                                B = 3
                            elif A["ruutu"] == 5:
                                B = 0
                            elif A["ruutu"] == 6:
                                B = 1
                            elif A["ruutu"] == 7:
                                B = 2
                            elif A["ruutu"] == 8:
                                B = 5
                            elif A["ruutu"] == 4:
                                B = 4



                        if B not in A["AIdata"]:
                            A["AIdata"].append(B)
    elif A["superäly"] == 1:
        with open("ristinolla_superAI.txt", "r") as kohde:
            for rivi in kohde.readlines():
                for rivi in kohde.readlines():
                    apudata = rivi.rstrip("\n").split(",")
                    apulaskuri = 0
                    luku = (A["siirrot"] + 1)
                    for i in range(luku):
                        if int(apudata[i]) == int(A["livedata"][i]):
                            apulaskuri += 1
                        if apulaskuri == luku:
                            if int(apudata[(luku)]) not in A["AIdata"]:
                                A["AIdata"].append(int(apudata[(luku)]))


def tallentaja():
    if A["superäly"] == 0:
        with open("ristinollaAI.txt", "a") as kohde:
            kohde.write("{A},{B},{C},{D},{E},{F},{G},{H},{J},{K}\n".format(A=A["livedata"][0], B=A["livedata"][1], \
                        C=A["livedata"][2], D=A["livedata"][3], E=A["livedata"][4], F=A["livedata"][5], \
                        G=A["livedata"][6], H=A["livedata"][7], J=A["livedata"][8], K=A["livedata"][9]))
    elif A["superäly"] == 1:
        with open("ristinolla_superAI.txt", "a") as kohde:
            kohde.write("{A},{B},{C},{D},{E},{F},{G},{H},{J},{K}\n".format(A=A["livedata"][0], B=A["livedata"][1], \
                        C=A["livedata"][2], D=A["livedata"][3], E=A["livedata"][4], F=A["livedata"][5], \
                        G=A["livedata"][6], H=A["livedata"][7], J=A["livedata"][8], K=A["livedata"][9]))


def valikko():
    soitin()
    ikkuna.blit(valikkotausta, (0, 0))
    pygame.font.init()
    fontti = pygame.font.SysFont("playbill", 100)
    classi = fontti.render(("CLASSIC"), False, (30, 140, 20))
    tyhmä = fontti.render(("TYHMÄ"), False, (190, 190, 0))
    botti = fontti.render(("BOTTI"), False, (190, 190, 0))
    vbotti = fontti.render(("BOTTI"), False, (240, 110, 0))
    sbotti = fontti.render(("BOTTI"), False, (255, 40, 0))
    viisas = fontti.render(("VIISAS"), False, (240, 110, 0))
    super = fontti.render(("SUPER"), False, (255, 40, 0))
    fontti = pygame.font.SysFont("playbill", 60)
    sulje = fontti.render(("SULJE"), False, (0, 0, 0))
    ääni = fontti.render(("MUSIIKKI"), False, (0, 0, 0))
    ikkuna.blit(sulje, (40, 40))
    ikkuna.blit(ääni, (420, 40))
    ikkuna.blit(classi, (50, 220))
    ikkuna.blit(tyhmä, (370, 180))
    ikkuna.blit(botti, (370, 260))
    ikkuna.blit(vbotti, (70, 520))
    ikkuna.blit(sbotti, (370, 520))
    ikkuna.blit(viisas, (70, 440))
    ikkuna.blit(super, (370, 440))
    pygame.display.update()
    tila = True
    while tila:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                R = (y - 120) // 200
                S = x // 300
                if R == 0 and S == 0:
                    classic()
                elif R == 0 and S == 1:
                    bottipeli()
                elif R == 1 and S == 0:
                    viisasbotti()
                elif R == 1 and S == 1:
                    A["superäly"] = 1
                    viisasbotti()
                elif R == -1 and S == 0:
                    pygame.quit()
                elif R == -1 and S == 1:
                    if A["musiikki"] == 1:
                        A["musiikki"] = 0
                        soitin()
                    elif A["musiikki"] == 0:
                        A["musiikki"] = 1
                        soitin()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    classic()
                elif event.key == pygame.K_d:
                    bottipeli()
                elif event.key == pygame.K_z:
                    viisasbotti()
                elif event.key == pygame.K_c:
                    A["superäly"] = 1
                    viisasbotti()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()


ikkuna = pygame.display.set_mode((600, 660))
ikkuna.blit(valikkotausta, (0, 0))
pygame.font.init()
valikko()