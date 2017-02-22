# See http://code.google.com/appengine/docs/python/tools/localunittesting.html

import sys
import unittest

sys.path.extend(['/usr/lib/google-cloud-sdk/platform/google_appengine'])
import dev_appserver
dev_appserver.fix_sys_path()

import main
import webtest

from google.appengine.ext import testbed

class ExampleTest(unittest.TestCase):

    def setUp(self):
        self.testbed = testbed.TestBed()
        self.testbed.activate()
        self.requester = webtest.TestApp(main.application)

    def tearDown(self):
        self.testbed.deactivate()

    def login(self, email, is_admin):
        self.testbed.set_env(user_email=email, overwrite=True)
        self.testbed.set_env(user_id=email, overwrite=True)
        self.testbed.set_env(user_is_admin='1' if is_admin else '0', overwrite=True)

