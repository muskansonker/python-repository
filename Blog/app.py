import streamlit as st
from streamlit_option_menu import option_menu


# page config
st.set_page_config(
    page_title='Writlico',
    page_icon='📃',
    layout='wide'
)

st.sidebar.title('Writlico')
#st.image('Blog/img.jpg', use_column_width=True)

with st.sidebar:
    selected = option_menu("Main Menu", ['My Blogs', 'Settings'], 
        icons=["list-task" ,'gear'], menu_icon="house", default_index=0)
    selected

if selected == 'My Blogs':
    st.sidebar.selectbox(label='Select the option',
        options=['Upload Blog','View Blog','Delete Blog'])
if selected == 'Settings':
    st.sidebar.selectbox(label='Select the option',
        options=['View Profile','Account Settings'])
    
