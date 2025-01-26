import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)



import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar[0])



import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)



import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar["y"])





import pandas as pd
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)



import pandas as pd
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)



import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)



import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
#load data into a DataFrame object:
df = pd.DataFrame(data)
print(df) 





import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
#load data into a DataFrame object:
df = pd.DataFrame(data)
print(df.loc[0])




import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(df.loc[[0, 1]])



import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df) 



import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df.loc["day2"])



#to string : imprimer l'intégralité 
#max8rows : nombre max de lignes renvoyées



import pandas as pd
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409.1,
    "1":479.0,
    "2":340.0,
    "3":282.4,
    "4":406.0,
    "5":300.5
  }
}
df = pd.DataFrame(data)
print(df) 


#head : renvoie les en têtes et un nombre spécifié de lignes sinon renvoie 5 lignes (par défault)
#tail: commence par le bas
#infos : plus d'infos sur les données
#dropna : suppression lignes, par défault renvoie un nouveau dataframe et ne modifie pas l'original sinon dropna(inplace=true)
#fillna : remplacer les valeurs vides, et on peut s^écifier le nom de la cellule
# mean: moyenne
# median
# mode : valeur qui apparait le plus frequemment
#to_datetime : convertir toutes les cellules dans le même format


'''import pandas as pd
df = pd.read_csv('data.csv')
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120
print(df.to_string())
definir des règles pour éviter les erreurs'''

#duplicated : boolenne : pour connaitre les valeurs dupliquées
#drop_duplicates(inplace=true) : pour les supprimer

#corr : calcule la relation entre chaque colonne de l'ensemble des données












