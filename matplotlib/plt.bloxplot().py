import matplotlib.pyplot as plt


# ages = [18,19,20,20,21,22,23,24,25,60]

# plt.boxplot(ages)
# plt.show()

male = [20,21,22,23,25]
female = [18,19,20,22,35]

plt.boxplot([male, female],
            label=["Male","Female"])

plt.show()
#показывает свечу из трейдинга, используется для сравнения, наример кто старше?
