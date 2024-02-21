# Importation du module "sys" pour interagir directement avec l'interpréteur
import sys
# Importation des classes "QApplication" et "QPushButton" depuis le module "PySide6.QtWidgets"
from PySide6.QtWidgets import QApplication, QPushButton


# Initialisation de l'application et création du bouton
app = QApplication(sys.argv)  # Création d'une instance de "QApplication" --> il doit y avoir une seule instance de "QApplication" par application
btn = QPushButton("Click me")  # Création d'un bouton avec le texte "Click me"


# Affichage du bouton et démarrage de la boucle d'événements (event loop)
btn.show()  # Affiche le bouton dans une fenêtre
app.exec()  # Démarre le programme pour réagir aux actions de l'utilisateur
