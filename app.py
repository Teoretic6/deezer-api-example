import os

from requests_oauthlib import OAuth2Session

from flask import Flask, request, redirect, session, url_for

from app_utils import *


app = Flask(__name__)

# Taken from app settings in "My Apps"
# https://developers.deezer.com/myapps
config = {}

# Common for all users
authorization_base_url = 'https://connect.deezer.com/oauth/auth.php?perms=listening_history'
token_url = 'https://connect.deezer.com/oauth/access_token.php'

# Path to access token
# If no file is provided, you will need to authorize with browser
access_token_path = 'access_token.json'


@app.route("/")
def demo():
    """Step 1: User Authorization.

    Redirect the user/resource owner to the OAuth provider (i.e. Deezer)
    using an URL with a few key OAuth parameters.
    """
    deezer = OAuth2Session(config['app_id'], redirect_uri=config['redirect_uri'])
    authorization_url, state = deezer.authorization_url(authorization_base_url)

    # State is used to prevent CSRF, keep this for later.
    session['oauth_state'] = state
    return redirect(authorization_url)


# Step 2: User authorization, this happens on the provider.
@app.route("/callback", methods=["GET"])
def callback():
    """ Step 3: Retrieving an access token.

    The user has been redirected back from the provider to your registered
    callback URL. With this redirection comes an authorization code included
    in the redirect URL. We will use that to obtain an access token.
    """
    deezer = OAuth2Session(config['app_id'], state=session['oauth_state'])
    token = deezer.fetch_token(token_url,
                               client_secret=config['client_secret'],
                               authorization_response=request.url)

    # At this point you can fetch protected resources but lets save
    # the token and show how this is done from a persisted token
    # in /profile.
    session['oauth_token'] = token

    return redirect(url_for('.profile'))


@app.route("/profile", methods=["GET"])
def profile():
    """
    Fetching a protected resource using an OAuth 2 token.
    """
    deezer = OAuth2Session(config['app_id'], token=session['oauth_token'])

    access_token = session['oauth_token']['access_token']
    url_to_get = 'https://api.deezer.com/user/{}/history&access_token={}'.format(config['user_id'],
                                                                                 access_token)

    # Load listening history from Deezer
    all_history = load_listening_history(deezer, url_to_get)

    # Write loaded history to a file
    write_history_to_file(all_history)

    msg = 'History has been loaded!\nCheck out the file in the project directory :)'
    return msg


if __name__ == "__main__":
    # This allows us to use a plain HTTP callback
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"

    # Reading config file
    config = read_json('config.json')

    # Checking config file and starting an application
    if ('app_id' in config and
        'client_secret' in config and
        'redirect_uri' in config and
        'user_id' in config):
        app.secret_key = os.urandom(24)
        app.run(debug=True)
    else:
        raise ValueError('Wrong config! '
                         'Config file must contain fields "app_id", "client_secret", "redirect_uri", "user_id"')