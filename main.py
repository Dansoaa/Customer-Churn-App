import streamlit as st
import streamlit_authenticator as stauth

st.set_page_config(
    page_title= "Home page",
    #page_icon=':house:',
    layout='wide'
)

# Initialize session state
if 'authentication_status' not in st.session_state:
    st.session_state.authentication_status = False
 
import yaml
from yaml.loader import SafeLoader

# Load YAML configuration
with open(r'C:\Users\USER\OneDrive - Azubi Africa\Desktop\AZUBI AFRICA\LP4Project\Customer-Churn-App\CustomerChurnApp\config.yaml') as file:
    config = yaml.safe_load(file)

# Initialize authenticator
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# Assuming the 'fields' parameter needs to be included based on your error message
# Since the exact syntax is not provided, this is a hypothetical example:

name, authentication_status, username = authenticator.login(fields=['username', 'password'])

# Rest of your authentication handling code
if authentication_status:
    authenticator.logout()
    st.write(f'Welcome *{name}*')
    st.title('Some content')
elif authentication_status is False:
    st.error('Username/password is incorrect')
<<<<<<< HEAD
elif authentication_status is None:
=======
elif st.session_state["authentication_status"] is None:
>>>>>>> 412ce7d60c1185e4371603e515a5c043cbdfcf36
    st.warning('Please enter your username and password')