from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QMessageBox,QHBoxLayout, QLineEdit

from maya import cmds

import random

class MessageBoard(QWidget): 

    def __init__(self): # Constructeur
        super().__init__() #Constructeur QWidget
        self.setWindowTitle("Programme cool") 
        self.create_ui()

    def create_ui(self):

        #region setup

        print_button = QPushButton("Create Objects")

        layout_main = QVBoxLayout(self)

        layout_h1 = QHBoxLayout()
        layout_h2 = QHBoxLayout()
        layout_v1 = QVBoxLayout()
        layout_v2 = QVBoxLayout()
        layout_v3 = QVBoxLayout()
        label_1 = QLabel("Number of objects :")
        label_2 = QLabel("Min :")
        label_3 = QLabel("Max :")
        label_4 = QLabel("Position X :")
        label_5 = QLabel("Position Y :")
        label_6 = QLabel("Position Z :")
        label_7 = QLabel("Scale :")
        label_8 = QLabel(" ")

        self.nb_obj = QLineEdit()
        self.xmin = QLineEdit()
        self.xmax = QLineEdit()
        self.ymin = QLineEdit()
        self.ymax = QLineEdit()
        self.zmin = QLineEdit()
        self.zmax = QLineEdit()
        self.smin = QLineEdit()
        self.smax = QLineEdit()


        layout_v3.addWidget(label_3)
        layout_v3.addWidget(self.xmax)
        layout_v3.addWidget(self.ymax)
        layout_v3.addWidget(self.zmax)
        layout_v3.addWidget(self.smax)
        layout_v2.addWidget(label_2)
        layout_v2.addWidget(self.xmin)
        layout_v2.addWidget(self.ymin)
        layout_v2.addWidget(self.zmin)
        layout_v2.addWidget(self.smin)
        layout_v1.addWidget(label_8)
        layout_v1.addWidget(label_4)
        layout_v1.addWidget(label_5)
        layout_v1.addWidget(label_6)
        layout_v1.addWidget(label_7)

        layout_h1.addWidget(label_1)
        layout_h1.addWidget(self.nb_obj)

        layout_h2.addLayout(layout_v1)
        layout_h2.addLayout(layout_v2)
        layout_h2.addLayout(layout_v3)

       

        #endregion

        layout_main.addLayout(layout_h1)
        layout_main.addLayout(layout_h2)

        layout_main.addWidget(print_button)
        print_button.pressed.connect(self.on_click)

    def on_click(self):

        self.create_object()

    def create_object(self):

        nb_obj_value = self.nb_obj.text()

        for i in range(int(nb_obj_value)):

            forme = random.choice(["cube", "cylindre", "sphere"])

            if forme == "cube":
                objet = cmds.polyCube()[0]

            elif forme == "cylindre":
                objet = cmds.polyCylinder()[0]

            else:
                objet = cmds.polySphere()[0]

            random_value_x = random.uniform(float(self.xmin.text()), float(self.xmax.text()))
            random_value_y = random.uniform(float(self.ymin.text()), float(self.ymax.text()))
            random_value_z = random.uniform(float(self.zmin.text()), float(self.zmax.text()))
            random_value_s = random.uniform(float(self.smin.text()), float(self.smax.text()))

            cmds.move(random_value_x, random_value_y, random_value_z, objet)
            cmds.scale(random_value_s, random_value_s, random_value_s, objet)

def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass

     
    widget = MessageBoard()
    widget.show()
 
main()

