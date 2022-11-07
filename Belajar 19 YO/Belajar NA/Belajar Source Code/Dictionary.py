###Basic Dictionary 
my_data = {"name" : "royger", "age" : 19, "mycity":"Bekasi"}
print (my_data)
print (my_data['name'])
print (my_data["age"])
print (my_data.get("mycity"))
my_data2 = {
    "name" : "Royger",
    "age" : 19,
    "my_city" : "Bekasi"
}
print(my_data2)

###untuk mengganti suatu nilai 
my_data2 ["age"] = 18
print(my_data2)

###menambahkan key baru
my_data2 ["culture"] = "jawa"
print(my_data2)

###method pada dictionary
#melihat key
print (my_data2.keys())
#melihat values
print (my_data2.values())
#menhapus item
my_data2.pop ("my_city")
print(my_data2)
#menghapus item terakhir 
my_data2.popitem()
print(my_data2)
#menghapus seluruh item
#my_data2.clear()

###method copy 
my_data3 = my_data2.copy()
my_data3 ["country"] = "indonesia"
print(my_data2)
print(my_data3)

###Nested Dictionary
my_data4 = {
    "key1" : 1,
    "key2" : ["kamu","dia","aku","mereka"],
    "key3" : {"a":"aku", "m" : "mereka", "d" : "dia"}
}
print (my_data4 ["key1"])
print (my_data4 ["key2"][3])
print (my_data4 ["key3"]["a"])