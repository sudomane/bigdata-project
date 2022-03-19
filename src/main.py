import time
import plotly.express as px
import dataprocessing as dp

t_1 = time.time()
df = dp.loadData()
t_2 = time.time()
print("Loaded database in " + "{:.2f}".format(t_2 - t_1) + " seconds!")

# Vehicle Types:
# - PL - Poids Lourd
# - VT - Véhicules Tourisme
# - VU - Véhicules Utilitaires
# - TC - Transport en Commun
# - Moto lourde
# - Moto légère
# - Cyclo

# Accident Types:
# - mortel
# - grave non mortel
# - Léger

t_1 = time.time()
# Demonstration on how to use the function
totalaccidents_2010 = dp.getInfo(df, 2010, accidentType="Léger",vehicleType="TC", age=2)
t_2 = time.time()

print(totalaccidents_2010)
print("Fetched data in " + "{:.2f}".format(t_2 - t_1) + " seconds!")

# TODO: Dynamically display different vehicle types, and accident types
fig = px.histogram(
    df,
    x = df["Année"]
)

fig.show()