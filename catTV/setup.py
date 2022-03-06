from setuptools import setup

setup(
    name='catTV',
    packages=['catTV'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-bootstrap'
    ],
)