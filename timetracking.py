import datetime
import os
import random
import string
import sys
import base64

from django.utils import simplejson

from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import login_required
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import urlfetch


_DEBUG = True

template.register_template_library('templatefilters')

class BaseRequestHandler(webapp.RequestHandler):
    """Supplies a common template generation function.

    When you call render(), we augment the template variables supplied with
    the current user in the 'user' variable and the current webapp request
    in the 'request' variable.
    """
    def render(self, template_name, template_values={}):
        values = {
            'request': self.request,
            'user': users.get_current_user(),
            'login_url': users.create_login_url(self.request.uri),
            'logout_url': users.create_logout_url('http://%s/' % (
                self.request.host,)),
            'debug': self.request.get('deb'),
            'application_name': 'Time Tracking',}
        values.update(template_values)
        directory = os.path.dirname(__file__)
        path = os.path.join(directory, os.path.join('templates', template_name))
        self.response.out.write(template.render(path, values, debug=_DEBUG))


class Home(BaseRequestHandler):
    def get(self):
        result =
        urlfetch.fetch("http://theplant.lighthouseapp.com/projects/18933-asics/tickets.json", headers={'Authorization': 'Basic %s' % base64.b64encode("username:password")})
        
        self.render('home.html', {'tickets': simplejson.loads(result.content)})



app = webapp.WSGIApplication([
        ('/timetracking/', Home),
        ], debug=_DEBUG)

def main():
    run_wsgi_app(app)

if __name__ == '__main__':
    main()

