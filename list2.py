list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ,34,34,34];

print "list1[0] = ",list1[0]
print "list2[1:5] = " , list2[1:5]

#update list1
print "List1 before update = " ,list1
list1[2] = 2001
print "Update list1 = ",list1

#Delete 4th item in the list
del list2[4]
print "After 4th item deleted in the list2 = " ,list2

a = cmp(list1,list2)
print "Compare of two list = " ,a

# length of list1 and list2
print "Length of list1 = " ,len(list1)
print "Length of list2 = " ,len(list2)

#maximum value in list
print "Maximum Value in list = " , max(list2)

#minimum value in list
print "Minimum Value in list = " , min(list2)

#count number of times item in list
print "Count number of times item present in list = " ,list2.count(34)

#Reverse
print "Reverse of list = " ,list1.reverse()







