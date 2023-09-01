import requests
import os


class GitHub:
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {os.environ.get('GITHUB_TOKEN', None)}",
    }

    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories", params={"q": name}
        )
        body = r.json()

        return body

    def list_users(self):
        r = requests.get("https://api.github.com/users")
        body = r.json()

        return body

    # Individual methods

    def get_emojis(self):
        r = requests.get("https://api.github.com/emojis")
        body = r.json()

        return body

    def get_list_commits(self, username, reponame):
        r = requests.get(f"https://api.github.com/repos/{username}/{reponame}/commits")
        body = r.json()

        return body

    def get_commit(self, username, reponame, sha):
        r = requests.get(
            f"https://api.github.com/repos/{username}/{reponame}/commits/{sha}"
        )
        body = r.json()
        return body

    def get_list_comments(self, username, reponame):
        r = requests.get(f"https://api.github.com/repos/{username}/{reponame}/comments")
        body = r.json()

        return body

    def get_commit_comment(self, username, reponame, com_id):
        r = requests.get(
            f"https://api.github.com/repos/{username}/{reponame}/comments/{com_id}"
        )
        body = r.json()

        return body

    def get_list_repo_issues(self, username, reponame):
        r = requests.get(f"https://api.github.com/repos/{username}/{reponame}/issues")
        body = r.json()

        return body
