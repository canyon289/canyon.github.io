#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ravin Kumar'
SITENAME = ['Manufacturing', 'and Machine Learning']
SITEURL = 'http://canyon289.github.io'

#Content Path
PATH = 'content'

OUTPUT_PATH = '..'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

THEME = "pelican-hyde-modified"

DELETE_OUTPUT_DIRECTORY = False

SUMMARY_MAX_LENGTH = 40

STATIC_PATHS = ['images', 'data', 'js', 'css']

OUTPUT_RETENTION = [".git", "dev"]

GOOGLE_ANALYTICS = 'UA-52706904-2'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/ravinakumar'),
          ('github', 'https://github.com/canyon289'),
          ('twitter', 'https://twitter.com/canyon289'))

DEFAULT_PAGINATION = False
DISPLAY_PAGES_ON_MENU = True
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["better_codeblock_line_numbering",
           "pelican_javascript",
           "liquid_tags.img", 
           'liquid_tags.include_code',
           'liquid_tags.notebook',
           'liquid_tags.literal',
           "render_math",
           "simple_footnotes"]

NOTEBOOK_DIR = 'notebooks'

# EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


MARKDOWN = {
            'extension_configs': {
                'markdown.extensions.codehilite': {'css_class': 'highlight'},
                'markdown.extensions.extra': {},
                'markdown.extensions.toc': {'anchorlink':True},
                'markdown.extensions.meta': {}
                    },
            'output_format': 'html5',
                }

