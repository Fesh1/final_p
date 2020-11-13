import pandas as pd
import re

from sklearn.preprocessing import LabelEncoder


class DataLoader(object):
    def fit(self, dataset):
        self.dataset = dataset.copy()

    # apply regex
    def get_title(self, name):
        pattern = ' ([A-Za-z]+)\.'
        title_search = re.search(pattern, name)
        # If the title exists, extract and return it.
        if title_search:
            return title_search.group(1)
        return ""

    def load_data(self):

        # fill Nan with mode
        self.dataset['Vmag'] = self.dataset['Vmag'].fillna(self.dataset['Vmag'].mean())

        self.dataset['Plx'] = self.dataset['Plx'].fillna(self.dataset['Plx'].mean())

        self.dataset['e_Plx'] = self.dataset['e_Plx'].fillna(self.dataset['e_Plx'].mean())

        self.dataset['B-V'] = self.dataset['B-V'].fillna(self.dataset['B-V'].mean())

        self.dataset['Amag'] = self.dataset['Amag'].fillna(self.dataset['Amag'].mean())
        # drop column


        return self.dataset