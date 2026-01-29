import random

def generer_mot_de_passe():
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    mot_de_passe = ""
    for i in range(8):
        mot_de_passe += random.choice(caracteres)
    return mot_de_passe
print("mot de passe genere :",generer_mot_de_passe())