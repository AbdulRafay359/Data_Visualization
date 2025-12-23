import matplotlib.pyplot as plt

regions = ['North','East','West','South']
revenue = [1000,1500,2000,1600]

plt.pie(revenue,labels = regions,autopct = '%1.1f%%',colors = ['Gold','Skyblue','Lightgreen','Coral'])
plt.title('Revenue Contribution By Regions')
plt.show()