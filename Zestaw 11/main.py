from SingleList import SingleList
from Node import Node

alist = SingleList()
alist.insert_head(Node(11))   # [11]
alist.insert_head(Node(22))   # [22, 11]
alist.insert_tail(Node(33))   # [22, 11, 33]
print("length {}".format(alist.length))   # odczyt atrybutu
print("length {}".format(alist.count()))   # wykorzystujemy interfejs
while not alist.is_empty():   # kolejność 22, 11, 33
    print("remove head {}".format(alist.remove_head()))


print("\nExample usage of remove_tail ")
# Example of remove_tail
blist = SingleList()
blist.insert_head(Node(44))   # [44]
blist.insert_head(Node(55))   # [55, 44]
blist.insert_tail(Node(66))   # [55, 44, 66]
print("B-list:")
blist.print_list()
while not blist.is_empty():   # kolejność 66, 44, 55
    print("remove tail {}".format(blist.remove_tail()))


print("\nExample usage of join ")

clist = SingleList()
dlist = SingleList()

clist.insert_head(Node('b'))
clist.insert_tail(Node('c'))
clist.insert_head(Node('a'))
print("C-list:")
clist.print_list()

dlist.insert_tail(Node('A'))
dlist.insert_tail(Node('B'))
dlist.insert_tail(Node('C'))
print("D-list:")
dlist.print_list()

clist.join(dlist)

print("After join: ")

print("C-list:")
clist.print_list()

print("D-list:")
dlist.print_list()
print("D-list.length = {}".format(dlist.length))
#
print("\nExample usage of clear ")

clist.clear()
print("C-list after clear:")
clist.print_list()
print("C-list.length = {}".format(clist.length))
