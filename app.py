import streamlit as st

# Title
st.title("Text Summarization using BERT2BERT Encoder Decoder Model")

# Subheader
st.subheader("Output:")

# Text
st.write("Model Trained Successfully!")

# Text
st.write("Accuracy:\nTraining Loss - Precision - Recall - F-Measure")

# Text
st.write("Training Loss - Precision - Recall - F-Measure")

# Text
st.write("7.481323 - 7.709305 - 0.004800 - 0.013600 - 0.007000")

# Display Image
st.image("comparison.png", caption="Comparison with Other Models", use_column_width=True)
