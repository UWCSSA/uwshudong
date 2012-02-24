# -*- coding: utf-8 -*-

import webapp2
import json

from weibo import new_status
from recaptcha import valid_recaptcha
#from anti_spam import is_spam

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
        with open("index.html") as html_file:
            html_content = html_file.read()
        self.response.out.write(html_content)


class NewWeibo(webapp2.RequestHandler):
    def return_json(self, success, text):
        res = {'success': success}
        res['text'] = text

        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.out.write(json.dumps(res))

    def post(self):
        status = self.request.get('status')
        if len(status) > 140:
            status = status[:140]  # only 140 chars in maximum
        challenge = self.request.get('challenge')
        response  = self.request.get('response')
        remoteip  = self.request.remote_addr
#        useragent = self.request.headers['User-Agent'] \
#                if 'User-Agent' in self.request.headers else 'None'
#        referer   = self.request.headers['Referer'] \
#                if 'Referer' in self.request.headers else 'None'


        if 0 == len(status):
            self.return_json(False, u'发布错误！不能发布空消息')
            return

        if len(challenge) == 0 or len(response) == 0:
            self.return_json(False, u"验证码错误！验证码不能为空")
            return

        if not valid_recaptcha(remoteip, challenge, response):
            self.return_json(False, u"验证码错误！请重新输入")
            return

#        if is_spam(status, remoteip, useragent):
#            self.return_json(False, u"内容错误！spam")
#            return
#        self.return_json(True, u'not spam')
#        return


        success, error = new_status(status)
        if success:
            text = u'发表成功！请稍后查看'
        else:
            if error == '400':
                text = u'发布失败！输入内容有误'
            else:
                text = u'发布失败！错误信息： ' + error

        self.return_json(success, text)


app = webapp2.WSGIApplication([('/', MainPage), ('/new', NewWeibo)], debug = True)