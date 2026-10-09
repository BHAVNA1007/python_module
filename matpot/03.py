#bar graph

import matplotlib.pyplot as plt



# students = ['Anil', 'Amit', 'Rahul', 'Neha']
# marks = [65, 80, 72, 90]
# plt.bar(students, marks)
# plt.xlabel("Students")
# plt.ylabel("Marks")
# plt.title("student marks..")

# plt.show()




#horizontal bar graph

# students = ['Anil', 'Amit', 'Rahul', 'Neha']
# marks = [65, 80, 72, 90]
# plt.barh(students, marks)
# plt.xlabel("Students")
# plt.ylabel("Marks")
# plt.title("student marks..")

# plt.show()



#PIE CHART

# students = ['Amit', 'Rahul', 'Priya', 'Neha']
# marks = [65, 80, 72, 90]
# plt.pie(marks, labels=students)
# plt.title("Student Marks")
# plt.show()




# students = ['Amit', 'Rahul', 'Priya', 'Neha']
# marks = [65, 80, 72, 90]

# plt.pie(marks, 
#         labels=students,
#         autopct="%1.1f%%",
#         startangle=90,
#         explode=(0.05, 0,0,0),
#         shadow=False
#     )

# plt.title("Student Marks")
# plt.axis("equal")
# plt.show()


#scatter

# students = ['Amit', 'Rahul', 'Priya', 'Neha']
# marks = [65, 80, 72, 90]

# plt.scatter(marks, students
        
#     )
# plt.xlabel("Students")
# plt.ylabel("Marks")
# plt.title("student vs marks..")
# plt.grid()
# plt.show()


#histogram


#wrong output correct it
# students = ['Amit', 'Rahul', 'Priya', 'Neha']
# marks = [65, 80, 72, 90]

# plt.hist(marks, students
        
#     )
# plt.xlabel("Students")
# plt.ylabel("Marks")
# plt.title("student vs marks..")
# plt.grid()
# plt.show()




# students = [1,2,3,4]
# marks = [65, 80, 72, 90]

# plt.fill_between(marks, students
        
#     )
# plt.xlabel("Students")
# plt.ylabel("Marks")
# plt.title("student vs marks..")
# plt.show()




#stem

# students = [1,2,3,4]
# marks = [65, 80, 72, 90]

# plt.stem(marks, students
        
#     )
# plt.xlabel("Students")
# plt.ylabel("Marks")
# plt.title("student vs marks..")
# plt.show()




#boxplot

marks = [65, 80, 72, 90]

plt.boxplot(marks)
plt.ylabel("Marks")
plt.title("student vs marks..")
plt.show()


