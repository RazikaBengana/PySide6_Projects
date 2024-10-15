from PySide6.QtWidgets import QApplication, QPushButton, QHBoxLayout, QWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Définition du titre de la fenêtre
        self.setWindowTitle("Custom Button")

        # Création d'un layout horizontal pour organiser les boutons
        self.layout = QHBoxLayout(self)

        # Création de trois boutons numérotés
        button1 = QPushButton("1")
        button2 = QPushButton("2")
        button3 = QPushButton("3")

        # Ajout des boutons dans le layout
        self.layout.addWidget(button1)
        self.layout.addWidget(button2)
        self.layout.addWidget(button3)

        # Définition des proportions des boutons dans le layout
        # Le premier et le troisième bouton occupent 2 fois plus d'espace que le deuxième
        self.layout.setStretch(0, 2)  # Étirement du premier bouton
        self.layout.setStretch(1, 1)  # Étirement du deuxième bouton
        self.layout.setStretch(2, 2)  # Étirement du troisième bouton


app = QApplication([])
win = MainWindow()
win.show()
app.exec()
