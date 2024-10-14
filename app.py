import streamlit as st
import os
from code_improve_class import model_improve

# Streamlit app title
st.title("Python Script Code Improver")

# File uploader for the user to upload a Python script
uploaded_file = st.file_uploader("Upload a Python script (.py)", type="py")

# Choose between Standard or Improve option
improve_option = st.radio(
    "Select Improvement Type:",
    ("Standard Option (Basic Improvements)", "Improve Option (User Suggestions)")
)
submit = st.button(label="submit improvements")
# If the user chooses "Improve Option", display a text area for user suggestions
user_suggestions = None
if improve_option == "Improve Option (User Suggestions)":
    user_suggestions = st.text_area(
        "Enter additional suggestions or next steps to improve the code (optional):"
    )

if submit and uploaded_file is not None:
    # Read the contents of the uploaded file
    file_content = uploaded_file.read().decode("utf-8")

    # Create two columns for the original and improved code
    col1, col2 = st.columns(2)

    # Column 1: Display the original code
    with col1:
        st.subheader("Original Code")
        st.code(file_content, language="python")

    # Improve the uploaded Python code using the model
    improve_model = model_improve(file_content, user_suggestions=user_suggestions)
    improved_code = improve_model.model_first_answer()

    # Column 2: Display the improved code
    with col2:
        # Download button for improved code
        improved_file_name = uploaded_file.name.replace(".py", "_improved.py")
        st.download_button(
            label="Download Improved Script",
            data=improved_code,
            file_name=improved_file_name,
            mime="text/x-python"
        )

        # Display the improved code
        st.subheader("Improved Code")
        st.code(improved_code, language="python")
