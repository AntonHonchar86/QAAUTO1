import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_non_exists(github_api):
    r = github_api.get_user("butenkosergii")

    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")
    print(r)
    assert r["total_count"] == 42
    assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("sergiibutenko_repo_non_exist")
    assert r["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo("s")
    assert r["total_count"] != 0


# Individual tests


@pytest.mark.api_my
def test_check_all_users(github_api):
    r = github_api.list_users()

    assert "mojombo" in r[0]["login"]


@pytest.mark.api_my
def test_check_list_emojis(github_api):
    r = github_api.get_emojis()

    assert "zzz" in r


@pytest.mark.api_my
def test_check_list_commits(github_api):
    r = github_api.get_list_commits("mojombo", "asteroids")

    assert "Tom Preston-Werner" in r[0]["commit"]["author"]["name"]


@pytest.mark.api_my
def test_commit_can_be_found(github_api):
    r = github_api.get_list_commits("mojombo", "asteroids")
    sha = r[0]["sha"]
    r = github_api.get_commit("mojombo", "asteroids", sha)

    assert r["commit"]["author"]["name"] == "Tom Preston-Werner"


@pytest.mark.api_my
def test_get_list_comments(github_api):
    r = github_api.get_list_comments("mojombo", "asteroids")

    assert "Anton" in r[0]["user"]["login"]


@pytest.mark.api_my
def test_commit_comment_can_be_found(github_api):
    r = github_api.get_list_comments("mojombo", "asteroids")
    comment_id = r[0]["id"]
    r = github_api.get_commit_comment("mojombo", "asteroids", comment_id)

    assert r["body"] == "Comment"


@pytest.mark.api_my
def test_get_list_repo_issues(github_api):
    r = github_api.get_list_repo_issues(
        "mojombo",
        "asteroids",
    )

    assert "Deprecated Atom" in r[0]["title"]
