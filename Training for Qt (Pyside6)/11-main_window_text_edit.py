from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLineEdit, QLabel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mon application")

        # Crée un layout vertical pour organiser les widgets
        main_layout = QVBoxLayout(self)

        # Création des widgets
        self.le_text = QLineEdit()  # Champ de saisie pour entrer du texte
        self.lbl_text = QLabel("...")  # Étiquette pour afficher le texte saisi
        self.btn_clear = QPushButton("Clear")  # Bouton pour effacer le texte saisi

        # Ajout des widgets au layout vertical principal
        main_layout.addWidget(self.le_text)  # Ajoute le champ de saisie au layout
        main_layout.addWidget(self.lbl_text)  # Ajoute l'étiquette au layout
        main_layout.addWidget(self.btn_clear)  # Ajoute le bouton au layout

        # Connexion des événements aux fonctions (slots) correspondantes
        self.le_text.textChanged.connect(self.lbl_text.setText)  # Met à jour l'étiquette avec le texte saisi dès sa modification
        self.btn_clear.clicked.connect(self.le_text.clear)  # Efface le texte saisi dans le champ de saisie lorsque le bouton est cliqué


app = QApplication()


main_window = MainWindow()
main_window.show()
app.exec()
