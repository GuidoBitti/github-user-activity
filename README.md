# GitHub Activity CLI

A simple Python command-line tool to fetch and display recent public activity from a GitHub user using the GitHub REST API — **without using any external libraries**.

---

## 🌐 Inspired by roadmap.sh
This project is based on the GitHub User Activity challenge from roadmap.sh, which guides you through building a CLI tool that consumes the GitHub API and shows recent activity in the terminal.

Check the original challenge here:
[roadmap.sh/projects/github-user-activity](https://roadmap.sh/projects/github-user-activity)

---

## 🛠️ Requirements

- Python 3.x
- No external libraries required (uses only the Python standard library)

---

## 📁 Project Structure

```
.
├── main.py               # CLI entry point
└── github_activity.py    # Fetches GitHub events via urllib
```

---

## ▶️ Usage

Run the script from the command line:

```bash
python main.py <github_username>
```

# 💡 Example of input
```bash
python main.py torvalds
```
# ➡️ Example of output

```bash
torvalds pushed commits to torvalds/1590A
torvalds pushed commits to torvalds/1590A
torvalds pushed commits to torvalds/linux
torvalds created a repository, branch, or tag at torvalds/linux
torvalds pushed commits to torvalds/linux
torvalds pushed commits to torvalds/1590A
torvalds pushed commits to torvalds/linux
torvalds pushed commits to torvalds/linux
torvalds pushed commits to torvalds/linux
torvalds pushed commits to torvalds/linux
torvalds pushed commits to torvalds/linux
torvalds pushed commits to torvalds/linux
torvalds pushed commits to torvalds/linux
torvalds pushed commits to torvalds/1590A
torvalds pushed commits to torvalds/linux
torvalds IssueCommentEventtorvalds/1590A
torvalds pushed commits to torvalds/linux
torvalds pushed commits to torvalds/1590A
torvalds IssueCommentEventtorvalds/1590A
torvalds pushed commits to torvalds/linux
torvalds IssueCommentEventtorvalds/1590A
torvalds opened, closed, or merged a pull request at torvalds/1590A
torvalds published, edited, or deleted a release at torvalds/1590A
torvalds created a repository, branch, or tag at torvalds/1590A
torvalds stopened, closed, or edited an issue at torvalds/1590A
torvalds IssueCommentEventtorvalds/1590A
torvalds pushed commits to torvalds/linux
torvalds pushed commits to torvalds/1590A
torvalds pushed commits to torvalds/linux
torvalds pushed commits to torvalds/linux
```

