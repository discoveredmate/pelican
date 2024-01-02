AUTHOR = 'aaron hauck'
SITENAME = 'discovered mate'
SITEURL = "https://discoveredmate.github.io/pelican"
OUTPUT_PATH = "output/"
GITHUB_PAGES_BRANCH = "gh-pages"

PATH = "content"

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

MARKUP = ('md',)
# Markdown Configuration:
MARKDOWN = {
    'extension_configs': {
	'markdown.extensions.codehilite': {'css_class': 'highlight'},
	'markdown.extensions.toc' : {},
	'markdown.extensions.extra': {},
	'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True