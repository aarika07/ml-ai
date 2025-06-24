list = [10,20,40,60]
length = len(list)-1
list.remove(list[length])
#print(list)

list = [10,20,40,60]
list.remove(60)
#print(list)

list = [10,20,40,60]
list.remove(list[3])
#print(list)

list = [10,20,40,60]
list.pop(3)
#print(list)

list = [10,20,40,60]
list.clear()
#print(list)

list = [10,20,40,60]
item = list[0]
slice = list[1:4]
last = list[-1]
#print(f"item{item} slice {slice} last {last}")

list = ["BobaTea", "Tesla", "FriedChiken", "PartyInTheHollywoodHills"]
gnarlyy = list[0]
gnarly = list[1:4]
gnnarly = list[-1]
#print(f"gnarlyy{gnarlyy} gnarly{gnarly} gnnarly{gnnarly}")

list = [10,20,40,60]
#list.sort(reverse=True)
#list.reverse()
reversed_list = list[::-1]
print(list)