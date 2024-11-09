import yaml
import streamlit_authenticator as stauth

def test():
    with open('../credential/config.yaml') as file:
        config = yaml.load(file, Loader=stauth.SafeLoader)
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days']
    )
    print(config)

if __name__ == '__main__':
    test()