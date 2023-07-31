import matplotlib.pyplot as plt

fig, ax = plt.subplots()
fig = plt.figure(figsize=(10, 10))

car_brand = ['Perodua', 'Hondaa', 'Toyota', 'Proton','BMW']
popularity = [60, 80, 30, 55, 100]
bar_labels = ['Perodua', 'Honda', 'Toyota', 'Proton', 'BMW']
bar_colors = ['tab:pink', 'tab:blue', 'tab:red', 'tab:green', 'tab:orange']

ax.bar(car_brand, popularity, label=bar_labels, color=bar_colors)

ax.set_ylabel('Popularity (%)')
ax.set_title('Popularity by Car Brand')
ax.legend(title='Popularity of Car Brand')

plt.show()