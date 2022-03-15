import pandas as pd

def loadData(dataset : str) -> pd.DataFrame:
    # Throw exception if we couldn't load the file, or URL is invalid.
    try:
        # Load dataframe
        df = pd.read_csv(dataset, sep=";")
                
        # Select the all the correspondances column
        df['Correspondances'] = df[df.columns[4:9]].values.tolist()
        
        df.drop(df.columns[4:11], axis=1, inplace=True)
        df.drop(df.columns[0:2], axis=1, inplace=True)

        return df
    except Exception as e:
        print("Caught exception: " + str(e))
        
# SHOULD WE USE DICTIONNARIES, OR RETURN A TUPLE OF X, Y LISTS?
def getLineInfo(df : pd.DataFrame, line : str) -> dict:
    dict = {}

    # 0 - Stations
    # 1 - Trafic
    # 2 - Correspondances

    for i in range(df.index.size):
        if line in df.iloc[i, 2]:
            dict[df.iloc[i, 0]]  = df.iloc[i, 1]
    
    return dict