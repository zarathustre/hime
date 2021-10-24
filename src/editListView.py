from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QStandardItemModel, QStandardItem

from src.editList import Ui_EditList
from src.databaseHandler import Database


class EditList(QWidget, Ui_EditList):
    def __init__(self):
        super(EditList, self).__init__()
        self.setupUi(self)
        self.init_widgets()
        self.assign_widgets()

    def init_widgets(self):
        self.init_lists_combo_box()
        self.init_list_tree_view()

    def assign_widgets(self):
        self.lists_combo_box.currentTextChanged.connect(self.init_list_tree_view)
        self.reset_button.clicked.connect(self.init_list_tree_view)

    def init_lists_combo_box(self):
        db = Database()
        select_tables_query = f"SELECT name FROM sqlite_schema WHERE type='table' and name!='sqlite_sequence'"
        tables = db.query_db(select_tables_query)[0]
        if tables:
            for table in tables:
                self.lists_combo_box.addItem(table[0])

    def init_list_tree_view(self):
        selected_table = self.lists_combo_box.currentText()
        if selected_table:
            db = Database()
            select_all_query = f"SELECT * FROM {selected_table};"

            table_results = db.query_db(select_all_query)
            table_rows = table_results[0]
            table_columns = table_results[1]

            self.items_model = QStandardItemModel()
            self.items_model.setHorizontalHeaderLabels([item[0] for item in table_columns[1:]])
            self.edit_list_tree_view.setModel(self.items_model)

            for row in table_rows:
                self.items_model.appendRow([QStandardItem(str(item)) for item in row[1:]])
