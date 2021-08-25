#!/usr/bin/env python
# -*- coding: utf-8 -*-

config = {
    'site': {
        'base_url': 'https://oliz.io/mocs',
        'generate_sitemap': True,
        'title': 'Lego Designs',
        'logo': 'static/owl.png',
        'head': [
            '''<meta http-equiv="Content-Security-Policy" content="script-src 'unsafe-inline'">''',
            '''<meta name="referrer" content="no-referrer">'''
        ]
    },
    'author': {
        'name': 'oz',
        'url': 'https://oliz.io'
    },
    'social': {
        'about': 'https://oliz.io/about.html'
    }
}
