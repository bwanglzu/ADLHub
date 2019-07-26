"""Human Activity Recognition using smartphones dataset.

Davide Anguita, Alessandro Ghio, Luca Oneto, Xavier Parra and Jorge L. Reyes-Ortiz.
A Public Domain Dataset for Human Activity Recognition Using Smartphones.
21th European Symposium on Artificial Neural Networks,
Computational Intelligence and Machine Learning, ESANN 2013.
Bruges, Belgium 24-26 April 2013.
"""

from io import BytesIO
from pathlib import Path
from zipfile import ZipFile
from typing import Union, Tuple

import requests
import numpy as np
from loguru import logger


def load_data() -> Union[Tuple[np.ndarray, np.ndarray], Tuple[np.ndarray, np.ndarray]]:
    """Download, extract & Load uci har smartphone dataset.

    The value will be split into train and test by :meth:`train_test_split`. Use
        (X_train, y_train), (X_test, y_test) to unpack returned value.

    :return: A tuple contains `X_train` and `y_train`.
    :return: A tuple contains `X_test` and `y_test`.
    """
    uri = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00240/UCI%20HAR%20Dataset.zip'
    ucihar_dir = Path.cwd().joinpath('UCI HAR Dataset')
    if not ucihar_dir.exists():
        logger.info('Downloading UCI HAR dataset...')
        response = requests.get(uri)
        logger.info('Download finished.')
        logger.info('Unzipping UCI HAR dataset...')
        zipfile = ZipFile(BytesIO(response.content))
        zipfile.extractall()
        logger.info('Unzip finished.')
    logger.info('Loading UCI HAR dataset...')
    X_train = np.loadtxt(str(ucihar_dir) + '/train/X_train.txt')
    y_train = np.loadtxt(str(ucihar_dir) + '/train/y_train.txt')
    X_test = np.loadtxt(str(ucihar_dir) + '/test/X_test.txt')
    y_test = np.loadtxt(str(ucihar_dir) + '/test/y_test.txt')
    logger.info('Load finished.')
    return (X_train, y_train), (X_test, y_test)
