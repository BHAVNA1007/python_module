#import matplotlib.pyplot as plt


# students = ["Amit", "Anil", "Rahul", "Neha"]
# marks = [65, 80, 72, 90]

# plt.plot(students, marks, marker="p", label="Students Marks", color='r', linestyle='-.' , linewidth=3, markersize=12, markerfacecolor='g',  markeredgecolor='k', markeredgewidth=3, alpha=0.5)

# #r=red, g=green, b=blue, c=Cyan, m=Megenta, o=Orange y = yellow, k= black

# plt.title("Students Marks")
# plt.xlabel("Students")
# plt.ylabel("Marks")
# plt.grid()

# plt.legend()
# plt.show()




import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]

sales = [100, 150, 120, 180, 220]
profit = [20, 40, 30, 50, 70]

plt.plot(
    days,
    sales,
    color="red",
    linestyle="-",
    marker="o",
    linewidth=3,
    label="Sales"
)

plt.plot(
    days,
    profit,
    color="blue",
    linestyle="--",
    marker="s",
    linewidth=2,
    label="Profit",
    solid_joinstyle="round"
)

plt.xlabel("Days")
plt.ylabel("Amount")
plt.title("Sales vs Profit")

plt.legend()
plt.grid()

plt.show()
