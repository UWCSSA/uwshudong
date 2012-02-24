from credentials import PRIVATE_KEY

import urllib2, urllib

RECAPTCHA_URL = "http://www.google.com/recaptcha/api/verify"

def valid_recaptcha(remoteip, challenge, response):
    data = {'privatekey': PRIVATE_KEY,
            'remoteip': remoteip,
            'challenge': challenge,
            'response': response}
    data = urllib.urlencode(data)
    f = urllib2.urlopen(RECAPTCHA_URL, data)
    result = f.read()
    f.close()

    if 'true' == result.splitlines()[0]:
        return True
    else:
        return False
