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

# figure = px.histogram(
#         dp.getInfo(df=df), 
#         x=df["Année"],
#         color = df["Catégorie véhicule"],
#         facet_col = "Type Accident", 
#         facet_col_wrap = 3,
# )
# figure.update_layout(barmode="stack", bargap=0.2)
# figure.show()

df2 = dp.getInfo(df=df)
res = df2.groupby(["Age véhicule", "Catégorie véhicule", "Type Accident", "Année"])
mdf = pd.DataFrame({'Age': [], 'V. Type': [], 'A. Type': [], 'Year': [], 'Count': []})
for i, g in enumerate(res):
    mdf.loc[i] = [g[0][0], g[0][1], g[0][2], g[0][3], g[1].size]

clr = {"Léger": "#4a1c40", "mortel": "#2b8b27", "grave non mortel": "#d18502"}

trace = go.Scatter3d(
    x = mdf['Count'],
    y = mdf['Age'],
    z = mdf['Year'],
    mode = 'markers',
    marker = dict( 
                  color = mdf['A. Type'].apply(lambda x: clr[x]),
        opacity = 0.8),

)

layout2 = go.Layout(scene = {'aspectmode':'cube'})
layout2['scene'].update(xaxis = {'title':'Age'}, yaxis = {'title':'Height'}, zaxis = {'title':'Rank'})
layout2['title'] = 'Number of accidents per year. The '

camera = dict( up=dict(x=1, y=0, z=0),           # determine the up direction on the page (here x i.e. Age)
               center=dict(x=0, y=0, z=0),       # (0,0,0) is always the center of the domain, no matter data values
               eye=dict(x=0.25, y=1.7, z=-1.2)   # x 2 to value unzoom by 2,  < 1 and you are in the domaine
             )

layout2['scene_camera'] = camera

fig = go.Figure(data=[trace], layout=layout2)
py.iplot(fig, show_link=False)
