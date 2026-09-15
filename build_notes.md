# Build Notes

## Challenge Overview

EyeDay Validator is a web challenge focused on exploiting a Server-Side Request Forgery (SSRF) vulnerability to access an internal telemetry service and recover sensitive deployment artefacts.

---

## Build Steps

1. Created the public-facing **EyeDay Validator** service.

2. Implemented a URL validation feature that fetches remote resources.

3. Added an internal **Telemetry** service that is only reachable within the Docker network.

4. Configured the validator and telemetry services using Docker Compose.

5. Created a leftover deployment configuration (`config.bak`) that exposes the internal telemetry endpoint.

6. Added telemetry monitoring endpoints:
   - `/`
   - `/health`
   - `/metrics`

7. Created a simulated backup directory containing operational files:
   - `config.json`
   - `runtime.log`
   - `notes.txt`

8. Added a dated backup folder:

```
backup_20260813/
```

9. Populated the backup with realistic deployment artefacts:
   - `backup_manifest.txt`
   - `old.log`
   - `temp/deployment_notes.txt`

10. Stored the challenge flag inside `deployment_notes.txt` to simulate an accidentally retained deployment reference.

11. Verified that the flag is **not directly accessible** from the public validator and can only be retrieved by exploiting the intended SSRF vulnerability.

12. Performed end-to-end testing to ensure the intended solve path is:

```
Recon
→ config.bak
→ SSRF
→ Internal Telemetry
→ Metrics
→ Backup Enumeration
→ Deployment Artefacts
→ Flag
```

---

## Intended Learning Objectives

Participants should demonstrate the ability to:

- Perform web reconnaissance.
- Identify exposed configuration files.
- Recognise and exploit SSRF.
- Enumerate internal services.
- Analyse deployment artefacts.
- Recover sensitive information from exposed backups.

---

## Difficulty

**Category:** Web

**Difficulty:** Beginner / Intermediate

Expected solve time:
**20–40 minutes**
