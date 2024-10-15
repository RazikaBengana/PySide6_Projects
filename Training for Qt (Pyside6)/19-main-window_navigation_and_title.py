# QSize pour gérer les dimensions, Qt pour les options d'alignement et les autres constantes
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QHBoxLayout, QLabel, QPushButton, QSizePolicy, QWidget, QApplication


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Définir le titre de la fenêtre
        self.setWindowTitle("Stretch")

        # Créer un layout horizontal pour organiser les widgets
        self.layout = QHBoxLayout(self)

        # Créer les boutons de navigation et l'étiquette du titre
        previous = QPushButton("<<")  # Bouton pour aller à la page précédente
        titre = QLabel("Introduction à Python")  # Titre centré
        titre.setAlignment(Qt.AlignCenter)  # Aligner le texte au centre horizontalement
        next = QPushButton(">>")  # Bouton pour aller à la page suivante

        # Solution #1 : Ajouter les widgets et des espaces vides (stretch)
        self.layout.addWidget(previous)
        self.layout.addStretch()  # Ajouter un espace extensible à gauche du titre
        self.layout.addWidget(titre)
        self.layout.addStretch()  # Ajouter un espace extensible à droite du titre
        self.layout.addWidget(next)

        # Solution #2 : Fixer la taille des boutons pour qu'ils ne s'étirent pas
        previous.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        next.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # Solution #3 : Ajuster les proportions de l'étirement des widgets
        self.layout.setStretch(0, 1)  # Le bouton "previous" a un espace d'étirement de 1
        self.layout.setStretch(1, 100)  # Le stretch autour du titre a une grande priorité
        self.layout.setStretch(2, 1)  # Le bouton "next" a un espace d'étirement de 1

        # Solution #4 : Limiter la largeur maximale des boutons pour éviter qu'ils ne s'étirent trop
        previous.setMaximumWidth(previous.sizeHint().width())
        next.setMaximumWidth(next.sizeHint().width())

        # Donner le focus à la fenêtre pour qu'elle réagisse immédiatement
        self.setFocus()


app = QApplication()
win = MainWindow()
win.show()
app.exec()
