import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



def fit():
    df:pd.DataFrame = pd.read_csv("csv/abalone.csv")

    #print(df.head())   

    #print(df.isnull())   


    #sns.histplot(data = df[['Diameter']], kde = True)
    #plt.show()


    # print(df.head())
    # print(df.info())
    # print(df.describe())

    #shape = df.shape
    #columns = df.columns.tolist()

    #print(f"Shape: {shape}")
    #print(f"Columns: {columns}")

    #duplicates = df.duplicated().sum()

    #print(duplicates)

    #print(df.describe().T)

    # plt.figure(figsize=(12, 5))
    # plt.subplot(1, 2, 1)
    # sns.histplot(df['Diameter'], kde=True, color='#1a5276')
    # plt.title('Diameter Distribution')    

    # plt.subplot(1, 2, 2)
    # df['Rings'].value_counts().plot.pie(autopct='%1.1f%%', colors=['#2ecc71', '#e74c3c'])
    # plt.title('Rings Frequency')
    
    # plt.show()

    # plt.figure(figsize=(10, 8))
    # corr = df.select_dtypes(include=[np.number]).corr()
    # sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    # plt.title('Risk Factor Correlation Matrix')
    # plt.show()    





if __name__ == "__main__":
    fit()

