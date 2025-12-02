from dataclasses import dataclass

"""
This class will validate that all comments are string and not none
"""
class ValidateStoryComments:
    def __init__(self, response):
        self.response = response
        # self.comments = StoryComment(**response)
    

    def validate_story_comment(self):
        for key, values in self.response.items():
            assert isinstance(key, str)
            assert isinstance(values, dict)

            for inner_key, inner_value in values.items():
                assert isinstance(inner_key, str) 
                assert isinstance(inner_value, str) and inner_value != None