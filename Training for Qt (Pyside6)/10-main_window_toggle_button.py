from PySide6.QtWidgets import QApplication, QPushButton, QHBoxLayout, QWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mon application")

        # Crée un layout horizontal pour placer les widgets
        main_layout = QHBoxLayout(self)

        # Crée un bouton cochable (checkable) avec le texte initial "Décoché"
        self.button = QPushButton("Décoché")
        self.button.setCheckable(True)  # Rend le bouton cochable, permettant deux états : "coché" et "décoché"
        main_layout.addWidget(self.button)  # Ajoute le bouton au layout horizontal

        # Connecte le signal "clicked" du bouton à la méthode "button_clicked"
        self.button.clicked.connect(self.button_clicked)

    # Méthode appelée lors du clic sur le bouton, "check" indique l'état "coché"/"décoché"
    def button_clicked(self, check):
        if check:
            self.button.setText("Coché")
        else:
            self.button.setText("Décoché")


app = QApplication()


main_window = MainWindow()
main_window.show()
app.exec()
