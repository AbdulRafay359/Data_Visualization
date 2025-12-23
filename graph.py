import matplotlib.pyplot as plt
"""
x_axis = [1,2,3,4] #horozontal axis
y_axis = [10,20,15,25] #vertical axis

plt.plot(x_axis,y_axis)
plt.show()

# 1 = 10; 2 = 20; 3 = 15; 4 = 25

"""
x = [1,2,3,4,5] #horizontal
y = [10,15,7,20,12] #vertical

plt.plot(x,y, color = 'Green', linestyle = '--', linewidth = 2 , marker = 'o', label = '2025 Sales!!!')

plt.title('Bakery Sales This Week!', color = 'Green')

plt.xlabel('Days of Week', color = 'Blue', fontsize = 12)
plt.ylabel('Sales per Day', color = 'Red', fontsize = 12)

plt.legend(loc = 'upper left', fontsize = 12)
plt.grid(color = 'gray', linestyle = ':', linewidth = 1)

plt.xlim(1,5)
plt.ylim(0,50)

plt.xticks([1,2,3,4,5],['D1','D2','D3','D4','D5'])

plt.show()