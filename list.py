list = [1,2,3,4,5]

print "List = ",list

list.append(6)
print "Appended List = ",list

list.extend([7,8])
print "Extended List = ",list

list.append([9,10])
print "Append list in List = ",list

sub_list = list[8][1]
print "Item in sub list = " ,sub_list

list.append(11)
print "List = ",list

list.remove(11)
print "Removed item(11) in List = ",list

n = len(list)
print "length of List = ",n

list.insert(2,"new")
print "Inserted item in List = ",list



