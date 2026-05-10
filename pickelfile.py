import pickle

data = {"name":"Harsh","city":"gondia"}
with open("data.pk1","rb") as file:
 load=pickle.load(file)
 print(load)