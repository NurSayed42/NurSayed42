"""Refresh the "Recently active" block in README.md.

Lists the most recently pushed public, non-fork, non-archived repositories
that have a description. Uses only the GitHub REST API (no third-party service).
"""
import datetime, json, os, re, urllib.request

USER = os.environ.get("GH_USER", "NurSayed42")
LIMIT = 4
START, END = "<!-- ACTIVITY:START -->", "<!-- ACTIVITY:END -->"

req = urllib.request.Request(
    f"https://api.github.com/users/{USER}/repos?per_page=100&sort=pushed&type=owner",
    headers={"Accept": "application/vnd.github+json",
             **({"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"} if os.environ.get("GITHUB_TOKEN") else {})},
)
repos = json.load(urllib.request.urlopen(req))
picked = [r for r in repos
          if not r["fork"] and not r["archived"] and not r["private"]
          and r.get("description") and r["name"].lower() != USER.lower()][:LIMIT]

def row(r):
    pushed = datetime.datetime.strptime(r["pushed_at"][:10], "%Y-%m-%d").strftime("%b %Y")
    return f"| [{r['name']}]({r['html_url']}) | {r['description']} | {pushed} |"

block = "\n".join([START, "| Repository | Description | Last push |", "|---|---|---|",
                   *map(row, picked), END])
path = "README.md"
text = open(path, encoding="utf-8").read()
new = re.sub(re.escape(START) + r".*?" + re.escape(END), block, text, flags=re.S)
if new != text:
    open(path, "w", encoding="utf-8").write(new)
    print("README updated")
else:
    print("No change")
