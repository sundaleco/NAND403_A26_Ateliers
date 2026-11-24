import random


from shiboken6 import wrapInstance

from maya import cmds
import maya.OpenMayaUI as omui
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QFormLayout,
    QSpinBox,
    QDoubleSpinBox,
    QPushButton,
    QMessageBox
)


from PySide6.QtCore import Qt



def maya_main_window():
    pointer = omui.MQtUtil.mainWindow()
    return wrapInstance(int(pointer), QWidget)


class Scatter(QWidget):

    def __init__(self):
        super().__init__(maya_main_window())
        self.setWindowFlags(Qt.Window)
        self.setWindowTitle("Scatter")
        self.setMinimumWidth(250)
        self.build_ui()

    def build_ui(self):
        layout = QVBoxLayout(self)
        form = QFormLayout()
        layout.addLayout(form)

        self.count_spin = QSpinBox()
        self.count_spin.setRange(1, 100)
        self.count_spin.setValue(10)
        form.addRow("Copies", self.count_spin)

        self.radius_spin = QDoubleSpinBox()
        self.radius_spin.setRange(1.0, 50.0)
        self.radius_spin.setValue(10.0)
        form.addRow("Radius", self.radius_spin)

        self.seed_spin = QSpinBox()
        self.seed_spin.setRange(0, 9999)
        form.addRow("Seed", self.seed_spin)

        scatter_button = QPushButton("Scatter")
        scatter_button.clicked.connect(self.scatter)
        layout.addWidget(scatter_button)

    def scatter(self):
        selection = cmds.ls(selection=True, transforms=True)
        if not selection:
            QMessageBox.warning(self, "Scatter", "Select an object first.")
            return
        source = selection[0]

        cmds.undoInfo(openChunk=True)
        try:
            random.seed(self.seed_spin.value())
            radius = self.radius_spin.value()
            group = cmds.group(empty=True, name="scatter_grp")
            for i in range(self.count_spin.value()):
                copy = cmds.duplicate(source)[0]
                copy = cmds.parent(copy, group)[0]
                x = random.uniform(-radius, radius)
                z = random.uniform(-radius, radius)
                cmds.move(x, 0, z, copy, relative=True)
        finally:
            cmds.undoInfo(closeChunk=True)


def show_tool():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = Scatter()
    tool_window.show()


show_tool()
