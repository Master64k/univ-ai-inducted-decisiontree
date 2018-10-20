import sqlite3

__author__ = "Nícolas Costa - Master64k"
__credits__ = ["Nícolas Costa - Master64k"]
__version__ = "0.1"
__license__ = "WTFPL"
__maintainer__ = "Nícolas Costa"
__email__ = "notyour@business.com"

history = {'bad':0, 'unknown': 1, 'good': 2}                    # 0 = bad, 1 = unknown, 2 = good
debt = {'low':0, 'high': 1}                                     # 0 = low, 1 = high
guarantee = {'none':0, 'adequate':1}                            # 0 = none, 1 = adequate
earnings = {'0 to 1500':0, '1500 to 3500':1, 'above 3500':2}    # 0 = 0 - 1,5k, 1 = 1,5k to 3,5k 2 = > 3,5k
risk = {'low':0, 'moderate':1, 'high':2}                        # 0 = low, 1 = moderated, 2 = high

training_data = {'attributes':
    [
        [history['bad'],  debt['high'], guarantee['none'], earnings['0 to 1500']],
        [history['unknown'], debt['high'], guarantee['none'], earnings['1500 to 3500']],
        [history['unknown'], debt['low'],  guarantee['none'],  earnings['1500 to 3500']],
        [history['unknown'], debt['low'],  guarantee['none'],  earnings['above 3500']],
        [history['unknown'], debt['low'],  guarantee['none'],  earnings['above 3500']],
        [history['unknown'], debt['low'],  guarantee['adequate'],  earnings['above 3500']],
        [history['bad'], debt['low'],  guarantee['none'],  earnings['0 to 1500']],
        [history['bad'], debt['low'],  guarantee['none'],  earnings['above 3500']],
        [history['good'], debt['low'],  guarantee['adequate'],  earnings['above 3500']],
        [history['good'], debt['high'],  guarantee['none'],  earnings['above 3500']],
        [history['good'], debt['high'],  guarantee['adequate'],  earnings['0 to 1500']],
        [history['good'], debt['high'],  guarantee['none'],  earnings['1500 to 3500']],
        [history['good'], debt['high'],  guarantee['none'],  earnings['above 3500']],
        [history['bad'], debt['high'],  guarantee['none'],  earnings['1500 to 3500']]
    ],
    'labels':
    [
         risk['high'],
         risk['high'],
         risk['moderate'],
         risk['high'],
         risk['low'],
         risk['low'],
         risk['high'],
         risk['moderate'],
         risk['low'],
         risk['low'],
         risk['high'],
         risk['moderate'],
         risk['low'],
         risk['high']
    ]}

class DataBase():

    connection = None

    def __init__(self):

        self.connection = sqlite3.connect('pred.db')

        cursor = self.connection.execute('SELECT * FROM sqlite_master WHERE type="table";')

        result = cursor.fetchall()

        cursor.close()

        if len(result) == 0:

            self.init_db_data()

    def init_db_data(self):

        cursor = self.connection\
            .execute('CREATE TABLE training( history INT NOT NULL,' +
                     ' debt INT NOT NULL, guarantee INT NOT NULL, earnings INT NOT NULL, label INT NOT NULL );')

        for a in zip(training_data['attributes'], training_data['labels']):

            serie = a[0]

            serie.append(a[1])

            data = tuple(serie)

            cursor = self.connection.execute('INSERT INTO training VALUES (?, ?, ?, ?, ?)', data)

            self.connection.commit()

        cursor.close()

    def get_db_data(self) -> list:

        attr_list = []
        lbl_list = []

        cursor = self.connection.execute('SELECT * FROM training')

        for line in cursor:

            attr = tuple(line[:(len(line) - 1)])
            label = tuple(line[-1:])

            attr_list.append(attr)
            lbl_list.append(label)

        return [attr_list, lbl_list]

    def __del__(self):

        self.connection.close()