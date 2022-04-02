import os
import glob
import pandas as pd
import plotly
                        
# Setting plotting backend to use plotly
pd.options.plotting.backend = "plotly"

# CSV databases from 2010 to 2020
path = os.path.join(os.getcwd(), "src")
path = os.path.join(path, "data")
path = os.path.join(path, "*.csv")

files = glob.glob(path)

def loadData() -> pd.DataFrame:
    # Read every CSV file, load it into one dataframe
    dataframe = pd.concat((pd.read_csv(f, sep=';', on_bad_lines='skip') for f in files))
    
    # Remove useless columns
    dataframe.drop(columns=["CNIT", 
                            "Lieu Admin Actuel - Territoire Nom", 
                            "Lettre Conventionnelle Véhicule", 
                            "Id_accident"], 
                   inplace=True)
    
    # Rename column for better readability
    dataframe.rename(columns={"Type Accident - Libellé" : "Type Accident"}, inplace=True)
    
    # Remove redundant "Accident" prefix in every row
    dataframe["Type Accident"].replace(to_replace="Accident *", value = "", regex=True, inplace=True)

    return dataframe

# This function returns a dataframe matching the given specifications.
# If accidentType, vehicleType and age are "None", then it will only
# select all the rows of the matching year.
def getInfo(df : pd.DataFrame, year=None, accidentType=None, vehicleType=None, age=None) -> pd.DataFrame:
    
    if (year == None and accidentType == None and vehicleType == None and age == None):
        return df

    mask = True

    if (year):
        mask = (df['Année'] == year)
    
    if (accidentType):
        mask = mask & (df["Type Accident"] == accidentType)

    if (vehicleType):
        mask = mask & (df["Catégorie véhicule"] == vehicleType)

    if (age):
        mask = mask & (df["Age véhicule"] == age)

    return df.loc[mask].copy(deep=True)

def getCounts(df: pd.DataFrame):
    res = df.groupby(["Age véhicule", "Type Accident", "Année"])
    mdf = pd.DataFrame({'Age véhicule': [], 'Type Accident': [], 'Année': [], 'Count': []})
    for i, g in enumerate(res):
        age, a_type, year = g[0]
        mdf.loc[i] = [age, a_type, year, g[1].size]
    return mdf
    
