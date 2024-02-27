import streamlit as st

def display_form():
    # Add elements to the form using Streamlit widgets
    st.header("PREDICTION")
    
    # Input field
    user_input = st.text_input("Model prediction")
    
   
    selected_option = st.selectbox("Select an option", ["Regression model", "Random forrest", "Decision Tree"])
    
    #  Button to submit the form
    if st.button("Submit"):
        # Display the submitted values
        st.success(f"Name: {user_input}, Selected Option: {selected_option}")

if __name__ == "__main__":
    # Create a three-column layout
    col1, col2, col3 = st.columns(3)

    # Place the form in the middle column
    with col2:
        display_form()

    # Function to load the first model
@st.cache_data
def load_model1():
    # Replace this with your actual code to load model1
    # Example: model1 = load_model("model1_path")
    model1 = "models/encoder.joblib"
    return model1

# Function to load the second model
@st.cache
def load_model2():
    # Replace this with your actual code to load model2
    # Example: model2 = load_model("model2_path")
    model2 = "models/finished_model.joblib"
    return model2

# Main Streamlit app
def main():
    # Load the models
    model1 = load_model1()
    model2 = load_model2()

    # Display information about the loaded models
    st.write("Model 1:", model1)
    st.write("Model 2:", model2)

# Run the Streamlit app
if __name__ == "__main__":
    main()