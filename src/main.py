import plotly.express as px
import dataprocessing as dp

df = dp.loadData()
print("Loaded database!")

totalaccidents_2010 = dp.getInfo(df, 2010, accidentType="mortel",vehicleType="PL",age=20)
print(totalaccidents_2010)
