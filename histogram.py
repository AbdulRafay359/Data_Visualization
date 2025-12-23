import matplotlib.pyplot as plt

scores = [50,60,70,80,90,95,94,93,76,64,65,66,67,78,79,81,85,49,57,62]

plt.hist(scores , bins = 5,color = 'Skyblue',edgecolor = 'Black') 
plt.xlabel('Score Range')
plt.ylabel('Number of Students')
plt.title('Score Distribution of Students')
plt.show()