from PySide6.QtWidgets import QApplication

from src.mainWindowView import MainWindow

import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())
    