# ---
# jupyter:
#   jupytext_format_version: '1.3'
#   jupytext_formats: ipynb,py
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.6.5
# ---

# %autosave 0

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', 100)
sns.set(style='darkgrid')

# pandas reads empty csv columns (',,') as 'Unnamed N' where N is the column number
def is_named(row):
    return not row.lower().startswith('unnamed')

def lower(element):
    return element.lower() if type(element) == str else element

def load(csv_path):
    df = pd.read_csv(csv_path, usecols=is_named)
    df.columns = df.columns.str.lower()
    df = df.applymap(lower)

    return df

df = load('data/2018.csv')
df.head()

df.gameid.nunique()

len(df)

df.playtype.value_counts()

df.formation.value_counts()

len(df[df.isrush == True])

df.rushdirection.value_counts()

len(df[df.ispass == True])

df.passtype.value_counts()

len(df[df.istouchdown == True])

len(df[df.playtype == 'field goal'])

len(df[df.isinterception == True])

len(df[df.isfumble == True])

len(df[df.issack == True])

len(df[df.ispenalty == True])

df.offenseteam.value_counts()

df.defenseteam.value_counts()

len(df.defenseteam.value_counts())

f, ax = plt.subplots(figsize=(12, 6))
td_df = df[df.istouchdown == True]
sns.countplot(x='offenseteam', data=td_df, order=td_df.offenseteam.value_counts().index, color='b')


