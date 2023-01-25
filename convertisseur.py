from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# fenêtre principale
fenêtre = tk.Tk()
fenêtre.title("Convertisseur")
fenêtre.geometry("600x250")
# pour que la fenêtre ne soit pas redimensionnable
fenêtre.resizable(height=FALSE, width=FALSE)

# configuration du gestionnaire de ma grille
fenêtre.rowconfigure(12)
fenêtre.columnconfigure(3)

# titre de ma grille
Titre = tk.Label(fenêtre, text="CONVERTISSEUR DE MONNAIES", bg="#013069", borderwidth=2, relief="groove", fg="white", font=("Comic Sans MS", 12))
Titre.grid(column=0)

# création de mon étiquette MONTANT
amount_label = tk.Label(fenêtre, text="MONTANT :", width=14, height=1, bg="#014886", borderwidth=1, relief="ridge", fg="white", font=("Comic Sans MS", 10))
amount_label.grid(row=2, column=0)

# espace vide pour entrer le montant à convertir
amount_data = tk.Entry(fenêtre, width=17, font=("Comic Sans MS", 10))
amount_data.grid(column=2, row=2)
# fonction qui envoie une pop-up d'erreur si la saisie est en lettres
def only_nbr():
        messagebox.showerror("ERREUR", "Les lettres ne sont pas valides, \nVeuillez saisir un nombre!")

# création de mon étiquette DE
devisedépart = tk.Label(fenêtre, text="DE :", width=14, height=1, bg="#014886", borderwidth=1, relief="ridge", fg="white", font=("Comic Sans MS", 10))
devisedépart.grid(row=4, column=0)

# menu déroulant pour choisir la devise de départ
def choix(menu):
    select = listeCombo.get()
    return(select)
listeDevisesDe=["Choisissez une devise","EUR","GPD","JPY","NOK"]
style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground="#FBCE01", background="#FBCE01")
listeCombo = ttk.Combobox(fenêtre, values=listeDevisesDe)
listeCombo.current(0)
listeCombo.grid(column=2, row=4)
listeCombo.bind("<<ComboboxSelected>>", choix)

# création de mon étiquette VERS
devisearrivée = tk.Label(fenêtre, text="VERS :", width=14, height=1, bg="#014886", borderwidth=1, relief="ridge", fg="white", font=("Comic Sans MS", 10))
devisearrivée.grid(row=6, column=0)

# menu déroulant pour choisir la devise de sortie
def choix2(menu):
    select = listeCombo2.get()
    return(select)
listeDevisesVers=["Choisissez une devise","EUR","GPD","JPY","NOK"]
listeCombo2 = ttk.Combobox(fenêtre, values=listeDevisesVers)
listeCombo2.current(0)
listeCombo2.grid(column=2, row=6)
listeCombo2.bind("<<ComboboxSelected>>", choix2)

# création de mon étiquette Montant converti
montantconverti = tk.Label(fenêtre, text="Montant converti :", width=14, height=1, bg="#014886", borderwidth=1, relief="ridge", fg="white", font=("Comic Sans MS", 10))
montantconverti.grid(row=10, column=0)

# espace vide pour afficher la conversion
amountconvert = tk.Listbox(fenêtre, width=30, heigh=4)
amountconvert.grid(column=2, row=10)

# taux de change fixes
EUR_VERS_GPD = 0.88
EUR_VERS_JPY = 141.44
EUR_VERS_NOK = 10.70
GPD_VERS_EUR = 1.13
GPD_VERS_JPY = 160.08
GPD_VERS_NOK = 12.12
JPY_VERS_EUR = 0.0071
JPY_VERS_GPD = 0.0062
JPY_VERS_NOK = 0.076
NOK_VERS_EUR = 0.093
NOK_VERS_GPD = 0.083
NOK_VERS_JPY = 13.20

# vérifier si les devises sont différentes
def liste_devises_diff(listeDevisesDe, listeDevisesVers):
    if listeDevisesDe == listeDevisesVers:
        # si les devises sont les mêmes, alors envoie une pop-up d'erreur
        messagebox.showerror("ERREUR", "Conversion impossible, \nChoisissez 2 devises différentes!")
        return False
    return True

# calculs de conversion
def calculConversion(montant, listeDevisesDe, listeDevisesVers):
    if listeDevisesDe == "EUR":
        if listeDevisesVers == 'GPD':
            return montant * EUR_VERS_GPD
        elif listeDevisesVers == 'JPY':
            return montant * EUR_VERS_JPY
        elif listeDevisesVers == 'NOK':
            return montant * EUR_VERS_NOK
    elif listeDevisesDe == 'GPD':
        if listeDevisesVers == "EUR":
            return montant * GPD_VERS_EUR
        elif listeDevisesVers == 'JPY':
            return montant * GPD_VERS_JPY
        elif listeDevisesVers == 'NOK':
            return montant * GPD_VERS_NOK
    elif listeDevisesDe == 'JPY':
        if listeDevisesVers == "EUR":
            return montant * JPY_VERS_EUR
        elif listeDevisesVers == 'GPD':
            return montant * JPY_VERS_GPD
        elif listeDevisesVers == 'NOK':
            return montant * JPY_VERS_NOK
    elif listeDevisesDe == 'NOK':
        if listeDevisesVers == "EUR":
            return montant * NOK_VERS_EUR
        elif listeDevisesVers == 'GPD':
            return montant * NOK_VERS_GPD
        elif listeDevisesVers == 'JPY':
            return montant * NOK_VERS_JPY

# action du bouton convertir
def btnconvert():
    # avec .get on récupère la valeur saisie dans MONTANT
    montant = (amount_data.get())
    # de même avec la devise saisie dans le menu déroulant DE
    listeDevisesDe = listeCombo.get()
    # de même avec la devise saisie dans le menu déroulant VERS
    listeDevisesVers = listeCombo2.get()
    # définit si mon montant est en nombre
    if montant.isdigit():
        # redéfinir montant en float pour avoir les décimales
        montant = float(amount_data.get())
        # si mon montant est en nombres alors le calcul de conversion se fait
        calculConversion(montant,listeDevisesDe,listeDevisesVers)
    else:
        # si le montant n'est pas en nombre la fonction envoie une pop-up d'erreur
        only_nbr()
    # vérifie si les devises sont différentes
    if liste_devises_diff(listeDevisesDe, listeDevisesVers):
        result = calculConversion(montant, listeDevisesDe, listeDevisesVers)
        # on affiche le résultat détaillé avec monnaie de départ, flèche, monnaie de sortie et le résultat de la conversion 
        détail = (listeDevisesDe, "\U00002192", listeDevisesVers, "=", result)
        # on affiche ce résultat dans l'espace amountconvert
        amountconvert.insert(0, détail)
        # on crée un fichier texte avec open, "a" ajoute, et UTF-8 permet d'afficher la flèche.
        f = open("test.txt", "a", encoding='UTF-8')
        # avec write on écrit dans le fichier notre conversion en détail, et le \n va à la ligne
        f.write(str(détail) + "\n")
        # le fichier se ferme
        f.close()

# bouton convertir fonctionnel avec la fonction btnconvert
button =tk.Button(fenêtre, text="CONVERTIR", width=14, bg="#F9BE01", command=btnconvert)
button.grid(column=1, row=10)

# fonction pour définir les devises favorites
def favorite(nom):
    # je détermine la position de mes devises favorites
    if nom == "Sophie":
        # listefavoris1 = ("EUR", "NOK")
        listeCombo.current(1)
        listeCombo2.current(4)
    elif nom == "Tara": 
        # listefavoris2 = ("GPD", "EUR")
        listeCombo.current(2)
        listeCombo2.current(1)

# bouton Favoris Sophie fonctionnel avec la fonction favorite "Sophie"
button3 =tk.Button(fenêtre, text="FAVORIS SOPHIE", width=14, bg="#F9BE01", command=lambda:favorite("Sophie"))
button3.grid(column=1, row=4)    
    
# bouton Favoris Tara fonctionnel avec la fonction favorite "Tara"
button4 =tk.Button(fenêtre, text="FAVORIS TARA", width=14, bg="#F9BE01", command=lambda:favorite("Tara"))
button4.grid(column=1, row=6)

# fonction qui permet d'effacer les champs amount_data et amountconvert et de remettre les menus déroulants au début
def effacer():
    amount_data.delete(0, END)
    amountconvert.delete(0, END)
    listeCombo.current(0)
    listeCombo2.current(0)

# bouton Effacer fonctionnel avec la fonction effacer
button2 =tk.Button(fenêtre, text="TOUT EFFACER", width=14, bg="#F9BE01", command=effacer)
button2.grid(column=1, row=12)

fenêtre.mainloop()
# ("EUR", "\U000020AC"),("GPD", "\U000000A3"),("JPY", "\U000000A5"),("NOK", "Kr")
# if monnaieEntrée == 'EUR':
#     if monnaieSortie == 'EUR':
#         sommeSortie = sommeEntrée * 1
#     elif monnaieSortie == 'GPD':
#         sommeSortie = sommeEntrée * 0.88
#     elif monnaieSortie == 'JPY':
#         sommeSortie = sommeEntrée * 141.44
#     elif monnaieSortie == 'NOK':
#         sommeSortie = sommeEntrée * 10.70
#     else:
#         print("Impossible de faire la conversion, erreur dans la monnaie de sortie")

# elif monnaieEntrée == 'GPD':
#     if monnaieSortie == 'EUR':
#         sommeSortie = sommeEntrée * 1.13
#     elif monnaieSortie == 'GPD':
#         sommeSortie = sommeEntrée * 1
#     elif monnaieSortie == 'JPY':
#         sommeSortie = sommeEntrée * 160.08
#     elif monnaieSortie == 'NOK':
#         sommeSortie = sommeEntrée * 12.12
#     else:
#         print("Impossible de faire la conversion, erreur dans la monnaie de sortie")

# elif monnaieEntrée == 'JPY':
#     if monnaieSortie == 'EUR':
#         sommeSortie = sommeEntrée * 0.0071
#     elif monnaieSortie == 'GPD':
#         sommeSortie = sommeEntrée * 0.0062
#     elif monnaieSortie == 'JPY':
#         sommeSortie = sommeEntrée * 1
#     elif monnaieSortie == 'NOK':
#         sommeSortie = sommeEntrée * 0.076
#     else:
#         print("Impossible de faire la conversion, erreur dans la monnaie de sortie")

# elif monnaieEntrée == 'NOK':
#     if monnaieSortie == 'EUR':
#         sommeSortie = sommeEntrée * 0.093
#     elif monnaieSortie == 'GPD':
#         sommeSortie = sommeEntrée * 0.083
#     elif monnaieSortie == 'JPY':
#         sommeSortie = sommeEntrée * 13.20
#     elif monnaieSortie == 'NOK':
#         sommeSortie = sommeEntrée * 1
#     else:
#         print("Impossible de faire la conversion, erreur dans la monnaie de sortie")
# else:
#     print("Impossible de faire la conversion, erreur dans la monnaie d'entrée")

# if sommeSortie != None:
#     print(f"Voici votre conversion {sommeSortie}")