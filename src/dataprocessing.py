import pandas as pd

def loadData(dataset):
    # Throw exception if we couldn't load the file, or URL is invalid.
    try:
        dataframe = pd.read_csv(dataset, sep=";")
        dataframe.rename(columns={
                "Correspondance_1" : "1",
                "Correspondance_2" : "2",
                "Correspondance_3" : "3",
                "Correspondance_4" : "4",
                "Correspondance_5" : "5"
            }, inplace=True)
        
        return dataframe
    except Exception as e:
        print(e)