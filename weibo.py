# -*- coding: utf-8 -*-

from credentials import USERNAME, PASSWORD, APP_KEY
import urllib2, base64

WEIBO_URL = 'https://api.weibo.com/2/statuses/update.json'
DATA_PRE  = 'source=' + str(APP_KEY) + '&status='

def new_status(status):
    DATA = DATA_PRE + status
    req = urllib2.Request(WEIBO_URL, DATA)
    sec = base64.encodestring('%s:%s' % (USERNAME, PASSWORD)).replace('\n', '')
    req.add_header('Authorization', 'Basic %s' % sec)
    try:
        f = urllib2.urlopen(req)
        f.close()
    except Exception as err:
        if hasattr(err, 'code'):
            return False, str(err.code)
        else:
            return False, str(err)

    return True, None


if __name__ == '__main__':
    status = u"试试6".encode("utf8")
    print new_status(status)