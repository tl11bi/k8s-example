from setuptools import setup

setup(
    name='python-flask-sample-app',
    version='1.0',
    long_description=__doc__,
    packages=['src'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)