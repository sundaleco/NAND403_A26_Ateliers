from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QSpinBox, QDoubleSpinBox

from maya import cmds

import random

class ProgramUI(QWidget):

    def __init__(self): 
        super().__init__() 
        self.setWindowTitle("Maya Fence Tool")
        self.create_ui()

    def create_ui(self):

        layout_main = QVBoxLayout(self)

        #region Nombre de sections
        layout_h1 = QHBoxLayout()
        layout_h1.addWidget(QLabel("Nombre de potaux verticals :"))

        self.nb_poteaux_vertical = QSpinBox()
        self.nb_poteaux_vertical.setRange(1, 100)
        self.nb_poteaux_vertical.setValue(5)

        layout_h1.addWidget(self.nb_poteaux_vertical)
        layout_main.addLayout(layout_h1)

        #endregion

        #region Longueur totale


        layout_h2 = QHBoxLayout()
        layout_h2.addWidget(QLabel("Longueur :"))

        self.longueur = QDoubleSpinBox()
        self.longueur.setRange(0.1, 1000)
        self.longueur.setValue(12)
        self.longueur.setSingleStep(1)
        self.longueur.setDecimals(2)

        layout_h2.addWidget(self.longueur)
        layout_main.addLayout(layout_h2)

        self.lg_tot = self.longueur.value()


        #endregion

        #region Hauteur des poteaux

        layout_h3 = QHBoxLayout()
        layout_h3.addWidget(QLabel("Hauteur :"))

        self.hauteur = QDoubleSpinBox()
        self.hauteur.setRange(0.1, 100)
        self.hauteur.setValue(2)
        self.hauteur.setSingleStep(0.5)
        self.hauteur.setDecimals(2)

        layout_h3.addWidget(self.hauteur)
        layout_main.addLayout(layout_h3)

        self.poteaux_y = self.hauteur.value()


        #endregion

        #region Epaisseur des poteaux
        layout_h4 = QHBoxLayout()
        layout_h4.addWidget(QLabel("Epaisseur des poteaux :"))

        self.epaisseur_poteau = QDoubleSpinBox()
        self.epaisseur_poteau.setRange(0.01, 10)
        self.epaisseur_poteau.setValue(0.2)
        self.epaisseur_poteau.setSingleStep(0.1)
        self.epaisseur_poteau.setDecimals(2)

        layout_h4.addWidget(self.epaisseur_poteau)
        layout_main.addLayout(layout_h4)

        self.thick_v = self.epaisseur_poteau.value()

        #endregion

        #region Nombre de barres horizontales
        layout_h5 = QHBoxLayout()
        layout_h5.addWidget(QLabel("Nombre de barres :"))

        self.nb_barres = QSpinBox()
        self.nb_barres.setRange(1, 20)
        self.nb_barres.setValue(2)

        layout_h5.addWidget(self.nb_barres)
        layout_main.addLayout(layout_h5)

        self.nb_barre_h = self.nb_barres.value()

        #endregion

        #region Epaisseur des barres


        layout_h6 = QHBoxLayout()
        layout_h6.addWidget(QLabel("Epaisseur des barres :"))

        self.epaisseur_barre = QDoubleSpinBox()
        self.epaisseur_barre.setRange(0.01, 10)
        self.epaisseur_barre.setValue(0.12)
        self.epaisseur_barre.setSingleStep(0.05)
        self.epaisseur_barre.setDecimals(2)

        layout_h6.addWidget(self.epaisseur_barre)
        layout_main.addLayout(layout_h6)


        self.thick_h = self.epaisseur_barre.value()

        #endregion

        #region Bouton
        print_button = QPushButton("Create Objects")
        #endregion

        layout_main.addWidget(print_button)
        print_button.pressed.connect(self.on_click)

        #region variables

        self.lg_tot = self.longueur.value()
        self.poteaux_y = self.hauteur.value()
        self.thick_v = self.epaisseur_poteau.value()
        self.nb_barre_h = self.nb_barres.value()
        self.thick_h = self.epaisseur_barre.value()

        #endregion

    def on_click(self):

        self.create_verticale_poly()
        self.create_horizontale_poly()

    def create_horizontale_poly(self):

        for i in range(self.nb_barre_h):

                    mesh_h = cmds.polyCylinder()[0]

                    longueur_h = self.lg_tot - (2 * self.thick_v)

                    pos_y = (i + 1) * self.poteaux_y / (self.nb_barre_h + 1)

                    cmds.scale(self.thick_h / 2, longueur_h / 2, self.thick_h / 2, mesh_h)

                    cmds.rotate(0, 0, 90, mesh_h)

                    cmds.move(self.lg_tot / 2, pos_y, 0, mesh_h)

    def create_verticale_poly(self):

        for i in range(self.nb_poteaux_vertical.value()):

            mesh_v = cmds.polyCylinder()[0]

            pos_x = self.thick_v / 2 + (i * (self.lg_tot - self.thick_v)) / (self.nb_poteaux_vertical.value() - 1)

            cmds.scale(self.thick_v / 2, self.poteaux_y / 2, self.thick_v / 2, mesh_v)

            cmds.move(pos_x, self.poteaux_y / 2, 0, mesh_v)


def main():

    global widget
    try:
        widget.close()
    except:
        pass


    widget = ProgramUI()
    widget.show()

main()