from PySide6.QtWidgets import QApplication, QListWidget


class MainWindow(QListWidget):
    def __init__(self):
        super().__init__()

        # Ajout d'éléments à la liste nouvellement créée
        self.addItem("Item 1")
        self.addItem("Item 2")
        self.addItem("Item 3")


app = QApplication()


main_window = MainWindow()
main_window.show()
app.exec()
