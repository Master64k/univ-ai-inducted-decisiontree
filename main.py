
from PySide import QtCore, QtGui
import sys

from ui.ui_rc import  Ui_Dialog

from decision_backend import Decision_Backend

__author__ = "Nícolas Costa - Master64k"
__credits__ = ["Nícolas Costa - Master64k"]
__version__ = "0.1"
__license__ = "WTFPL"
__maintainer__ = "Nícolas Costa"
__email__ = "notyour@business.com"


class FA_UI(QtGui.QMainWindow):

    main_ui = None

    decision = None

    def __init__(self):

        QtGui.QMainWindow.__init__(self, None)

        self.main_ui = Ui_Dialog()

        self.main_ui.setupUi(self)

        self.init_controls()

        self.decision = Decision_Backend()

        self.show()

        self.start()

    def init_controls(self):

        self.main_ui.credit_history.addItem('Ruim')
        self.main_ui.credit_history.addItem('Desconhecido')
        self.main_ui.credit_history.addItem('Bom')

        self.main_ui.debt.addItem('Baixo')
        self.main_ui.debt.addItem('Alto')

        self.main_ui.guarantees.addItem('Nenhuma')
        self.main_ui.guarantees.addItem('Adequadas')

        self.main_ui.earnings.addItem('< 1,5k')
        self.main_ui.earnings.addItem('> 1,5k e < 3,5k')
        self.main_ui.earnings.addItem('> 3,5k')

        self.main_ui.simulate.clicked.connect(self.show_result)

        self.main_ui.quit.clicked.connect(lambda: QtGui.QApplication.exit(0))


    def show_result(self):


        credit_h = self.main_ui.credit_history.currentIndex()

        debt = self.main_ui.debt.currentIndex()

        guarantee = self.main_ui.guarantees.currentIndex()

        earnings = self.main_ui.earnings.currentIndex()

        result = self.decision.make_prediction((credit_h, debt, guarantee, earnings))[0]

        level = '--'

        if result == 0:
            level = 'Baixo'
            self.main_ui.risk_level.setStyleSheet('color:green; font-weight:bold')
        elif result == 1:
            level = 'Moderado'
            self.main_ui.risk_level.setStyleSheet('color:orange; font-weight:bold')
        else:
            level = 'Alto'
            self.main_ui.risk_level.setStyleSheet('color:red; font-weight:bold')

        self.main_ui.risk_level.setText(level)

    def start(self):
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            QtGui.QApplication.instance().exec_()


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    window = FA_UI()




