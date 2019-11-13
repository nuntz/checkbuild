import requests
from os import environ
from datetime import datetime


def last_updated(username, repo):
    url = f"https://hub.docker.com/v2/repositories/{username}/{repo}/tags/latest"
    r = requests.get(url)
    json_data = r.json()
    last_updated_string = json_data["last_updated"]
    if r.status_code == 200:
        return datetime.strptime(last_updated_string, "%Y-%m-%dT%H:%M:%S.%fZ")


def trigger_build(url):
    r = requests.post(url)
    if r.status_code == 200:
        return r.json()


def post_to_slack(url):
    r = requests.post(
        url, json={"text": "Upstream image has changed, triggering new build."}
    )
    if r.status_code == 200:
        return r.text


if __name__ == "__main__":
    if last_updated(
        environ["BASE_USERNAME"], environ["BASE_REPOSITORY"]
    ) > last_updated(environ["MY_USERNAME"], environ["MY_REPOSITORY"]):
        print("The base image was updated!")
        print("Posting notification to Slack...")
        print(post_to_slack(environ["SLACK_WEBHOOK"]))
        print("Triggering a new build...")
        print(trigger_build(environ["BUILD_TRIGGER_URL"]))
    else:
        print("Still current.")
