import requests
import random
from selenium import webdriver


# API testing
# 1.
def test_check_repositories_exist():
    username = "avielb"
    min_repos = 5
    check_repositories_exist(username, min_repos)


def check_repositories_exist(username, min_repos=5):
    url = f'https://api.github.com/users/{username}/repos'
    response = requests.get(url)

    assert response.status_code == 200, f"Error: Unable to fetch data for {username}"

    repositories = response.json()
    assert len(repositories) >= min_repos, f"{username} does not have enough repositories. Found {len(repositories)} repositories."


# 2.
def test_get_age_for_name():
    num_names = 3
    random_names = generate_random_names(num_names)

    for name in random_names:
        age = get_age_for_name(name)
        assert age is not None and 0 <= age <= 120, f"The age for {name} is not within the valid range"


def get_age_for_name(name):
    url = f'https://api.agify.io/?name={name}'
    response = requests.get(url)

    assert response.status_code == 200, f"Error: Unable to fetch data for {name}"

    data = response.json()
    age = data.get('age')
    return age


def generate_random_names(num_names):
    names = ["Amit", "Matt", "Jack", "Ramy", "Koby", "Jonathan", "Chris", "Kim", "Niv", "Adva"]
    return random.sample(names, num_names)


# 3.
def test_check_universities():
    country = "Israel"
    check_universities(country)


def check_universities(country):
    url = f'http://universities.hipolabs.com/search?country={country}'
    response = requests.get(url)

    assert response.status_code == 200, f"Error: Unable to fetch universities data for {country}"

    repositories = response.json()
    unis = [repo['name'] for repo in repositories if 'University' in repo.get('name', '')]

    assert len(unis) >= 5, f"Expected at least 5 universities in {country}, but found {len(unis)}."

    print(f'Found {len(unis)} universities in {country}')


if __name__ == "__main__":
    test_check_repositories_exist()
    test_get_age_for_name()
    test_check_universities()

# UI testing
# 4.
driver1 = webdriver.Chrome()
driver1.get("https://www.ycombinator.com")

assert driver1.title == 'Y Combinator'

# 5.
driver2 = webdriver.Chrome()
driver2.get("https://hub.docker.com")

assert driver2.title == 'Docker Hub Container Image Library | App Containerization'
# For some reason the it sends assert false, even though the title is the same


