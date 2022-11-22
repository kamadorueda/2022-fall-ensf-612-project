import glob
import json


def main() -> None:
    for issues_path in sorted(glob.glob("step-0-raw-data/issues/*.json")):
        with open(issues_path, mode="r", encoding="utf-8") as issues_file:
            issues = json.load(issues_file)

        for issue in issues:
            if "pull_request" in issue:
                continue

            print(issue["number"])
            issue = {
                "_url": f"https://github.com/PowerShell/PowerShell/issues/{issue['number']}",
                "number": issue["number"],
                "state": issue["state"],
                "title": issue["title"],
                "body": issue["body"],
                "created_at": issue["created_at"],
                "closed_at": issue["closed_at"],
                "updated_at": issue["updated_at"],
                "author": issue["user"]["login"],
                "labels": [label["name"] for label in issue["labels"]],
                "comments": [],
            }

            for comments_path in sorted(
                glob.glob(
                    f"step-0-raw-data/comments/issue-{issue['number']}-page-*.json"
                )
            ):
                print(f"  {comments_path}")
                with open(
                    comments_path, mode="r", encoding="utf-8"
                ) as comments_file:
                    comments = json.load(comments_file)

                for comment in comments:
                    issue["comments"].append(
                        {
                            "author_association": comment[
                                "author_association"
                            ],
                            "body": comment["body"],
                            "created_at": comment["created_at"],
                            "updated_at": comment["updated_at"],
                            "author": comment["user"]["login"],
                        }
                    )

            with open(
                f"step-1-structured-data/issues/{issue['number']}.json",
                mode="w",
                encoding="utf-8",
            ) as issue_file:
                json.dump(issue, issue_file, indent=2, sort_keys=True)


if __name__ == "__main__":
    main()
