import sys
from PyQt4 import QtGui, QtCore

class XpdanSerch(QtGui.QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # option_list
        self.field_list = ['bt_piLast', 'sa_name', 'ex_name', 'sp_type']
        self.field_option_list = []

        #generate btn
        generate_btn = QtGui.QPushButton("generate query", self)
        generate_btn.clicked.connect(self.generate)
        generate_btn.resize(generate_btn.sizeHint())

        # set up fileds
        self.f1 = QtGui.QLabel('PI last name')
        self.f1_Edit = QtGui.QLineEdit()
        self.f1_cbox = QtGui.QComboBox(self)
        self.f1_cbox.addItem("and")
        self.f1_cbox.addItem("or")
        self.field_option_list.append((self.f1_Edit, self.f1_cbox))

        #self.f1_cbox.activated[str].connect(self.f1_and_or_option)

        self.f2 = QtGui.QLabel('sample name')
        self.f2_Edit = QtGui.QLineEdit()
        self.f2_cbox = QtGui.QComboBox(self)
        self.f2_cbox.addItem("and")
        self.f2_cbox.addItem("or")
        self.field_option_list.append((self.f2_Edit, self.f2_cbox))

        self.f3 = QtGui.QLabel('experiment name')
        self.f3_Edit = QtGui.QLineEdit()
        self.f3_cbox = QtGui.QComboBox(self)
        self.f3_cbox.addItem("and")
        self.f3_cbox.addItem("or")
        self.field_option_list.append((self.f3_Edit, self.f3_cbox))

        self.f4 = QtGui.QLabel('scan type')
        self.f4_Edit = QtGui.QLineEdit()
        self.f4_cbox = QtGui.QComboBox(self)
        self.f4_cbox.addItem("and")
        self.f4_cbox.addItem("or")
        self.field_option_list.append((self.f4_Edit, self.f4_cbox))

        grid = QtGui.QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(self.f1, 1, 0)
        grid.addWidget(self.f1_Edit, 1, 1)
        grid.addWidget(self.f1_cbox, 1, 2)

        grid.addWidget(self.f2, 2, 0)
        grid.addWidget(self.f2_Edit, 2, 1)
        grid.addWidget(self.f2_cbox, 2, 2)

        grid.addWidget(self.f3, 3, 0)
        grid.addWidget(self.f3_Edit, 3, 1)
        grid.addWidget(self.f3_cbox, 3, 2)

        grid.addWidget(self.f4, 4, 0)
        grid.addWidget(self.f4_Edit, 4, 1)
        grid.addWidget(self.f4_cbox, 4, 2)

        # layout
        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(generate_btn)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(grid)
        vbox.addLayout(hbox)


        self.setLayout(vbox)

        self.setWindowTitle("xpdAn search")
        self.setGeometry(2048, 0, 400, 300)

        self.show()


    def generate(self):
        """ generate search query """
        print('Generate search query')
        search_dict = {}
        for i in range(len(self.field_list)):
            key = self.field_list[i]
            val = self.field_option_list[i][0].text()
            option = self.field_option_list[i][1].currentText()
            if val is not '':
                search_dict.update({key:val})
        print('search dict = {}'.format(search_dict))

def main():
    app = QtGui.QApplication(sys.argv)
    gui = XpdanSerch()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
