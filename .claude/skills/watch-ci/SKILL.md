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

2. Otherwise, find the most recent run for the current branch. Note: `gh run list`
   does NOT support `--branch`. Filter using `--json` instead:
   ```
   gh run list --limit 20 --json databaseId,status,conclusion,name,headBranch,createdAt
   ```
   Filter the output where `headBranch` matches `$(git branch --show-current)`,
   then pick the entry with the most recent `createdAt`.

   Valid `--json` fields are: `conclusion`, `createdAt`, `databaseId`, `event`,
   `headBranch`, `headSha`, `name`, `status`, `updatedAt`, `url`, `workflowDatabaseId`.
   (`workflowName` is NOT valid — use `name`.)

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

6. Report a plain-language summary: which jobs passed, which failed, and — if there
   were failures — the most likely cause based on the log output (e.g. Prettier
   formatting, Terraform validation). If Prettier is the cause, fix the files and
   commit before reporting back.
