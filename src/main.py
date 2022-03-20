import time
import plotly.graph_objects as go
import plotly.express as px
import dataprocessing as dp
from IPython.display import display

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

# TODO: Dynamically display different vehicle types, and accident types
# NOTE: Refer to Chapter 23 - Dynamic Graphs with Plotly -- Subplots, in docker courses, check unemployment graph for more info
fig = px.histogram(
    df,
    x = "Année",
    color = "Type Accident"
)
fig.update_layout(bargap=0.2)
fig.show()
