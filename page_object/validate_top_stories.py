"""
This class validates the top stories GET call.
"""

class ValidateTopStories:
    def __init__(self, response):
        self.response = response
        self.response_length = 500
    
    def validate_top_stories_length(self):
        # validate response lengh should be 500
        assert len(self.response) == self.response_length
    
    def validate_top_stories_instance(self):
        for item in self.response:
            assert isinstance(item, int), f'Top Stories item is not int {item}'
    