# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createList.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTreeView, QVBoxLayout,
    QWidget)

class Ui_CreateListPage(object):
    def setupUi(self, CreateListPage):
        if not CreateListPage.objectName():
            CreateListPage.setObjectName(u"CreateListPage")
        CreateListPage.resize(800, 600)
        self.verticalLayout = QVBoxLayout(CreateListPage)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.back_button = QPushButton(CreateListPage)
        self.back_button.setObjectName(u"back_button")

        self.horizontalLayout.addWidget(self.back_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(CreateListPage)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(CreateListPage)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(CreateListPage)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.name_edit = QLineEdit(CreateListPage)
        self.name_edit.setObjectName(u"name_edit")

        self.horizontalLayout_2.addWidget(self.name_edit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.column_edit = QLineEdit(CreateListPage)
        self.column_edit.setObjectName(u"column_edit")

        self.horizontalLayout_3.addWidget(self.column_edit)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.type_combo_box = QComboBox(CreateListPage)
        self.type_combo_box.setObjectName(u"type_combo_box")

        self.horizontalLayout_4.addWidget(self.type_combo_box)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.remove_button = QPushButton(CreateListPage)
        self.remove_button.setObjectName(u"remove_button")

        self.horizontalLayout_4.addWidget(self.remove_button)

        self.add_button = QPushButton(CreateListPage)
        self.add_button.setObjectName(u"add_button")

        self.horizontalLayout_4.addWidget(self.add_button)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_4)


        self.verticalLayout.addLayout(self.formLayout)

        self.columns_tree_view = QTreeView(CreateListPage)
        self.columns_tree_view.setObjectName(u"columns_tree_view")

        self.verticalLayout.addWidget(self.columns_tree_view)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.submit_button = QPushButton(CreateListPage)
        self.submit_button.setObjectName(u"submit_button")

        self.horizontalLayout_5.addWidget(self.submit_button)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(CreateListPage)

        QMetaObject.connectSlotsByName(CreateListPage)
    # setupUi

    def retranslateUi(self, CreateListPage):
        CreateListPage.setWindowTitle(QCoreApplication.translate("CreateListPage", u"Form", None))
        self.back_button.setText(QCoreApplication.translate("CreateListPage", u"Back", None))
        self.label.setText(QCoreApplication.translate("CreateListPage", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("CreateListPage", u"Column", None))
        self.label_3.setText(QCoreApplication.translate("CreateListPage", u"Type", None))
        self.remove_button.setText(QCoreApplication.translate("CreateListPage", u"Remove", None))
        self.add_button.setText(QCoreApplication.translate("CreateListPage", u"Add", None))
        self.submit_button.setText(QCoreApplication.translate("CreateListPage", u"Submit", None))
    # retranslateUi

