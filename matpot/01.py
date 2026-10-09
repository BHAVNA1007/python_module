import matplotlib.pyplot as plt
# a = [10, 20, 30]

# plt.plot(a)
# plt.show()



# x = [1, 2, 3, 4, 5]
# y = [10, 20, 15, 30, 25]

# plt.plot(x, y)
# plt.xlabel("month")
# plt.ylabel("sales")
# plt.show()




# x = [1, 2, 3, 4, 5]
# y = [10, 20, 15, 30, 25]

# plt.plot(x, y)
# plt.title("Weekly sales")
# plt.xlabel("month")
# plt.ylabel("sales")
# plt.grid()
# plt.show()




# x = [1, 2, 3, 4, 5]
# y = [10, 20, 15, 30, 25]

# plt.plot(x, y, marker="o")
# plt.title("Weekly sales")
# plt.xlabel("month")
# plt.ylabel("sales")
# plt.grid()
# plt.show()




students = ["Amit", "Anil", "Rahul", "Neha"]
marks = [65, 80, 72, 90]

plt.plot(students, marks, marker="o", label="Students Marks")

plt.title("Students Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid()

plt.legend()
plt.show()