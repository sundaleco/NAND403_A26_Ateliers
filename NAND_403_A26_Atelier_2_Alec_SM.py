  
import sys 
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLineEdit,  QMessageBox
import json
from pathlib import Path
from PySide6.QtCore import Qt

# fenetre pyside6

app = QApplication(sys.argv) 
main_fenetre = QMainWindow() 
tableau = QTableWidget() 

verticle_box = QVBoxLayout()
verticle_box.addWidget(tableau)  

main_widget = QWidget()
main_widget.setLayout(verticle_box)

#load json (facon vu en classe marche pas)

path = Path(__file__).parent / "drinks.json"
with path.open("r", encoding="utf-8") as fichier:
    fichier_json = json.load(fichier) 

#remplir tablo

header_labels = list(fichier_json[0].keys()) 

tableau.setRowCount(len(fichier_json))
tableau.setColumnCount(len(header_labels))
tableau.setHorizontalHeaderLabels(header_labels)


#avec enum

# for i ,objet in enumerate(fichier_json):

#     for j, key in enumerate(colonnes): 
       
#        tableau.setItem(i,j, QTableWidgetItem(objet[key]))


for i in range(len(fichier_json)):
    for j in range(len(header_labels)):
        tableau.setItem(i, j, QTableWidgetItem(str(fichier_json[i][header_labels[j]])))


#run app

main_fenetre.setCentralWidget(main_widget)
main_fenetre.show()
app.exec()
