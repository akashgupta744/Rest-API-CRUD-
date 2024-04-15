# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys
import django

# Add the parent directory of the Sphinx documentation directory to sys.path
sys.path.insert(0, os.path.abspath('../../'))  # Adjust the number of '..' to match the project structure

# Specify the path to the Django settings module relative to the Sphinx documentation directory
os.environ['DJANGO_SETTINGS_MODULE'] = 'project02.settings'  # Adjust the settings module path if necessary

# Initialize Django's settings and configuration
django.setup()
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'project02'
copyright = '2024, axxonet'
author = 'axxonet'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
