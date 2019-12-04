#!/usr/bin/python

import locale
import json

this_locale=locale.getdefaultlocale()
print(json.dumps({
    "changed": False,
    "locale": ".".join(this_locale)}))
