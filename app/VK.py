import vk_api

class VK:
    def __init__(self, login, password):
        self.session = self.auth(login, password)
        self.tools = vk_api.VkTools(self.session)

    def auth(self, login, password):
        session = vk_api.VkApi(login, password)
        session.auth(token_only=True)
        return session

    def get_all_friends(self, user_id):
        response = self.tools.get_all('friends.get', 100, {'user_id': user_id, 'fields': ['city' ,'domain']})
        if 'items' in response:
            return response['items']