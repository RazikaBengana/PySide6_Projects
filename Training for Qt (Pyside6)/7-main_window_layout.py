from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mon application")

        # Création et configuration du layout principal
        # Le layout est parenté à la fenêtre principale avec "self"
        main_layout = QVBoxLayout(self)  # Initialise "QVBoxLayout" pour organiser les widgets verticalement
        for i in range(10):
            button = QPushButton("Click me")  # Crée un bouton avec le texte "Click me"
            main_layout.addWidget(button)  # Ajoute le bouton au layout vertical

        """
        QHBoxLayout  # Organise les widgets sur un axe horizontal
        QGridLayout  # Organise les widgets en grille
        """


app = QApplication()


main_window = MainWindow()
main_window.show()
app.exec()
