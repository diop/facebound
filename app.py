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
            st.text('Original Image')
            st.image(uploaded)

    elif choice == 'About':
        st.subheader('About')

if __name__ == '__main__':
    main()