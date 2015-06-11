#!/usr/bin/env python
# encoding: utf-8
from __future__ import (unicode_literals, division,
                        print_function, absolute_import)
from collections import OrderedDict
from flask import request, Blueprint

import json
import scraperwiki

sql_query = Blueprint('sql_query', __name__, static_folder='static',
                       static_url_path='/static/sql_query')

@sql_query.route('/')
def index():
    return sql_query.send_static_file('sql_query_tool_index.html')
