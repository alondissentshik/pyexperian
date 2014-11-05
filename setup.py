try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python wrapper for Experian\'s Net Connect API',
    'author': 'Carlos Eduardo Rivera',
    'url': 'https://github.com/AbleEng/pyexperian',
    'download_url': 'https://github.com/AbleEng/pyexperian',
    'author_email': 'carlos@hiable.com',
    'version': '0.1',
    'install_requires': ['nose', 'requests', 'xmltodict'],
    'packages': ['pyexperian', 'pyexperian.test', 'pyexperian.lib'],
    'scripts': [],
    'name': 'pyexperian'
}

setup(**config)