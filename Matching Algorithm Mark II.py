import pandas as pd

# Read Excel as a Data Frame
df = pd.read_excel("C:/Users\Admin\Desktop\disease and symptoms (1).xlsx")

# Clean All Unwated Symbols In The Excel File - Note : Use "For" command to create a loop so that it cleans all columns.
for column in df.columns:
    if df[column].dtype == 'object':
        df[column] = df[column].str.replace('"', '')
        df[column] = df[column].str.replace('{', '')
        df[column] = df[column].str.replace('}', '')
        df[column] = df[column].str.replace('[', '')
        df[column] = df[column].str.split(':').str.get(-1) # I used str.get (-1) so that anything after the : is still kept as a value.

# Save The Clean Data Into A New Excel File. Note : This cleaned file was further modified in excel by taking out unnessary data points.
df.to_excel("C:/Users/Admin/Desktop/cleaned_data.xlsx", index=False)

# Creating the Matching Algorithm
data = pd.read_excel(r"C:\Users\Admin\Desktop\Better Data.xlsx")

# # There Are Many Coloumns That Start With Symptoms, All Of Them Should Be Considered.
diseases = data['Disease Name']
symptoms_columns = [col for col in data.columns if col.startswith('Symptoms')]

# User Input Code With Prompt "Enter your symptoms (comma-separated)"
user_input = input("Please enter your symptoms separated by commas and no spaces: ")

# Convert User Symptoms From a String To a List, Split Function Ensures Gaps and Spaces Are Not Considered.
user_symptoms = [s.strip() for s in user_input.split(",")]

# Create Loops To Ensure All User Inputted Symptoms Are Accociated With A Disease.
matching_diseases = []
for i, row in data.iterrows():
    disease_symptoms = row[symptoms_columns].dropna().tolist()
    common_symptoms = set(disease_symptoms) & set(user_symptoms)
    if len(common_symptoms) > 0:
        matching_diseases.append((row['Disease Name'], len(common_symptoms)))

# To Avoid Information Overload, Set Max Diseases to 5 at a Time.
max_diseases = 5

# Set Condtions To Display Results | Len - Returns the number of items in a container | Lambda Used For Matching_Disease Recall So as to Avoid Repeating Code.
if len(matching_diseases) > 0:
    matching_diseases.sort(key=lambda x: x[1], reverse=True)
    total_diseases = len(matching_diseases)
    start_index = 0
    while start_index < total_diseases:
        end_index = start_index + max_diseases
        print("Most likely diseases based on your symptoms:")
        for i, (disease, match_count) in enumerate(matching_diseases[start_index:end_index], start=1): # Note : enumerate fuction keeps tracks how many loops in a loop.
            print(f"- {disease} ({match_count} matching symptoms)")
        if end_index < total_diseases:
            choice = input("Show more diseases? (yes/no): ").lower() # We Cannot Limit The Possibilties of Potential Diseases, So We Have To Allow The User To See All Possible Diseases.
            if choice.lower() != "yes":                     #.lower(), the above fuction allows the user to type symptoms in both Lower and Upper case.
                break
        else:
            print("No more diseases to display.")
        start_index = end_index
else:
    print("No matching diseases found.")

print("Thank you for using our services.")
