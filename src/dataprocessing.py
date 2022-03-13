import pandas as pd

def loadData(dataset):
    # Throw exception if we couldn't load the file, or URL is invalid.
    try:
        dataframe = pd.read_json(dataset)
        return dataframe
    except Exception as e:
        print(e)
