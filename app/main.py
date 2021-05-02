import yaml
from VK import VK

def main():
    credentials = yaml.safe_load(open('credentials.yml').read())
    login, password = credentials['login'], credentials['password']
    vk_session = VK(login, password)

    wall = vk_session.get_data_about_user_and_all_friends('444597545')
    print(wall[0])

if __name__ == '__main__':
    main()