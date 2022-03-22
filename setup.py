from setuptools import setup, find_packages

setup(
    name='xbrl2oracle',
    version='0.1.0',
    url='https://github.com/mahmost/xbrl2oracle.git',
    author='Mahmoud Mostafa',
    author_email='mah@moud.info',
    description='Simple example of parsing xbrl document and storing parts of its data into an oracle database',
    long_description=open('README.md').read(),
    license='MIT',
    packages=find_packages(),
    install_requires=['py-xbrl == 2.1.0', 'cx_Oracl == 8.3.0'],
)
