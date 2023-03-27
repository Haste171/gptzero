# GPTZero API Wrapper
![PyPi](https://github.com/Haste171/gptzero/actions/workflows/pypi_upload.yml/badge.svg)  
![Build](https://github.com/Haste171/gptzero/actions/workflows/build.yml/badge.svg)  
  
[![PyPi version](https://badgen.net/pypi/v/gptzero/)](https://pypi.org/project/gptzero)  
[![Latest release](https://badgen.net/github/release/Haste171/gptzero)](https://github.com/Haste171/gptzero/releases)  
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Haste171/gptzero/graphs/commit-activity)  
[![GitHub license](https://img.shields.io/github/license/Haste171/gptzero)](https://github.com/Haste171/gptzero/blob/master/LICENSE)  
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)  
  

This is a Python wrapper for the GPTZero API, which allows you to generate natural language text using GPT technology. This wrapper provides a simple way to interact with the GPTZero API using Python.

Featured on https://gptzero.me/docs

## Getting started

To use the GPTZero API, you'll need to have an API key. If you don't have an API key yet, you can sign up for one on the [GPTZero website](https://gptzero.me/).

Once you have your API key, you can install the `gptzero` package and use it.


```python
from gptzero import GPTZeroAPI

api_key = 'your_api_key_here' # Your API Key from https://gptzero.me
gptzero_api = GPTZeroAPI(api_key)
```

### Making a text prediction
```python
document = 'Hello world!'
response = gptzero_api.text_predict(document)
print(response)
```

### Making a file prediction
```python
file_path = 'path/to/your/file'
response = gptzero_api.file_predict(file_path)
print(response)
```
