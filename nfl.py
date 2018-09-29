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

df = pd.read_csv('data/2018.csv', usecols=is_named)
df.head()
