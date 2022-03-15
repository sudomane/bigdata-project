import pandas as pd

def loadData(dataset):
    # Throw exception if we couldn't load the file, or URL is invalid.
    try:
        dataframe = pd.read_csv(dataset, sep=";")
 
        c_1 = dataframe.Correspondance_1=="2"
        c_2 = dataframe.Correspondance_2=="2"
        c_3 = dataframe.Correspondance_3=="2"
        c_4 = dataframe.Correspondance_4=="2"
        c_5 = dataframe.Correspondance_5=="2"
        filtered = dataframe.loc[(c_1) | (c_2) | (c_3) | (c_4) | (c_5)]
        return filtered.loc[:, ('Trafic', 'Station')]
    except Exception as e:
        print(e)
