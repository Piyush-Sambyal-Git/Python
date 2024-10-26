# it is ordered collection of elements which is immutable(unchangeable) and can also store all types of data
# elements of list can be changed but of tupple can't 
t=()
print(type(t))

t=(1,5,4,5.5,'today',False)

print(t.count(5)) #prints number of times a given element comes
print(t.index(5)) #prints the index of given element