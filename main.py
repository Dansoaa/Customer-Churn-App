import streamlit as st
import streamlit_authenticator as stauth
 
import yaml
from yaml.loader import SafeLoader

# Load YAML configuration
with open(r'C:/Users/DELL/OneDrive/github/Churn-App/Customer-Churn-App/config.yaml') as file:
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
elif authentication_status is None:
    st.warning('Please enter your username and password')