import numpy as np

student_scores = np.array([
    [50, 60, 70, 80],
    [55, 65, 64, 75],
    [88, 99, 77, 66],
    [75, 62, 99, 87]
])

subjects = ["math", "science", "english", "history"]
subject_averages = np.mean(student_scores, axis=0)
max_index = np.argmax(subject_averages)
print("Average scores for each subject:", subject_averages)
print("Subject with highest average:", subjects[max_index])
