from select import select
from turtle import onclick
import streamlit as st
from PIL import Image

global selected_model

selected_model = ""



st.title("""
Outliers App
Unsupervised Learning
""")
image = Image.open("movie_rec.jpg")
st.image(image,caption='movie reccomendations')

#st.image(image, caption='Sunrise by the mountains')

# st.write ("""
# # Unsupervised Learning 
# Movie recommedantion challenge

# """+selected_model)

# st.sidebar.selectbox("select model",("model1","model2","model3"))

current_model = st.sidebar.radio("Select a model:",("Gradient descent","Random forest","K Neural Network"))
st.sidebar.button("SELECT")

def update_selected_model(model):
    global selected_model
    selected_model = model