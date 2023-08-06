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


@pytest.mark.api
def test_check_all_users(github_api):
    r = github_api.list_users()
    assert "mojombo" in r[0]["login"]


@pytest.mark.api
def test_check_list_emojis(github_api):
    r = github_api.get_emojis()
    assert "zzz" in r
    assert (
        r.get("+1")
        == "https://github.githubassets.com/images/icons/emoji/unicode/1f44d.png?v8"
    )


@pytest.mark.api
def test_check_list_commits(github_api):
    r = github_api.get_list_commits("mojombo", "asteroids")
    assert "Tom Preston-Werner" in r[0]["commit"]["author"]["name"]
    print(r[0])


@pytest.mark.api
def test_commit_can_be_found(github_api):
    r = github_api.get_commit(
        "mojombo", "asteroids", "96cb01e8cdcc39d6c411805dddd60bf1e41eb8f9"
    )
    assert r["commit"]["author"]["name"] == "Tom Preston-Werner"


@pytest.mark.api
def test_get_list_comments(github_api):
    r = github_api.get_list_comments("mojombo", "asteroids")
    print(r[0]["id"])
    assert "Anton" in r[0]["user"]["login"]


@pytest.mark.api
def test_commit_comment_can_be_found(github_api):
    r = github_api.get_commit_comment("mojombo", "asteroids", 122974012)
    print(r)
    assert r["body"] == "Comment"


@pytest.mark.api
def test_delete_commit_comment(github_api):
    r = github_api.delete_commit_comment("mojombo", "asteroids", 122974012)
    print(r)
    r = github_api.get_commit_comment("mojombo", "asteroids", 122974012)


@pytest.mark.api
def test_commit_comment_can_be_create(github_api):
    r = github_api.create_commit_comment()
    print(r)


@pytest.mark.api
def test_get_list_repo_issues(github_api):
    r = github_api.get_list_repo_issues("mojombo", "asteroids")
    print(r)
    assert "Deprecated Atom" in r[0]["title"]
