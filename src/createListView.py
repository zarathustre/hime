from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem 
from PySide6.QtCore import Qt

from src.createList import Ui_CreateListPage
from src.databaseHandler import Database

import threading


class CreateList(QWidget, Ui_CreateListPage):
    def __init__(self):
        super(CreateList, self).__init__()
        self.setupUi(self)
        self.init_widgets()
        self.assign_widgets()

    def init_widgets(self):
        self.init_type_combo_box()
        self.init_tree_view()
        self.remove_button.setEnabled(False)
        self.submit_button.setEnabled(False)

    def assign_widgets(self):
        self.add_button.clicked.connect(lambda: self.add_entry())
        self.remove_button.clicked.connect(lambda: self.remove_selected_entry())
        self.columns_tree_view.selectionModel().selectionChanged.connect(self.on_selection_change)
        self.name_edit.textChanged.connect(self.on_name_text_changed)

    def init_type_combo_box(self):
        types = ['INTEGER', 'TEXT', 'DATE']      
        for type in types: 
            self.type_combo_box.addItem(type)

    def init_tree_view(self):
        self.items_model = QStandardItemModel()
        self.items_model.setHorizontalHeaderLabels(['Column', 'Type'])
        self.columns_tree_view.setModel(self.items_model)
        self.columns_tree_view.header().setDefaultAlignment(Qt.AlignHCenter)
        self.columns_tree_view.setColumnWidth(0, 500)

    def on_name_text_changed(self):
        if self.name_edit.text() == "":
            self.submit_button.setEnabled(False)
        if self.name_edit.text() != "" and self.items_model.rowCount() != 0:
            self.submit_button.setEnabled(True)

    def on_selection_change(self):
        selected_item = self.columns_tree_view.selectionModel().selectedRows()
        if selected_item:
            self.remove_button.setEnabled(True)
    
    def add_entry(self):
        name_col = QStandardItem(self.column_edit.text())
        type_col = QStandardItem(self.type_combo_box.currentText())
        name_col.setEditable(False)
        type_col.setEditable(False)
        name_col.setTextAlignment(Qt.AlignHCenter)
        type_col.setTextAlignment(Qt.AlignHCenter)
        if self.column_edit.text() != '': 
            self.items_model.appendRow([name_col, type_col])
        self.column_edit.setText('')
        if self.items_model.rowCount() > 0 and self.name_edit.text() != '':
            self.submit_button.setEnabled(True)

    def remove_selected_entry(self):
        selected_item = self.columns_tree_view.selectionModel().selectedRows()
        if selected_item: 
            self.items_model.removeRow(selected_item[0].row())
        if self.items_model.rowCount() == 0:
            self.submit_button.setEnabled(False)
            self.remove_button.setEnabled(False)

    def get_data_from_tree(self):
        tree_data = {}
        for row in range(self.items_model.rowCount()):
            name_col = self.items_model.item(row, 0).text()
            type_col = self.items_model.item(row, 1).text()
            tree_data[name_col] = type_col

        return tree_data

    # TODO: column names uniqueness
    def check_db_constraints(self):
        db = Database()
        table_name = self.name_edit.text()
        table_exists_query = f"select * from sqlite_schema where type='table' and name='{table_name}'"
        table_exists = db.query_db(table_exists_query)
        if not table_exists:
            return True

        return False

    def save_to_db(self):
        db = Database()
        table_name = self.name_edit.text()
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT)"
        db.query_db(create_table_query)
        for col,type in self.get_data_from_tree().items():
            add_columns_query = f"ALTER TABLE {table_name} ADD {col} {type}"
            db.query_db(add_columns_query)

    def save_and_go_back(self, delete_objects_and_go_back):
        if self.check_db_constraints():
            save_to_db_thread = threading.Thread(target=self.save_to_db)
            save_to_db_thread.start()
            delete_objects_and_go_back(self)
        else:
            QMessageBox.warning(self, "Warning", "List already exists. Pick a different name")
