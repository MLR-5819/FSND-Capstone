import os
import json
from flask import request, _request_ctx_stack
from functools import wraps
from jose import jwt
from urllib.request import urlopen

#get auth0 info from setup.sh for app deployment
AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')
ALGORITHMS = [os.environ.get('ALGORITHMS')]
API_AUDIENCE = os.environ.get('API_AUDIENCE')

#Sets auth0 info during local usage
if not all([AUTH0_DOMAIN, ALGORITHMS, API_AUDIENCE]):
    AUTH0_DOMAIN = 'dev-mrose.us.auth0.com'
    ALGORITHMS = ['RS256']
    API_AUDIENCE = #createauth0api

class AuthError(Exception):
    #TODO


