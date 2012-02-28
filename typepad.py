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

import urllib, urllib2
from credentials import TYPEPAD_API_KEY, AKISMET_BLOG_URL

TYPEPAD_URL = 'http://' + TYPEPAD_API_KEY + '.api.antispam.typepad.com/1.1/comment-check'
TYPEPAD_AGENT  = 'Weibo/1.0 | UW Shudong/1.0'

def check_typepad(remoteip, comment, user_agent):
    """
    seems not effective as akismet, but can check chinese comments
    return True if the comment is spam; False if not
    """
    data = {'blog': AKISMET_BLOG_URL,
            'user_ip': remoteip,
            'user_agent': user_agent}
    data = urllib.urlencode(data)
    data = data + '&comment_content=' + comment
    req = urllib2.Request(TYPEPAD_URL, data)
    req.add_header('User-Agent', TYPEPAD_AGENT)
    req.add_header("Content-type", "application/x-www-form-urlencoded; charset=UTF-8")
    f = urllib2.urlopen(req)
    result = f.read()
    f.close()

    if 'false' == result:
        return False
    else:
        return True


if __name__ == '__main__':
    print TYPEPAD_URL