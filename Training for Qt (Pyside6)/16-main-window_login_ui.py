from PySide6.QtWidgets import QApplication, QPushButton, QHBoxLayout, QWidget, QLineEdit


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Custom Button")
        self.layout = QHBoxLayout(self)

        # Création d'un champ de texte (QLineEdit) pour entrer des informations
        line_edit = QLineEdit()

        # Création d'un bouton "Login"
        button = QPushButton("Login")

        # La méthode sizeHint() renvoie la taille recommandée (idéale) pour chaque widget
        # Cela dépend des propriétés du widget et du style, et permet d'optimiser l'interface
        print(line_edit.sizeHint(), button.sizeHint())

        # La méthode sizePolicy() détermine comment le widget doit se redimensionner
        # Elle renvoie une politique de redimensionnement influençant le widget dans le layout (fixe, expansible, minimum, etc.)
        print(line_edit.sizePolicy())
        print(button.sizePolicy())

        # Ajout des widgets (champ de texte et bouton) dans le layout horizontal
        self.layout.addWidget(line_edit)
        self.layout.addWidget(button)

        # Définit le focus sur le widget (le premier à recevoir les événements de saisie)
        self.setFocus()


app = QApplication()
win = MainWindow()
win.show()
app.exec()
