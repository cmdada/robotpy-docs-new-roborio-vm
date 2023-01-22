#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# RobotPy WPILib documentation build configuration file, created by
# sphinx-quickstart on Sun Nov  2 21:31:04 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

#
# Imports
#

import sys
import os
from datetime import date
import subprocess

from os.path import abspath, join, dirname

sys.path.insert(0, abspath(join(dirname(__file__))))

# -- RTD configuration ------------------------------------------------

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get("READTHEDOCS", None) == "True"

# This is used for linking and such so we link to the thing we're building
rtd_version = os.environ.get("READTHEDOCS_VERSION", "latest")
if rtd_version not in ["stable", "latest"]:
    rtd_version = "stable"

# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx_inline_tabs",
    "sphinxext.opengraph",
    "sphinx_reredirects",
]

ogp_custom_meta_tags = [
    '<meta property="og:ignore_canonical" content="true" />',
    '<meta name="theme-color" content="#3393d5" />',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "RobotPy"
copyright = f"2014-{date.today().year}, RobotPy development team"


intersphinx_mapping = {
    "commandsv1": (
        "https://robotpy.readthedocs.io/projects/commands-v1/en/%s/" % rtd_version,
        None,
    ),
    "commandsv2": (
        "https://robotpy.readthedocs.io/projects/commands-v2/en/%s/" % rtd_version,
        None,
    ),
    "pyfrc": (
        "https://robotpy.readthedocs.io/projects/pyfrc/en/%s/" % rtd_version,
        None,
    ),
    "ntcore": (
        "https://robotpy.readthedocs.io/projects/pyntcore/en/%s/" % rtd_version,
        None,
    ),
    "wpilib": (
        "https://robotpy.readthedocs.io/projects/wpilib/en/%s/" % rtd_version,
        None,
    ),
    "hal": (
        "https://robotpy.readthedocs.io/projects/hal/en/%s/" % rtd_version,
        None,
    ),
    "robotpy_ext": (
        "https://robotpy.readthedocs.io/projects/utilities/en/%s/" % rtd_version,
        None,
    ),
    "cscore": (
        "https://robotpy.readthedocs.io/projects/cscore/en/%s/" % rtd_version,
        None,
    ),
    "frc": ("https://docs.wpilib.org/en/stable", None),
}

redirects = {
    "2020_notes": "upgrade_notes.html",
    "install/pynetworktables": "pyntcore.html"
}

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = subprocess.check_output(("git", "describe", "--tags"), text=True).split(".")[0]
# The full version, including alpha/beta/rc tags.
release = version

autoclass_content = "both"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "default"

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme

    html_theme = "sphinx_rtd_theme"
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
else:
    html_theme = "default"

# Output file base name for HTML help builder.
htmlhelp_basename = "RobotPy"


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        "index",
        "RobotPy.tex",
        "RobotPy Documentation",
        "RobotPy development team",
        "manual",
    )
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        "RobotPy",
        "RobotPy Documentation",
        "RobotPy development team",
        "RobotPy",
        "One line description of project.",
        "Miscellaneous",
    )
]

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = "RobotPy"
epub_author = "RobotPy development team"
epub_publisher = "RobotPy development team"
epub_copyright = "2014-2022, RobotPy development team"

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]

# -- Custom Document processing ----------------------------------------------

from robotpy_sphinx.sidebar import generate_sidebar

generate_sidebar(
    globals(),
    "robotpy",
    "https://raw.githubusercontent.com/robotpy/docs-sidebar/master/sidebar.toml",
)
