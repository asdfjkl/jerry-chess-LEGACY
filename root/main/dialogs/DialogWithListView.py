from PyQt4.QtGui import *
from PyQt4.QtCore import *

class DialogWithListView(QDialog):
 
    def __init__(self, moveList, parent=None):
        super(DialogWithListView, self).__init__(parent) 

        self.resize(20, 40)
        
        for mv in moveList :
            print(mv)

        self.selected_idx = 0
 
        self.listWidget = QListWidget()
        
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok| QDialogButtonBox.Cancel)
        
        self.okButton = QPushButton("&OK")
        cancelButton = QPushButton("Cancel")
        
        buttonLayout = QHBoxLayout() 
        buttonLayout.addStretch() 
        buttonLayout.addWidget(self.okButton) 
        buttonLayout.addWidget(cancelButton)
        layout = QGridLayout()
        layout.addWidget(self.listWidget,0,1)
        #layout.addLayout(buttonLayout, 2, 0, 1, 3)
        layout.addWidget(buttonBox, 3, 0, 1, 3)
        self.setLayout(layout)
        self.listWidget.addItems(moveList)
        self.listWidget.item(0).setSelected(True)

        self.connect(buttonBox, SIGNAL("accepted()"),
                 self, SLOT("accept()"))
        self.connect(buttonBox, SIGNAL("rejected()"),
                 self, SLOT("reject()"))
        
        #self.connect(self.okButton, SIGNAL("clicked()"),
        #         self, SLOT("accept()"))

        self.connect(self,SIGNAL("rightclick()"), SLOT("accept()") )
        self.connect(self,SIGNAL("leftclick()"), SLOT("reject()") )
        #self.connect(self.listWidget, QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem *)"), SLOT("accept()"))   
            
        #self.connect(self.listWidget, SIGNAL("itemDoubleClicked()"), SLOT("accept()"))
        self.listWidget.itemDoubleClicked.connect(self.accept)
        self.listWidget.currentItemChanged.connect(self.on_item_changed)
    
    def on_item_changed(self):
        self.selected_idx = self.listWidget.currentRow()    
        
    def keyPressEvent(self, event):
        key = event.key()
        print("CURRENT ROW:" + str(self.listWidget.currentRow()))
        if key == Qt.Key_Left or key == Qt.Key_Escape:
            print("left key or esc pressed")
            self.emit(SIGNAL("leftclick()"))
        elif key == Qt.Key_Right or key == Qt.Key_Return:
            print("right key or return pressed")
            self.emit(SIGNAL("rightclick()"))
