import streamlit as st
import torch
import numpy as np

st.header('camera_input()')
st.subheader('PyTorch 라이브러리')

file_buffer = st.camera_input("사진을 찍을 수 있습니다.")

if file_buffer is not None:
    bytes_data = file_buffer.getvalue()
    image_torch = torch.ops.image.decode_image(
        torch.from_numpy(np.frombuffer(bytes_data, np.uint8)), 3
    )

    # image_torch의 타입 출력
    # <class 'torch.Tensor'>
    st.write(type(image_torch))

    # image_torch의 shape 출력  
    # torch.Size([channels, height, width])
    st.write(image_torch.shape)