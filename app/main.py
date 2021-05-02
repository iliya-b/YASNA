import yaml
import vk_api

def main():
    credentials = yaml.safe_load(open('credentials.yml').read())
    login, password = credentials['login'], credentials['password']
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    tools = vk_api.VkTools(vk_session)
    wall = tools.get_all('wall.get', 100, {'owner_id': 1})
    print('Posts count:', wall['count'])

    if wall['count']:
        print('First post:', wall['items'][0], '\n')

    if wall['count'] > 1:
        print('Last post:', wall['items'][-1])


if __name__ == '__main__':
    main()