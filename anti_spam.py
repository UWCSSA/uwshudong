import akismet
from credentials import AKISMET_API_KEY

akismet.USERAGENT = 'Weibo/1.0 | UW Shu Dong/1.0'

def is_spam(comment, remoteip, useragent):
    "seems akismet treats every chinese comment as spam, so useless"

    comment = comment.encode('utf-8')
    return akismet.comment_check(AKISMET_API_KEY, 'http://uwshudong.appspot.com',
            remoteip, useragent, comment_content = comment)