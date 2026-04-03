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
ctypes.windll.gdi32.AddFontResourceW("assets/fonts/Montserrat/Montserrat-Light.ttf")

#Side Bar
sidebar = ctk.CTkFrame(fenetre, width=200, corner_radius=0, fg_color="#2b2b2b")
sidebar.pack(side="left", fill="y") 
sidebar.pack_propagate(False)

#Logo
logo = ctk.CTkImage(Image.open("assets/img/logo.png"), size=(100, 100))
ctk.CTkLabel(sidebar, image=logo, text="Compta Clair \n Suivi de dépenses", 
             compound="top", text_color="white").pack(pady='30')  # image en haut, texte en bas



#Bouttons (ne pas oublier les commandes pour les bouttons)
btn_dashboard = ctk.CTkButton(sidebar, text="🔰​ Tableau de bord", fg_color="gray30", hover_color="gray")
btn_dashboard.pack(fill='x', pady=8, padx='15')

btn_dashboard = ctk.CTkButton(sidebar, text="​💲​ Dépenses", fg_color="gray30", hover_color="gray")
btn_dashboard.pack(fill='x', pady=8, padx='15')

btn_dashboard = ctk.CTkButton(sidebar, text="📊​ Graphiques", fg_color="gray30", hover_color="gray")
btn_dashboard.pack(fill='x', pady=8,padx='15')

# JN = ctk.CTkLabel(sidebar ,text="JN Industries \n Tous droits reservés ®️​")


contenu = ctk.CTkFrame(fenetre, corner_radius=0, fg_color="#1f1f1f")
contenu.pack(side="right", fill="both", expand=True)



# tabs = ctk.CTkTabview(fenetre, anchor="w")
# tabs.pack(fill="both", expand=True, padx=20, pady=20)

# # Ajouter les onglets
# tabs.add("Tableau de Bord")
# tabs.add("Dépenses")
# tabs.add("Graphiques")




fenetre.mainloop()



