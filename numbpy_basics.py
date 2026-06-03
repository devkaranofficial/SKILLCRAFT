import numpy as np

#task 1
array = np.array([5 , 10 , 15 , 20 , 25])

print(np.sum(array))
print(np.max(array))
print(np.min(array))
print(np.mean(array))

#task 2
print(array * 10)

#Mini Project
student_marks = np.array([78,85,92,67,88])
print(f"Highest marks:{np.max(student_marks)}")
print(f"Lowest marks:{np.min(student_marks)}")
print(f"Average Marks:{np.mean(student_marks)}")
print(f"Total Marks:{np.sum(student_marks)}")

#Task 3
marks = np.array([65, 72, 88, 90, 55])

print("~~~~~~~~~~~~~Student Analysis~~~~~~~~~~~~~")
print(f"Average Marks Before Giving Grace marks {np.mean(marks)}")

New_marks = (marks + 5)

print(f"Average Marks after Giving Grace marks {np.mean(New_marks)}")
print(f"Highest marks after giveing grace marks {np.max(New_marks)}")
print(f"Lowest Marks after giving grace marks {np.min(New_marks)}")
