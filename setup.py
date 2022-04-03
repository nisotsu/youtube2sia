from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='youtube2sia',
    version='1.0',
    description='YouTubeから動画をダウンロードし,Siaネットワークのポータルへアップロードします.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['siaskynet','yt_dlp'],
    author='nisotsu',
    url='https://github.com/nisotsu/youtube2sia',
    packages=find_packages(),
    entry_points = {
        'console_scripts': ['youtube2sia=youtube2sia.youtube2sia:main'],
    }
)