import streamlit as st

st.title("Streamlit Tutorial App")
st.write("This is my new app")
button1 = st.button("Click me")
if button1:
    st.write("Clicked the button")

like = st.checkbox("Do you like this app?")
button2 = st.button('Submit')
if button2:
    if like:
        st.write('Thanks')
    else:
        st.write('I am sorry.')


st.header('Start of the Radio Button Section')
animal = st.radio("What is your favourite animal?", ("Lion", "Tiger", "Bear"))
button3 = st.button('Submit Animal')
if button3:
    st.write('Animal')
    if animal == "Lion":
        st.write('ROAR!')


st.header('Start of the Selectbox Section')
animal2 = st.selectbox("What is your favourite animal 2?", ("Lion", "Tiger", "Bear"))
button4 = st.button('Submit Animal 2')
if button4:
    st.write('Animal')
    if animal2 == "Lion":
        st.write('ROAR!')


st.header("Start of the Multiselection Section")
options = st.multiselect("What animal do you like?", ["Lion", "Tiger", "Bear"])
button5 = st.button("Print Animal/s")
if button5:
    st.write(options)