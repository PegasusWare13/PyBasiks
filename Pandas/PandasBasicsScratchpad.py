import pandas as pd

#Series ->Analogy to columns
print("Series:")
list1 = [2,12,25,87,54]
series1=pd.Series(list1)
print(f"series1 = {series1}")
print(f"Default Index series1[2]: {series1[2]}")
list2 = ["Verstappen", "Leclerc", "Lando", "Oscar"]
series2 = pd.Series(list2, index=['a','b','c','d'])
print(f"series2['b']: {series2['b']}\n")

#DictionaryToSeries
print("Dictionary To Series:")
SccuderriaFerrari = {
    "TP " : "Fred",
    "Driver_1" : "Hamilton",
    "Driver_2 " : "Leclerc",
    "Nickname" : "Hopium Exploiters",
    "LastTitle" : 2007
}
DictSeries = pd.Series(SccuderriaFerrari) #keys will act as labels
print(f"DictSeries['Driver_1']: {DictSeries['Driver_1']}")
RedBull = {
    "Drivers" : ["Verstappen", "Hadjar"],
    "Machinery" : ["RB 19", "RB"],
    "Titles" : [8,6]
}
RBseries = pd.Series(RedBull, index=['Drivers', 'Titles'])
print(RBseries,"\n\n\n")#selective creation of Series by specifying specific keys as indexes

#DataFrame -> Analogy to multidimensional tables
print("DataFrames:")
RedBull = {
    "Drivers" : ["Verstappen", "Hadjar"],
    "Machinery" : ["RB 19", "RB"],
    "Titles" : [8,6]
}
print(pd.__version__)
x = pd.DataFrame(RedBull)
print(x,"\n")
print(x.loc[1],"\n") #So each DataSet is its own row. 
print(x.loc[[0,1]],"\n\n\n") #[] returns a DatFrame


#Indexed DataFrames
print("Indexeded DataFrames:")
RBseries = pd.DataFrame(RedBull, index=['MV33', 'IH6'])
print(RBseries.loc[["MV33","IH6"]],"\n")
print(RBseries.loc["MV33"])

