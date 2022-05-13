from pathlib import Path

from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='apple_searchads_api',
    description='Apple SearchAds API non-official python library',
    version='1.6.0',
    url='https://github.com/dapanas/searchads_api',
    author='Abdul Majeed Alkattan',
    author_email='alkattan@phiture.com',
    packages=["searchads_api"],
    keywords=['python', 'searchads', 'library'],
    install_requires=['requests>=2.27.1', 'PyJWT==2.4.0', 'cryptography==3.4.8'],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
