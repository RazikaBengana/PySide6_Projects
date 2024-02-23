from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLineEdit, QLabel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mon application")

        # Création et configuration du layout vertical principal
        main_layout = QVBoxLayout(self)

        # Initialisation des widgets
        self.le_text = QLineEdit()  # Champ de saisie pour le texte
        self.lbl_text = QLabel("...")  # Étiquette pour afficher les modifications de texte
        self.btn_clear = QPushButton("Clear")  # Bouton pour effacer le texte saisi

        # Ajout des widgets au layout vertical principal
        main_layout.addWidget(self.le_text)  # Ajoute le champ de saisie au layout
        main_layout.addWidget(self.lbl_text)  # Ajoute l'étiquette au layout
        main_layout.addWidget(self.btn_clear)  # Ajoute le bouton au layout

        # Connexion des signaux aux slots pour interactivité
        self.le_text.textChanged.connect(self.lbl_text.setText)  # Actualise l'étiquette avec le texte saisi en temps réel
        self.btn_clear.clicked.connect(self.clear_text)  # Efface le texte saisi lorsque le bouton "Clear" est cliqué

    def clear_text(self):
        # Méthode pour effacer le texte saisi et réinitialiser l'étiquette
        self.le_text.clear()  # Efface le contenu du champ de saisie
        self.lbl_text.setText("Saisie de texte")  # Réinitialise l'étiquette pour indiquer que le texte peut à nouveau être saisi


app = QApplication()


main_window = MainWindow()
main_window.show()
app.exec()
