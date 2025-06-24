list1=["b1",1, 2.0, "b2"]
def listdisplay1(list, searchItem):
    #iterate over the list
    for i in list:
        if i == searchItem:
            print(i)
            break
    else:

        print(f"the searchItem{searchItem} is not in the list")
#listdisplay1(list1, 2.0)

#list1=["b1", 1, 2.0, "b2"]
#def displaylist(list1):
    #for item in list:
       # print(item)
#displaylist(list1)


def listbay1(list1):
    length=len(list1)-1
    print(list1[0])
    print(list1[length])

list1=["b1", 1, 2.0, "b2"]
listbay1(list1)