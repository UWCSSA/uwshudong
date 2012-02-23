import webapp2

from html import index_content
from weibo import new_status

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
        self.response.out.write(index_content())

class NewStatus(webapp2.RequestHandler):
    def post(self):
        status = self.request.get('content')
        success, error = new_status(status)

        self.response.out.write('<html><body>')
        if success:
            self.response.out.write('succeeded!')
        else:
            self.response.out.write('error code: ' + error)
        self.response.out.write('</body></html>')

app = webapp2.WSGIApplication([('/', MainPage), ('/new', NewStatus)],
                                debug = True)