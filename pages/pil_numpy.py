import streamlit as st
from PIL import Image
import numpy as np

st.header('camera_input()')
st.subheader('PIL, Numpy 라이브러리')

file_buffer = st.camera_input("사진을 찍을 수 있습니다.")

if file_buffer is not None:
    image_pil = Image.open(file_buffer)

    # To convert PIL Image to numpy array:
    image_array = np.array(image_pil)

    # image_array의 타입 출력
    # <class 'numpy.ndarray'>
    st.write(type(image_array))

    # image_array의 shape 출력
    # (height, width, channels)
    st.write(image_array.shape)
