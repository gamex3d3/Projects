import pandas as pd

# Data for the target score spreadsheet
data_targets = {
    'Subjects': ['Basic Electricity', 'Biology', 'Chemistry', 'Civic Education', 'Diction', 'Economics',
                 'English Language', 'Further Mathematics', 'ICT', 'Music', 'Photography', 'Physics', 'Mathematics'],
    'Current Cumulative Score': [81.6, 83.2, 85.3, 91.4, 89.3, 95.9, 88.2, 93.5, 91.2, 83, 96, 83.7, 91.3],
    'Target Score for 91 Average': [85, 88, 90, 93, 92, 96, 91, 95, 93, 88, 97, 89, 94]
}

# Creating DataFrame for target scores
df_targets = pd.DataFrame(data_targets)

print(df_targets)