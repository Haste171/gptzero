from setuptools import setup, find_packages

setup(
    name='gptzero-async',
    version='0.1.1',
    description='Asynchronous Python wrapper for the GPTZero API',
    authors=[
        {"David Peterson", "dapanon@proton.me"},
        {"Leo Ghanem", "crspy8687@gmail.com"}
    ],
    url='https://github.com/Haste171/gptzero/tree/async',
    packages=find_packages(),
    install_requires=['aiohttp'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)

