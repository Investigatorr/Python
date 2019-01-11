from sklearn.datasets import load_boston
import pandas as pd
import seaborn as sns
import matplotlib as plt
from sklearn.linear_model import LinearRegression

boston = load_boston()
print(boston.data.shape)