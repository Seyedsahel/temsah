from setuptools import setup

setup(
    name='temsah',
    version='1.1.1',
    author='sahel seyedyazdi',
    author_email='seyedsahel1383@gmail.com',
    description='Temsah is a powerful Python library specifically designed for web scraping e-commerce platforms such as Amazon.',
    packages=['temsah'],
    install_requires=[
       'requests','BeautifulSoup4','chardet'    ],
)