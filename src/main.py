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
# - Moto legere
# - Cyclo
t_1 = time.time()
totalaccidents_2010 = dp.getInfo(df, 2010, accidentType="mortel",vehicleType="VU")
t_2 = time.time()

print(totalaccidents_2010)
print("Fetched data in " + "{:.2f}".format(t_2 - t_1) + " seconds!")
