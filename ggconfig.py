#!/usr/bin/env python
# -*- coding: utf-8 -*-

config = {
    'site': {
        'base_url': 'https://oliz.io/lego',
        'render_root_readme': True,
        'generate_sitemap': True,
        'title': 'Lego Designs',
        'logo': 'static/owl.png',
        'about_url': 'https://oliz.io/about.html',
        'csp': '''<meta http-equiv="Content-Security-Policy" content="script-src 'unsafe-inline'">''',
        'referrer': '''<meta name="referrer" content="no-referrer">'''
    },
    'author': {
        'name': 'oz',
        'url': 'https://oliz.io'
    },
    'social': {
        'github_url': 'https://github.com/ooz/lego'
    }
}
