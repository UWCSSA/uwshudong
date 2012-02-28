# -*- coding: utf-8 -*-

"""
    UW Shudong. GAE application for anonymous weibo.
    Copyright (C) 2012  UWCSSA <uwcssa.it@gmail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

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