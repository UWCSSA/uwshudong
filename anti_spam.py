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
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import akismet
from credentials import AKISMET_API_KEY

akismet.USERAGENT = 'Weibo/1.0 | UW Shu Dong/1.0'

def is_spam(comment, remoteip, useragent):
    "seems akismet treats every chinese comment as spam, so useless"

    comment = comment.encode('utf-8')
    return akismet.comment_check(AKISMET_API_KEY, 'http://uwshudong.appspot.com',
            remoteip, useragent, comment_content = comment)