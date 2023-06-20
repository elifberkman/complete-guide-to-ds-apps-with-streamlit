# Hash the passwords
# source: https://blog.streamlit.io/streamlit-authenticator-part-1-adding-an-authentication-component-to-your-app/

# import streamlit_authenticator as stauth
#
# hashed_passwords = stauth.Hasher(['abc', 'def']).generate()
# print(hashed_passwords)

# Step 1 Import the YAML file into your script:
import yaml
from streamlit_authenticator import Authenticate
from yaml.loader import SafeLoader
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Step 2. Create the authenticator object:
authenticator = Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# Step 3.Render the login widget by providing a name for the form and its location (i.e., sidebar or main):
name, authentication_status, username = authenticator.login('Login', 'main')

import streamlit as st

# You can ppt-in for a logout button and add it as follows:
# if authentication_status:
#     authenticator.logout('Logout', 'main')
#     st.write(f'Welcome *{name}*')
#     st.title('Some content')
# elif authentication_status == False:
#     st.error('Username/password is incorrect')
# elif authentication_status == None:
#     st.warning('Please enter your username and password')


# Or you can access the same values through a session state:

# if st.session_state["authentication_status"]:
#     authenticator.logout('Logout', 'main')
#     st.write(f'Welcome *{st.session_state["name"]}*')
#     st.title('Some content')
# elif st.session_state["authentication_status"] == False:
#     st.error('Username/password is incorrect')
# elif st.session_state["authentication_status"] == None:
#     st.warning('Please enter your username and password')


# How to implement user privileges


if authentication_status:
    authenticator.logout('Logout', 'main')
    if username == 'jsmith':
        st.write(f'Welcome *{name}*')
        st.title('Application 1')
    elif username == 'rbriggs':
        st.write(f'Welcome *{name}*')
        st.title('Application 2')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')