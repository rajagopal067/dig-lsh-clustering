try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = {
    'name': 'dig-lsh-clustering',
    'description': 'code to cluster based on lsh algorithm',
    'author': 'Dipsy Kapoor',
    'url': 'https://github.com/usc-isi-i2/dig-lsh-clustering.git',
    'download_url': 'https://github.com/usc-isi-i2/dig-lsh-clustering.git',
    'author_email': 'dipsykapoor@gmail.com',
    'install_requires': ['nose2',
                         'digSparkUtil',
                         'jq'],
    # dependency_links=['http://github.com/user/repo/tarball/master#egg=package-1.0']
    # these are the (sub)modules of the current directory that we care about
    'packages': ['hasher', 'hasher.old', 'hasher.lsh','gen_int_input','clusterer','clusterer.old','utils'],
    'scripts': []
}

setup(**config)
