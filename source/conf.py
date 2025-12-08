# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import tibas.tt
import alabaster

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'portfolio'
copyright = '2025, magenta'
author = 'magenta'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration'
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'tt'
html_theme_path = [tibas.tt.get_path(), alabaster.get_path()]
html_sidebars = {
    '**': [
        # 'about.html',
        'navigation.html',
    ]
}

html_static_path = ['_static']
html_css_files = ['custom.css',]
html_js_files = ['custom.js',]
html_favicon = '_static/alien_emoji.svg'

html_scaled_image_link = False

html_theme_options = {
    'show_powered_by': False,
    'show_relbars': False,
    'logo': '_static/alien_emoji.svg',
    'logo_name': True,
    'extra_nav_links': {
        '🔙': 'index.html'
    }
}

