import base64
from email.charset import BASE64
import urllib.request

def getTokens(clientID, clientSecret, authCode):
    concat = clientID + ":" + clientSecret
    # Must decode this in the header
    concatRes = base64.b64encode(bytes(concat, "utf8"))

    reqUrl = "https://api.fitbit.com/oauth2/token"
    urlPayload = {'code' : clientID,
            'client_id' : clientSecret,
            'grant_type' : 'authorization_code',
            'redirect_uri' : 'http://localhost'}

    urlEncoded = urllib.parse.urlencode(urlPayload)

    print (urlEncoded)
    #   |
    #   |   Finish below
    #   V
    Session = urllib.request.Request(reqUrl, data=urlPayload)
    Session.add_header('Authorization', f'Basic {concatRes.decode()}')
    Session.add_header('Content-Type', 'application/x-www-form-urlencoded')
    
    response = urllib.request.urlopen(Session)

    FullResponse = response.read()
    print(FullResponse)
    # bodyUrl = urllib.parse.urlencode(BodyText)
   # print(BodyURLEncoded)
    return 