__author__ = 'Felix Sun'

import datetime
import time

from google.appengine.ext.webapp import template

def short_date(date):
    return ''

register = template.create_template_register()
register.filter(short_date)

