import os
from dotenv import load_dotenv

load_dotenv()
from gql import Client
from gql.transport.requests import RequestsHTTPTransport
import requests

# Configure these to match the settings on your Dash Deployment Server:

# Domain name, from the settings in the Plotly On-Premise Server Manager (ask
# your local administrator if you don't know this).
DDS_DOMAIN_NAME = os.getenv("DDS_DOMAIN_NAME")
# Username and API key; you can obtain an API key from the Dash App Manager.
DDS_USERNAME = os.getenv("DDS_USERNAME")
DDS_API_KEY = os.getenv("DDS_API_KEY")
AUTH = (DDS_USERNAME, DDS_API_KEY)
# SSL/TLS certificate verification can be disabled here FOR TEST/DEMO SYSTEMS
# ONLY.
VERIFY = True

# It's safe to leave this option unchanged:
DDS_ENDPOINT = "https://{}/Manager/graphql".format(DDS_DOMAIN_NAME)

transport = RequestsHTTPTransport(
    url=DDS_ENDPOINT, auth=AUTH, use_json=True, verify=VERIFY, timeout=300
)

client = Client(transport=transport)