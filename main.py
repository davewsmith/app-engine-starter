import os

from google.appengine.api import users
import webapp2
from webapp2_extras import jinja2


jinja2.default_config['template_path'] = os.path.join(
    os.path.dirname(__file__),
    'templates'
)


class BaseHandler(webapp2.RequestHandler):
    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2()

    def render(self, template_name, template_context):
        context = {
            'user': users.get_current_user(),
            'login_url': users.create_login_url(self.request.uri),
            'logout_url': users.create_logout_url('/'),
        }
        context.update(template_context)
        template = self.jinja2.render_template(template_name, **context)
        self.response.write(template)


class HomePage(BaseHandler):
    def get(self):
        self.render('index.html', {})


class AdminPage(BaseHandler):
    def get(self):
        self.render('admin.html', {})


application = webapp2.WSGIApplication([
        ('/', HomePage),
        ('/admin/?', AdminPage),
    ],
    debug = not os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/')
)
