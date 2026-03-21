---
name: watch-ci
description: Check and wait for GitHub Actions CI results on the current branch or a specific run
argument-hint: "[run-id]"
allowed-tools: Bash(gh *)
---

# Watch CI

Check the status of GitHub Actions workflows for this repo.

## Steps

1. If `$ARGUMENTS` is provided, treat it as a run ID and jump to step 3.

2. Otherwise, list recent runs for the current branch:
   ```
   gh run list --branch $(git branch --show-current) --limit 5
   ```
   Pick the most recent run (top of the list).

3. Watch the run until it completes (this streams live output and blocks until done):
   ```
   gh run watch <run-id>
   ```

4. Once complete, show the final status:
   ```
   gh run view <run-id>
   ```

5. If any jobs failed, show their logs:
   ```
   gh run view <run-id> --log-failed
   ```

6. Report a plain-language summary: which jobs passed, which failed, and — if there were failures — the most likely cause based on the log output (e.g. Prettier formatting, Terraform validation).
