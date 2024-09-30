# dictionary = a collection of { key : value } pairs ordered and changable. No duplicates 
capitals = { "USA" : "Washignion DC ","India":"New Delhi","China":"Beijing"," Russia" : "Mascow" }
 # print (dir(captials))
 #print (help( capitals ))
#help - gives you 
print(capitals.get("USA"))
#print (capitals.get (japan)) - doesnt exist 
if capitals.get("Ruissa"):
print ("that capital exist")
else:
print ("that capital doesn exist")
capitals.update ({"Germany":"Berlin"})
capitals.update ({"USA":"Detroits"})
capitals.pop("China") # removes item 
#remove the last item in the dctionary 
capitals.popitem()
#capitaisl.clear () will clear the dictornary 
capitaisl.clear () 
# returns the keys ans not the values 
keys = capitals.keys()
for keys in capitals.key ( )
print(keys)
#returns all values nd not keys 
values = capitals.values()
print ( values)
for value in capitals.values :
print (values)
capitals.items()
print(items)
for key, value in capitals.item ():
print (f"{key}":"{value}")