import streamlit as st
from orm import Category,Product,create_engine
from sqlalchemy.orm import sessionmaker

# boilerplate code
def opendb():
    engine=create_engine('sqlite:///db.sqlite',echo=True)
    Session=sessionmaker(bind=engine)
    session=Session()
    return session

def closedb(session):
    session.commit() #! save changes
    session.close()
     
#! category add fun
def add_category(name):
    db=opendb()
    obj=Category(name=name)
    db.add(obj)
    closedb(db)

def view_categories():
    db=opendb()
    categories=db.query(Category).all()
    return categories

st.title("SQLAlchemy Demo")

#! add category
form=st.form(key='add_category')
name=form.text_input(label='Category Name')
submit=form.form_submit_button(label='Add Category')
if submit:
    add_category(name)

#! view category
if st.checkbox(label='View Category'):
    for category in view_categories():
        st.info(f' {category.id} {category.name}')

#! add product
form2=st.form(key='add_product')
name=form2.text_input(label='Product Name')
category=form2.text_input(label='Category ID')
submit=form2.form_submit_button(label='Add Product')
if submit:
    add_product(name,category)