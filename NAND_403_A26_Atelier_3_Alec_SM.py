from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QTextEdit, QPushButton, QMessageBox

class MessageBoard(QWidget): 
    def __init__(self): # Constructeur
        super().__init__() #Constructeur QWidget
        self.setWindowTitle("Programme cool") 
        self.create_ui()


    def create_ui(self):

        global texte_recu 

        self.input_bar = QTextEdit()
        print_button = QPushButton("Print")
        layout = QVBoxLayout(self)
        label = QLabel("Message Board")

        
        print_button.pressed.connect(self.on_click)


        layout.addWidget(label)
        layout.addWidget(self.input_bar)
        layout.addWidget(print_button)


    def on_click(self):

        texte_recu = self.input_bar.toPlainText()
        print_box = QMessageBox()
        print_box.setText(texte_recu)
        print_box.exec()
       
def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass

     
    widget = MessageBoard()
    widget.show()
 
main()
