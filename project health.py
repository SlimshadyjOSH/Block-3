import pandas as pd
# Read the Excel file into a DataFrame
df = pd.read_excel("C:/Users\Admin\Desktop\disease and symptoms (1).xlsx")

# Clean all string columns
for column in df.columns:
    if df[column].dtype == 'object':
        df[column] = df[column].str.replace('"', '')
        df[column] = df[column].str.replace('{', '')
        df[column] = df[column].str.replace('}', '')
        df[column] = df[column].str.replace('[', '')
        df[column] = df[column].str.split(':').str.get(-1)

# Save the cleaned data to a new Excel file
df.to_excel("C:/Users\Admin\Desktop\cleaned_data.xlsx", index=False)

# Creating The Matching Algorithm.
data = pd.read_excel(r"C:\Users\Admin\Desktop\Better Data.xlsx")

# There Are Many Coloumns That Start With Symptoms, All Of Them Should Be Considered.
diseases = data['Disease Name']
symptoms_columns = [col for col in data.columns if col.startswith('Symptoms')]

# User Input Code With Prompt "Enter your symptoms (comma-separated)"
user_input = input("Enter your symptoms (comma-separated): ")

# Convert User Symptoms From a String To a List, Split Function Ensures Gaps and Spaces Are Not Considered.
user_symptoms = [s.strip() for s in user_input.split(",")]

# Create Loops To Ensure All User Inputted Symptoms Are Accociated With A Disease.
matching_diseases = []
for i, d in enumerate(diseases):
    disease_symptoms = []
    for col in symptoms_columns:
        symptom = data.loc[i, col]
        if isinstance(symptom, str):
            disease_symptoms.append(symptom)
    common_symptoms = set(disease_symptoms) & set(user_symptoms)
    if len(common_symptoms) > 0:
        matching_diseases.append((d, len(common_symptoms)))

# Set Condtions To Display Results | Len - Returns the number of items in a container | Lambda Used For Matching_Disease Recall ( To save space)
if len(matching_diseases) > 0:
    matching_diseases.sort(key=lambda x: x[1], reverse=True)
    print("Possible diseases based on your symptoms:")
    for disease, match_count in matching_diseases:
        print(f"- {disease} ({match_count} matching symptoms)")
else:
    print("No matching diseases found.")




