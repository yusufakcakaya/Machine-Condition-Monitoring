
import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image


st.sidebar.title("Machine Condition Monitoring")

st.sidebar.info("This model is monitoring  conditon of fans.")

models = ["VGG","KNN","SVM","About"]
choice = st.sidebar.selectbox("Menu",models)

if choice == "VGG":
	st.subheader("VGG")

elif choice == "KNN":
	st.subheader("KNN")

elif choice == "SVM":
	st.subheader("SVM")

elif choice == "About":
	st.subheader("About")




def load_image(image_file):
	return Image.open(image_file)
