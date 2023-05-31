import streamlit as st
import pandas as pd
from fuzzywuzzy import fuzz

# Function to clean unwanted symbols in the Excel file
def clean_data(df):
    # Code for cleaning the data
    cleaned_df = df  # Placeholder, replace with actual cleaning logic
    return cleaned_df

# Read Excel as a Data Frame
df = pd.read_excel("C:/Users/Admin/Desktop/disease and symptoms (1).xlsx")

# Clean All Unwanted Symbols In The Excel File
cleaned_df = clean_data(df)

# Save The Clean Data Into A New Excel File
cleaned_df.to_excel("C:/Users/Admin/Desktop/cleaned_data.xlsx", index=False)

# Creating the Matching Algorithm
data = pd.read_excel(r"C:\Users\Admin\Desktop\Better Data.xlsx")

# There Are Many Columns That Start With Symptoms, All Of Them Should Be Considered.
diseases = data['Disease Name']
symptoms_columns = [col for col in data.columns if col.startswith('Symptoms')]

# Streamlit App
def main():
    # Add Title and Prompt for User Name
    st.title("Diagnostic Support System")
    user_name = st.text_input("Enter your last name")

    # Check if the user name is entered
    if user_name:
        # Add Title with User Name
        st.title(f"Welcome Doctor {user_name}")

        # User Input Code With Prompt "Enter your symptoms (comma-separated)"
        user_input = st.text_input("Enter your symptoms (comma-separated)")

        # Convert User Symptoms From a String To a List
        user_symptoms = [s.strip() for s in user_input.split(",")]

        # Create Loops To Ensure All User Inputted Symptoms Are Associated With A Disease
        matching_diseases = []
        for i, row in data.iterrows():
            disease_symptoms = row[symptoms_columns].dropna().tolist()
            common_symptoms = set(disease_symptoms) & set(user_symptoms)
            if len(common_symptoms) > 0:
                match_count = sum(fuzz.partial_ratio(symptom, disease) >= 80 for symptom in user_symptoms for disease in diseases)
                matching_diseases.append((row['Disease Name'], match_count))

        # To Avoid Information Overload, Set Max Diseases to 5 at a Time
        max_diseases = 5

        # Set Conditions To Display Results
        if len(matching_diseases) > 0:
            matching_diseases.sort(key=lambda x: x[1], reverse=True)
            total_diseases = len(matching_diseases)
            start_index = 0
            show_more_diseases = True  # Flag to control showing more diseases
            while start_index < total_diseases and show_more_diseases:
                end_index = start_index + max_diseases
                st.write("Most likely diseases based on your symptoms:")
                for i, (disease, match_count) in enumerate(matching_diseases[start_index:end_index], start=1):
                    st.write(f"- {disease} ({match_count} matching symptoms)")
                if end_index < total_diseases:
                    choice = st.selectbox("Show more diseases?", (None, "Yes", "No"), key=f"choice-{start_index}")
                    if choice == "Yes":
                        show_more_diseases = True  # Set flag to True to show more diseases
                    else:
                        show_more_diseases = False  # Set flag to False to stop showing more diseases
                        st.write("Thank you for using our services.")
                else:
                    st.write("No more diseases to display.")
                start_index = end_index
        else:
            st.write("No matching diseases found.")

    # Display a message if the user name is not entered
    else:
        st.write("Please enter your name.")

if __name__ == "__main__":
    main()
