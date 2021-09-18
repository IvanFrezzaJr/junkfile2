from PySide6.QtCore import *
from PySide6.QtWidgets import *


class FindDialog(QDialog):
    def __init__(self, parent=None):
        super(FindDialog, self).__init__(parent)

        self.setWindowTitle(self.tr("pi Plot") + " - " + self.tr("Find"))
        self.setSizeGripEnabled(True)
        self.setAttribute(Qt.WA_DeleteOnClose)

        topLayout = QGridLayout()
        bottomLayout = QGridLayout()

        topLayout.addWidget(QLabel(self.tr("Start From")), 0, 0)
        self.labelStart = QLabel()
        self.labelStart.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.labelStart.setSizePolicy(
            QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        )
        topLayout.addWidget(self.labelStart, 0, 1, 1, 4)

        topLayout.addWidget(QLabel(self.tr("Find")), 1, 0)
        self.boxFind = QComboBox(self)
        self.boxFind.setEditable(True)
        self.boxFind.setDuplicatesEnabled(False)
        self.boxFind.setInsertPolicy(QComboBox.InsertAtTop)
        # boxFind.setAutoCompletion(True)
        self.boxFind.setMaxCount(10)
        self.boxFind.setMaxVisibleItems(10)
        self.boxFind.setSizePolicy(
            QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        )
        topLayout.addWidget(self.boxFind, 1, 1, 1, 4)

        self.groupBox = QGroupBox(self.tr("Search in"))
        self.groupBoxLayout = QVBoxLayout(self.groupBox)

        self.boxWindowNames = QCheckBox(self.tr("&Window Names"))
        self.boxWindowNames.setChecked(True)
        self.groupBoxLayout.addWidget(self.boxWindowNames)

        self.boxWindowLabels = QCheckBox(self.tr("Window &Labels"))
        self.boxWindowLabels.setChecked(False)
        self.groupBoxLayout.addWidget(self.boxWindowLabels)

        self.boxFolderNames = QCheckBox(self.tr("Folder &Names"))
        self.boxFolderNames.setChecked(False)
        self.groupBoxLayout.addWidget(self.boxFolderNames)

        bottomLayout.addWidget(self.groupBox, 0, 0, 3, 1)

        self.boxCaseSensitive = QCheckBox(self.tr("Case &Sensitive"))
        self.boxCaseSensitive.setChecked(False)
        bottomLayout.addWidget(self.boxCaseSensitive, 0, 1)

        self.boxPartialMatch = QCheckBox(self.tr("&Partial Match Allowed"))
        self.boxPartialMatch.setChecked(True)
        bottomLayout.addWidget(self.boxPartialMatch, 1, 1)

        self.boxSubfolders = QCheckBox(self.tr("&Include Subfolders"))
        self.boxSubfolders.setChecked(True)
        bottomLayout.addWidget(self.boxSubfolders, 2, 1)

        self.buttonFind = QPushButton(self.tr("&Find"))
        self.buttonFind.setDefault(True)
        bottomLayout.addWidget(self.buttonFind, 0, 2)

        self.buttonReset = QPushButton(self.tr("&Update Start Path"), self)
        bottomLayout.addWidget(self.buttonReset, 1, 2)
        self.buttonCancel = QPushButton(self.tr("&Close"), self)
        bottomLayout.addWidget(self.buttonCancel, 2, 2)
        bottomLayout.setColumnStretch(4, 1)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(bottomLayout)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)
