import vk_api
import networkx as nx

class VK:
    def __init__(self, credentials):
        self.session = self.auth(credentials)
        self.api = self.session.get_api()
        self.major_fields = ['uid' ,'first_name', 'last_name', 'deactivated',\
            'sex', 'bdate', 'city', 'country', 'home_town', 'domain', 'contacts',\
            'site', 'education', 'universities', 'schools', 'status', 'last_seen',\
            'followers_count', 'common_count', 'counters', 'occupation', 'nickname',\
            'relatives', 'relation', 'personal', 'connections', 'exports', 'activities',\
            'interests', 'music', 'movies', 'tv', 'books', 'games', 'about', 'quotes',\
            'timezone', 'screen_name']

    def auth(self, credentials):
        if 'login' in credentials:
            session = vk_api.VkApi(credentials['login'], credentials['password'])
            session.auth(token_only=True)
        elif 'client_secret' in credentials:
            session = vk_api.VkApi(app_id=credentials['app_id'], client_secret=credentials['client_secret'])
            session.auth(token_only=True)
        elif 'token' in credentials:
            session = vk_api.VkApi(token=credentials['token'])
        return session
        
    def get_graph_of_users_and_his_friends(self, user_id, number=1):
        friends = nx.Graph()
        previous_friends = {user_id}
        current_friends = set()
        for i in range(number):
            for friend in previous_friends:
                try:
                    new_friends = self.api.friends.get(user_id=friend)['items']
                    current_friends.update(new_friends)
                    friends.add_edges_from([(friend, i) for i in new_friends])
                except:
                    print(friend)
            previous_friends = current_friends
            current_friends = set()

        batch_size = 256
        friends_nodes = list(friends)
        for batch in [friends_nodes[i:i+batch_size] for i in range(0, len(friends_nodes), batch_size)]:
            data = self.api.users.get(user_ids=batch, fields=self.major_fields)
            nx.set_node_attributes(friends, {k:v for k, v in zip(batch, data)})
        return friends

    def get_graph_of_users_and_his_friends_pool(self, user_id, number=1):
        friends = nx.Graph()
        previous_friends = {user_id}
        current_friends = set()
        for i in range(number):
            new_friends, errors = vk_api.vk_request_one_param_pool(
                self.session,
                'friends.get', 
                key='user_id',
                values=list(previous_friends)
            )
            for core_friend, list_friends in new_friends.items():
                list_friends = list_friends['items']
                current_friends.update(list_friends)
                friends.add_edges_from([(core_friend, i) for i in list_friends])
            previous_friends = current_friends
            current_friends = set()

        batch_size = 1000
        friends_nodes = list(friends)
        for batch in [friends_nodes[i:i+batch_size] for i in range(0, len(friends_nodes), batch_size)]:
            data = self.api.users.get(user_ids=batch, fields=self.major_fields)
            nx.set_node_attributes(friends, {k:v for k, v in zip(batch, data)})
       
        return friends
        