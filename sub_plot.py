import matplotlib.pyplot as plt


fig , ax = plt.subplots(2,3, figsize = (10,5))
fig.suptitle('Comparison of line and Bar Chart')

x1 = [1,2,3,4]
y1 = [10,15,13,8]

x2 = [1,2,3,4]
y2 = [25,15,10,18]

scores = [50,60,70,80,90,95,94,93,76,64,65,66,67,78,79,81,85,49,57,62]

regions = ['North','East','West','South']
revenue = [1000,1500,2000,1600]

ax[0][0].plot(x1,y1,color = 'green',marker = 'o')
ax[0][0].set_title('Line Plot')
ax[0][0].grid(color='black', linestyle='--', linewidth=1)

ax[0][1].bar(x2,y2,color = 'Orange')
ax[0][1].set_title('Bar Plot')
ax[0][1].grid(color='gray', linestyle='--', linewidth=1)


ax[0][2].hist(scores , bins = 5,color = 'Skyblue',edgecolor = 'Black')
ax[0][2].set_title('Histogram Plot')
ax[0][2].grid(color='gray', linestyle='--', linewidth=1)

ax[1][0].pie(revenue,labels = regions,autopct = '%1.1f%%',colors = ['Gold','Skyblue','Lightgreen','Coral'])
ax[1][0].set_title('Pie Plot')
ax[1][0].grid(color='gray', linestyle='--', linewidth=1)

ax[1][1].scatter([1,2,3],[50,60,70], color = 'Blue',label = 'Class A')
ax[1][1].scatter([1,2,3],[45,40,35], color = 'Orange',label = 'Class B')
ax[1][1].set_xlabel('Hours Studied')
ax[1][1].set_ylabel('Exam Score')
ax[1][1].set_title('Relatinship Between Two Classes')
ax[1][1].grid(True)


plt.tight_layout()
plt.savefig('Dashboards.png', dpi =300, bbox_inches = 'tight')
plt.show()