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
totalaccidents = dp.getInfo(df, vehicleType="TC")
t_2 = time.time()

print("Fetched data in " + "{:.2f}".format(t_2 - t_1) + " seconds!")
print(totalaccidents)

# TODO: Dynamically display different vehicle types, and accident types
# NOTE: Refer to Chapter 23 - Dynamic Graphs with Plotly -- Subplots, in docker courses, check unemployment graph for more info
fig = px.histogram(
    totalaccidents,
    x = "Année"
)

fig.show()