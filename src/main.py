import time
import plotly.graph_objects as go
import plotly.express as px
import dataprocessing as dp
from IPython.display import display
from plotly.subplots import make_subplots
import pandas as pd
import plotly.offline as py

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
# NOTE: Refer to "Aggregation" for more information. Check plotly documentation

figure1 = px.histogram(
        dp.getInfo(df=df),
        x=df["Année"],
        color = df["Catégorie véhicule"],
        facet_col = "Type Accident",
        facet_col_wrap = 3,
)
figure1.update_layout(barmode="stack", bargap=0.2)
figure1.show()

mdf = dp.getCounts(df=df)
clr = {"Léger": "#9ecbed", "mortel": "#2a6a99", "grave non mortel": "#3c97da"}

figure2 = px.scatter_3d(
    mdf,
    x = 'Année',
    y = 'Age véhicule',
    z = 'Count',
    color = 'Type Accident',
    color_discrete_map=clr,
) 

figure2.show()
