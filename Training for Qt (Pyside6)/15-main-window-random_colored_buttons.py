from random import randrange
from PySide6.QtWidgets import QApplication, QHBoxLayout, QPushButton, QWidget


# Crée une classe héritée de QPushButton pour un bouton personnalisé
class RandomButton(QPushButton):
    def __init__(self, size=48, flat=False):
        super().__init__()  # Appelle le constructeur de la classe parente QPushButton

        self.setText(str(randrange(999)))  # Définit un texte aléatoire pour le bouton
        self.setMinimumSize(size, size)  # Définit une taille minimale pour le bouton
        self.setFlat(flat)  # Rend le bouton plat si flat est défini à True
        self.setCheckable(True)  # Rend le bouton "vérifiable" (comme un interrupteur)
        self.setStyleSheet(f"color: rgb({randrange(255)}, {randrange(255)}, {randrange(255)});")  # Définit une couleur de texte aléatoire
        self.clicked.connect(self.random_color)  # Connecte le signal "clicked" à la méthode "random_color"

    def random_color(self):
        # Change la couleur du texte du bouton à chaque clic
        self.setStyleSheet(f"color: rgb({randrange(255)}, {randrange(255)}, {randrange(255)});")


# Crée une fenêtre principale héritée de QWidget
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()  # Appelle le constructeur de la classe parente QWidget

        self.setWindowTitle("Custom Button")  # Définit le titre de la fenêtre
        self.layout = QHBoxLayout(self)  # Crée un layout horizontal pour la fenêtre

        for _ in range(10):  # Ajoute 10 boutons personnalisés au layout
            btn_random = RandomButton(size=randrange(10, 80), flat=True)
            self.layout.addWidget(btn_random)  # Ajoute le bouton au layout

        # Met le focus sur la fenêtre pour que l'utilisateur puisse interagir directement sans cliquer
        self.setFocus()


app = QApplication()
win = MainWindow()
win.show()
app.exec()
