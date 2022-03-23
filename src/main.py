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
# NOTE: Refer to "Aggregation" for more information. Check plotly documentation

vehicles = ["VT", "Cyclo", "Moto lourde", "VU", "Moto légère", "PL", "Autres", "TC", "Indéterminable"]

fig = go.Figure()#make_subplots(rows=1, cols=1)

for v in vehicles:
    data = dp.getInfo(df=df, vehicleType=v)
    trace = go.Histogram(name = v, x = data["Année"])
    fig.add_trace(trace)

fig.update_layout(barmode="stack", bargap=0.2)
fig.show()

#f2 = px.scatter(df[df["Année"] == 2019], y="Age véhicule", color = "Catégorie véhicule")
#f2.show()
