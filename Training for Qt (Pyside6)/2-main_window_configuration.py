from PySide6.QtWidgets import QApplication, QWidget


# Définition de la classe "MainWindow" qui hérite de "QWidget"
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()  # Appel du constructeur de la classe parente "QWidget"

        # Utilisation de "self" pour faire référence à l'instance actuelle de "MainWindow"
        # Définition du titre de la fenêtre principale
        self.setWindowTitle("Mon application")

        # Les lignes suivantes sont commentées et montrent différentes manières de définir la taille de la fenêtre

        # self.setFixedSize(200, 200)  # Définir une taille fixe de 200x200 pixels pour la fenêtre
        # self.setMinimumWidth(200)  # Définir la largeur minimale de la fenêtre à 200 pixels
        # self.setMinimumHeight(300)  # Définir la hauteur minimale de la fenêtre à 300 pixels

        # Définir la taille de la fenêtre à 400x400 pixels
        self.resize(400, 400)


# Initialisation de l'application "QApplication"
app = QApplication()

# Création et affichage de l'instance de "MainWindow"
main_window = MainWindow()
main_window.show()

# Démarrage de la boucle d'événements de l'application (event loop)
app.exec()
