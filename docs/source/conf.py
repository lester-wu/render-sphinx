# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list, see the official documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# Standard library
import os
import sys

# Add project-level path so that the `autodoc` can import specified modules.
sys.path.insert(0, os.path.abspath("../../../"))


# -- Project information -----------------------------------------------------

project = "Hail"
copyright = "2020-2021, eyos"
author = "eyos"

# The full version, including alpha/beta/rc tags
release = "0.0.1"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names as strings here. They can be
# extensions coming with Sphinx (named "sphinx.ext.*") or your custom
# ones.
extensions = [
    # Extension for including documentation from docstrings.
    "sphinx.ext.autodoc",
    # Extension for providing Google-style docstring support.
    "sphinx.ext.napoleon",
    # Extension for documenting Python 3 argument and return value types.
    "sphinx_autodoc_typehints",
    # Extension for linking directly to the code behind the documentation.
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to the source directory, that match files and
# directories to ignore when looking for source files. This pattern is also
# consulted when looking for static files in `html_static_path`
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML pages. See the documentation for a list of builtin
# themes: https://www.sphinx-doc.org/en/master/usage/theming.html
# `alabaster` is the default theme.
html_theme = "alabaster"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are subsequently copied to the builtin static
# files, so a file named "default.css" will overwrite the builtin
# "default.css".
html_static_path = ["_static"]

# These paths are relative to `html_static_path`.
html_css_files = ["sphinx-customized.css"]

# Add type hint options here.
always_document_param_types = True
typehints_fully_qualified = True
