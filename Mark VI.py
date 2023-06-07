import streamlit as st
import pandas as pd
from fuzzywuzzy import fuzz

# Load the data
data = pd.read_excel(r"C:\Users\Admin\Desktop\Better Data.xlsx")

# Streamlit App
def main():
    # Add Title and Prompt for User Name
    
    def add_bg_from_url():
        st.markdown(
             f"""
             <style>
             .stApp {{
                 background-image: url("https://png.pngtree.com/background/20210709/original/pngtree-ppt-medical-background-blue-border-picture-image_963073.jpg");
                 background-attachment: fixed;
                 background-position: center top;
                 background-size: cover
             }}
             </style>
             """,
             unsafe_allow_html=True
         )

    add_bg_from_url()
    
    
    # Add Title and Prompt for User Name
    st.title("Diagnostic Support System (DSS)")
    user_name = st.text_input("Enter your last name")
    if user_name:
        st.header(f"Welcome Doctor {user_name}")
        st.write("This is DSS. A diagnostic tool to assist your diagnostic process.")
        st.write("Warning - Use this software to inquire a second opinion and not as a primary method to diagnose patients.")

    # Check if the user name is entered
    if user_name:
          
        select = st.button("Show instructions")

        if "show_text" not in st.session_state:
            st.session_state["show_text"] = False

        if select:
            st.session_state["show_text"] = not st.session_state["show_text"]

        if st.session_state["show_text"]:
            st.write("The DSS can help assist you in diagnosing patients by simply inputting the observed symptoms of the patient below, making sure to separate each symptom with a comma. The software will then check the inputted symptoms against all known diseases associated with the symptoms and provide you with the top 5 most relevant diseases based on matching symptoms. Note that many diseases share common symptoms, which is why the disease with the highest number of matching symptoms will appear first. If you feel that the top 5 suggested diseases are not the right fit, simply select 'Yes' to show more diseases based on shared symptoms.")
            st.write("Let's get started!")
            st.caption('Input symptoms below & the top 5 suggested diseases/illnesses will appear.')

        # User Input Code With Prompt "Enter your symptoms (comma-separated)"
        user_input = st.text_input("Enter your symptoms (comma-separated)")

        # Convert User Symptoms From a String To a List
        user_symptoms = [s.strip() for s in user_input.split(",")]

        # Create a column with matching counts for each disease
        data['Match Count'] = data.apply(lambda row: sum(fuzz.partial_ratio(symptom, row['Disease Name']) >= 80
                                                        for symptom in user_symptoms), axis=1)

        # Filter the data to keep only diseases with at least one matching symptom
        matching_data = data[data['Match Count'] > 0]

        # Sort the data by the matching count in descending order
        matching_data = matching_data.sort_values(by='Match Count', ascending=False)

        # To Avoid Information Overload, Set Max Diseases to 5 at a Time
        max_diseases = 5

        # Set Conditions To Display Results
        if not matching_data.empty:
            total_diseases = len(matching_data)
            start_index = 0
            show_more_diseases = True  # Flag to control showing more diseases
            while start_index < total_diseases and show_more_diseases:
                end_index = start_index + max_diseases
                st.write("Most likely diseases based on your symptoms:")
                for _, row in matching_data[start_index:end_index].iterrows():
                    st.write(f"- {row['Disease Name']} ({row['Match Count']} matching symptoms)")
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
