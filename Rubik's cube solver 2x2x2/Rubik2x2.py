import random

A = {
    "aloituskuutio": [
    ['va', 'va', 'or', 'va'],
    ['vi', 'ke', 'ke', 'vi'],
    ['vi', 'vi', 'va', 'pu'],
    ['si', 'si', 'ke', 'si'],
    ['or', 'ke', 'or', 'or'],
    ['pu', 'pu', 'si', 'pu']],

    "kuutio": [],

    "apukuutio": [
    ['', '', '', ''], 
    ['', '', '', ''], 
    ['', '', '', ''], 
    ['', '', '', ''], 
    ['', '', '', ''], 
    ['', '', '', '']],

    "siirrot": [],

    "edellinen": 6,

    "yritykset": [0],
    
    "x": 10,

    "tallennus": "ei tallenna"
}

A["kuutio"] = A["aloituskuutio"]

"""Siirrot: (M=myötäpäivään, V=vastapäivään, Y=ylä, E=etu, O=oikea)
YM-YV,
EM-EV,
OM-OV
"""

def YM():
    A["apukuutio"][1] = A["kuutio"][1]
    A["apukuutio"][0][0] = A["kuutio"][0][2]
    A["apukuutio"][0][1] = A["kuutio"][0][0]
    A["apukuutio"][0][2] = A["kuutio"][0][3]
    A["apukuutio"][0][3] = A["kuutio"][0][1]
    A["apukuutio"][2][0:2] = A["kuutio"][5][0:2]
    A["apukuutio"][3][0:2] = A["kuutio"][4][0:2]
    A["apukuutio"][4][0:2] = A["kuutio"][2][0:2]
    A["apukuutio"][5][0:2] = A["kuutio"][3][0:2]
    A["apukuutio"][2][2:4] = A["kuutio"][2][2:4]
    A["apukuutio"][3][2:4] = A["kuutio"][3][2:4]
    A["apukuutio"][4][2:4] = A["kuutio"][4][2:4]
    A["apukuutio"][5][2:4] = A["kuutio"][5][2:4]
    kuutionpalauttaja()

def YV():
    A["apukuutio"][1] = A["kuutio"][1]
    A["apukuutio"][0][0] = A["kuutio"][0][1]
    A["apukuutio"][0][1] = A["kuutio"][0][3]
    A["apukuutio"][0][2] = A["kuutio"][0][0]
    A["apukuutio"][0][3] = A["kuutio"][0][2]
    A["apukuutio"][2][0:2] = A["kuutio"][4][0:2]
    A["apukuutio"][3][0:2] = A["kuutio"][5][0:2]
    A["apukuutio"][4][0:2] = A["kuutio"][3][0:2]
    A["apukuutio"][5][0:2] = A["kuutio"][2][0:2]
    A["apukuutio"][2][2:4] = A["kuutio"][2][2:4]
    A["apukuutio"][3][2:4] = A["kuutio"][3][2:4]
    A["apukuutio"][4][2:4] = A["kuutio"][4][2:4]
    A["apukuutio"][5][2:4] = A["kuutio"][5][2:4]
    kuutionpalauttaja()
    
def EM():
    A["apukuutio"][3] = A["kuutio"][3]
    A["apukuutio"][2][0] = A["kuutio"][2][2]
    A["apukuutio"][2][1] = A["kuutio"][2][0]
    A["apukuutio"][2][2] = A["kuutio"][2][3]
    A["apukuutio"][2][3] = A["kuutio"][2][1]
    
    A["apukuutio"][0][2] = A["kuutio"][4][3]
    A["apukuutio"][0][3] = A["kuutio"][4][1]
    A["apukuutio"][4][1] = A["kuutio"][1][0]
    A["apukuutio"][4][3] = A["kuutio"][1][1]
    A["apukuutio"][1][0] = A["kuutio"][5][2]
    A["apukuutio"][1][1] = A["kuutio"][5][0]
    A["apukuutio"][5][0] = A["kuutio"][0][2]
    A["apukuutio"][5][2] = A["kuutio"][0][3]
    
    A["apukuutio"][0][0:2] = A["kuutio"][0][0:2]
    A["apukuutio"][1][2:4] = A["kuutio"][1][2:4]
    A["apukuutio"][4][0] = A["kuutio"][4][0]
    A["apukuutio"][4][2] = A["kuutio"][4][2]
    A["apukuutio"][5][1] = A["kuutio"][5][1]
    A["apukuutio"][5][3] = A["kuutio"][5][3]
    kuutionpalauttaja()
    
def EV():
    A["apukuutio"][3] = A["kuutio"][3]
    A["apukuutio"][2][0] = A["kuutio"][2][1]
    A["apukuutio"][2][1] = A["kuutio"][2][3]
    A["apukuutio"][2][2] = A["kuutio"][2][0]
    A["apukuutio"][2][3] = A["kuutio"][2][2]
    
    A["apukuutio"][0][2] = A["kuutio"][5][0]
    A["apukuutio"][0][3] = A["kuutio"][5][2]
    A["apukuutio"][4][1] = A["kuutio"][0][3]
    A["apukuutio"][4][3] = A["kuutio"][0][2]
    A["apukuutio"][1][0] = A["kuutio"][4][1]
    A["apukuutio"][1][1] = A["kuutio"][4][3]
    A["apukuutio"][5][0] = A["kuutio"][1][1]
    A["apukuutio"][5][2] = A["kuutio"][1][0]
    
    A["apukuutio"][0][0:2] = A["kuutio"][0][0:2]
    A["apukuutio"][1][2:4] = A["kuutio"][1][2:4]
    A["apukuutio"][4][0] = A["kuutio"][4][0]
    A["apukuutio"][4][2] = A["kuutio"][4][2]
    A["apukuutio"][5][1] = A["kuutio"][5][1]
    A["apukuutio"][5][3] = A["kuutio"][5][3]
    kuutionpalauttaja()
    
def OM():
    A["apukuutio"][4] = A["kuutio"][4]
    A["apukuutio"][5][0] = A["kuutio"][5][2]
    A["apukuutio"][5][1] = A["kuutio"][5][0]
    A["apukuutio"][5][2] = A["kuutio"][5][3]
    A["apukuutio"][5][3] = A["kuutio"][5][1]
    
    A["apukuutio"][0][1] = A["kuutio"][2][1]
    A["apukuutio"][0][3] = A["kuutio"][2][3]
    A["apukuutio"][2][1] = A["kuutio"][1][1]
    A["apukuutio"][2][3] = A["kuutio"][1][3]
    A["apukuutio"][1][1] = A["kuutio"][3][2]
    A["apukuutio"][1][3] = A["kuutio"][3][0]
    A["apukuutio"][3][0] = A["kuutio"][0][3]
    A["apukuutio"][3][2] = A["kuutio"][0][1]
    
    A["apukuutio"][0][0] = A["kuutio"][0][0]
    A["apukuutio"][0][2] = A["kuutio"][0][2]
    A["apukuutio"][1][0] = A["kuutio"][1][0]
    A["apukuutio"][1][2] = A["kuutio"][1][2]
    A["apukuutio"][2][0] = A["kuutio"][2][0]
    A["apukuutio"][2][2] = A["kuutio"][2][2]
    A["apukuutio"][3][1] = A["kuutio"][3][1]
    A["apukuutio"][3][3] = A["kuutio"][3][3]
    kuutionpalauttaja()

def OV():
    A["apukuutio"][4] = A["kuutio"][4]
    A["apukuutio"][5][0] = A["kuutio"][5][1]
    A["apukuutio"][5][1] = A["kuutio"][5][3]
    A["apukuutio"][5][2] = A["kuutio"][5][0]
    A["apukuutio"][5][3] = A["kuutio"][5][2]
    
    A["apukuutio"][0][1] = A["kuutio"][3][2]
    A["apukuutio"][0][3] = A["kuutio"][3][0]
    A["apukuutio"][3][2] = A["kuutio"][1][1]
    A["apukuutio"][3][0] = A["kuutio"][1][3]
    A["apukuutio"][1][1] = A["kuutio"][2][1]
    A["apukuutio"][1][3] = A["kuutio"][2][3]
    A["apukuutio"][2][1] = A["kuutio"][0][1]
    A["apukuutio"][2][3] = A["kuutio"][0][3]
    
    A["apukuutio"][0][0] = A["kuutio"][0][0]
    A["apukuutio"][0][2] = A["kuutio"][0][2]
    A["apukuutio"][1][0] = A["kuutio"][1][0]
    A["apukuutio"][1][2] = A["kuutio"][1][2]
    A["apukuutio"][2][0] = A["kuutio"][2][0]
    A["apukuutio"][2][2] = A["kuutio"][2][2]
    A["apukuutio"][3][1] = A["kuutio"][3][1]
    A["apukuutio"][3][3] = A["kuutio"][3][3]
    kuutionpalauttaja()
    
def kuutionpalauttaja():
    A["kuutio"] = A["apukuutio"]
    A["apukuutio"] = [
    ['', '', '', ''], 
    ['', '', '', ''], 
    ['', '', '', ''], 
    ['', '', '', ''], 
    ['', '', '', ''], 
    ['', '', '', ''],]


vastasiirto = [1, 0, 3, 2, 5, 4, 30]

siirtolista = [YV, YM, EM, EV, OM, OV]

def ratkaisija():
    A["kuutio"] = A["aloituskuutio"]
    x = A["x"]

    for i in range(x):
        while True:
            siirto = random.randint(0, 5)
            if not siirto == vastasiirto[A["edellinen"]]:
                break

        A["edellinen"] = siirto
        x = siirtolista[siirto]
        A["siirrot"].append(siirto)
        x()

        if tarkistus():
            if A["tallennus"] == "tallentaa":
                tilastontallentaja()

            else:
                print("\n{} yritystä\n".format(A["yritykset"][0]))
                for s in range(i + 1):
                    if A["siirrot"][s] == 4:
                        print("{}. siirto: Oikea sivu myötäpäivään".format(s + 1))
                    elif A["siirrot"][s] == 5:
                        print("{}. siirto: Oikea sivu vastapäivään".format(s + 1))
                    elif A["siirrot"][s] == 1:
                        print("{}. siirto: Yläpuoli myötäpäivään".format(s + 1))
                    elif A["siirrot"][s] == 0:
                        print("{}. siirto: Yläpuoli vastapäivään".format(s + 1))
                    elif A["siirrot"][s] == 2:
                        print("{}. siirto: Etupuoli myötäpäivään".format(s + 1))
                    else:
                        print("{}. siirto: Etupuoli vastapäivään".format(s + 1))
                print("\nYhteensä {} siirtoa\n".format(i + 1))
                valikko()

def tarkistus():
    if not A["kuutio"][0][0] == A["kuutio"][0][1] == A["kuutio"][0][2] == A["kuutio"][0][3]:
        return False
    elif not A["kuutio"][1][0] == A["kuutio"][1][1] == A["kuutio"][1][2] == A["kuutio"][1][3]:
        return False
    elif not A["kuutio"][2][0] == A["kuutio"][2][1] == A["kuutio"][2][2] == A["kuutio"][2][3]:
        return False
    elif not A["kuutio"][3][0] == A["kuutio"][3][1] == A["kuutio"][3][2] == A["kuutio"][3][3]:
        return False
    elif not A["kuutio"][4][0] == A["kuutio"][4][1] == A["kuutio"][4][2] == A["kuutio"][4][3]:
        return False
    elif not A["kuutio"][5][0] == A["kuutio"][5][1] == A["kuutio"][5][2] == A["kuutio"][5][3]:
        return False
    else:
        return True
             
def main(): 
    div = 0
    while True:
        ratkaisija()
        A["siirrot"].clear()
        A["yritykset"][0] += 1
        div += 1
        if div == 10000:
            div = 0
            print(A["yritykset"])

sivut = ["yläpuoli", "alapuoli", "etupuoli", "takapuoli", "vasen puoli", "oikea puoli"]

palat = ["ensimmäinen pala", "toinen pala", "kolmas pala", "neljäs pala"]

def valikko():
    while True:
        try:
            valinta = int(input("1 = uusi kuutio, 2 = edellinen kuutio, 3 = testi, 4 = sulje, 5 = kerää dataa: "))
        except ValueError:
            valikko()

        if valinta == 1:
            for i in range(6):
                sivu = sivut[i]
                for u in range(4):
                    pala = palat[u]
                    while True:
                        try:
                            A["aloituskuutio"][i][u] = input("{a} {b}: ".format(a=sivu, b=pala))
                            abc = A["aloituskuutio"][i][u]
                            if abc == "pu" or abc == "si" or abc == "ke" \
                                    or abc == "va" or abc == "vi" or abc == "or":
                                break
                            else:
                                print("Anna väri (pu, si, vi, ke, va, or): ")
                        finally:
                            pass
            while True:
                try:
                    A["x"] = int(input("Anna siirtojen maksimimäärä: "))
                except ValueError:
                    print("Anna luku (suositus 14-20): ")
                else:
                    pass
                    main()

        elif valinta == 2:
            A["edellinen"] = 6
            A["yritykset"][0] = 0
            while True:
                try:
                    A["x"] = int(input("Anna siirtojen maksimimäärä: "))
                except ValueError:
                    print("Anna luku (suositus 14-20): ")
                else:
                    pass
                    main()

        elif valinta == 3:
            main()

        elif valinta == 4:
            quit()

        elif valinta == 5:
            tilastoesityöt()

def tilastoesityöt():
    A["yritykset"][0] = 0
    A["x"] = 30
    A["kuutio"] = A["aloituskuutio"]
    x = A["x"]
    for i in range(x):
        while True:
            siirto = random.randint(0, 5)
            if not siirto == vastasiirto[A["edellinen"]]:
                break

        A["edellinen"] = siirto
        x = siirtolista[siirto]
        x()

    A["tallennus"] = "tallentaa"
    A["aloituskuutio"] = A["kuutio"]
    A["x"] = 14
    main()

def tilastontallentaja():
    s = len(A["siirrot"])
    with open("2x2rubiktilastot.txt", "a") as kohde:
        kohde.write("[[{A}], {B}, {C}],\n".format(A=s, B=A["siirrot"], C=A["yritykset"]))
    tilastoesityöt()

valikko()