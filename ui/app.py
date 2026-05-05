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
from db.database import ajout_depense, creer_user, get_recents


# La fenêtre (taille, icon, titre)
fenetre = ctk.CTk()
fenetre.title("Compta Clair")
fenetre.iconbitmap("assets\img\icon.ico")
fenetre.state("zoomed")


# Charger la police Montserrat
ctypes.windll.gdi32.AddFontResourceW("assets/fonts/Montserrat/Montserrat-Bold.ttf") #Montserrat Bold
ctypes.windll.gdi32.AddFontResourceW("assets/fonts/Montserrat/Montserrat-Light.ttf") #Montserrat Light

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
    
def verifie_recents() :
    if get_recents() == None :
        return False
    

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

    contenu.rowconfigure(0, weight=0)
    contenu.rowconfigure(2, weight=0)
    contenu.rowconfigure(3, weight=0)
    contenu.rowconfigure(4, weight=0)
    contenu.rowconfigure(5, weight=1)

    frame1 = ctk.CTkFrame(contenu, fg_color="#2b2b2b")
    frame1.columnconfigure(0, weight=1)
    frame1.grid(row=2, column=0, padx=(20,10), pady=10, sticky="nsew", ipady=20)

    frame1_texte = ctk.CTkLabel(frame1, text="Dernière dépense", fg_color="transparent", anchor="center",text_color="white",font=ctk.CTkFont(family="Montserrat Bold", size=18))
    frame1_texte.grid(row=1,column=0, sticky="ew",pady=(15,0))

    frame1_texte = ctk.CTkLabel(frame1, text=f"{str(verifie_derniere_depense())} €", fg_color="transparent", text_color="white",font=ctk.CTkFont(family="Montserrat Bold", size=24))
    frame1_texte.grid(row=3,column=0,sticky="ew",pady=(20,5))

    #Frame2

    frame2 = ctk.CTkFrame(contenu, fg_color="#2b2b2b")
    frame2.columnconfigure(0, weight=1)
    frame2.grid(row=2, column=1, padx=10, pady=10, sticky="nsew", ipady=20)

    frame2_texte = ctk.CTkLabel(frame2, text="Ce mois-ci", fg_color="transparent",anchor="center",text_color="white",font=ctk.CTkFont(family="Montserrat Bold", size=18))
    frame2_texte.grid(row=1,column=0, sticky="ew",pady=(15,0))

    frame2_texte = ctk.CTkLabel(frame2, text=f"{str(verifie_depense_mois())} €", fg_color="transparent", text_color="white",font=ctk.CTkFont(family="Montserrat Bold", size=24))
    frame2_texte.grid(row=3,column=0,sticky="ew",pady=(20,5))

    #Frame3

    frame3 = ctk.CTkFrame(contenu, fg_color="#2b2b2b")
    frame3.columnconfigure(0, weight=1)
    frame3.grid(row=2, column=2, padx=10, pady=10, sticky="nsew", ipady=20)

    frame3_texte = ctk.CTkLabel(frame3, text="Transactions", fg_color="transparent", text_color="white",anchor="center",font=ctk.CTkFont(family="Montserrat Bold", size=18))
    frame3_texte.grid(row=1,column=0, sticky="ew",pady=(15,0))

    frame3_texte = ctk.CTkLabel(frame3, text=f"{str(verifie_transaction())}", fg_color="transparent", text_color="white",font=ctk.CTkFont(family="Montserrat Bold", size=24))
    frame3_texte.grid(row=3,column=0,sticky="ew",pady=(20,5))
    
    #Frame4

    frame4 = ctk.CTkFrame(contenu, fg_color="#2b2b2b")
    frame4.columnconfigure(0, weight=1)
    frame4.grid(row=2, column=3, padx=10, pady=10, sticky="nsew", ipady=20)

    frame4_texte = ctk.CTkLabel(frame4, text="Top catégorie", fg_color="transparent", text_color="white",anchor="center", font=ctk.CTkFont(family="Montserrat Bold", size=18))
    frame4_texte.grid(row=1,column=0, sticky="ew",pady=(15,0))

    frame4_texte = ctk.CTkLabel(frame4, text=f"{str(verifie_top_categorie())}", fg_color="transparent", text_color="white",font=ctk.CTkFont(family="Montserrat Bold", size=24))
    frame4_texte.grid(row=3,column=0,sticky="ew",pady=(20,5))

    btn_redirect_depense = ctk.CTkButton(contenu, text="➕​​  Ajouter une dépense", width=50,height=40, corner_radius=8,fg_color="#27ae60", hover_color="#1ad668",text_color="white", command=afficher_depenses,font=ctk.CTkFont(family="Montserrat Bold", size=12))
    btn_redirect_depense.grid(row=3, column=0, padx=(20,5), pady=10, sticky="w")

    #Frame Centrale
        #Titre + Tracé
    frame4_texte = ctk.CTkLabel(contenu, text="Dépenses récentes", fg_color="transparent", text_color="white",font=ctk.CTkFont(family="Montserrat Bold", size=18))
    frame4_texte.grid(row=4,column=0, sticky="w",pady=(10,0), padx=19)

    frame_centrale = ctk.CTkFrame(contenu, fg_color="#2b2b2b")
    contenu.grid_rowconfigure(5, weight=1)
    frame_centrale.grid(row=5, column=0, columnspan=4, padx=(18,12), pady=(10,20),sticky="nsew")
    
        #Affichage des 5 dernières dépenses

    if verifie_recents() == False :

        aucune_depense = ctk.CTkLabel(frame_centrale, 
                                      text="Aucune dépense pour le moment !", 
                                      fg_color="transparent", 
                                      text_color="white",
                                      font=ctk.CTkFont(family="Montserrat Bold", size=25))
        aucune_depense.place(relx=0.5, rely=0.5, anchor="center")
    else :
        label_date = ctk.CTkLabel(frame_centrale, text="Date",
                                  text_color="white", 
                                  font=ctk.CTkFont(family="Montserrat Bold", size=18)
                                  )     
        label_cat = ctk.CTkLabel(frame_centrale, text="Catégorie",
                                  text_color="white", 
                                  font=ctk.CTkFont(family="Montserrat Bold", size=18)
                                  )
        label_desc = ctk.CTkLabel(frame_centrale, text="Descritption",
                                  text_color="white", 
                                  font=ctk.CTkFont(family="Montserrat Bold", size=18)
                                  )      
        label_montant = ctk.CTkLabel(frame_centrale, text="Montant",
                                  text_color="white", 
                                  font=ctk.CTkFont(family="Montserrat Bold", size=18)
                                  )    
        
        frame_centrale.columnconfigure(0, weight=1)
        frame_centrale.columnconfigure(1, weight=1)
        frame_centrale.columnconfigure(2, weight=1)
        frame_centrale.columnconfigure(3, weight=1)

        label_date.grid(row=0, column=0, sticky="ew", padx=20)
        label_cat.grid(row=0, column=1, sticky="ew", padx=20)
        label_desc.grid(row=0, column=2, sticky="ew", padx=20)
        label_montant.grid(row=0, column=3, sticky="ew", padx=20)

        depenses = get_recents()
        c = 1
        for dep in depenses :

            date = dep[4]
            montant = dep[1]
            categorie = dep[2]
            description = dep[3]

            date_label = ctk.CTkLabel(frame_centrale,text=date, 
                         text_color="white",
                         font=ctk.CTkFont(family="Montserrat Light", size=18)
                         )
            date_label.grid(row=c, column=0)

            cat_label = ctk.CTkLabel(frame_centrale, text=categorie, 
                         text_color="white",
                         font=ctk.CTkFont(family="Montserrat Light", size=18)
                         )
            cat_label.grid(row=c, column=1)

            desc_label = ctk.CTkLabel(frame_centrale,text=description, 
                         text_color="white",
                         font=ctk.CTkFont(family="Montserrat Light", size=18)
                         )
            desc_label.grid(row=c, column=2)
            
            montant_label = ctk.CTkLabel(frame_centrale,text=montant, 
                         text_color="white",
                         font=ctk.CTkFont(family="Montserrat Light", size=18)
                         )
            montant_label.grid(row=c, column=3)
            c += 1
            

            
            
            



        # for i, dep in enumerate(depenses, start=1):
        #     date = dep[4]
        #     montant = dep[1]
        #     categorie = dep[2]
        #     description = dep[3]

        #     ctk.CTkLabel(frame_centrale, text=date).grid(row=i, column=0)
        #     ctk.CTkLabel(frame_centrale, text=f"{montant} €").grid(row=i, column=1)
        #     ctk.CTkLabel(frame_centrale, text=categorie).grid(row=i, column=2)
        #     ctk.CTkLabel(frame_centrale, text=description).grid(row=i, column=3)




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
        ax1.set_title("Dépenses par catégorie (en %)", color="white", fontsize=12)

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
        ax2.set_title("Dépenses par mois (en €)", color="white", fontsize=12)
        ax2.tick_params(colors="white")
        ax2.spines['bottom'].set_color('white')
        ax2.spines['left'].set_color('white')
        ax2.spines['top'].set_visible(False)
        ax2.spines['right'].set_visible(False)

        canvas2 = FigureCanvasTkAgg(fig2, master=contenu)
        canvas2.draw()
        canvas2.get_tk_widget().place(relx=0.02, rely=0.15, relwidth=0.55, relheight=0.8)
        plt.close(fig2)


# def afficher_depenses() :
#     for w in contenu.winfo_children():  # récupère tous les widgets dans contenu
#         w.destroy()
#     titre = ctk.CTkLabel(contenu ,text="DÉPENSES​", text_color="white", font=ctk.CTkFont(family="Montserrat Bold", size=35))
#     titre.place(relx=0.05, rely=0.05)

def afficher_depenses():
    for widget in contenu.winfo_children():
        widget.destroy()
    titre = ctk.CTkLabel(contenu ,text="DÉPENSES​", text_color="white", font=ctk.CTkFont(family="Montserrat Bold", size=35))
    titre.place(relx=0.05, rely=0.05)

    ctk.CTkLabel(contenu, text="Mes Dépenses", text_color="white",
                 font=ctk.CTkFont(family="Montserrat Bold", size=35)
                 ).place(relx=0.02, rely=0.04)


    barre_filtres = ctk.CTkFrame(contenu, fg_color="transparent")
    barre_filtres.place(relx=0.02, rely=0.15, relwidth=0.96, relheight=0.07)

    ctk.CTkLabel(barre_filtres, text="Catégorie:", text_color="white",
                 font=ctk.CTkFont(family="Montserrat Bold", size=13)
                 ).place(relx=0.00, rely=0.5, anchor="w")

    liste_categories = ["Toutes", "Alimentation", "Transport", "Logement",
                        "Loisirs", "Santé", "Vêtements", "Éducation", "Autre"]
    menu_categorie = ctk.CTkComboBox(barre_filtres, values=liste_categories, width=160)
    menu_categorie.set("Toutes")
    menu_categorie.place(relx=0.09, rely=0.5, anchor="w")

    ctk.CTkLabel(barre_filtres, text="Mois:", text_color="white",
                 font=ctk.CTkFont(family="Montserrat Bold", size=13)
                 ).place(relx=0.27, rely=0.5, anchor="w")

    champ_mois = ctk.CTkEntry(barre_filtres, placeholder_text="YYYY-MM", width=120)
    champ_mois.place(relx=0.32, rely=0.5, anchor="w")

    ctk.CTkButton(barre_filtres, text="🔍 Filtrer", width=100, height=35,
                  fg_color="#3b3b6b", hover_color="#5555aa", text_color="white",
                  font=ctk.CTkFont(family="Montserrat Bold", size=12),
                  command=lambda: appliquer_les_filtres()
                  ).place(relx=0.47, rely=0.5, anchor="w")

    ctk.CTkButton(barre_filtres, text="↺ Reset", width=100, height=35,
                  fg_color="#555555", hover_color="#777777", text_color="white",
                  font=ctk.CTkFont(family="Montserrat Bold", size=12),
                  command=lambda: reinitialiser_filtres()
                  ).place(relx=0.57, rely=0.5, anchor="w")

    ctk.CTkButton(barre_filtres, text="⬆ Export CSV", width=140, height=35,
                  fg_color="#27ae60", hover_color="#1ad668", text_color="white",
                  font=ctk.CTkFont(family="Montserrat Bold", size=12),
                  command=lambda: ...
                  ).place(relx=0.72, rely=0.5, anchor="w")

    ctk.CTkButton(barre_filtres, text="＋ Ajouter", width=130, height=35,
                  fg_color="#3498db", hover_color="#2980b9", text_color="white",
                  font=ctk.CTkFont(family="Montserrat Bold", size=12),
                  command=lambda: ouvrir_popup_ajout()
                  ).place(relx=0.87, rely=0.5, anchor="w")


    cadre_tableau = ctk.CTkFrame(contenu, fg_color="#2b2b2b", corner_radius=10)
    cadre_tableau.place(relx=0.02, rely=0.24, relwidth=0.96, relheight=0.62)

    style_tableau = ttk.Style()
    style_tableau.theme_use("clam")
    style_tableau.configure("Style.Treeview",
                            background="#2b2b2b", foreground="white",
                            fieldbackground="#2b2b2b", rowheight=30,
                            font=("Montserrat Light", 13))
    style_tableau.configure("Style.Treeview.Heading",
                            background="#1f1f1f", foreground="white",
                            font=("Montserrat Bold", 13), relief="flat")
    style_tableau.map("Style.Treeview", background=[("selected", "#27ae60")])

    noms_colonnes = ("id", "date", "categorie", "montant", "description")
    tableau = ttk.Treeview(cadre_tableau, columns=noms_colonnes,
                           show="headings", style="Style.Treeview")

    tableau.heading("id",          text="ID")
    tableau.heading("date",        text="Date")
    tableau.heading("categorie",   text="Catégorie")
    tableau.heading("montant",     text="Montant")
    tableau.heading("description", text="Description")

    tableau.column("id",          width=60,  anchor="center")
    tableau.column("date",        width=130, anchor="center")
    tableau.column("categorie",   width=160, anchor="center")
    tableau.column("montant",     width=120, anchor="center")
    tableau.column("description", width=500, anchor="w")

    barre_defilement = ttk.Scrollbar(cadre_tableau, orient="vertical", command=tableau.yview)
    tableau.configure(yscrollcommand=barre_defilement.set)
    tableau.place(relx=0, rely=0, relwidth=0.97, relheight=1)
    barre_defilement.place(relx=0.97, rely=0, relwidth=0.03, relheight=1)


    barre_bas = ctk.CTkFrame(contenu, fg_color="transparent")
    barre_bas.place(relx=0.02, rely=0.88, relwidth=0.96, relheight=0.07)

    ctk.CTkButton(barre_bas, text="✏ Modifier", width=130, height=38,
                  fg_color="#e67e22", hover_color="#f39c12", text_color="white",
                  font=ctk.CTkFont(family="Montserrat Bold", size=12),
                  command=lambda: ouvrir_popup_modification()
                  ).place(relx=0.00, rely=0.5, anchor="w")

    ctk.CTkButton(barre_bas, text="🗑 Supprimer", width=130, height=38,
                  fg_color="#e74c3c", hover_color="#c0392b", text_color="white",
                  font=ctk.CTkFont(family="Montserrat Bold", size=12),
                  command=lambda: supprimer_la_depense()
                  ).place(relx=0.14, rely=0.5, anchor="w")

    label_total = ctk.CTkLabel(barre_bas, text="Total filtré : 0.00 €",
                               text_color="white",
                               font=ctk.CTkFont(family="Montserrat Bold", size=15))
    label_total.place(relx=1.0, rely=0.5, anchor="e")


    # Fonctions internes

    def charger_depenses_dans_tableau(liste_depenses):
        """Vide le tableau, le remplit et recalcule le total."""
        for ligne in tableau.get_children():
            tableau.delete(ligne)
        total = 0
        for depense in liste_depenses:
            tableau.insert("", "end", values=(
                depense[0], depense[4], depense[2],
                f"{depense[1]:.2f} €", depense[3]
            ))
            total += depense[1]
        label_total.configure(text=f"Total filtré : {total:.2f} €")

    def recuperer_toutes_les_depenses():
        """Retourne toutes les dépenses depuis la base de données."""
        connexion = sqlite3.connect("tables.db")
        curseur   = connexion.cursor()
        curseur.execute("SELECT * FROM depenses ORDER BY id DESC")
        resultat  = curseur.fetchall()
        connexion.close()
        return resultat

    def appliquer_les_filtres():
        """Filtre les dépenses selon la catégorie et/ou le mois saisis."""
        categorie_choisie = menu_categorie.get()
        mois_choisi       = champ_mois.get().strip()

        connexion  = sqlite3.connect("tables.db")
        curseur    = connexion.cursor()
        requete    = "SELECT * FROM depenses WHERE 1=1"
        parametres = []

        if categorie_choisie and categorie_choisie != "Toutes":
            requete += " AND categorie = ?"
            parametres.append(categorie_choisie)

        if mois_choisi:
            try:
                annee = mois_choisi[2:4]
                mois  = mois_choisi[5:7]
                requete += " AND substr(date,4,2) = ? AND substr(date,7,2) = ?"
                parametres += [mois, annee]
            except Exception:
                pass

        requete += " ORDER BY id DESC"
        curseur.execute(requete, parametres)
        depenses_filtrees = curseur.fetchall()
        connexion.close()
        charger_depenses_dans_tableau(depenses_filtrees)

    def reinitialiser_filtres():
        """Remet les filtres à zéro et réaffiche toutes les dépenses."""
        menu_categorie.set("Toutes")
        champ_mois.delete(0, "end")
        charger_depenses_dans_tableau(recuperer_toutes_les_depenses())


    def ouvrir_popup_ajout():
        """Ouvre une fenêtre pour saisir une nouvelle dépense."""
        fenetre_ajout = ctk.CTkToplevel(fenetre)
        fenetre_ajout.title("Ajouter une dépense")
        fenetre_ajout.geometry("400x420")
        fenetre_ajout.grab_set()

        ctk.CTkLabel(fenetre_ajout, text="Montant (€)"
                     ).place(relx=0.5, rely=0.05, anchor="n")
        champ_montant = ctk.CTkEntry(fenetre_ajout, width=250)
        champ_montant.place(relx=0.5, rely=0.13, anchor="n")

        ctk.CTkLabel(fenetre_ajout, text="Catégorie"
                     ).place(relx=0.5, rely=0.25, anchor="n")
        categories_disponibles = ["Alimentation", "Transport", "Logement",
                                   "Loisirs", "Santé", "Vêtements", "Éducation", "Autre"]
        menu_cat_ajout = ctk.CTkComboBox(fenetre_ajout, values=categories_disponibles, width=250)
        menu_cat_ajout.set(categories_disponibles[0])
        menu_cat_ajout.place(relx=0.5, rely=0.33, anchor="n")

        ctk.CTkLabel(fenetre_ajout, text="Description"
                     ).place(relx=0.5, rely=0.45, anchor="n")
        champ_description = ctk.CTkEntry(fenetre_ajout, width=250)
        champ_description.place(relx=0.5, rely=0.53, anchor="n")

        ctk.CTkLabel(fenetre_ajout, text="Date (dd/mm/yy) — vide = aujourd'hui"
                     ).place(relx=0.5, rely=0.65, anchor="n")
        champ_date = ctk.CTkEntry(fenetre_ajout, width=250)
        champ_date.place(relx=0.5, rely=0.73, anchor="n")

        def valider_ajout():
            try:
                montant_saisi = float(champ_montant.get().replace(",", "."))
            except ValueError:
                return
            date_saisie = champ_date.get().strip() or None
            ajout_depense(1, montant_saisi, menu_cat_ajout.get(),
                          champ_description.get().strip(), date_saisie)
            fenetre_ajout.destroy()
            reinitialiser_filtres()

        ctk.CTkButton(fenetre_ajout, text="✅ Valider", fg_color="#27ae60",
                      width=200, command=valider_ajout
                      ).place(relx=0.5, rely=0.87, anchor="n")

    def supprimer_la_depense():
        """Supprime la dépense sélectionnée dans le tableau."""
        ligne_selectionnee = tableau.selection()
        if not ligne_selectionnee:
            return
        identifiant_depense = tableau.item(ligne_selectionnee[0])["values"][0]
        connexion = sqlite3.connect("tables.db")
        curseur   = connexion.cursor()
        curseur.execute("DELETE FROM depenses WHERE id = ?", (identifiant_depense,))
        connexion.commit()
        connexion.close()
        reinitialiser_filtres()

    def ouvrir_popup_modification():
        """Ouvre une fenêtre pré-remplie pour modifier la dépense sélectionnée."""
        ligne_selectionnee = tableau.selection()
        if not ligne_selectionnee:
            return
        valeurs_actuelles   = tableau.item(ligne_selectionnee[0])["values"]
        identifiant_depense = valeurs_actuelles[0]

        fenetre_modification = ctk.CTkToplevel(fenetre)
        fenetre_modification.title("Modifier la dépense")
        fenetre_modification.geometry("400x420")
        fenetre_modification.grab_set()

        ctk.CTkLabel(fenetre_modification, text="Montant (€)"
                     ).place(relx=0.5, rely=0.05, anchor="n")
        champ_montant = ctk.CTkEntry(fenetre_modification, width=250)
        champ_montant.insert(0, str(valeurs_actuelles[3]).replace(" €", ""))
        champ_montant.place(relx=0.5, rely=0.13, anchor="n")

        ctk.CTkLabel(fenetre_modification, text="Catégorie"
                     ).place(relx=0.5, rely=0.25, anchor="n")
        categories_disponibles = ["Alimentation", "Transport", "Logement",
                                   "Loisirs", "Santé", "Vêtements", "Éducation", "Autre"]
        menu_cat_modif = ctk.CTkComboBox(fenetre_modification, values=categories_disponibles, width=250)
        menu_cat_modif.set(valeurs_actuelles[2])
        menu_cat_modif.place(relx=0.5, rely=0.33, anchor="n")

        ctk.CTkLabel(fenetre_modification, text="Description"
                     ).place(relx=0.5, rely=0.45, anchor="n")
        champ_description = ctk.CTkEntry(fenetre_modification, width=250)
        champ_description.insert(0, str(valeurs_actuelles[4]))
        champ_description.place(relx=0.5, rely=0.53, anchor="n")

        ctk.CTkLabel(fenetre_modification, text="Date (dd/mm/yy)"
                     ).place(relx=0.5, rely=0.65, anchor="n")
        champ_date = ctk.CTkEntry(fenetre_modification, width=250)
        champ_date.insert(0, str(valeurs_actuelles[1]))
        champ_date.place(relx=0.5, rely=0.73, anchor="n")

        def valider_modification():
            try:
                montant_modifie = float(champ_montant.get().replace(",", ".").replace(" €", ""))
            except ValueError:
                return
            connexion = sqlite3.connect("tables.db")
            curseur   = connexion.cursor()
            curseur.execute(
                "UPDATE depenses SET montant=?, categorie=?, description=?, date=? WHERE id=?",
                (montant_modifie, menu_cat_modif.get(),
                 champ_description.get().strip(), champ_date.get().strip(),
                 identifiant_depense)
            )
            connexion.commit()
            connexion.close()
            fenetre_modification.destroy()
            reinitialiser_filtres()

        ctk.CTkButton(fenetre_modification, text="✅ Enregistrer", fg_color="#27ae60",
                      width=200, command=valider_modification
                      ).place(relx=0.5, rely=0.87, anchor="n")

    # Chargement initial
    charger_depenses_dans_tableau(recuperer_toutes_les_depenses())


# Boutons sidebar
    

#Page de droite (par opposition au sidebar)
contenu = ctk.CTkFrame(fenetre, corner_radius=0, fg_color="#1f1f1f")
contenu.pack(side="right", fill="both", expand=True)

#Bouttons (ne pas oublier les commandes pour les bouttons)

btn_dashboard = ctk.CTkButton(sidebar, 
                              text="🔰​ Tableau de bord", 
                              fg_color="gray30", 
                              hover_color="gray", 
                              command=afficher_dashboard,
                              font=ctk.CTkFont(family="Montserrat Bold", size=12)
                              )

btn_dashboard.pack(fill='x', pady=11, padx=15)

btn_depenses = ctk.CTkButton(sidebar, 
                             text="​💲​ Dépenses", 
                             fg_color="gray30", 
                             hover_color="gray", 
                             command=afficher_depenses, 
                             font=ctk.CTkFont(family="Montserrat Bold", size=12))
btn_depenses.pack(fill='x', pady=11, padx=15)
    
btn_graphiques = ctk.CTkButton(sidebar, 
                               text="📊​ Graphiques", 
                               fg_color="gray30", 
                               hover_color="gray", 
                               command=afficher_graphiques, 
                               font=ctk.CTkFont(family="Montserrat Bold", size=12))
btn_graphiques.pack(fill='x',pady=11, padx=15)

JN = ctk.CTkLabel(sidebar ,text="JN Industries \n Tous droits reservés ®️​", text_color="white",font=ctk.CTkFont(family="Montserrat Bold", size=13))
JN.pack(side="bottom", pady=10)
 
btn_dashboard.invoke()
fenetre.mainloop()