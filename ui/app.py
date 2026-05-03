import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from PIL import Image
import sqlite3
import ctypes
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime
from db.database import selection_date_barres, selection_cat_camembert
from db.database import depense_mois, top_categorie
from db.database import nombre_transaction, derniere_depense
from db.database import ajout_depense, creer_user


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

def verifie_derniere_depense() :
    if derniere_depense() != None:
        return derniere_depense()
    if derniere_depense() == None :
        return 0
    
def verifie_depense_mois() :
    if depense_mois(1) != None:
        return depense_mois(1)
    if depense_mois(1) == None :
        return 0
    
def verifie_transaction() :
    if nombre_transaction() != None:
        return nombre_transaction()
    if nombre_transaction() == None :
        return 0
    
def verifie_top_categorie() :
    if top_categorie(1) != None:
        return top_categorie(1)
    if top_categorie(1) == None :
        return 0
    

#Logo
logo = ctk.CTkImage(Image.open("assets/img/logo.png"), size=(100, 100))
ctk.CTkLabel(sidebar, image=logo, text="Compta Clair \n Suivi de dépenses", 
             compound="top", text_color="white", font=ctk.CTkFont(family="Montserrat Bold", size=10)).pack(pady=30)  # image en haut, texte en bas

def afficher_dashboard() :
    for w in contenu.winfo_children():  # récupère tous les widgets dans contenu
        w.destroy()     

    contenu.columnconfigure(0, weight=1)
    contenu.columnconfigure(1, weight=1)
    contenu.columnconfigure(2, weight=1)
    contenu.columnconfigure(3, weight=1)
    titre = ctk.CTkLabel(contenu ,text="TABLEAU DE BORD​", text_color="white",font=ctk.CTkFont(family="Montserrat Bold", size=35))
    titre.grid(row=0, column=0, columnspan=4, pady=(40,5), padx=(20,5), sticky="w")

    #Frame1


    frame1 = ctk.CTkFrame(contenu, fg_color="#2b2b2b",height=120,width=250)
    frame1.grid_propagate(False)
    frame1.grid(row=2, column=0, padx=(20,10), pady=10, sticky="nsew")

    frame1_texte = ctk.CTkLabel(frame1, text="Dernière dépense", fg_color="transparent", text_color="white",font=ctk.CTkFont(family="Montserrat Bold", size=18))
    frame1_texte.grid(row=1,column=0, sticky="w",pady=(10,0), padx= 48)

    frame1_texte = ctk.CTkLabel(frame1, text=f"{str(verifie_derniere_depense())} €", fg_color="transparent", text_color="white",font=ctk.CTkFont(family="Montserrat Bold", size=24))
    frame1_texte.grid(row=3,column=0,sticky="w",pady=(20,5), padx=95)

    #Frame2

    frame2 = ctk.CTkFrame(contenu, fg_color="#2b2b2b",height=120,width=250)
    frame2.grid_propagate(False)
    frame2.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

    frame2_texte = ctk.CTkLabel(frame2, text="Ce mois-ci", fg_color="transparent", text_color="white",font=ctk.CTkFont(family="Montserrat Bold", size=18))
    frame2_texte.grid(row=1,column=0, sticky="w",pady=(10,0), padx= 80)

    frame2_texte = ctk.CTkLabel(frame2, text=f"{str(verifie_depense_mois())} €", fg_color="transparent", text_color="white",font=ctk.CTkFont(family="Montserrat Bold", size=24))
    frame2_texte.grid(row=3,column=0,sticky="w",pady=(20,5), padx=95)

    #Frame3

    frame3 = ctk.CTkFrame(contenu, fg_color="#2b2b2b",height=120,width=250)
    frame3.grid_propagate(False)
    frame3.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

    frame3_texte = ctk.CTkLabel(frame3, text="Transactions", fg_color="transparent", text_color="white",font=ctk.CTkFont(family="Montserrat Bold", size=18))
    frame3_texte.grid(row=1,column=0, sticky="w",pady=(10,0), padx= 69)

    frame3_texte = ctk.CTkLabel(frame3, text=f"{str(verifie_transaction())}", fg_color="transparent", text_color="white",font=ctk.CTkFont(family="Montserrat Bold", size=24))
    frame3_texte.grid(row=3,column=0,sticky="w",pady=(20,5), padx=110)
    
    #Frame4

    frame4 = ctk.CTkFrame(contenu, fg_color="#2b2b2b",height=120,width=250)
    frame4.grid_propagate(False)
    frame4.grid(row=2, column=3, padx=10, pady=10, sticky="nsew")

    frame4_texte = ctk.CTkLabel(frame4, text="Top catégorie", fg_color="transparent", text_color="white",font=ctk.CTkFont(family="Montserrat Bold", size=18))
    frame4_texte.grid(row=1,column=0, sticky="w",pady=(10,0), padx= 64)

    frame4_texte = ctk.CTkLabel(frame4, text=f"{str(verifie_derniere_depense())} €", fg_color="transparent", text_color="white",font=ctk.CTkFont(family="Montserrat Bold", size=24))
    frame4_texte.grid(row=3,column=0,sticky="w",pady=(20,5), padx=95)

    btn_redirect_depense = ctk.CTkButton(contenu, text="➕​​  Ajouter une dépense", width=50,height=40, corner_radius=8,fg_color="#27ae60", hover_color="#1ad668",text_color="white", command=afficher_depenses,font=ctk.CTkFont(family="Montserrat Bold", size=12))
    btn_redirect_depense.grid(row=3, column=0, padx=(20,5), pady=10, sticky="w")


def afficher_graphiques() :
    for w in contenu.winfo_children():  # récupère tous les widgets dans contenu
        w.destroy()

    titre = ctk.CTkLabel(contenu, text="GRAPHIQUES​", text_color="white",
                         font=ctk.CTkFont(family="Montserrat Bold", size=35))
    titre.place(relx=0.05, rely=0.05)

    #Camembert
    resultats_cat = selection_cat_camembert()

    if resultats_cat:
        categories = [r[0] for r in resultats_cat]
        montants_cat = [r[1] for r in resultats_cat]

        fig1, ax1 = plt.subplots(figsize=(4, 3))
        fig1.patch.set_facecolor("#1f1f1f")
        ax1.set_facecolor("#1f1f1f")
        colors = ["#27ae60", "#1E7040", "#00ffcc", "#3498db", "#9b59b6", "#e74c3c", "#f39c12"]
        ax1.pie(montants_cat, labels=categories, autopct='%1.1f%%',
                colors=colors[:len(categories)], textprops={'color': 'white', 'fontsize': 8})
        ax1.set_title("Dépenses par catégorie", color="white", fontsize=12)

        canvas1 = FigureCanvasTkAgg(fig1, master=contenu)
        canvas1.draw()
        canvas1.get_tk_widget().place(relx=0.57, rely=0.15, relwidth=0.40, relheight=0.8)
        plt.close(fig1)

    #Barres

    resultats_mois = selection_date_barres()

    if resultats_mois:
        mois_noms = {
            "01": "Jan", "02": "Fév", "03": "Mar", "04": "Avr",
            "05": "Mai", "06": "Juin", "07": "Juil", "08": "Août",
            "09": "Sep", "10": "Oct", "11": "Nov", "12": "Déc"
        }
        mois = [mois_noms.get(r[0], r[0]) for r in resultats_mois]
        montants_mois = [r[1] for r in resultats_mois]

        fig2, ax2 = plt.subplots(figsize=(12, 8))
        fig2.patch.set_facecolor("#1f1f1f")
        ax2.set_facecolor("#2b2b2b")
        ax2.bar(mois, montants_mois, color="#11b455")
        ax2.set_title("Dépenses par mois", color="white", fontsize=12)
        ax2.tick_params(colors="white")
        ax2.spines['bottom'].set_color('white')
        ax2.spines['left'].set_color('white')
        ax2.spines['top'].set_visible(False)
        ax2.spines['right'].set_visible(False)

        canvas2 = FigureCanvasTkAgg(fig2, master=contenu)
        canvas2.draw()
        canvas2.get_tk_widget().place(relx=0.02, rely=0.15, relwidth=0.55, relheight=0.8)
        plt.close(fig2)


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