from PySide6.QtWidgets import QMainWindow

from src.mainWindow import Ui_MainWindow
from src.createListView import CreateList


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.assign_widgets()
        self.show()

    def assign_widgets(self):
        self.create_list_button.clicked.connect(lambda: self.create_list())
        self.view_list_button.clicked.connect(lambda: self.view_list())

    def create_list(self):
        self.create_list_page = CreateList()
        self.add_widget_and_change_tab(self.main_window_stack, self.create_list_page, 1)
        self.create_list_page.back_button.clicked.connect(lambda: self.delete_objects_and_go_back(self.create_list_page))
        self.create_list_page.submit_button.clicked.connect(\
            lambda: self.create_list_page.save_and_go_back(self.delete_objects_and_go_back))

    def view_list(self):
        pass

    def add_widget_and_change_tab(self, stack, widget, tab):
        stack.addWidget(widget)
        stack.setCurrentIndex(tab)

    def delete_objects_and_go_back(self, *args):
        self.main_window_stack.setCurrentIndex(0)
        self.delete_objects(*args)

    def delete_objects(self, *args):
        for arg in args:
            arg.deleteLater()