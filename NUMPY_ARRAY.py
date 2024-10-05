import numpy as np
datatype=[("name","S15"),("class",int),("height",float)]
studentdetails=[("James",5,48.5),("Jhon",6,50),("Emily",5,45)]
students=np.array(studentdetails,dtype=datatype)
print("original array",students)
print("Sort By Height",np.sort(students,order="height"))
arr = np.array([1,2,3,4,5],dtype=str)
print(arr)
print(type(arr))
#print(np.sort(arr,order=[]))
print(arr[::-1])