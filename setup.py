from setuptools import setup

setup(
    name="armycook",
    version="0.0.1",
    packages=['armycook'],
    include_package_data=True,
    install_requires=[
        'click',
        'tweepy'
    ],
    entry_points='''
        [console_scripts]
        armycook=armycook.cli:cli
    ''',

    # metadata to display on PyPI
    author="Travis Shears",
    author_email="t@travisshears.com",
    description="Twitter bot that tweets army recipes",
    license="MIT",
    keywords="twitter bot army recipes",
    # url="http://example.com/HelloWorld/",
    # could also include long_description, download_url, classifiers, etc.
)
