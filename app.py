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

if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

# Subheader
st.subheader("Example:")

# Button logic
if st.button("Run"):
    # Toggle the state
    st.session_state.button_clicked = not st.session_state.button_clicked

# Display messages based on the state
if st.session_state.button_clicked:
    st.success("Summary: \nAI transforms healthcare, finance, and education by improving efficiency, but challenges like data privacy, ethics, and transparency must be addressed for broader impact.")
else:
    st.info("Text: \nArtificial intelligence (AI) is rapidly transforming various industries, including healthcare, finance, and education. In healthcare, AI-powered systems are used for diagnosing diseases, predicting patient outcomes, and personalizing treatments. The financial sector benefits from AI in fraud detection, algorithmic trading, and risk assessment. In education, AI enhances learning experiences through personalized tutoring systems and automated grading. Despite these advancements, challenges remain, such as ensuring data privacy, addressing ethical concerns, and overcoming the lack of transparency in AI algorithms. As AI continues to evolve, it holds significant potential to improve efficiency, reduce costs, and create innovative solutions across many fields.")
