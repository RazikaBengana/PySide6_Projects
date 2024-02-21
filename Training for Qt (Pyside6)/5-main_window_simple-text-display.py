from PySide6.QtWidgets import QApplication, QLabel


class MainWindow(QLabel):
    def __init__(self):
        super().__init__()

        # Définit le texte du "QLabel" à "Click me"
        # Cela sert à indiquer à l'utilisateur qu'il peut interagir avec le label, même si dans ce cas, le "QLabel" ne gère pas les clics
        self.setText("Click me")
        print(self.text())


app = QApplication()


main_window = MainWindow()
main_window.show()
app.exec()
