import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.set_page_config(page_title="Word Cloud Generator", layout="centered")
st.title("🌀 Word Cloud Generator")

st.write("Enter some text below and click 'Generate Word Cloud' to visualize it.")

# Text input area
text_input = st.text_area("Enter your text here:", height=200)

# Generate button
if st.button("Generate Word Cloud"):
    if text_input.strip():
        # Generate the word cloud
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_input)
        
        # Display the word cloud
        fig, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)
    else:
        st.warning("Please enter some text to generate a word cloud.")
