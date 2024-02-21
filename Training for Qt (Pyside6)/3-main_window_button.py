from PySide6.QtWidgets import QApplication, QPushButton


class MainWindow(QPushButton):
    def __init__(self):
        super().__init__()

        self.setText("Click me")  # Création d'un bouton cliquable affichant le texte "Click me"


app = QApplication()


main_window = MainWindow()
main_window.show()
app.exec()
