import webapp2

from weibo import new_status

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
        with open("index.html") as html_file:
            html_content = html_file.read()
        self.response.out.write(html_content)

class ResultPage(webapp2.RequestHandler):
    def post(self):
        status = self.request.get('content')
        success, error = new_status(status)

        self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
        self.response.out.write('<html><body>')
        if success:
            self.response.out.write('succeeded!')
        else:
            self.response.out.write('error code: ' + error)
        self.response.out.write('</body></html>')

class NewWeibo(webapp2.RequestHandler):
    def post(self):
        status = self.request.get('input_content');
        success, error = new_status(status)

        self.response.headers['Content-Type'] = 'text/plain; charset=utf-8'
        if success:
            self.response.out.write(u'发表成功！请稍后查看')
        else:
            self.response.out.write(u'发生错误，错误代码： ' + error)


app = webapp2.WSGIApplication([('/', MainPage), ('/result', ResultPage)],
                                debug = True)