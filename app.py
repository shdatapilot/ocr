import streamlit as st
from paddleocr import PaddleOCR, draw_ocr
from PIL import Image
import numpy as np

st.title("OCR")
st.write()

ocr = PaddleOCR(use_angle_cls=True, lang='en')
print("loading image")
st.write("Load Image")
uploaded_file = st.file_uploader("Choose an image...")
if uploaded_file is not None:
    img_ = Image.open(uploaded_file).convert('RGB')
    image_ = np.array(img_)  # convert image to numpy array for ocr
    # st.image(image_, caption='Uploaded Image.', use_column_width=True) # Display image on streamlit
    st.write(" Extracting Text from Image.......")
    result = ocr.ocr(image_, cls=True)

    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    lang_url = './AAntiCorona-L3Ax3.ttf'
    im_show = draw_ocr(image_, boxes, txts, scores,
                       font_path=lang_url)  # draw detection result
    im_show = Image.fromarray(im_show)
    st.image(im_show, caption='OCR Result', use_column_width=True)
