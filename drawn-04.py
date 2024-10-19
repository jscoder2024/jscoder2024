import matplotlib.pyplot as plt

fruits = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries']
quantities = [30, 20, 15, 10, 5]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']
plt.figure(figsize=(8, 8))
plt.pie(quantities, labels=fruits, colors=colors, autopct='%1.1f%%',
startangle=140, pctdistance=0.85, wedgeprops={'edgecolor': 'black'})
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title('Proportions of Different Fruits in the Basket', fontsize=15)
plt.axis('equal')
plt.show()
