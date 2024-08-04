from setuptools import setup, find_packages

# Read the content of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='cinagu',
    version='0.1.3',
    description='A Python package for detecting cheats and hacks in various games.',
    author='Quy Anh Nguyen',
    author_email='quyanh082013@gmail.com',
    url='',
    packages=find_packages(),
    install_requires=[
        "chess"
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    long_description=long_description,
    long_description_content_type='text/markdown',
)
