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

from bad_words import BAD_WORDS_LIST

def has_bad_words(s):
    """
    a very simple filter
    """
    for word in BAD_WORDS_LIST:
        if -1 != s.find(word):
            return True
    return False


if __name__ == '__main__':
    sentence = u'这是一个禁播的电影'
    print has_bad_words(sentence)



