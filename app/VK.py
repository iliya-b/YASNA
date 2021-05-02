import vk_api

class VK:
    def __init__(self, login, password):
        self.session = self.auth(login, password)
        self.tools = vk_api.VkTools(self.session)
        self.api = self.session.get_api()
        self.major_fields = ['uid' ,'first_name', 'last_name', 'deactivated',\
            'sex', 'bdate', 'city', 'country', 'home_town', 'domain', 'contacts',\
            'site', 'education', 'universities', 'schools', 'status', 'last_seen',\
            'followers_count', 'common_count', 'counters', 'occupation', 'nickname',\
            'relatives', 'relation', 'personal', 'connections', 'exports', 'activities',\
            'interests', 'music', 'movies', 'tv', 'books', 'games', 'about', 'quotes',\
            'timezone', 'screen_name']

    def auth(self, login, password):
        session = vk_api.VkApi(login, password)
        session.auth(token_only=True)
        return session

    def get_data_about_user_and_all_friends(self, user_id):
        response_get_user = self.api.users.get(user_ids=user_id, fields=self.major_fields)
        response_get_friends = self.api.friends.get(user_id=user_id, fields=self.major_fields)
        if response_get_user and 'items' in response_get_friends:
            return response_get_user + response_get_friends['items']
        return response_get_friends