# A rough starting point for testing
#
# See http://code.google.com/appengine/docs/python/tools/localunittesting.html
#
# Note that webest, by virtue of bypassing dev_appserver, doesn't trigger
# the bevahior required by 'login: (required|admin)' in app.yaml


import sys
import unittest

sys.path.extend(['/usr/lib/google-cloud-sdk/platform/google_appengine'])
import dev_appserver
dev_appserver.fix_sys_path()

import main
import webtest

from google.appengine.ext import testbed
from google.appengine.api import users


class TestBase(unittest.TestCase):

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_user_stub()
        self.requester = webtest.TestApp(main.application)

    def tearDown(self):
        self.testbed.deactivate()

    def login(self, email, is_admin=False):
        self.testbed.setup_env(user_email=email, overwrite=True)
        self.testbed.setup_env(user_id=email, overwrite=True)
        self.testbed.setup_env(user_is_admin=('1' if is_admin else '0'), overwrite=True)


class MainTest(TestBase):

    def test_not_logged_in(self):
        response = self.requester.get('/')
        self.assertEquals(200, response.status_code)
        self.assertIn("Hello", response.body)
        self.assertNotIn("@", response.body)
        self.assertIn("login", response.body)

    def test_logged_in(self):
        self.login("user@example.com")
        response = self.requester.get('/')
        self.assertEquals(200, response.status_code)
        self.assertIn("user@example.com", response.body)
        self.assertIn("logout", response.body)

