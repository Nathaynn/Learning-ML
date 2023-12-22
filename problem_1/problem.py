'''
Create a estimate of what a person may pay for Health Insurance with ACME using past data of other people based off
their age, sex, BMI, children, smoking habits and region of residence.
'''

'''
Pandas allows for data visualization
urlretrieve is self-explanatory
'''
import pandas as pd
from urllib.request import urlretrieve

# Saves the csv file locally
medical_charges_url = 'https://raw.githubusercontent.com/JovianML/opendatasets/master/data/medical-charges.csv'
urlretrieve(medical_charges_url, 'medical.csv')

'''
Pandas allows us to see the data and make some inferences
Its good practice to look for anything out of line
For example, if any charges were negative then that is extremely out of line
'''
medical_df = pd.read_csv('medical.csv')
print(medical_df)
print(medical_df.info())
print(medical_df.describe())

'''
More imports
These are all used for the visualization charts of the data
'''
import jovian
import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# Settings to see the data easily
sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (10, 6)
matplotlib.rcParams['figure.facecolor'] = '#00000000'

# Age data
print(medical_df.age.describe())
figure = px.histogram(medical_df, x = 'age', marginal = 'box', nbins = 47, title = 'Distribution Of Age')
figure.update_layout(bargap=0.1)
figure.show()