import pandas as pd

# Read the cvs file 
data =  pd.read_cvs("tips_cvs.txt", header = 0)

#See  how the data look like
print(data.head())