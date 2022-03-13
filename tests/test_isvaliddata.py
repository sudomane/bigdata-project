import pytest

url = "https://data.ratp.fr/explore/dataset/trafic-annuel-entrant-par-station-du-reseau-ferre-2020/download/?format=json&timezone=Europe/Berlin&lang=fr"

# Simply checking if the column "Rang" is in the dataframe.
# If it is, then the dataframe has been correctly loaded.
# If not, then we need to properly clean the data.
def test_isvaliddata():
    dataframe = loadData(url)
    assert "Rang" in dataframe
