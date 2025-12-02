# hackernews-api-test
Validate Hacker News Public API.

## Environment

* Python - 3.8
* Install pytest (pip3 install pytest)

&nbsp;

## Setup
```
git clone https://github.com/umang642/hackernews-api-test.git
```

&nbsp;

##  Run Tests against Gamma Skyfire
1. cd to tests root
   - cd to `src/tests/`
2. Run the following command to start the test

#### Run below command for test_top_stories
- `pytest -s -vv test_top_stories.py`

#### Run below command to run any specific test suites.
- `pytest -s -vv -m regression`
- `pytest -s -vv -m acceptance`


## Package Structure:
- `src/lib`: have a common library and util methods. In future, if we want to add any AWS architecture or any other AI tool injection, we can use this layer to add. 
- `src/page_object`: have POM test framework. This folder will contain testing business logic.
- `src/tests`: this folder will have a test files. As well we have conftest.py (why we need this? added comment in file) as well pytest.ini (this file will contain all markers).
- `setup.py`: this file we need in future to integrate this autoamtion framework to pipeline for CI/CD.


