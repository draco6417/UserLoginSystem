import pandas as pd
import matplotlib.pyplot as plt
dataframe = pd.read_csv("C:\\Users\\shahbaz khan\\Downloads\\data.csv")
print("Data frame\n",dataframe)
plt.xlabel('Sepal Length',fontsize=20)
plt.ylabel('Petal Length',fontsize=20)
plt.title('A Scatter Plot of IRIS')
plt.scatter(dataframe['SepalLengthCm'],dataframe['SepalWidthCm'], color='red')
plt.show()
plt.plot(dataframe.Id,dataframe["SepalLengthCm"],"r--")
plt.show()
