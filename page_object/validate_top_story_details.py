from dataclasses import dataclass
from lib import constants
import re

"""
This class validate the detail parameters of Top Stories.
"""

class ValidateTopStoryDetails:
    def __init__(self, response):
        self.response = response
    
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
                raise AssertionError(f'URL is missing in story details - {value}')
            else:
                assert re.match(url_pattern, value['url']), f'Failed!! expected is {value['url']}'
