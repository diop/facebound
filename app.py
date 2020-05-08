
import cv2, os
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance

@st.cache
def load_image(img):
    im = Image.open(img)
    return im

FACE_CASCADE_PATH = '/algos/haarcascade_frontalface_default.xml'

face_cascade = cv2.CascadeClassifier(FACE_CASCADE_PATH )
# eye_cascade = cv2.CascadeClassifier('algos/haarcascade_eye.xml')
# smile_cascade = cv2.CascadeClassifier('algos/haarcascade_smile.xml')

def detect_faces(uploaded_image):
    new_img = np.array(uploaded_image.convert('RGB'))
    temp_img = cv2.cvtColor(new_img, 1)
    gray = cv2.cvtColor(temp_img, cv2.COLOR_BGR2GRAY)
    # Detect Face
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw Rectangle
    for (x,y,w,h) in faces:
        cv2.rectangle(temp_img, (x,y), (x+w, y+h), (255,0,0), 2)

    return temp_img, faces

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
            temp_img = cv2.cvtColor(new_img, 1)
            gray = cv2.cvtColor(temp_img, cv2.COLOR_BGR2GRAY)
            st.image(gray)
            # Print on screen
            st.write(gray)
            st.write(new_img)

        if enhance_type == 'Contrast':
            contrast_rate = st.sidebar.slider('Contrtast', 0.5, 3.5)
            enhancer = ImageEnhance.Contrast(uploaded)
            img_output = enhancer.enhance(contrast_rate)
            st.image(img_output)

        if enhance_type == 'Brightness':
            contrast_rate = st.sidebar.slider('Brigthness', 0.5, 3.5)
            enhancer = ImageEnhance.Brightness(uploaded)
            img_output = enhancer.enhance(contrast_rate)
            st.image(img_output)

        if enhance_type == 'Blur':
            blur_rate = st.sidebar.slider('Blur', 0.5, 3.5)
            new_img = np.array(uploaded.convert('RGB'))
            temp_img = cv2.cvtColor(new_img, 1)
            blurred = cv2.GaussianBlur(temp_img, (11,11), blur_rate)
            st.image(blurred)
        # else:
        #     st.image(uploaded)

        # Face Detection
        target = ['Face', 'Smiles', 'Eyes']
        feature_choice = st.sidebar.selectbox('Find Features', target)
        if st.button('Detect Faces'):
            if feature_choice == 'Faces':
                st.write('Print something goda damn it!!!!')
                result_img, result_faces = detect_faces(uploaded)
                st.image(result_img)

                st.success(f'Found {len(result_faces)} faces.')
            

    elif choice == 'About':
        st.subheader('About Facebound')
        st.markdown("Built with Streamlit and OpenCV by [Fodé Diop](https://www.github.com/diop)")
        st.text("© Copyright 2020 Fodé Diop - MIT")
        st.success("Dakar Institute of Technology")

if __name__ == '__main__':
    main()