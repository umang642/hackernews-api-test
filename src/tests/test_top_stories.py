import pytest
from lib import constants
import requests
from page_object.validate_top_stories import ValidateTopStories
from page_object.validate_top_story_details import ValidateTopStoryDetails
from page_object.validate_story_comments import ValidateStoryComments

"""
This fixure is calling TopStory GET Call.
"""
@pytest.fixture(scope='module')
def top_stories_api_request():
    url = constants.HACKER_RANK_DOMAIN + constants.TOP_STORIES_API
    response = requests.get(url=url, headers=constants.HEADERS)
    assert response.ok, f"API failed. body: {response.json()}"
    return response.json()

"""
This fixture is calling Top Stories Details using Item GET call.
"""
@pytest.fixture(scope='module')
def retrive_top_stories_details(top_stories_api_request):
    response = top_stories_api_request
    all_top_stories = {}
    for item in response[:100]:
        # get call the item api and get the top news details.
        url = constants.HACKER_RANK_DOMAIN + constants.ITEM_API + str(item) +'.json'
        response = requests.get(url=url, headers=constants.HEADERS)
        assert response.ok, f"API failed. body: {response.json()}"
        data = response.json()
        all_top_stories[str(item)] = data
    
    return all_top_stories

"""
This fixutre is going to get the Top Comment from story. GET call on Item API.
"""
@pytest.fixture(scope='module')
def retrive_top_comment_from_story(retrive_top_stories_details):
    top_stories = retrive_top_stories_details
    top_comment = {}
    for key, value in top_stories.items():
        if 'kids' in value:
            comment_id = value['kids'][0]
            title = value['title']

            comment_url = constants.HACKER_RANK_DOMAIN + constants.ITEM_API + str(comment_id) +'.json'
            response = requests.get(url=comment_url, headers=constants.HEADERS)
            assert response.ok, f"API failed. body: {response.json()}"
            comment_data = response.json()
            comment = comment_data['text']

            # append this data into a dictonary and return the dictonary
            top_comment[key]= {title:comment}
    
    return top_comment


@pytest.mark.acceptance
def test_top_stories(top_stories_api_request):
    response = top_stories_api_request
    top_story_obj = ValidateTopStories(response = response)
    top_story_obj.validate_top_stories_length()
    top_story_obj.validate_top_stories_instance()
    
@pytest.mark.regression
def test_top_stories_details(retrive_top_stories_details):
    all_top_stories_details = retrive_top_stories_details
    top_story_details_obj = ValidateTopStoryDetails(response=all_top_stories_details)
    top_story_details_obj.validate_story_instance()

@pytest.mark.regression
def test_top_comment_from_story(retrive_top_comment_from_story):
    top_comment = retrive_top_comment_from_story
    story_comment_obj = ValidateStoryComments(response=top_comment)
    story_comment_obj.validate_story_comment()