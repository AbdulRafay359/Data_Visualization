import matplotlib.pyplot as plt
'''
hours_studied = [1,2,3,4,5,6,7,8]
exam_score = [50,55,60,65,70,75,80,85]

plt.scatter(hours_studied, exam_score, color = 'orange', marker = '^', label ='Student Data')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.title('Relatinship Between Study Time And Exam Score')
plt.legend()
plt.grid(True)
plt.show()

'''
plt.scatter([1,2,3],[50,60,70], color = 'Blue',label = 'Class A')
plt.scatter([1,2,3],[45,40,35], color = 'Orange',label = 'Class B')

plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.title('Relatinship Between Two Classes')
plt.legend()
plt.grid(True)
plt.show()
