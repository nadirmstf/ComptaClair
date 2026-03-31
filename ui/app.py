from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication(sys.argv) 
 
fenetre = QMainWindow()        
fenetre.setWindowTitle("ComptaClair - Suivez vos dépenses")
fenetre.setFixedSize(1300, 600) 
fenetre.show()                 

sys.exit(app.exec())           