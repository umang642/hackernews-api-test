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

##  Run Tests
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


## Found bugs too
- Kids and URLs are missing in Few Top Stories Details.

```
test_top_stories.py::test_top_stories PASSED                                                                                          [ 33%]
test_top_stories.py::test_top_stories_details FAILED                                                                                  [ 66%]
test_top_stories.py::test_top_comment_from_story PASSED                                                                               [100%]

================================================================= FAILURES ==================================================================
_________________________________________________________ test_top_stories_details __________________________________________________________

retrive_top_stories_details = {'46045643': {'by': 'speckx', 'descendants': 19, 'id': 46045643, 'kids': [46105630, 46104504, 46105033, 46116237, 4610... ...}, '46054471': {'by': 'keyle', 'descendants': 9, 'id': 46054471, 'kids': [46111474, 46111291, 46110973], ...}, ...}

    @pytest.mark.regression
    def test_top_stories_details(retrive_top_stories_details):
        all_top_stories_details = retrive_top_stories_details
        top_story_details_obj = ValidateTopStoryDetails(response=all_top_stories_details)
>       top_story_details_obj.validate_story_instance()

test_top_stories.py:70: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <page_object.validate_top_story_details.ValidateTopStoryDetails object at 0x106e27770>

    def validate_story_instance(self):
        for _, value in self.response.items():
            assert value['id'] is not None
            assert isinstance(value['id'], int)
    
            # get the kids parameter
            kids = value.get('kids')
            if kids is None:
                raise AssertionError(f'Kids parameter is missing in story details - {value}')
            else:
                assert isinstance(kids, list)
    
            assert value['title'] is not None
            assert value['type'] == constants.STORY
    
            url_pattern = r'https?://[^\s]+'
            url = value.get('url')
            if url is None:
>               raise AssertionError(f'URL is missing in story details - {value}')
```