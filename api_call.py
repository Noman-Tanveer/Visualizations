
import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
# print("Status code: ", r.status_code)

response_dict = r.json()
# print(response_dict.keys())
repo_dicts = response_dict['items']
# print("Total repositories:", response_dict['total_count'])
# print("Repositories returned:", len(repo_dicts))

repo_dict = repo_dicts[0]
# print("\nKeys:", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print('', end='')

# for repo_dict in repo_dicts:
#     print('Name' , repo_dict['name'])
#     print('Stars', repo_dict['stargazers_count'])
#     print('Owner', repo_dict['owner']['login'])
#     print('Link', repo_dict['html_url'])
#     print('Description', repo_dict['description'])

import pygal
from pygal.style import LightColorizedStyle as LCS , LightenStyle as LS

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

my_style = LS('#333399', Base_style = LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 36
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style)

# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']
plot_dicts = [
{'value': 16101, 'label': 'Description of httpie.'},
{'value': 15028, 'label': 'Description of django.'},
{'value': 14798, 'label': 'Description of flask.'},
]
chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')
