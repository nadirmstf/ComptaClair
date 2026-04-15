from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from PIL import Image
import sqlite3
import ctypes

# La fenêtre (taille, icon, titre)
fenetre = ctk.CTk()
fenetre.title("Compta Clair")
fenetre.iconbitmap("assets\img\icon.ico")
fenetre.geometry("600x400")


# Charger la police Montserrat
ctypes.windll.gdi32.AddFontResourceW("assets/fonts/Montserrat/Montserrat-Bold.ttf")

#Side Bar
sidebar = ctk.CTkFrame(fenetre, width=200, corner_radius=0, fg_color="#2b2b2b")
sidebar.pack(side="left", fill="y") 
sidebar.pack_propagate(False)



#Logo
logo = ctk.CTkImage(Image.open("assets/img/logo.png"), size=(100, 100))
ctk.CTkLabel(sidebar, image=logo, text="Compta Clair \n Suivi de dépenses", 
             compound="top", text_color="white", font=ctk.CTkFont(family="Montserrat Bold", size=10)).pack(pady=30)  # image en haut, texte en bas


#connexion à la DB
def connexion_db():
    connexion = sqlite3.connect("tables.db")
    connexion.row_factory = sqlite3.Row
    return connexion

def derniere_depense():
    connexion = connexion_db()
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM depenses ORDER BY id DESC LIMIT 1")
    colonne = cursor.fetchone()
    connexion.close()
    if colonne:
        return dict(colonne)
    else:
        return None


def afficher_dashboard() :
    for w in contenu.winfo_children():  # récupère tous les widgets dans contenu
        w.destroy()     

    contenu.columnconfigure(0, weight=1)
    contenu.columnconfigure(1, weight=1)
    contenu.columnconfigure(2, weight=1)
    contenu.columnconfigure(3, weight=1)
    titre = ctk.CTkLabel(contenu ,text="TABLEAU DE BORD​", text_color="white",font=ctk.CTkFont(family="Montserrat Bold", size=35))
    titre.grid(row=0, column=0, columnspan=4, pady=(40,5), padx=(20,5), sticky="w")

    # test = ctk.CTkLabel(contenu, text="Bonjour",text_color="white")
    # test.grid(row=3, column=1)


    frame1 = ctk.CTkFrame(contenu, fg_color="#2b2b2b",height=120,width=250)
    frame1.grid_propagate(False)
    frame1.grid(row=2, column=0, padx=(20,10), pady=10, sticky="nsew")

    frame1_texte = ctk.CTkLabel(frame1, text="Dernière dépense", fg_color="transparent", text_color="white",font=ctk.CTkFont(family="Montserrat Bold", size=15))
    frame1_texte.grid(row=0,column=1, pady=10,padx=10)

    frame2 = ctk.CTkFrame(contenu, fg_color="#2b2b2b",height=120,width=250)
    frame2.grid_propagate(False)
    frame2.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

    frame2_texte = ctk.CTkLabel(frame2, text="Ce mois-ci", fg_color="transparent", text_color="white",font=ctk.CTkFont(family="Montserrat Bold", size=15))
    frame2_texte.grid(row=0,column=1, pady=10,padx=10)

    frame3 = ctk.CTkFrame(contenu, fg_color="#2b2b2b",height=120,width=250)
    frame3.grid_propagate(False)
    frame3.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

    frame3_texte = ctk.CTkLabel(frame3, text="Transactions", fg_color="transparent", text_color="white",font=ctk.CTkFont(family="Montserrat Bold", size=15))
    frame3_texte.grid(row=0,column=1, pady=10,padx=10)
    
    frame4 = ctk.CTkFrame(contenu, fg_color="#2b2b2b",height=120,width=250)
    frame4.grid_propagate(False)
    frame4.grid(row=2, column=3, padx=10, pady=10, sticky="nsew")

    frame4_texte = ctk.CTkLabel(frame4, text="Top catégorie", fg_color="transparent", text_color="white",font=ctk.CTkFont(family="Montserrat Bold", size=15))
    frame4_texte.grid(row=0,column=1, pady=10,padx=10)

    btn_redirect_depense = ctk.CTkButton(contenu, text="➕​​  Ajouter une dépense", width=50,height=40, corner_radius=8,fg_color="#27ae60", hover_color="#1ad668",text_color="white", command=afficher_depenses,font=ctk.CTkFont(family="Montserrat Bold", size=12))
    btn_redirect_depense.grid(row=3, column=0, padx=(20,5), pady=10, sticky="w")

    # if derniere_depense():
    #     derniere_depense_montant = ctk.CTkLabel(frame1, text=derniere_depense()['montant'], fg_color="transparent", text_color="white",font=ctk.CTkFont(family="Montserrat Bold", size=15))
    #     derniere_depense_montant.place(x=20, y=15)
    # else :
    #     derniere_depense_montant = ctk.CTkLabel(frame1, text='0.00$', fg_color="transparent", text_color="white",font=ctk.CTkFont(family="Montserrat Bold", size=15))
    #     derniere_depense_montant.place(x=20, y=15)

def afficher_graphiques() :
    for w in contenu.winfo_children():  # récupère tous les widgets dans contenu
        w.destroy()
    titre = ctk.CTkLabel(contenu ,text="GRAPHIQUES​", text_color="white",font=ctk.CTkFont(family="Montserrat Bold", size=35))
    titre.place(x=50, y=40)
    

def afficher_depenses() :
    for w in contenu.winfo_children():  # récupère tous les widgets dans contenu
        w.destroy()
    titre = ctk.CTkLabel(contenu ,text="DÉPENSES​", text_color="white", font=ctk.CTkFont(family="Montserrat Bold", size=35))
    titre.place(x=50, y=40)

#Page de droite (par opposition au sidebar)
contenu = ctk.CTkFrame(fenetre, corner_radius=0, fg_color="#1f1f1f")
contenu.pack(side="right", fill="both", expand=True)

#Bouttons (ne pas oublier les commandes pour les bouttons)

btn_dashboard = ctk.CTkButton(sidebar, text="🔰​ Tableau de bord", fg_color="gray30", hover_color="gray", command=afficher_dashboard,font=ctk.CTkFont(family="Montserrat Bold", size=12))
btn_dashboard.pack(fill='x', pady=11, padx=15)

btn_depenses = ctk.CTkButton(sidebar, text="​💲​ Dépenses", fg_color="gray30", hover_color="gray", command=afficher_depenses, font=ctk.CTkFont(family="Montserrat Bold", size=12))
btn_depenses.pack(fill='x', pady=11, padx=15)

btn_graphiques = ctk.CTkButton(sidebar, text="📊​ Graphiques", fg_color="gray30", hover_color="gray", command=afficher_graphiques, font=ctk.CTkFont(family="Montserrat Bold", size=12))
btn_graphiques.pack(fill='x',pady=11, padx=15)

JN = ctk.CTkLabel(sidebar ,text="JN Industries \n Tous droits reservés ®️​", text_color="white",font=ctk.CTkFont(family="Montserrat Bold", size=13))
JN.pack(side="bottom", pady=10)
 
btn_dashboard.invoke()
fenetre.mainloop()