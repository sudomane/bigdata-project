import pandas as pd

def loadData(dataset):
    # Throw exception if we couldn't load the file, or URL is invalid.
    try:
        # Load dataframe
        df = pd.read_csv(dataset, sep=";")
                
        df['Correspondances'] = df[df.columns[4:9]].values.tolist()
        
        df.drop(df.columns[4:11], axis=1, inplace=True)
        df.drop(df.columns[0:2], axis=1, inplace=True)

        return df
    except Exception as e:
        print("Caught exception: " + str(e))