from PySide6.QtWidgets import QApplication, QPushButton, QHBoxLayout, QWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mon application")

        # Crée un layout horizontal pour la fenêtre principale
        main_layout = QHBoxLayout(self)

        button = QPushButton("Click me")
        main_layout.addWidget(button)  # Ajoute le bouton au layout horizontal

        # Connecte les signaux des événements de pression et de relâchement du bouton à leurs slots (méthodes) respectifs
        # Note : on passe la référence de la méthode sans les parenthèses pour ne pas l'exécuter immédiatement (on veut juste la connecter)
        button.pressed.connect(self.button_pressed)
        button.released.connect(self.button_released)

    # Méthode appelée lorsque le bouton est pressé
    def button_pressed(self):
        print("Le bouton a bien été pressé.")

    # Méthode appelée lorsque le bouton est relâché
    def button_released(self):
        print("Le bouton a bien été relâché.")


app = QApplication()


main_window = MainWindow()
main_window.show()
app.exec()
