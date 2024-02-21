from PySide6.QtWidgets import QApplication, QLineEdit


class MainWindow(QLineEdit):
    def __init__(self):
        super().__init__()

        # Initialise le "QLineEdit" avec un texte par défaut invitant l'utilisateur à entrer du texte
        # Cela sert de guide visuel pour l'utilisateur, indiquant où le texte peut être saisi
        self.setText("Enter text here")


app = QApplication()


main_window = MainWindow()
main_window.show()
app.exec()
