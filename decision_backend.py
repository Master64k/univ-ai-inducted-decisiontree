from sklearn import tree
from database import DataBase

__author__ = "Nícolas Costa - Master64k"
__credits__ = ["Nícolas Costa - Master64k"]
__version__ = "0.1"
__license__ = "WTFPL"
__maintainer__ = "Nícolas Costa"
__email__ = "notyour@business.com"

class Decision_Backend():

    idtc = None
    db_access = None
    trained = False


    def __init__(self):

        self.idtc = tree.DecisionTreeClassifier()

        self.db_access = DataBase()

    def train_tree(self):

        data = self.db_access.get_db_data()

        self.idtc.fit(data[0], data[1])

        self.trained = True

    def make_prediction(self, financ_data: tuple) -> int:

        if not self.trained:

            self.train_tree()

        return self.idtc.predict([financ_data])


