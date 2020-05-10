import urllib.request, urllib.parse, urllib.error
import oauth
import twkeys

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

def augment(url, parameters):
    secrets = twkeys.oauth()
    consumer = oauth.OAuthConsumer(secrets['API_key'],
                                   secrets['API_secret_key'])
    token = oauth.OAuthToken(secrets['Access_token'], secrets['Access_token_secret'])

    oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer,
                    token=token, http_method='GET', http_url=url,
                    parameters=parameters)
    oauth_request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(),
                               consumer, token)
    return oauth_request.to_url()
