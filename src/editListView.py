from PySide6.QtWidgets import QWidget

from src.editList import Ui_EditList
from src.databaseHandler import Database


class EditList(QWidget, Ui_EditList):
    def __init__(self):
        super(EditList, self).__init__()
        self.setupUi(self)
        self.init_widgets()

    def init_widgets(self):
        self.init_lists_combo_box()
        self.lists_combo_box.currentTextChanged.connect(self.init_list_tree_view)

    def init_lists_combo_box(self):
        db = Database()
        select_tables_query = f"SELECT name FROM sqlite_schema WHERE type='table' and name!='sqlite_sequence'"
        tables = db.query_db(select_tables_query)
        for table in tables:
            self.lists_combo_box.addItem(table[0])

    def init_list_tree_view(self):
        selected_table = self.lists_combo_box.currentText()
        db = Database()
        select_all_query = f"SELECT * FROM {selected_table}"
        table_rows = db.query_db(select_all_query)
        print(table_rows)