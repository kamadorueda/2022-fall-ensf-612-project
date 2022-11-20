import glob
import json


def main() -> None:
    issue_numbers = []
    for issue_path in glob.glob("step-1-structured-data/issues/*.json"):
        with open(issue_path, mode="r", encoding="utf-8") as issues_file:
            issue = json.load(issues_file)
        issue_numbers.append(issue["number"])

    issue_numbers.sort(reverse=True)
    with open(
        "step-1-structured-data/issue-numbers.json",
        mode="w",
        encoding="utf-8",
    ) as file:
        json.dump(issue_numbers, file, indent=2, sort_keys=True)


if __name__ == "__main__":
    main()
