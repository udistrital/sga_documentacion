import datetime
import os
from github import Github

token = os.environ.get('GITHUB_TOKEN')

gh = Github(token)

org = gh.get_organization('udistrital')

""" for team in org.get_teams(): # para listar ids de teams
    print(team.name, team.id) """

team = org.get_team(3227786) # id team Académica

repos = team.get_repos()

fecha_actual = datetime.datetime.now()
fecha_actual = fecha_actual.strftime("%d/%m/%Y")

readme_content = "## Pull Requests Activos a la fecha: " + fecha_actual + "\n\n"
print(readme_content)

for repo in repos:
    open_pulls = repo.get_pulls(state='open')
    print(repo.name, open_pulls.totalCount)
    if open_pulls.totalCount > 0:
        readme_content += f"---\n### {repo.name}\n"
        for pull in open_pulls:
            readme_content += f"- {pull.title} ({pull.html_url}) | **{pull.user.login}**\n"

print(" ")
print(readme_content)
# save to readme.md
with open('README.md', 'w') as f:
    f.write(readme_content)
