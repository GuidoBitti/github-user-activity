import argparse
from github_activity import get_activity

parser = argparse.ArgumentParser(description="GitHub activity")

parser.add_argument("username", type=str, help="username")

args = parser.parse_args()

TYPES = {
    "PushEvent": "pushed commits to ",
    "PullRequestEvent": "opened, closed, or merged a pull request at ",
    "CommitCommentEvent": "commented on a commit at ",
    "CreateEvent": "commented on a commit at ",
    "CreateEvent": "created a repository, branch, or tag at ",
    "DeleteEvent": "deleted a branch or tag on ",
    "ForkEvent": "forked ",
    "WatchEvent": "starred ",
    "IssuesEvent": "stopened, closed, or edited an issue at ",
    "IssueCommentEvents": "commented on an issue at ",
    "PullRequestReviewEvent": "submitted a review on a pull request at ",
    "PullRequestReviewCommentEvent": "commented on a pull request review at ",
    "PublicEvent":	"made a repository public at ",
    "GollumEvent":	"created or updated wiki pages at ",
    "ReleaseEvent":	"published, edited, or deleted a release at ",
    "MemberEvent":	"was added/removed as a collaborator at ",
    "RepositoryEvent":	"renamed, archived, transferred, or made public ",
    "TeamAddEvent":	"was added to a team",
    "DeploymentEvent":	"created a deployment at ",
    "DeploymentStatusEvent": "updated the status of a deployment at ",
    "StatusEvent":	"updated the status of a commit at ",
    "CheckRunEvent":	"created, rerequested, completed, etc., a check run at ",
    "CheckSuiteEvent":	"created, rerequested, or completed a check suite at ",
    "CodeScanningAlertEvent":	"created, fixed, or reopened a code scanning alert at ",
    "PackageEvent":	"published, updated, or deleted a package at ",
}

if __name__=="__main__":
    username = args.username
    activity = get_activity(username)
    i=0
    for act in activity:
        activity_type = TYPES[act["type"]] if act["type"] in TYPES else act["type"]
        url = act["repo"]["url"].split("/")
        repo = f"{url[-2]}/{url[-1]}"
        print(f"{username} {activity_type}{repo}")
