### list basic 
list = ["roy", 10, 11.1]
print (list[1])
list2 = [ "one",'two','three','four']
print (list2[2])

###menambahkan object pada list 
list2.append("five")
print(list2)
list2.insert (0, "zero")
print(list2)


###menghapus object pada list 
list2.remove ("three")
print(list2)
list2.remove(list2[1])
print(list2)
list2.pop()
print (list2)

###Menggabungkan list dan beberapa method 
list3 = 1,2,3,4,5,6
list4 = 9,15,10,11,17,15,16
list5 = list3 + list4
print (list5)
print (list5.count (1))
print (list5.index(15))

### Method copy
list10 = ["aku", "adik", "mama","papa"]
list11 = list10.copy()
print (list11)
print (list10)
list11.append("dia")
list11.insert(0, "kamu")
print (list11)
print (list10)


#nested list 
list6 = (1,2,3,4)
list7 = (5,6,7)
list8 = (8,9,10)
list9 = [list6, list7, list8]
print (list9)
print (list9[0][3])