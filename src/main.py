import time
import plotly.graph_objects as go
import plotly.express as px
import dataprocessing as dp
from plotly.subplots import make_subplots
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

print(df)
vechicles = ["VT", "Cyclo", "Moto lourde", "VU", "Moto légère", "PL", "Autres", "TC", "Indéterminable"]

# Accident Types:
# - mortel
# - grave non mortel
# - Léger

# TODO: Dynamically display different vehicle types, and accident types
# NOTE: Refer to "Aggregation" for more information. Check plotly documentation
f1 = px.histogram(
    df,
    x = "Année",
    color = "Catégorie véhicule"
)
f1.update_layout(bargap=0.2)
f1.show()
#
#
# fig2 = make_subplots(rows=2, cols=1)
#
# for v in vechicles:
#     data = dp.getInfo(df=df, vehicleType=v)
#     trace = go.Histogram(
#         name = v,
#         x = data["Année"],
#         bingroup=1
#     )
#     fig2.add_trace(trace, 1, 1)
# fig2.update_layout(barmode="overlay",
#                    bargap=0.1)
# fig2.show()

f2 = px.scatter(df[df["Année"] == 2019], y="Age véhicule", color = "Catégorie véhicule")
f2.show()
