from PySide6.QtWidgets import QApplication, QPushButton, QHBoxLayout, QWidget
# Importation de "partial" depuis "functools" pour permettre le passage d'arguments supplémentaires aux slots
from functools import partial


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mon application")

        # Initialisation d'un layout horizontal pour organiser les widgets
        main_layout = QHBoxLayout(self)

        # Création de deux boutons
        self.btn_left = QPushButton("Left")
        self.btn_right = QPushButton("Right")

        # Ajout des boutons au layout horizontal
        main_layout.addWidget(self.btn_left)
        main_layout.addWidget(self.btn_right)

        # Connexion des événements de clic des boutons à la méthode "button_clicked"
        # Utilisation de "partial" pour passer un argument supplémentaire (le message) à la méthode "button_clicked"
        self.btn_left.clicked.connect(partial(self.button_clicked, "Bouton de gauche"))
        self.btn_right.clicked.connect(partial(self.button_clicked, "Bouton de droite"))

    # Méthode exécutée lors du clic sur un bouton
    # Affiche le message correspondant au bouton cliqué dans la console
    def button_clicked(self, message):
        print(message)


app = QApplication()


main_window = MainWindow()
main_window.show()
app.exec()
