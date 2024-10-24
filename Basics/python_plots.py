# Imports
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

plt.style.use("seaborn-whitegrid")
plt.rc("figure", autolayout=True)
plt.rc("axes", labelweight="bold", labelsize="large", titleweight="bold", titlesize=14, titlepad=10)



# 1a) plt.plot()
x = list(range(1, 21))
y = [i**2 for i in x]

plt.plot(x, y)
plt.plot(x, y, 'ro')
plt.title('plt.plot()')
plt.xlabel('x')
plt.ylabel('y')
plt.show()



# 1b) plt.bar()
x = list(range(1, 11))
xticks = ["Dog", "Cat", "Rabbit", "Sheep", "Goat", "Cow", "Goldfish", "Snake", "Lion", "Tiger"]
y = np.random.randint(1, 101, 10)
y = sorted(y, reverse=True)
plt.figure(figsize=(10, 4))
plt.bar(x, y)
plt.title('plt.bar()')
plt.xlabel('Animals')
plt.ylabel('Love')
plt.xticks(x, xticks)
plt.show()

# Indeces 4 and 6: Overlapping
x1 = [1, 3, 4, 5, 6, 7, 9]
y1 = [4, 7, 2, 4, 7, 8, 3]
x2 = [2, 4, 6, 8, 10]
y2 = [5, 6, 2, 6, 2]
plt.bar(x1, y1, label="Blue Bar", color='b')
plt.bar(x2, y2, label="Green Bar", color='g')
plt.xlabel("bar number")
plt.ylabel("bar height")
plt.title("plt.bar() - Overlapping Bar Chart Example")
plt.legend()
plt.show()


# 1c) plt.barh()
x = list(range(1, 11))
xticks = ["Dog", "Cat", "Rabbit", "Sheep", "Goat", "Cow", "Goldfish", "Snake", "Lion", "Tiger"]
y = np.random.randint(1, 101, 10)
y = sorted(y, reverse=True)

plt.figure(figsize=(8, 5))
plt.barh(x, y)
plt.title('plt.barh()')
plt.xlabel('Love')
plt.ylabel('Animals')
plt.yticks(x, xticks)
plt.show()



# 1d) plt.scatter()
x = np.random.randint(1, 101, 90)
y = np.random.randint(1, 101, 90)
x1, x2, x3 = x[:30], x[30:60], x[60:]
y1, y2, y3 = y[:30], y[30:60], y[60:]

plt.figure(figsize=(8, 5))
plt.scatter(x1, y1, label="Group 1", color='b', marker='o')
plt.scatter(x2, y2, label="Group 2", color='g', marker='^')
plt.scatter(x3, y3, label="Group 3", color='r', marker='v')
plt.title('plt.scatter()')
plt.xlabel('x')
plt.ylabel('y')
plt.show()



# 1e) plt.hist()
mean_value = 5
LEN = 200
noise = mean_value + np.random.randn(LEN)
x = list(range(LEN))

plt.figure(figsize=(8, 5))
plt.bar(x, noise)
plt.xlabel("x")
plt.ylabel("noise")
plt.title("plt.bar() - Raw Data")
plt.show()

plt.hist(noise, bins=20)
plt.title("plt.hist()")
plt.xlabel("Noise")
plt.ylabel("Frequency of appearance")
plt.plot([mean_value, mean_value], [0, LEN/5], 'r--')
plt.show()

plt.hist(noise, cumulative=True, bins=20)
plt.title("plt.hist() - Cumulative Histogram")
plt.show()



# 1f) plt.pie()
expenses = [8000, 6000, 4000, 2000]
labels = ['Rental Home', 'Food', 'Car', 'Entertainment']
colors = ['r', 'g', 'b', 'y']

plt.pie(expenses, labels=labels, colors=colors, startangle=90, explode = (0, 0.08, 0.16, 0.24), autopct = '%1.2f%%', shadow=True)
plt.title('plt.pie() - Annual Expenses')
plt.show()



# 1g) plt.stackplot()
x = list(range(1, 13))
y1  = [23, 40, 28, 43,  8, 44, 43, 18, 17, 40, 23, 26]
y2  = [17, 30, 22, 14, 17, 17, 29, 22, 30, 10, 29, 20]
y3  = [15, 31, 18, 22, 18, 19, 13, 32, 39, 12, 30, 17]

# !!!! Adding Legend for stack plots is tricky !!!!
plt.plot([], [], color='r', label = 'Rental Expenses')
plt.plot([], [], color='g', label = 'Car Expenses')
plt.plot([], [], color='b', label = 'Food Expenses')

plt.stackplot(x, y1, y2, y3, colors= ['r', 'g', 'b'])
plt.title('plt.stackplot() - Month Expenses')
plt.xlabel('Month')
plt.ylabel('Expenses')
plt.legend()
plt.show()



# 1h) plt.fill_between()
LEN = 50
x = list(range(1, LEN+1))
y = 200 + np.random.randn(LEN)

plt.plot(x, y, '-')
plt.fill_between(x, y, 195, where=(y > 195), facecolor='g', alpha=0.4)
plt.title("plt.fill_between() - Fills and Alpha Example")
plt.show()



# 2a) sns.barplot()
movies = ["Pirates of the Caribbean", "Harry Potter", "Lord of the Rings", "Da Vinci Code"]
ratings = [9.5, 4.5, 7.8, 6.2]
df = pd.DataFrame({"Movie": movies, "Rating": ratings})
print(df)

plt.figure(figsize=(8, 4))
sns.barplot(x="Movie", y="Rating", data=df)    # sns.barplot(x=df["Movie"], y=df["Rating"])
plt.title('sns.barplot()')
plt.show()



# 2b) sns.lineplot()
x = list(range(1, 13))
xticks = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
y = [1000, 1100, 1120, 1080, 1040, 990, 970, 970, 1000, 1080, 1160, 1050]
sns.lineplot(x=x, y=y)
plt.xticks(x, xticks)
plt.title('sns.lineplot()')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
apple = [1000, 1100, 1120, 1080, 1040, 990, 970, 970, 1000, 1080, 1160, 1050]
microsoft = [950, 970, 1000, 980, 1080, 1060, 1040, 1100, 1080, 1070, 1120, 1150]
amazon = [1100, 1080, 1020, 1050, 980, 1000, 1100, 1120, 1030, 950, 1000, 1000]
df = pd.DataFrame({"Apple": apple, "Microsoft": microsoft, "Amazon": amazon}, index=months)
print(df)
sns.lineplot(data=df)
plt.title('sns.lineplot()')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()



# 2c) sns.heatmap()
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
aegean = [0.51, -1.02, 1.43, -0.65, 0.76, 2.01, 3.12, 3.56, 1.21, -1.23, -1.42, 1.21]
ryanair = [0.82, -0.72, 1.33, -0.32, 1.07, 2.52, 3.43, 2.98, 1.03, -1.54, -1.09, 0.76]
easyjet = [0.65, -1.29, 1.88, -0.43, 0.99, 2.12, 3.37, 3.59, 0.72, -0.62, -1.01, 0.98]
olympicair = [0.78, -1.32, 1.59, -1.00, 0.85, 1.98, 3.23, 3.18, 0.56, -1.05, -1.65, 0.57]
flight_delays = pd.DataFrame({"Aegean": aegean, "Ryanair": ryanair, "Easyjet": easyjet, "Olympic Air":olympicair}, index=months)
print(flight_delays)

sns.heatmap(data=flight_delays, annot=True)
plt.title('sns.heatmap() - Average flight Delays')
plt.xlabel('Airline')
plt.ylabel('Month')
plt.show()



# 2d) sns.scatterplot()
x = np.random.randint(1, 101, 20)
y = np.random.randint(1, 101, 20)
y_higher_than_50 = ['Higher' if elem >=50 else 'Lower' for elem in y]
df = pd.DataFrame({"X": x, "Y": y, "Is y higher than 50?":y_higher_than_50})
print(df)

sns.scatterplot(x=df.X, y=df.Y, hue=df['Is y higher than 50?'])
plt.plot([0, 100], [50, 50], 'r--')
plt.title('sns.scatterplot()')
plt.xlabel('x')
plt.ylabel('y')
plt.show()



# 2e) sns.regplot()
from math import sqrt, log, log10
x = list(range(1, 51))
y = [sqrt(i) + 0.5*np.random.randn() for i in x]
sns.regplot(x=x, y=y)



# 2f) sns.lmplot()
penguins = pd.read_csv("/content/penguins.csv")
sns.lmplot(data=penguins, x="bill_length_mm", y="bill_depth_mm")
plt.title('sns.lmplot() with 2 arguments')
plt.show()
print("\n")
sns.lmplot(data=penguins, x="bill_length_mm", y="bill_depth_mm", hue="species")
plt.title('sns.lmplot() with 3 arguments')
plt.show()
print("\n")
sns.lmplot(data=penguins, x="bill_length_mm", y="bill_depth_mm", hue="species", col="sex", height=4)
plt.title('sns.lmplot() with 4 arguments')
plt.show()



# 2g) sns.swarmplot()
tips = pd.read_csv("/content/tips.csv")
sns.swarmplot(data=tips, x="total_bill")
plt.title('sns.swarmplot() with 1 argument (x)')
plt.show()
print("\n")
sns.swarmplot(data=tips, x="total_bill", y="day")
plt.title('sns.swarmplot() with 2 argument (x, y)')
plt.show()
print("\n")
sns.swarmplot(data=tips, x="total_bill", y="day", hue="sex", legend=True)
plt.title('sns.swarmplot() with 3 arguments (x, y, hue)')
plt.show()



# 2h) sns.histplot()
cancer_data = pd.read_csv("/content/cancer_data.csv")
sns.histplot(data=cancer_data, x="radius_mean", bins=25)
plt.title('sns.histplot() with 1 argument (x)')
plt.show()
sns.histplot(data=cancer_data, x="radius_mean", hue="diagnosis", bins=25)
plt.title('sns.histplot() with 2 arguments (x, hue)')
plt.show()



# 2i) sns.kdeplot()
cancer_data = pd.read_csv("/content/cancer_data.csv")
sns.kdeplot(data=cancer_data, x="radius_mean")
plt.title('sns.kdeplot() with 1 argument (x)')
plt.show()
print("\n")
sns.kdeplot(data=cancer_data, x="radius_mean", hue="diagnosis")
plt.title('sns.kdeplot() with 2 arguments (x, hue)')
plt.show()



# 2j) sns.jointplot()
sns.jointplot(data=cancer_data, x="radius_mean", y="area_mean")
plt.title('sns.jointplot() with 2 arguments (x, y)')
plt.show()
print("\n")
sns.jointplot(data=cancer_data, x="radius_mean", y="area_mean", kind="hist")
plt.title('sns.jointplot() with 2 arguments (x, y) and kind')
plt.show()
print("\n")
sns.jointplot(data=cancer_data, x="radius_mean", y="area_mean", kind="kde")
plt.title('sns.jointplot() with 2 arguments (x, y) and kind')
plt.show()
print("\n")



# 2k) sns.catplot()
LEN = 600
classes1 = ["Primary" for i in range(int(LEN/3))]
classes2 = ["Secondary" for i in range(int(LEN/3))]
classes3 = ["Tertiary" for i in range(int(LEN/3))]
classes = classes1 + classes2 + classes3
ages1 = list(np.random.randint(7, 13, int(LEN/3)))
ages2 = list(np.random.randint(13, 19, int(LEN/3)))
ages3 = list(np.random.randint(19, 25, int(LEN/3)))
ages = ages1 + ages2 + ages3
heights1 = list(np.random.randint(140, 165, int(LEN/3)))
heights2 = list(np.random.randint(155, 185, int(LEN/3)))
heights3 = list(np.random.randint(155, 195, int(LEN/3)))
heights = heights1 + heights2 + heights3

df = pd.DataFrame({"Class": classes, "Age": ages, "Height": heights})
df = df.sample(frac=1)
print(df.head(8))
sns.catplot(data=df, x="Class", y="Height", kind="box")
plt.show()



# 3a) 3D scatter plot
from mpl_toolkits.mplot3d import axes3d

x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = np.random.randint(10, size=10)
z1 = np.random.randint(10, size=10)
x2 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
y2 = np.random.randint(-10, 0, size=10)
z2 = np.random.randint(10, size=10)

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(x1, y1, z1, c='b', marker='o', label='blue')
ax.scatter(x2, y2, z2, c='g', marker='D', label='green')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')
plt.title("3D Scatter Plot Example")
plt.legend()
plt.tight_layout()
plt.show()




# 3b) 3D bar plot
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

# Data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = np.random.randint(10, size=10)
z = np.zeros(10)
# Positional Arguments
dx = np.ones(10)
dy = np.ones(10)
dz = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ax.bar3d(x, y, z, dx, dy, dz, color='g')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')
plt.title("3D Bar Chart Example")
plt.tight_layout()
plt.show()



# 3c) Wireframe plot
from mpl_toolkits.mplot3d import axes3d
x, y, z = axes3d.get_test_data()
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.plot_wireframe(x, y, z, rstride = 2, cstride = 2)

plt.title("Wireframe Plot Example")
plt.tight_layout()
plt.show()



# 3d) Subplots
def random_plots():
    xs = list(range(20))
    ys = np.random.randint(1, 10, 20)
    return xs, ys
  
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = [0, 1, 2, 3]
y2 = [10, 20, 30, 40]
plt.subplot(1, 2, 1)
plt.plot(x1, y1)
plt.subplot(1, 2, 2)
plt.plot(x2, y2)
plt.show()

fig = plt.figure()
ax1 = plt.subplot2grid((5, 2), (0, 0), rowspan=1, colspan=2)
ax2 = plt.subplot2grid((5, 2), (1, 0), rowspan=3, colspan=2)
ax3 = plt.subplot2grid((5, 2), (4, 0), rowspan=1, colspan=1)
ax4 = plt.subplot2grid((5, 2), (4, 1), rowspan=1, colspan=1)
x, y = random_plots()
ax1.plot(x, y)
x, y = random_plots()
ax2.plot(x, y)
x, y = random_plots()
ax3.plot(x, y)
x, y = random_plots()
ax4.plot(x, y)
plt.tight_layout()
plt.show()




# 3e) Graph objects
from plotly.offline import iplot
import plotly.graph_objs as go

z1 = [10, 10.625, 12.5, 15.625, 20]
z2 = [5.625, 6.25, 8.125, 11.25, 15.625]
z3 = [2.5, 3.125, 5., 8.125, 12.5]
z4 = [0.625, 1.25, 3.125, 6.25, 10.625]
z5 = [0, 0.625, 2.5, 5.625, 10]
data = [go.Contour(z=[z1, z2, z3, z4, z5])]
iplot(data)



# 3f) Interactive visualizations
import altair as alt
from vega_datasets import data
cars = data.cars()
alt.Chart(cars).mark_point().encode(x='Horsepower', y='Miles_per_Gallon', color='Origin').interactive()

sns.scatterplot(data=cars, x='Horsepower', y='Miles_per_Gallon', hue='Origin')
plt.show()
