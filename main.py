import streamlit as st
from PIL import Image
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.models import *
import matplotlib.pyplot as plt



def predict(path):

    img = image.load_img(path, target_size=(432, 288))
    # Preprocessing the image
    pp_img = image.img_to_array(img)
    pp_img = pp_img/255
    pp_img = np.expand_dims(pp_img, axis=0)
    #Load Model
    saved_model = load_model("mel.h5")
    #predict
    img_pred= saved_model.predict(pp_img)
    
    if img_pred[0][0] >= 0.5: 
        pred = ('Abnormal')
    else: 
        pred = ('Normal')
    
    return  pred



# sourcery skip: use-named-expression
uploaded_file = st.file_uploader("Upload an image", type="png")
img = Image.open(uploaded_file)

if img is not None:
    st.image(img, caption='Uploaded Image.', use_column_width=True)
    
    classify = st.button("classify image")
    if classify :
        st.write("")
        st.write("Classifying...")
        label = predict(img)
else:
    st.write("Paste Image URL")
