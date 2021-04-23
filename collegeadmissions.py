import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel (r'IPEDS_data.xlsx')

datax = pd.DataFrame(df,columns=["Longitude location of institution", "Religious affiliation"])
datay = pd.DataFrame(df,columns=["Latitude location of institution", "Religious affiliation"])

datax_n = datax[datax['Religious affiliation'].isin(['Not applicable'])]
datax_y = datax[~datax['Religious affiliation'].isin(['Not applicable'])]

datay_n = datay[datay['Religious affiliation'].isin(['Not applicable'])]
datay_y = datay[~datay['Religious affiliation'].isin(['Not applicable'])]

plt.figure()

plt.scatter(datax_n.drop("Religious affiliation", axis=1), datay_n.drop("Religious affiliation", axis=1), color='red',alpha=0.2,s=10)
plt.scatter(datax_y.drop("Religious affiliation", axis=1), datay_y.drop("Religious affiliation", axis=1), color='green',alpha=0.2,s=10)

plt.show