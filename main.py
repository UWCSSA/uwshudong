# -*- coding: utf-8 -*-

import webapp2
import json

from weibo import new_status

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
        with open("index.html") as html_file:
            html_content = html_file.read()
        self.response.out.write(html_content)


class NewWeibo(webapp2.RequestHandler):
    def post(self):
        status = self.request.get('status')
        if len(status) > 0:
            success, error = new_status(status)
        else:
            success = False
            error = u'不能发布空消息'

        res = {'success': success}

        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'

        if success:
            res['text'] = u'发表成功！请稍后查看'
        else:
            if error == '400':
                res['text'] = u'请不要连续发布同样的内容'
            else:
                res['text'] = u'发生错误！错误信息： ' + error

        self.response.out.write(json.dumps(res))


app = webapp2.WSGIApplication([('/', MainPage), ('/new', NewWeibo)], debug = True)