from datetime import datetime as dt

"""
Structure de la création de variable
          a
          v
        ####
  f -> #   # <- b
       #### <- g
e ->  #   # <- c
      ####
        ^
        d
"""

def contructeurSegmentNumbers() -> list:
    r = "\n"
    # s = symbole utilisé pour afficher les nombres par défaut '#'
    s = "#"
    # e3 variable récupérant une espace 3 fois
    e3 = " " * 3
    a = s * 4
    b = c = r + e3 + s
    d = g = r + s * 4
    e = f = r + s
    comb = s + "  " + s
    # Variable combinant le retour à la ligne(r) et la combinaison de l'espace plus le symbole (comb)
    r_comb = r + comb
    # somme des 3 variables a + f + g
    afg = a + f + g
    # somme des 3 variables a + b + g
    abg = a + b + g
    
    # Le variable qui conserve les chiffres de 0 à 9 au format segment de 7
    _0 = a + (r_comb * 3) + r + s * 4
    _1 = (s + r) * 4 + s
    _2 = abg + e  + e3 + d
    _3 = abg + c + d
    _4 = comb + r_comb + g + (b * 2)
    _5 = afg + c + d
    _6 = afg + r_comb + d
    _7 = a + (b * 4)
    _8 = a + r_comb + g + r_comb + g
    _9 = a + "\n" + e3 + comb + g + c + d
    
    # Liste qui englobe toute les variables contenant les chiffres de 0 à 9 au système de 7 segments
    list_numbers_segment = [_0, _1, _2, _3, _4, _5, _6, _7, _8, _9]
    # retour d'un dictionnaire qui contiennt les chiffres de 0 à 9 comme clé et de 0 à 9 au système segment
    # de 7 comme les valeurs
    return dict(zip(list(range(10)), list_numbers_segment))

# Fonction permetant l'assemblage des chiffre du time en séparant les heures et les minutes par une ligature de deux points
def assembleurNumberSegment(hour1, hour2, ligature, minute1, minute2) -> str:
    hour1 = hour1.split("\n")
    hour2 = hour2.split("\n")
    ligature = ligature.split("\n")
    minute1 = minute1.split("\n")
    minute2 = minute2.split("\n")
    es = "  "
    _all = [h1 + es + h2 + es + l + es + m1 + es + m2 + es for h1, h2, l, m1, m2 in zip(hour1, hour2, ligature, minute1, minute2)]
    return "\n".join(_all)
    

# Fonction permetant de récupér l'heure actuelle au format str et de le renvoyer au format de system de 7 segments
def digital_time() -> str:
    # Objet stockant le format complet de l'heure actuelle
    time_now = dt.now()
    # Variable stockant l'heure actuelle et le converti en string pour une bonne manipulation
    dt_hour = str(time_now.hour)
    # Stockant le minute actuelle au format str
    dt_minute = str(time_now.minute)
    # variable combinant et les heures et les minutes à un bon format plus lisible 
    # exemple: 13h33, 22h44, etc
    timing = f"{dt_hour}h{dt_minute}"

    tm = []
    # Boucle permettant le completer la forme des heures ou des minutes si elles sont à un seul caractère
    # exmple: 1h33 -> 01h33, 11h9 -> 11h09, 8h8 -> 08h08
    for i in timing.split("h"):
        i = "0" + i if len(i) != 2 else i
        tm.append(i)

    # Décomenter la variable ci-dessous pour le différente test
    # tm = "17h26".split("h")

    # La ligature qui permet de lier les heures et le minutes
    ligature = " \n#\n \n#\n "
    # Reçoit le dictionnaire des nombres
    dict_numbers = contructeurSegmentNumbers()

    # Les varialble qui décompose le temp
    # voici le format de tm = ["03", "19"]
    # h1 recupère le premier nombre nombre des heures dont ici c'est 0
    h1 = tm[0][0]
    h2 = tm[0][1]
    # m1 recupère le premier nombre nombre des minutes dont ici c'est 1
    m1 = tm[1][0]
    m2 = tm[1][1]

    # Ces variables récupère le nombre(au format de 7 seg) à l'aide du dictionnaire des nombres revoyer ci-dessus
    hour1 = dict_numbers[int(h1)]
    hour2 = dict_numbers[int(h2)]
    minute1 = dict_numbers[int(m1)]
    minute2 = dict_numbers[int(m2)]

    # ce return renvoie le temps au complet qui est déjà ligaturé grace à cette fonction
    return assembleurNumberSegment(hour1, hour2, ligature, minute1, minute2)
    

print(digital_time())

