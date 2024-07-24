# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Line Follower Tracker'
copyright = ''
author = 'Abhishekh Reddy, WSL'
release = 'Draft'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_rtd_theme',
    'sphinx_copybutton',
    # 'sphinx_simplepdf',
]

templates_path = ['_templates']
exclude_patterns = []

numfig = True
numfig_format = {
    'code-block': 'Figure %s',
    'figure': 'Figure %s',
    'section': 'Section',
    'table': 'Table %s',
}
numref = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
# html_static_path = ['_static']

# -- Options for LaTeX output --------------------------------------------------

latex_engine = 'xelatex'
latex_paper_size = 'letter'
latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'writeup.tex', u'Line Follower Tracker',
   u'Abhishekh Reddy, WSL', 'howto'),
]

latex_elements = {
  'sphinxsetup': 'hmargin={0.75in,0.75in}, vmargin={0.75in,0.75in}, marginpar=0.75in',
}

#latex_logo = None
#latex_use_parts = False
#latex_show_pagerefs = False
#latex_show_urls = False
#latex_preamble = ''
#latex_appendices = []
#latex_domain_indices = True
