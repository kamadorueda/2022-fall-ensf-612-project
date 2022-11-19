import csv
import glob
import json

COLUMN_URL = "URL"
COLUMN_WAS_FIXED = "Was fixed? (yes/no)"


def main() -> None:
    with open(
        "step-1-structured-data/issue-numbers.json",
        mode="r",
        encoding="utf-8",
    ) as file:
        issue_numbers = json.load(file)

    with open(
        "step-2-labeling/labels.csv", mode="w", encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[COLUMN_URL, COLUMN_WAS_FIXED],
            quoting=csv.QUOTE_NONNUMERIC,
        )
        writer.writeheader()

        for issue_number in issue_numbers:
            with open(
                f"step-1-structured-data/issues/{issue_number}.json",
                mode="r",
                encoding="utf-8",
            ) as file:
                issue = json.load(file)

            if issue["state"] == "closed":
                writer.writerow(
                    {
                        COLUMN_URL: issue["_url"],
                        COLUMN_WAS_FIXED: "",
                    }
                )


if __name__ == "__main__":
    main()
