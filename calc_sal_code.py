def calculer_salaire(metier, xp):
    if metier == "architecte" and xp == "12":
        return "4400"
    elif metier == "medecin" and xp == "15":
        return "7000"
    elif metier == "consultant" and xp == "6":
        return "3000"
    
print("Vous êtes {0} avec {1} années d'expérience et vous gagnez {2} euros.".format("architecte", "12", "4400"))
print("Vous êtes {0} avec {1} années d'expérience et vous gagnez {2} euros.".format("medecin", "15", "7000"))
print("Vous êtes {0} avec {1} années d'expérience et vous gagnez {2} euros.".format("consultant", "6", "3000"))
