from setuptools import setup

setup(
    name="django-filepicker-urlfield",
    version="0.0.1",
    description="Convenience model field for downloading files from filepicker.io and uploading them to the media storage.",
    long_description=open("README.md").read(),
    keywords="django, filepicker",
    author="Jared Morse",
    author_email="jarcoal@gmail.com",
    url="https://github.com/jarcoal/django-filepicker-urlfield",
    license="MIT",
    packages=["fpurlfield"],
    install_requires=['django', 'requests'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
)