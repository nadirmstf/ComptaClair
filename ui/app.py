from tkinter import *
from tkinter import ttk
import customtkinter as ctk
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


btn_dashboard = ctk.CTkButton(sidebar, text="🔰​ Tableau de bord", fg_color="gray30", hover_color="gray")
btn_dashboard.pack()

btn_dashboard = ctk.CTkButton(sidebar, text="​💲​ Dépenses", fg_color="gray30", hover_color="gray")
btn_dashboard.pack()

btn_dashboard = ctk.CTkButton(sidebar, text="📊​ Graphiques", fg_color="gray30", hover_color="gray")
btn_dashboard.pack()


contenu = ctk.CTkFrame(fenetre, corner_radius=0, fg_color="#1f1f1f")
contenu.pack(side="right", fill="both", expand=True)



# tabs = ctk.CTkTabview(fenetre, anchor="w")
# tabs.pack(fill="both", expand=True, padx=20, pady=20)

# # Ajouter les onglets
# tabs.add("Tableau de Bord")
# tabs.add("Dépenses")
# tabs.add("Graphiques")




fenetre.mainloop()



