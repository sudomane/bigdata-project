import plotly.express as px
import dataprocessing as dp

df = dp.loadData()
print("Loaded database!")

totalaccidents_2010 = dp.getInfo(df, 2010, accidentType="mortel",vehicleType="PL",age=20)
print(totalaccidents_2010)
#fig = px.line(df, x="Année", y="Type Accident", title="Accidents en France 2010 - 2020")
#fig.show()

#light_accident = dataframe["Type Accident"] == "Léger"
#fatal_accident = dataframe["Type Accident"] == "mortel"
#nonfatal_accident = dataframe["Type Accident"] == "grave non mortel"

# TODO: Find a way to select accident type within group
#sum = dataframe.groupby('Année')

#light = dataframe[light_accident].groupby('Année').size()
#fatal = dataframe[fatal_accident].groupby('Année').size()
#nonfatal = dataframe[nonfatal_accident].groupby('Année').size()

#fig = light.plot()
#fig = fatal.plot()
#fig = nonfatal.plot()
#fig.show()