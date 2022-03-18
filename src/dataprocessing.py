import os
import glob
import pandas as pd

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
