import streamlit as st
st.write("# This is my face")
from PIL import Image
face = Image.open('myface.jpg')
face
st.image(face, caption='average my face')
st.write("# but this...")
deep = Image.open('deep.jpg')
deep
st.image(deep, caption="don't worry it's just my face")