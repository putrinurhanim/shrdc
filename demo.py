import streamlit as st
st.write("This is Day 4 of learning DA with Python")
st.write("How do i stop this session")


st.write("This is write!")
st.header("This is header!")
st.subheader("This is subheader!")
st.caption("This is caption!")

st.markdown("*Streamlit* is **really** ***cool***.")

st.markdown(''' :red[Streamlit ] :orange[is ]:green[ fun] ''')

st.markdown("Here's a bouquet &mdash;\:tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

st.success("good")
st.warning("bad")
st.info("info")
st.error("Error!")

new_title = '<p style="font-family:sans-serif;color:Pink; font-size: 24px;">This is advanced font manipulation!</p>'

st.markdown(new_title, unsafe_allow_html=True)

st.markdown("*Italic*")
st.markdown("**Bold**")
st.markdown("***Bold Italic***")

st.selectbox("Kuala Lumpur is located at",['Malaysia', 'Turkey', 'UK'])
st.multiselect("Select 2 states",['Pahang','Johor','Selangor'])

st.button("Click Here to Proceed")

st.slider("Select the length of stay", 1,10, value=3)

number = st.number_input("Insert a number", value=None)
st.write("The current number is ", number)

number = st.number_input("Insert a number",value=None,placeholder="Type a number...")
st.write("The current number is ", number)

#st.text("Type a number below:")
#number = st.number_input("Insert a number", value=0)  # You can change the default value here
#st.write("The current number is", number)

from PIL import Image
im = Image.open('shrdc_logo.png')
st.image(im, width=300)

import pandas as pd
df = pd.read_excel('sampledata.xlsx')
st.dataframe(df)

st.bar_chart(df, x="Location", y="Income")
st.line_chart(df, x="Household", y="Income")
st.scatter_chart(df, x="Household", y="Income")

#import altair as alt
#scatter_plot = alt.Chart(df).mark_circle().encode(x='Household',y='Income')
#st.altair_chart(scatter_plot, use_container_width=True)

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

col4, col5 = st.columns(2)

with col4:
    st.slider("Select the length of stay", 1,10)

with col5:
    st.write(" ")
