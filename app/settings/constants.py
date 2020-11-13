import os

DATA_FOLDER = 'data'
SAVED_ESTIMATOR = os.path.join('models', 'KNN.pickle')
TRAIN_CSV = os.path.join(DATA_FOLDER, 'train.csv')
VAL_CSV = os.path.join(DATA_FOLDER, 'val.csv')