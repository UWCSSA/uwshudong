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
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import webapp2, json, cgi

from weibo import new_status
from recaptcha import valid_recaptcha
from anti_spam import is_spam

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
        status = cgi.escape(self.request.get('status'))
        if len(status) > 140:
            status = status[:140]  # only 140 chars in maximum
        challenge = cgi.escape(self.request.get('challenge'))
        response  = cgi.escape(self.request.get('response'))
        remoteip  = cgi.escape(self.request.remote_addr)
        useragent = cgi.escape(self.request.headers['User-Agent']) \
                if 'User-Agent' in self.request.headers else 'Unknown'


        if 0 == len(status):
            self.return_json(False, u'发布错误！不能发布空消息')
            return

        if len(challenge) == 0 or len(response) == 0:
            self.return_json(False, u"验证码错误！验证码不能为空")
            return

        if not valid_recaptcha(remoteip, challenge, response):
            self.return_json(False, u"验证码错误！请重新输入")
            return

#        # all chinese comments are treated as spam by akismet?
#        if is_spam(remoteip, status, useragent):
#            self.return_json(False, u"内容错误！spam")
#            return
#        self.return_json(True, 'not spam')
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