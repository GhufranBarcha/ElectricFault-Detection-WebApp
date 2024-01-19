import streamlit as st
import joblib
import pandas as pd

st.markdown("""
<style>
    button.step-up {display: none;}
    button.step-down {display: none;}
    div[data-baseweb] {border-radius: 4px;}
</style>""",
unsafe_allow_html=True)

# Load the trained model and dictionary
trainedModel, dictValue = joblib.load("./trainedModel.pkl")
dictVal = {j: i for i, j in dictValue.items()}

# Streamlit app
def main():
    st.title("Fault Prediction App")
    with st.container(border=True):
            
        # Create a layout with three columns and two rows
        col1, col2, col3 = st.columns(3)

        # First row of input values
        with col1:
            X = st.text_input("X value", value="0.0")
        with col2:
            Y = st.text_input("Y value", value="0.0")
        with col3:
            Z = st.text_input("Z value", value="0.0")

        # Second row of input values
        with col1:
            Sound = st.text_input("Sound value", value="0.0")
        with col2:
            Current = st.text_input("Current (A) value", value="0.0")
    
    # Predict button
    if st.button("Predict"):
        try:# Convert input values to float
            X = float(X)
            Y = float(Y)
            Z = float(Z)
            Sound = float(Sound)
            Current = float(Current)
        except Exception as e:
            st.warning("Please enter Numerical input.")   

        if X == Y == Z == Sound == Current == 0:
            st.warning("Please enter non-zero values for at least one input.")
        else:
            # Create a DataFrame with input values
            data = {"X": [X], "Y": [Y], "Z": [Z], "Sound": [Sound], "Current (A)": [Current]}
            df0 = pd.DataFrame(data)
            st.dataframe(df0, width=3000)
            
            # Predict
            try:
                prediction = trainedModel.predict(df0)
                fault_prediction = dictVal[prediction[0]]
                st.subheader("Prediction Result:")
                st.success(f"The predicted fault is: {fault_prediction}")
            except Exception as e:
                st.error(f"An error occurred during prediction: {str(e)}")

if __name__ == "__main__":
    main()

