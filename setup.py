from distutils.core import setup

setup(
    name = 'indeedpy',
    version = open("./VERSION").read(),
    description = 'Indeed Job Search Python Api Client',
    author = 'Chad Masso',
    author_email = 'labs-team@indeed.com',
    packages = ['indeedpy'],
    install_requires=['requests==0.14.1']
)
