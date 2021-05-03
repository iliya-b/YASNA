import yaml
from VK import VK
import networkx as nx
import matplotlib.pyplot as plt

def main():
    credentials = yaml.safe_load(open('credentials.yml').read())
    login, password = credentials['login'], credentials['password']
    vk_session = VK(login, password)

    G = vk_session.get_graph_of_users_and_his_friends(444597545, 1).nodes()
    G_pool = vk_session.get_graph_of_users_and_his_friends_pool(444597545, 1).nodes()
    print(G == G_pool)
if __name__ == '__main__':
    main()