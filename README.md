# Deezer API Python 3 Example

**Example of working with Deezer API in Python 3.**

**Download your listening history** with this simple Flask App!

Used libraries:
* [Requests-OAuthlib](https://github.com/requests/requests-oauthlib)
* [Flask](http://flask.pocoo.org/)

Based on Requests-OAuthlib [GitHub OAuth 2 Tutorial](https://requests-oauthlib.readthedocs.io/en/latest/examples/github.html)

## To Get Started

1. **Create a new Deezer Application at the [Deezer for developers](https://developers.deezer.com/myapps)**  

**Important**: When creating your app, set field __Redirect URL after authentication__ to  *http://127.0.0.1:5000/callback*  

Other fields can be set to whatever you want :)

2. **Fill in missing fields in "config.json" file**
* **app_id**:  
  *"Application ID"* in application settings  
  
  *(Example: __289071__)*
* **client_secret**:  
  *"Secret Key"* in application settings
    
  *(Example: __23a1ca17cf5ea13a03e1f4155320aec6__)*
* **user_id**:  
  *"Deezer User ID"* from your profile page URL  
  
  *(Example: if your profile page URL is "https://www.deezer.com/en/profile/102643295", your User ID is __102643295__)*

3. **Install dependencies**:  
```pip install -r requirements.txt```

4. **Launch your application**  
```python3 app.py```

5. **Go to __http://127.0.0.1:5000/__ in your web-browser**

**You will be asked to give permissions to your newly created application.**

Press "Accept".

**After that you should see the line:**  
*History has been loaded! Check out the file in the project directory :)*  

**If this line appears, congratulations!**  
You have successfully downloaded all of your available Deezer listening history!

6. **Open "deezer_history<current_date>.json" file in your project directory.**

It's structure is basically:  
```
{
    "data": [
        {track_1_dict},
        {track_2_dict},
        ...
        {track_n_dict}
    ]
}
```

For the format of track information, see [Deezer API Explorer](https://developers.deezer.com/api/explorer).

## Further information

Check [Deezer API Page](https://developers.deezer.com/api) for more information on Deezer API.