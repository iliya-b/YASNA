import yaml
import time
from VK import VK
import networkx as nx
import matplotlib.pyplot as plt

def main():
    credentials = yaml.safe_load(open('credentials.yml').read())
    login, password = credentials['login'], credentials['password']
    vk_session = VK(login, password)

    start = time.time()
    G = vk_session.get_graph_of_users_and_his_friends(444597545).nodes()
    end = time.time()
    start_pool = time.time()
    G_pool = vk_session.get_graph_of_users_and_his_friends_pool(444597545).nodes()
    end_pool = time.time()
    print(G == G_pool)
    print(end - start, end_pool - start_pool)
if __name__ == '__main__':
    main()