import streamlit as st

# Title
st.title("Text Summarization using BERT2BERT Encoder Decoder Model")

# Subheader
st.subheader("Model Info:")

# Text
st.write("Model Trained Successfully with following Rouge Scores: ")

# Text
st.write("Training Loss - Precision - Recall - F-Measure")

# Text
st.write("7.481323 - 7.709305 - 0.004800 - 0.013600 - 0.007000")

# Display Image
st.image("comparison.png", caption="Comparison with Other Models", use_column_width=True)

# Subheader
st.subheader("Example:")

if st.button("Run"):
    st.success("Summary")
else:
    st.info("Text")
