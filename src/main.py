import dataprocessing as dp

dataframe = dp.loadData()
print("Loaded database!")

# TODO: Find a way to select accident type within group
sum = dataframe.groupby('Année').size()

fig = sum.plot()
fig.show()