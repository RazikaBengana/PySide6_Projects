from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mon application")

        # Crée un layout horizontal principal
        main_layout = QHBoxLayout(self)

        # Crée 2 layouts verticaux pour organiser les boutons
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()

        # Ajoute les layouts verticaux au layout horizontal principal pour une organisation en colonnes
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        # Crée et ajoute 10 boutons au layout vertical de gauche
        for i in range(1, 11):
            btn = QPushButton(str(i))
            left_layout.addWidget(btn)

        # Crée et ajoute 10 boutons au layout vertical de droite
        for i in range(11, 21):
            btn = QPushButton(str(i))
            right_layout.addWidget(btn)


app = QApplication()


main_window = MainWindow()
main_window.show()
app.exec()
