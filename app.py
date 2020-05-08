import streamlit as st
import cv2
from PIL import Image, ImageEnhance
import numpy as np
import os

@st.cache
def load_image(img):
    im = Image.open(img)
    return im

def main():
    '''
    Face Detection App
    '''

    st.title('Facebound')
    st.text('by Fodé Diop')

    options = ['Detection', 'About']
    choice = st.sidebar.selectbox('Select Option', options)

    if choice == 'Detection':
        st.subheader('Face Detection')

        image_file = st.file_uploader('Upload Image', type=['jpg', 'png', 'jpeg'])

        if image_file is not None:
            uploaded = Image.open(image_file)
            # st.write(type(uploaded))
            st.text('Original Image')
            st.image(uploaded)

        enhance_type = st.sidebar.radio('Enhance Type', ['Original', 'Grayscale', 'Contrast', 'Brightness', 'Blur'])
        if enhance_type == 'Grayscale':
            new_img = np.array(uploaded.convert('RGB'))
            mid_img = cv2.cvtColor(new_img, 1)
            gray = cv2.cvtColor(mid_img, cv2.COLOR_BGR2GRAY)
            st.image(gray)
            # st.write(gray)
            # st.write(new_img)


    elif choice == 'About':
        st.subheader('About')

if __name__ == '__main__':
    main()