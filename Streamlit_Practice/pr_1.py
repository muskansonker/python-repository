import streamlit as st
#title
st.title('Clothify')
# sub Header
st.subheader('Shop, Smile & Slay')

# Text
#st.text("This is Text")
st.write("Make a Statement with Clothify: Personalized Style and Sustainable Fashion")

# Image
from PIL import Image
img=Image.open('cloth.jpg')
st.image(img,caption='Clothify')

# Colorful Text
st.success('Success')
st.error('Error')
st.warning('Warning')
st.info('Note: Info')
st.exception('Name error(name is not defined)')

#! Help
st.help(help)

#^ Vedio
vid=open('ved.mp4','rb').read()
st.video(vid)

#* side Bar
st.sidebar.header('Menu')


#& Widgets
if st.sidebar.checkbox('About'):
    st.sidebar.text('''Clothing has always been an essential aspect of human life, and it is no secret that it plays a vital role in shaping one's personality and identity. It is not just a mere necessity, but also an expression of style, individuality, and creativity. With that being said, introducing Clothify, a clothing brand that is all about making a statement with your wardrobe.
Clothify is a brand that aims to bring together fashion and comfort to create a unique and personalized experience for its customers. Our brand is built on the foundation of quality, innovation, and creativity. We believe that fashion is not just about following the latest trends, but it is also about creating your own trends and defining your style.
Our clothing line is designed to cater to all types of customers, from the fashion-forward trendsetters to those who value comfort and functionality over style. We offer a wide range of clothing items, including t-shirts, jackets, hoodies, joggers, shorts, and much more. All our products are made using premium quality materials, ensuring durability and comfort.
At Clothify, we understand that fashion is not just limited to clothing, but it also extends to accessories. We offer a range of accessories, including hats, bags, and phone cases, that are designed to complement our clothing line and enhance your overall style
One of the unique aspects of our brand is the option to personalize your clothing items. We offer customization options that allow you to add your own touch to our products. You can choose from a variety of design templates, fonts, and colors to create a personalized item that reflects your individuality and style.
We take pride in our commitment to sustainability and ethical practices. All our products are made using eco-friendly materials, and we ensure that our manufacturing process adheres to ethical standards. We believe in creating a positive impact on society, and we strive to make a difference through our brand.
In conclusion, Clothify is a clothing brand that is all about making a statement with your wardrobe. We offer a unique and personalized experience that caters to all types of customers. Our commitment to quality, innovation, and sustainability sets us apart from the competition. So why wait? Head over to our website and explore our clothing line and accessories to create your own statement-making wardrobe.''')

status=st.sidebar.radio('Show Status',('Active','Inactive'))
if status is 'Active':
    st.sidebar.success('Active')
   
else:
    st.sidebar.warning('Inactive')

category=st.sidebar.selectbox('Category',['Women','Men','Kids','Pet'])
st.sidebar.write('Shop for',category)

price=st.sidebar.multiselect('Price filter',('Under 500','500-1000','1000-5000','Above 5000'))

st.sidebar.slider('Age',1,70)

if st.sidebar.button('Save'):
    st.sidebar.write('Processing... ')

#~ Text Input
subscription=st.sidebar.text_input('Enter your Email for notification')
if '@gmail.com' in subscription:
    st.sidebar.write(f'Confirm your Email id {subscription}')
elif '' in subscription:
    st.sidebar.text('For Know the latest deals first, enter your email address.')
else:
    st.sidebar.write('Incorrect Email')

msg=st.sidebar.text_area('Give feedback')
if msg:
    st.sidebar.write('Thank You!')

#^ Date And time
import datetime
st.sidebar.date_input('Expected Delivery Date',datetime.datetime.now())

#^ Time
import time
st.sidebar.time_input('Expected Delivery Time',datetime.time())

#! display raw code
st.sidebar.text('How to install Sreamlit')
st.sidebar.code('pip install streamlit')

#& echo
with st.echo():
    # how to import sreamlit module
    import streamlit

#* Display JSON
st.json({'module':'Sreamlit', 'version':'1.0'})

#@ Spinner
with st.spinner('Wait a second...'):
    time.sleep(5)
    st.success('Success')

st.balloons()