from setuptools import setup, find_packages

setup(
    name='dirgen',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        dirgen=__init__:generate_directories
    ''',
    author="Jean-Paul Fiorini",
    maintainer="Jean-Paul Fiorini"
)
