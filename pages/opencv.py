import streamlit as st
import cv2
import numpy as np

st.header('camera_input()')
st.subheader('OpenCV 라이브러리')

file_buffer = st.camera_input("사진을 찍을 수 있습니다.")

if file_buffer is not None:
    bytes_data = file_buffer.getvalue()
    # openCV로 이미지 버퍼 읽기
    image_cv2 = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR) 

    # cv2_img의 타입 출력
    # <class 'numpy.ndarray'>
    st.write(type(image_cv2))

    # cv2_img의 shape 출력
    # (height, width, channels)
    st.write(image_cv2.shape)