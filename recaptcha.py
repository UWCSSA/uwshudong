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
