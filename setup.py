from distutils.core import setup

setup(
    name = 'indeed',
    version = open("./VERSION").read(),
    description = 'Indeed Job Search Python Api Client',
    author = 'Indeed Labs',
    author_email = 'labs-team@indeed.com',
    packages = ['indeed'],
    install_requires=['requests==0.14.1']
)
