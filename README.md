# EyeDay Validator

| Key | Value |
| --- | --- |
| Challenge Name | EyeDay Validator |
| Author | raephrod-ite |
| Category | Web |
| Description | Can you reach what was never meant to be exposed? |
| Challenge Type | Dynamic |
| Docker Image | |
| Flag | sunctf26{s3rv3r_s1d3_r3qu3st_f0rg3ry_byp4ss3d_v14_0x7f000001_dNS_r3b1nd} |
| Score | 200 |

The challenge runs using Docker Compose inside the `src/` directory.

---

## Challenge Scenario

EyeDay recently deployed a URL validation service for internal use.

During deployment, an internal telemetry service was accidentally left accessible through the validator. Investigate the exposed services and recover the sensitive deployment reference.

---

## Files

```
attachments/
docs/
src/
```

Files inside `attachments/` are provided to participants.

---

## Screenshot

![screenshot](docs/screenshot.png)

---

## Solution

<details>
<summary>Click to expand</summary>

### Intended Solve Path

1. Open the EyeDay Validator web application.

2. Perform reconnaissance on the public application.

3. Discover the exposed configuration file:

```
/config.bak
```

4. Read the configuration and identify the internal telemetry service.

5. Exploit the SSRF vulnerability by submitting the internal telemetry URL to the validator.

6. Access:

```
/metrics
```

7. Identify the latest backup:

```
backup_20260813
```

8. Browse:

```
/backups/
```

9. Read:

```
config.json
```

10. Navigate into:

```
/backups/backup_20260813/
```

11. Read:

```
backup_manifest.txt
```

12. Read:

```
old.log
```

13. Discover that cleanup was skipped.

14. Navigate to:

```
/backups/backup_20260813/temp/
```

15. Read:

```
deployment_notes.txt
```

16. Recover the flag.

### Exploit Chain

Recon

↓

config.bak

↓

Internal Telemetry URL

↓

SSRF

↓

Metrics

↓

Latest Backup

↓

Backup Enumeration

↓

Deployment Artefacts

↓

Flag

</details>

---

## Local Testing

Run the challenge locally:

```bash
cd src
docker compose up --build
```

The validator will be available at:

```
http://localhost:8000
```

---

## Notes

- The Telemetry service must not be directly accessible from outside the Docker network.
- The intended solution relies solely on SSRF and information disclosure.
- No brute force or unintended vulnerabilities are required.
