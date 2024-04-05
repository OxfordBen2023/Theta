from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
import sys

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

    def closeEvent(self, event):
        # Show a message box to confirm closing the window
        reply = QMessageBox.question(self, 'Message', 
            "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

        # Return None if the window is closed
        return None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
