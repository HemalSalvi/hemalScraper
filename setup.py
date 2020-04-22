from setuptools import setup, find_packages

setup(
    name='hemalScraper',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A simple webscraper for tracking web data.',
    long_description=open('README.md').read(),
    install_requires=['bs4', 'pandas', 'requests'],
    url='unspecified',
    author='Hemal Salvi',
    author_email='hemal.salvi@utdallas.edu'
)