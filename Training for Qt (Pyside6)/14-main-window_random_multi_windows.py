# Importation de "randrange" pour générer un numéro aléatoire
from random import randrange
from PySide6.QtWidgets import QApplication, QPushButton, QHBoxLayout, QWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configuration du titre de la fenêtre principale
        self.setWindowTitle("Multi Window")

        # Création et configuration du layout horizontal pour la fenêtre principale
        self.layout = QHBoxLayout(self)

        # Création du bouton pour ouvrir une nouvelle fenêtre
        self.btn_new_window = QPushButton("New Window")

        # Connexion du bouton à la méthode de création de nouvelles fenêtres
        self.btn_new_window.clicked.connect(self.create_new_window)

        # Ajout du bouton au layout de la fenêtre principale
        self.layout.addWidget(self.btn_new_window)

        # Initialisation d'un dictionnaire pour stocker les références des fenêtres ouvertes
        self.window = {}  # Cela empêche les fenêtres de se fermer automatiquement (voir "Garbage Collector")

        # Réglage de la taille de la fenêtre principale
        self.resize(600, 400)

    def create_new_window(self):
        # Génération d'un numéro aléatoire pour la nouvelle fenêtre
        window_number = randrange(999)

        # Création et stockage d'une nouvelle fenêtre dans le dictionnaire
        self.window[f"window{window_number}"] = QWidget()

        # Configuration du titre de la nouvelle fenêtre avec le numéro unique
        self.window[f"window{window_number}"].setWindowTitle(f"Fenêtre #{window_number}")

        # Affichage de la nouvelle fenêtre
        self.window[f"window{window_number}"].show()


app = QApplication()
main_window = MainWindow()
main_window.show()
app.exec()


"""
Garbage Collector (GC):

en Python, c'est un mécanisme qui permet de libérer automatiquement la mémoire allouée aux objets
qui ne sont plus utilisés par le programme (c'est-à-dire les objets qui ne sont plus référencés).

En conservant des références actives aux fenêtres ouvertes dans ce dictionnaire, on empêche le GC
de les considérer comme inutilisées et donc de les supprimer.

Cela assure que les fenêtres restent ouvertes tant qu'elles sont stockées dans le dictionnaire,
évitant ainsi leur fermeture et destruction automatiques par le mécanisme de gestion de la mémoire.
"""
