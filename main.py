import base64
import json
from getTokens import getTokens
# First, we will need a variable with the access token and another variable with a refresh token
def main():
    clientID = "239824"
    clientSecret = "78ca013aa8147e78910d27f91328f560"
    authCode = "2ed10d0f90c5b50b4226a07b669ca1edc868aaa5"
    getTokens(clientID, clientSecret, authCode)


if __name__ == "__main__":
    main()