import base64
from email.charset import BASE64
import urllib.request

def getTokens(clientID, clientSecret, authCode):
    concat = clientID + ":" + clientSecret
    # Must decode this in the header
    concatRes = base64.b64encode(bytes(concat, "utf8"))

    reqUrl = "https://api.fitbit.com/oauth2/token"
    urlPayload = {'code' : authCode,
            'grant_type' : 'authorization_code',
            'redirect_uri' : 'http://localhost'}

    urlEncoded = urllib.parse.urlencode(urlPayload, encoding='utf-8')
    urlEncoded = bytes(urlEncoded, 'utf-8')
    Session = urllib.request.Request(reqUrl, data=urlEncoded)
    Session.add_header('Authorization', f'Basic {concatRes.decode()}') 
    Session.add_header('Content-Type', 'application/x-www-form-urlencoded')
    response = urllib.request.urlopen(Session) 


    FullResponse = response.read()
    return FullResponse