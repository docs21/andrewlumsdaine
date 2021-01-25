# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Andrew Lumsdaine'
copyright = '2021, Andrew Lumsdaine'
author = 'Andrew Lumsdaine'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_title = project
html_theme_path = ['_themes' ]

# html_logo = '_themes/edy_theme/static/css/lums_portrait_small.jpg'

html_theme = 'alabaster'

html_theme_options = {
    'logo': 'lums_portrait_small.jpg',
#     'github_user': 'bitprophet',
#     'github_repo': 'alabaster',

    'extra_nav_links' : {
        'Site Index' : 'genindex.html',
        'Google Scholar' : 'https://scholar.google.com/citations?user=rc_EJ2kAAAAJ',
        'LinkedIn' : 'https://www.linkedin.com/in/andrew-lumsdaine-704782',
    },
    'analytics_id': 'G-YT14YTSBSC'
}



# body_text_align: Which CSS text-align value to use for body text (if there is any.)

# canonical_url: If set, is used as the base URL (set before the relative path/pagename) for a <link rel="canonical"> canonical URL header tag.

# Note
# This value must end with a trailing slash.
# description: Text blurb about your project, to appear under the logo.

# description_font_style: Which CSS font-style to use for description text.

# fixed_sidebar: Makes the sidebar ‘fixed’ or pinned in place, so that the main body of the page scrolls but the sidebar remains visible. (Applies only to desktop window sizes; the mobile view is unaffected.)

# logo: Relative path (from $PROJECT/_static/) to a logo image, which will appear in the upper left corner above the name of the project.

# If logo is not set, your project name setting (from the top level Sphinx config) will be used in a text header instead. This preserves a link back to your homepage from inner doc pages.
# logo_name: Set to true to insert your site’s project name under the logo image as text. Useful if your logo doesn’t include the project name itself.

# logo_text_align: Which CSS text-align value to use for logo text (if there is any.)

# page_width: CSS width specifier controlling default content/page width.

# sidebar_width: CSS width specifier controlling default sidebar width.

# touch_icon: Path to an image (as with logo, relative to $PROJECT/_static/) to be used for an iOS application icon, for when pages are saved to an iOS device’s home screen via Safari.

# Service links and badges
# Third-party services (GitHub, Travis-CI, etc etc) and related badges or banners.

# analytics_id: Set to your Google Analytics ID (e.g. UA-#######-##) to enable tracking.

# badge_branch: Set which branch is used in the Travis, CodeCov, etc badges.

# codecov_button: true, false or a Github-style "account/repo" string - used to display a Codecov build status button in the sidebar. If true, uses your github_(user|repo) settings.

# donate_url: URL to generic/arbitrary donation service; causes display of a basic ‘Donate’ badge/shield (from https://shields.io) linking to the URL given.

# github_banner: true or false - whether to apply a ‘Fork me on Github’ banner in the top right corner of the page.

# If true, requires that you set github_user and github_repo (see below).
# May also submit a string file path (as with logo, relative to $PROJECT/_static/) to be used as the banner image instead of the default.
# github_button: true or false - whether to link to your Github.

# If true, requires that you set github_user and github_repo.
# There are also the github_type and github_count options, which behave as described in Github Buttons’ documentation.
# github_repo: Used by github_button and github_banner (see above); does nothing if both of those are set to false.

# github_user: Used by github_button and github_banner (see above); does nothing if both of those are set to false.

# gittip_user / gratipay_user: Deprecated, as that service is no longer running. These options still exist (removing them would break backwards compatibility; Sphinx errors when users try to set nonexistent options) but they no longer do anything.

# tidelift_url: Set this to your Tidelift project URL if you want a “Professional support” section in your sidebar.

# If copying the URL straight from Tidelift’s site, you’ll probably want to change &utm_campaign=readme to &utm_campaign=docs.
# travis_button: true, false or a Github-style "account/repo" string - used to display a Travis-CI build status button in the sidebar. If true, uses your github_(user|repo) settings.

# Non-service sidebar control
# Sidebar-related options that aren’t directly related to service links.

# extra_nav_links: Dictionary mapping link names to link targets; these will be added in a UL below the main sidebar navigation (provided you’ve enabled navigation.html via the html_sidebars option; see Installation.) Useful for static links outside your Sphinx doctree.

# show_related: Boolean controlling whether the sidebar ‘next/previous/related’ secondary navigation elements are hidden or displayed. Defaults to false since on many sites these elements are superfluous.

# Note
# This is distinct from the show_relbars setting found in the header/footer options; the two visual components are orthogonal and may be enabled/disabled independently of one another.
# sidebar_collapse: Boolean determining whether all TOC entries that
# are not ancestors of the current page are collapsed. You can read more about this in the Sphinx toctree docs.

# sidebar_includehidden: Boolean determining whether the TOC sidebar should include hidden Sphinx toctree elements. Defaults to true so you can use :hidden: in your index page’s root toctree & avoid having 2x copies of your navigation on your landing page.

# Header/footer options
# Which elements should appear in the header and/or footer, or modification of same.

# show_powered_by: Boolean controlling display of the Powered by Sphinx N.N.N. & Alabaster M.M.M section of the footer. When true, is displayed next to the copyright information; when false, is hidden.

# show_relbars: true or false - used to display next and previous links above and below the main page content. If you only want to display one, this setting can be further overridden through the show_relbar_top and show_relbar_bottom settings.

# Note
# This is distinct from the show_related setting found in the sidebar control options, which controls sidebar-only next/previous links.
# Style colors
# These should be fully qualified CSS color specifiers such as #004B6B or #444. The first few items in the list are “global” colors used as defaults for many of the others; update these to make sweeping changes to the colorscheme. The more granular settings can be used to override as needed.

# anchor: Foreground color of section anchor links (the ‘paragraph’ symbol that shows up when you mouseover page section headers.)
# anchor_hover_bg: Background color of anchor text.
# anchor_hover_fg: Foreground color of section anchor links (as above) when moused over.
# body_text: Main content text.
# code_highlight: Color of highlight when using :emphasize-lines: in a code block.
# footer_text: Footer text (includes links.)
# footnote_bg: Background of footnote blocks.
# footnote_border: Border of same.
# gray_1: Dark gray.
# gray_2: Light gray.
# gray_3: Medium gray.
# link_hover: Body links, hovered.
# link: Non-hovered body links.
# narrow_sidebar_bg: Background of ‘sidebar’ when narrow window forces it to the bottom of the page.
# narrow_sidebar_fg: Text color of same.
# narrow_sidebar_link: Link color of same.
# note_bg: Background of .. note:: blocks.
# note_border: Border of same.
# pink_1: Light pink.
# pink_2: Medium pink.
# pre_bg: Background of preformatted text blocks (including code snippets.)
# relbar_border: Color of border between bar holding next and previous links, and the rest of the page content.
# seealso_bg: Background of .. seealso:: blocks.
# seealso_border: Border of same.
# sidebar_header: Sidebar headers.
# sidebar_hr: Color of sidebar horizontal rule dividers.
# sidebar_link: Sidebar links (there is no hover variant.) Applies to both header & text links.
# sidebar_list: Foreground color of sidebar list bullets & unlinked text.
# sidebar_link_underscore: Sidebar links’ underline (technically a bottom-border).
# sidebar_search_button: Background color of the search field’s ‘Go’ button.
# sidebar_text: Sidebar paragraph text.
# warn_bg: Background of .. warn:: blocks.
# warn_border: Border of same.
# Fonts
# caption_font_size: Font size of caption block text.
# caption_font_family: Font family of caption block text.
# code_font_size: Font size of code block text.
# code_font_family: Font family of code block text. Defaults to 'Consolas', 'Menlo', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', monospace.
# font_family: Font family of body text.
# font_size: Font size of body text.
# head_font_family: Font family of headings. Defaults to 'Garamond', 'Georgia', serif.


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
