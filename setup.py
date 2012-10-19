from distutils.core import setup

setup(
    name = 'indeed',
    version = '0.0.3',
    description = 'Indeed Job Search Python Api Client',
    author = 'Indeed Labs',
    author_email = 'labs-team@indeed.com',
    packages = ['indeed'],
    install_requires=['requests==0.14.1'],
    url = "https://github.com/indeedlabs/indeed-python",
)
