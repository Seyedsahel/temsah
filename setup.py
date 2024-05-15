from setuptools import setup

setup(
    name='temsah',
    version='2.1.5',
    author='sahel seyedyazdi',
    author_email='seyedsahel1383@gmail.com',
    description='Temsah is a powerful Python library specifically designed for web scraping e-commerce platforms such as Amazon.',
    packages=['temsah'],
    install_requires=[
       'requests','BeautifulSoup4','chardet'    ],
)