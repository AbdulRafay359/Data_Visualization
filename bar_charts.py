import matplotlib.pyplot as plt

product = ['Bread','Eggs','Milk','Jam','Nutella']
sales = [1000,2000,1800,1500,1700]

plt.bar(product,sales,color = 'Orange',label = 'Sales 2025')
plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Product Sale Comparison!!')
plt.legend()
plt.grid(color = 'Gray',linestyle = ':',linewidth = 0.5)
plt.show()