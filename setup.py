from setuptools import setup, find_packages
import reveal

setup(
    name="reveal",
    version=reveal.__version__,
    description='Utility tracking user access to contact details and links.',
    long_description=open('README.rst').read(),
    license='BSD License',
    platforms=['OS Independent'],
    keywords='access control',
    author='F. Malina',
    author_email='fmalina@gmail.com',
    url="https://github.com/fmalina/django-reveal",
    packages=find_packages(),
    include_package_data=True,
    install_requires=open('requirements.txt').read().split(),
)
