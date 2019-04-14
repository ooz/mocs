#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
from html import escape
import os
import sys
import markdown

import ggconfig as gg

MD = markdown.Markdown(
        extensions = [
            'extra',
            'meta',
            'sane_lists',
            'toc',
            'pymdownx.magiclink',
            'pymdownx.betterem',
            'pymdownx.tilde',
            'pymdownx.emoji',
            'pymdownx.tasklist',
            'pymdownx.superfences'
        ]
    )

def render_template(title, canonical_url, description, tags, date, body, root=False):
    base_url = gg.config.get('site', {}).get('base_url', '')
    logo_url = base_url + '/' + gg.config.get('site', {}).get('logo', '')
    style_url = base_url + '/' + gg.config.get('site', {}).get('style', '')
    author_name = gg.config.get('author', {}).get('name', '')
    author_url = gg.config.get('author', {}).get('url', '')
    return \
f'''<!DOCTYPE html>
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta name="viewport" content="width=device-width,initial-scale=1">

<title>{convert_title2pagetitle(title)}</title>
<link rel="canonical" href="{canonical_url}">
<link rel="shortcut icon" href="{logo_url}">

{external_stylesheets_with_highlightjs()}
<link rel="stylesheet" href="{style_url}">

{meta(author_name, description, tags)}
{twitter(gg.config.get('social', {}).get('twitter_username', ''))}
{opengraph(title, canonical_url, description, date)}
</head>

<body class="container">
<div style="text-align:center">
<a href="{author_url}"><img src="{logo_url}" class="avatar" /></a>
</div>
{post_header(title, date)}
<div style="padding-top:2.5rem;">
{body}
</div>
<div>
{'' if root else render_footer_navigation(base_url)}
{render_about_and_social_icons()}
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.11.0/highlight.min.js"></script>
<script type="text/javascript">hljs.initHighlightingOnLoad();</script>
</body>
</html>
'''

def render_about_and_social_icons():
    github = gg.config.get('social', {}).get('github_url', '')
    twitter = gg.config.get('social', {}).get('twitter_url', '')
    email = gg.config.get('author', {}).get('email', '')
    about = gg.config.get('site', {}).get('about_url', '')
    icons = []

    if len(email):
        icons.append('<a href="mailto:%s" class="social-icon">email</a>' % email)
    if len(twitter):
        icons.append('<a href="%s" class="social-icon">twitter</a>' % twitter)
    if len(github):
        icons.append('<a href="%s" class="social-icon">github</a>' % github)
    if len(about):
        icons.append('<a href="%s" class="social-icon">about</a>' % about)
    return '\n'.join(icons)

def render_footer_navigation(root_url):
    return f'''<a href="{root_url}" class="nav-arrow">back</a>
<a href="#" class="nav-arrow">top</a>'''

def meta(author, description, tags):
    return \
f'''<meta name="author" content="{author}" />
<meta name="description" content="{description}" />
<meta name="keywords" content="{tags}" />'''

def twitter(twitter_username):
    return \
f'''<meta name="twitter:author" content="{twitter_username}" />
<meta name="twitter:card" content="summary" />
<meta name="twitter:creator" content="{twitter_username}" />'''

# URL should end with "/" for a directory!
def opengraph(title, url, description, date,
              image=gg.config.get('site', {}).get('base_url', '') + '/' + gg.config.get('site', {}).get('logo', '')):
    return \
f'''<meta property="og:title" content="{title}" />
<meta property="og:type" content="article" />
<meta property="og:url" content="{url}" />
<meta property="og:description" content="{description}" />
<meta property="og:image" content="{image}" />
<meta property="og:locale" content="en-US" />
<meta property="article:published_time" content="{date}" />'''

def post_header(title, date):
    name = gg.config.get('author', {}).get('name', '')
    author_url = gg.config.get('author', {}).get('url', '')
    name_and_date = date[:10]
    if len(name) and len(name_and_date):
        maybe_linked_author = name
        if len(author_url):
            maybe_linked_author = f'<a href="{author_url}">{name}</a>'
        name_and_date = f'{maybe_linked_author}, {name_and_date}'
    return \
f'''<div>
{MD.reset().convert('# ' + title)}
<small style="float:right;">{name_and_date}</small>
</div>'''

def external_stylesheets():
    external_styles = gg.config.get('site', {}).get('external_styles', [])
    if not external_styles:
        external_styles = [
            'https://cdn.rawgit.com/necolas/normalize.css/master/normalize.css',
            'https://cdn.rawgit.com/milligram/milligram/master/dist/milligram.min.css' # mini.css is also nice!
        ]
    return '\n'.join([f'<link rel="stylesheet" href="{style}">' for style in external_styles])

def external_stylesheets_with_highlightjs():
    return external_stylesheets() + '''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.11.0/styles/default.min.css">'''

def convert(directory, filepath, root=False):
    with open(filepath, 'r') as infile:
        markdown_post = infile.read()
        html_post = MD.reset().convert(markdown_post)
        targetpath = convert_path(filepath)
        with open(targetpath, 'w') as outfile:
            canonical_url = convert_canonical(directory, targetpath)
            date = convert_meta(MD, 'date')
            tags = convert_meta(MD, 'tags')
            title = convert_meta(MD, 'title')
            html = render_template(title,
                canonical_url,
                convert_meta(MD, 'description', default=title),
                tags,
                date,
                html_post,
                root
            )
            outfile.write(html)
            return {
                'date': date,
                'url': canonical_url,
                'title': title,
                'tags': tags
            }

def convert_meta(md, field, default=''):
    field_value = MD.Meta.get(field, '')
    if len(field_value) > 0:
        return escape(', '.join(field_value))
    return default

def convert_path(filepath):
    targetpath = filepath[:-3]
    if targetpath.endswith('README'):
        targetpath = targetpath[:-6] + 'index'
    targetpath += '.html'
    return targetpath

def convert_canonical(directory, targetpath):
    base_url = gg.config.get('site', {}).get('base_url', '')
    targetpath = os.path.relpath(targetpath, directory)
    if targetpath.endswith('index.html'):
        return f'{base_url}/{targetpath[:-10]}'
    return f'{base_url}/{targetpath}'

def convert_title2pagetitle(title):
    root_title = gg.config.get('site', {}).get('title', '')
    if len(title) and title != root_title:
        return f'{title} | {root_title}'
    return root_title

def make_index(posts):
    base_url = gg.config.get('site', {}).get('base_url', '')
    root_title = gg.config.get('site', {}).get('title', '')
    logo_url = base_url + '/' + gg.config.get('site', {}).get('logo', '')
    style_url = base_url + '/' + gg.config.get('site', {}).get('style', '')
    author_url = gg.config.get('author', {}).get('url', '')
    posts_html = []
    for post in reversed(sorted(posts, key=lambda post: post['date'])):
        day = post['date'][:10]
        title = post['title']
        url = post['url']
        if (day != '' and title != ''):
            posts_html.append('<tr><td>%s</td><td><a href="%s">%s</a></td></tr>' % (day, url, title))
    posts_html = "\n".join(posts_html)

    index_html = \
f'''<!DOCTYPE html>
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta name="viewport" content="width=device-width,initial-scale=1">

<title>Blog Index | {root_title}</title>
<link rel="canonical" href="{base_url}">
<link rel="shortcut icon" href="{logo_url}">

{external_stylesheets()}
<link rel="stylesheet" href="{style_url}">
</head>

<body class="container">
<div style="text-align:center">
<a href="{author_url}"><img src="{logo_url}" class="avatar" /></a>
</div>
<h1>Blog</h1>
<div style="padding-top:2.5rem;">
<table><tbody>
{posts_html}
</tbody></table>
</div>
<div>
{render_about_and_social_icons()}
</div>
</body>
</html>
'''
    with open('index.html', 'w') as index_file:
        index_file.write(index_html)

def is_root_readme(path):
    return os.path.relpath(path) == 'README.md'

def make_sitemap(posts):
    sitemap_xml = []
    sitemap_xml.append('<?xml version="1.0" encoding="utf-8" standalone="yes" ?>')
    sitemap_xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    additional_entries = gg.config.get('site', {}).get('additional_sitemap_entries', [])
    all_entries = [post['url'] for post in posts] + additional_entries
    all_entries = sorted(all_entries)
    for entry in all_entries:
        sitemap_xml.append('  <url>')
        sitemap_xml.append('    <loc>%s</loc>' % escape(entry))
        sitemap_xml.append('  </url>')
    sitemap_xml.append('</urlset>\n')
    sitemap_xml = '\n'.join(sitemap_xml)
    with open('sitemap.xml', 'w') as sitemap_file:
        sitemap_file.write(sitemap_xml)

def main(directories):
    render_root_readme = gg.config.get('site', {}).get('render_root_readme', True)
    posts = []
    for directory in directories:
        paths = glob.glob(directory + '/**/*.md', recursive=True)
        for path in paths:
            root_readme = is_root_readme(path)
            if not root_readme or render_root_readme:
                posts.append(convert(directory, path, root=root_readme))

    posts = [post for post in posts if 'draft' not in post['tags']]
    if not render_root_readme:
        make_index(posts)

    generate_sitemap = gg.config.get('site', {}).get('generate_sitemap', False)
    if generate_sitemap:
        make_sitemap(posts)

if __name__ == '__main__':
    main(sys.argv[1:])
