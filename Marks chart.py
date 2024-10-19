import numpy as np
import matplotlib.pyplot as plt
student_names=["Aarv","Yaksh","Jhon","Jeff","Adam","Ram","Emily","Rose"]
student_marks=[50,32,34,49,10,48,40,29]
marks_percentage=[]
for x in student_marks:
    res=(x/50)*100
    marks_percentage.append(res)
print(marks_percentage)
def marks_linechart():
    plt.plot(student_names,student_marks)
    plt.title("Students' Marks Chart")
    plt.xlabel("Students' Names")
    plt.ylabel("Students' Marks")
    plt.show()
marks_linechart()
def percentagebarchart():
    plt.bar(student_names,marks_percentage)
    plt.title("Students' Marks In Percentage")
    plt.xlabel("Students' Names")
    plt.ylabel("Students' Marks")
    plt.show()
percentagebarchart()