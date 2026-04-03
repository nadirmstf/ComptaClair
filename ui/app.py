from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from PIL import Image
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

def afficher_dashboard() :
    for w in contenu.winfo_children():  # récupère tous les widgets dans contenu
        w.destroy()
    titre = ctk.CTkLabel(contenu ,text="TABLEAU DE BORD​", text_color="white",font=ctk.CTkFont(family="Montserrat Bold", size=35))
    titre.place(x=50, y=40)
    #Dernière dépense
    frame1 = ctk.CTkFrame(contenu, fg_color="#2b2b2b", height=120,width=250)
    frame1.place(x=50, y=110)
    frame2 = ctk.CTkFrame(contenu, fg_color="#2b2b2b", height=120,width=250)
    frame2.place(x=315, y=110)
    frame3 = ctk.CTkFrame(contenu, fg_color="#2b2b2b", height=120,width=250)
    frame3.place(x=580, y=110)
    frame4 = ctk.CTkFrame(contenu, fg_color="#2b2b2b", height=120,width=250)
    frame4.place(x=845, y=110)


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

btn_dashboard = ctk.CTkButton(sidebar, text="🔰​ Tableau de bord", fg_color="gray30", hover_color="gray", command=afficher_dashboard, font=ctk.CTkFont(family="Montserrat Bold", size=12))
btn_dashboard.pack(fill='x', pady=11, padx=15)

btn_depenses = ctk.CTkButton(sidebar, text="​💲​ Dépenses", fg_color="gray30", hover_color="gray", command=afficher_depenses, font=ctk.CTkFont(family="Montserrat Bold", size=12))
btn_depenses.pack(fill='x', pady=11, padx=15)

btn_graphiques = ctk.CTkButton(sidebar, text="📊​ Graphiques", fg_color="gray30", hover_color="gray", command=afficher_graphiques, font=ctk.CTkFont(family="Montserrat Bold", size=12))
btn_graphiques.pack(fill='x',pady=11, padx=15)

JN = ctk.CTkLabel(sidebar ,text="JN Industries \n Tous droits reservés ®️​", text_color="white",font=ctk.CTkFont(family="Montserrat Bold", size=8))
JN.pack(side="bottom", pady=10)


btn_dashboard.invoke()
fenetre.mainloop()



