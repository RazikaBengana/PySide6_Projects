from PySide6.QtCore import QSize  # QSize permet de définir des dimensions (largeur, hauteur) pour les objets
from PySide6.QtWidgets import QApplication, QPushButton, QHBoxLayout, QWidget, QLineEdit, QSizePolicy


class CustomLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        # Initialisation du QLineEdit personnalisé

    # Redéfinition de la méthode sizeHint pour spécifier une taille préférée personnalisée
    def sizeHint(self):
        return QSize(200, 20)  # Retourne une taille fixe de 200x20 pixels pour le champ texte

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Custom Button")  # Définition du titre de la fenêtre
        self.layout = QHBoxLayout(self)  # Utilisation d'un layout horizontal pour organiser les widgets

        line_edit = CustomLineEdit()  # Création du QLineEdit personnalisé
        button = QPushButton("Login")  # Création d'un bouton avec le texte "Login"

        print(button.sizePolicy())  # Affichage de la politique de taille du bouton pour information/debug

        # Définir les politiques de taille des widgets
        line_edit.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)  # Taille fixe en largeur, mais expansible en hauteur
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # Expansible en largeur et en hauteur

        # Ajout des widgets au layout
        self.layout.addWidget(line_edit)
        self.layout.addWidget(button)

        self.setFocus()  # Met le focus par défaut sur l'élément de la fenêtre


app = QApplication()
win = MainWindow()
win.show()
app.exec()
