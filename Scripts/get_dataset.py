#!/usr/bin/env python
# coding: utf-8

import os
import opendatasets as od

# Download the dataset


os.chdir('../Datasets/')
dataset = 'https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset'
od.download(dataset)
dataset = 'https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata'
od.download(dataset)
os.chdir('../Scripts/')
