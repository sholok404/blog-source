#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Syed Subeh-Sadik Sholok'
SITENAME = "Sholok's Notes"
SITEURL = 'https://sholok404.github.io'

PATH = 'content'

TIMEZONE = 'Asia/Dhaka'

DEFAULT_LANG = 'en'

THEME = 'pelican-themes/pelican-clean-blog'
RELATIVE_URLS = True


FEED_DOMAIN = SITEURL
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'

STATIC_PATHS = ['images', 'favicon.ico']
HEADER_COVER = 'http://peek.space/art/earth-lights-lrg/full.jpg'
FAVICON = 'favicon.ico'
DISPLAY_PAGES_ON_MENU = True
COLOR_SCHEME_CSS = 'monokai.css'
DISQUS_SITENAME = 'sholoks-notes'

MENUITEMS = (
	 ('Portfolio', 'https://sholok404.github.io/resume/'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/sholok404'),
			('Codepen', 'https://codepen.io/Sholok404/'),
			('envelope','mailto:syedsholok@gmail.com'),
			('Linkedin', 'https://bd.linkedin.com/in/subeh-sadik-sholok-436705103'),
            ('YouTube', 'https://www.youtube.com/channel/UCABF-0VCiJ1HaNCs4x7L36A'),
			('Facebook', 'https://www.facebook.com/subehsadik.sholok'),
			('rss', 'feeds/all.rss.xml'))

DEFAULT_PAGINATION = 10


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
