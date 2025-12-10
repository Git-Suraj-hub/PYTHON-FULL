import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create a sample dataset
data = {
    'Student': ['Aman', 'Bhavna', 'Chirag', 'Vansh', 'Eshan'],
    'Math': [78, 85, 92, 70, 88],
    'Science': [80, 82, 89, 75, 90],
    'English': [85, 78, 88, 72, 84]
}

# Step 2: Convert into DataFrame
df = pd.DataFrame(data)

# Step 3: Calculate subject-wise average marks
subject_averages = df[['Math', 'Science', 'English']].mean()

# Step 4: Plot the bar chart
plt.figure(figsize=(6, 4))
subject_averages.plot(kind='bar', color=['#4C72B0', '#55A868', '#C44E52'])
plt.title('Average Marks per Subject')
plt.xlabel('Subjects')
plt.ylabel('Average Marks')
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Step 5: Show and save the chart
plt.savefig("student_subject_performance.png", bbox_inches='tight')
plt.show()

print("✅ Chart saved as 'student_subject_performance.png'")
