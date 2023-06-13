import streamlit as st
import tensorflow as tf

st.header('camera_input()')
st.subheader('TensorFlow 라이브러리')

file_buffer = st.camera_input("사진을 찍을 수 있습니다.")

if file_buffer is not None:
    bytes_data = file_buffer.getvalue()
    image_tensor = tf.io.decode_image(bytes_data, channels=3)

    # img_tensor의 타입 출력
    # <class 'tensorflow.python.framework.ops.EagerTensor'>
    st.write(type(image_tensor))

    # img_tensor의 shape 출력 
    # (height, width, channels)
    st.write(image_tensor.shape)