import base64
import json
from getTokens import getTokens
# First, we will need a variable with the access token and another variable with a refresh token
def main():
    clientID = "239824"
    clientSecret = "78ca013aa8147e78910d27f91328f560"
    authCode = "94d1cfb1bb2d0b19b8dd7d5727113d8292e0a263"
    getTokens(clientID, clientSecret, authCode)


if __name__ == "__main__":
    main()