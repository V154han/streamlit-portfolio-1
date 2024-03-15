import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Setting Page Configuration
st.set_page_config(page_title='My Webpage', page_icon=':imp:', layout = 'wide')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css('style.css\style.css')

#Load Assets
lottie_coding_tech = 'https://lottie.host/a7505417-be8b-4749-863f-37b66388d5fa/QPEup9FLA7.json'
lottie_coding_bank = 'https://lottie.host/98dbe694-a711-4938-abd2-8f16e3ec4f58/s75RWiWuk8.json'
lottie_coding_form = 'https://lottie.host/218866c2-b858-423d-bb32-18545e5d2a26/5vXeLY78Uq.json'


# Header Section
with st.container():
    st.subheader('Hi, I am Visahan Sritharan')
    st.title('A Machine Learning Engineer from London')
    st.write('I am using Python and Streamlit to build a website')
    st.write('[View my profile at >](https://v154han.github.io/Capstone-Project-1/)')

# What i do
with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('Who am I')
        st.write('My name is Visahan Sritharan and I am currently working as a Machine Learning Engineer however I have also worked in the field of Data Engineering and Data Analytics. With experience in Python, SQL, Snowflake and HTML, I am always looking to expand my skillset and delve further into the world of technology. Having worked in a vast array of projects including a Banking Churn project alongside analysing data from a Microsoft Form, I would describe myself as a keen learning and am always looking for opportunities to undertake new challenges')

    with right_column:
        st_lottie(lottie_coding_tech, height=300, key='coding')

# Showing Work
with st.container():
    st.write('---')
    st.header('My Projects')
    st.write('##')
    image_column, text_column = st.columns((1,2))
    with image_column:
        st_lottie(lottie_coding_bank, height=200)
    with text_column:
        st.subheader('Banking Churn Project')
        st.write('''
        Produced a Machine Learning Algorithm to predict if a customer is likely to churn or not. This was done by:
        - Running different Machine Learning models to see which produced the highest accuracy
        - Minimising the false positives as we do not want the customer to churn whilst we think think that theyt won't
        - Using PowerBI to present our findings
        ''')

    with st.container():
        st.write('##')
        text_column, image_column = st.columns((1,2))
        with text_column:
            st.subheader('Consultant Journal Project')
            st.write('''
            Within this project, we parsed data from Microsoft Forms to provide Data Analytics into the constltant training experience. This was done by:
            - Using Snowflake to carry out any ELT transformations and producing a bronze, silver and gold layer.
            - Cleared out any unwanted characters as well as separating out all the data into a useful format
            - Performed any relevant aggregations which would aid in analytics
            - Used Thoughspot to produce relevant graphs
            ''')
        with image_column:
            st_lottie(lottie_coding_form, height=200, width=600)


    # Contact Form
    with st.container():
        st.write('---')
        st.header('Get in Touch With Me!')

        contact_form = '''
        <form action="https://formsubmit.co/visahan2001@yahoo.co.uk" method="POST">
        
        <input type='hidden' name='_captcha' value='false'>
            <input type="text" name="name" placeholder= 'Your name' required>
            <input type="email" name="email" placeholder= 'Your email' required>
            <textarea name='message' placeholder='Your message here' required></textarea>
            <button type="submit">Send</button>
        </form>
        '''

        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()
            

