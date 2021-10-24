# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editList.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QSpacerItem, QToolButton,
    QTreeView, QVBoxLayout, QWidget)

class Ui_EditList(object):
    def setupUi(self, EditList):
        if not EditList.objectName():
            EditList.setObjectName(u"EditList")
        EditList.resize(800, 600)
        self.verticalLayout = QVBoxLayout(EditList)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.back_button = QPushButton(EditList)
        self.back_button.setObjectName(u"back_button")

        self.horizontalLayout.addWidget(self.back_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lists_combo_box = QComboBox(EditList)
        self.lists_combo_box.setObjectName(u"lists_combo_box")

        self.horizontalLayout.addWidget(self.lists_combo_box)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.delete_row_button = QToolButton(EditList)
        self.delete_row_button.setObjectName(u"delete_row_button")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_row_button.sizePolicy().hasHeightForWidth())
        self.delete_row_button.setSizePolicy(sizePolicy)
        self.delete_row_button.setMinimumSize(QSize(24, 0))

        self.horizontalLayout.addWidget(self.delete_row_button)

        self.add_row_button = QToolButton(EditList)
        self.add_row_button.setObjectName(u"add_row_button")

        self.horizontalLayout.addWidget(self.add_row_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.edit_list_tree_view = QTreeView(EditList)
        self.edit_list_tree_view.setObjectName(u"edit_list_tree_view")

        self.verticalLayout.addWidget(self.edit_list_tree_view)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(30)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.reset_button = QPushButton(EditList)
        self.reset_button.setObjectName(u"reset_button")

        self.horizontalLayout_2.addWidget(self.reset_button)

        self.save_button = QPushButton(EditList)
        self.save_button.setObjectName(u"save_button")

        self.horizontalLayout_2.addWidget(self.save_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(EditList)

        QMetaObject.connectSlotsByName(EditList)
    # setupUi

    def retranslateUi(self, EditList):
        EditList.setWindowTitle(QCoreApplication.translate("EditList", u"Form", None))
        self.back_button.setText(QCoreApplication.translate("EditList", u"Back", None))
        self.delete_row_button.setText(QCoreApplication.translate("EditList", u"-", None))
        self.add_row_button.setText(QCoreApplication.translate("EditList", u"+", None))
        self.reset_button.setText(QCoreApplication.translate("EditList", u"Reset", None))
        self.save_button.setText(QCoreApplication.translate("EditList", u"Save", None))
    # retranslateUi

