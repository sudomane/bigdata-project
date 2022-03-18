import os
import glob
import pandas as pd

# CSV databases from 2010 to 2020
path = os.path.join(os.getcwd(), "src")
path = os.path.join(path, "data")
path = os.path.join(path, "*.csv")

files = glob.glob(path)

print(files)

def loadData() -> pd.DataFrame:
    dataframe = pd.concat((pd.read_csv(f, sep=';', on_bad_lines='skip') for f in files))
    return dataframe
