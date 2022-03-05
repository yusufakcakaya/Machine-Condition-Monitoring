
import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
from os import listdir
from os.path import isfile, join


st.sidebar.title("Machine Condition Monitoring")

st.sidebar.info("This model is monitoring  conditon of fans.")

models = ["VGG","KNN","SVM","About"]
choice = st.sidebar.selectbox("Menu",models)


def load_image(image_file):
	# sourcery skip: inline-immediately-returned-variable
	img = Image.open(image_file)
	return img

prediction_images = [f for f in listdir("/Users/yusufakcakaya/GitHub/Machine-Condition-Monitoring/prediction_images/") 
			if isfile(join("/Users/yusufakcakaya/GitHub/Machine-Condition-Monitoring/prediction_images/", f))]

image_select = st.sidebar.selectbox("Chose an image.", prediction_images)

if choice == "VGG":
	st.subheader("VGG-16")
	image_file = st.file_uploader("Upload Images", type="png",accept_multiple_files = True)

	selected_image = Image.open("/Users/yusufakcakaya/GitHub/Machine-Condition-Monitoring/prediction_images/" + image_select)
	st.image(selected_image, caption="Anomaly Detection", use_column_width=True)

	if image_file is not None:

		file_details = {"filename":image_file.name, "filetype":image_file.type,
                              "filesize":image_file.size}
		st.write(file_details)
		st.image(load_image(image_file),width=250)

elif choice == "KNN":
	st.subheader("KNN")

elif choice == "SVM":
	st.subheader("SVM")

elif choice == "About":
	st.subheader("About")



