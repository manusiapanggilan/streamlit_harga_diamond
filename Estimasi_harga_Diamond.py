import pickle
import streamlit as st
from PIL import Image

image = Image.open('Diamond.jpg')

st.image(image, caption=' ')

diamond_model = pickle.load(open('estimasi_harga_diamond.sav','rb'))

st.title('Estimasi Harga Diamond')
st.caption(' Muhammad Ziyan Marzuqi | 191351178')


carat = st.number_input ('Input Carat Berlian')
depth = st.number_input('Input Depth Berlian')
table = st.number_input('Input Table Berlian')
x = st.number_input('Input Panjang (mm)')
y = st.number_input('Input Lebar (mm)')
z = st.number_input('Input Kedalaman (mm)')

predict = ''

if st.button('Estimasi Harga Belian') :
    predict = diamond_model.predict([[carat,depth,table,x,y,z]])

    st.write('Estimasi Harga Diamond dalam USD :', predict)
    st.write('Estimasi Harga Diamond dalam IDR :', predict*14964)
    