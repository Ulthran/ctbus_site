# CLAUDE.md — ctbus_site

Personal portfolio site for Charlie Bushman (charliebushman.com). Monorepo of microservices deployed via AWS.

## Repo Structure

```
ctbus_site/
├── frontend/           # Main Vue.js SPA (served via S3/CloudFront)
│   ├── src/src/
│   │   ├── main.js         # Router definitions (add new routes here)
│   │   ├── App.vue          # Top-level layout, nav links, social icons
│   │   ├── views/           # One file per page/route
│   │   └── components/      # Shared components (Hero, Timeline, etc.)
│   └── terraform/           # AWS infra for frontend
├── games/              # Separate React games SPA (S3/CloudFront)
├── assets/             # Static files (images, PDFs, certs) with own terraform
├── spotify/            # Spotify Lambda integration
├── jupyter/            # Jupyter notebooks
├── maintenance/        # Maintenance scripts
└── .github/workflows/  # CI per service area (frontend, assets, spotify, etc.)
```

## Frontend

### Key Pages (frontend/src/src/views/)

| File | Route | Purpose |
|------|-------|---------|
| `Home.vue` | `/` | Landing page — nav buttons, certs, contact |
| `About.vue` | `/about` | Career timeline |
| `WHOOP.vue` | `/whoop` | Current job (Software Engineer, HAX Team) |
| `PCMP.vue` | `/pcmp` | Previous job (Penn-CHOP Microbiome Program) |
| `PastWork.vue` | `/past-work` | Internships and older roles |
| `Resume.vue` | `/resume` | Resume viewer/download |
| `ProjectsList.vue` | `/projects` | Personal projects list |
| `Certifications.vue` | `/certifications` | AWS and other certs |
| `Education.vue` | `/education` | Carleton College, Marblehead HS |

**Adding a new page:** create the `.vue` file in `views/`, add a route object in `main.js`, and add a nav button in `Home.vue` if appropriate.

## Development Workflow

### 1. Branch
```bash
git checkout -b <descriptive-branch-name>
```

### 2. Lint (before committing)
```bash
npx prettier --config .prettierrc.json --write "frontend/**/*.{js,vue,css,html}" "spotify/lambda/**/*.js"
python -m black example.py another_example.py
terraform fmt -recursive
```

### 3. Commit
Keep messages short and descriptive (one line is fine for small changes):
```bash
git add <specific files>
git commit -m "Short description of what changed"
```

### 4. Push & PR
```bash
git push -u origin <branch-name>
gh pr create --title "..." --body "..."
```

Use `/watch-ci` after pushing to monitor GitHub Actions results.

## CI / GitHub Actions

Workflows run per service area on push/PR to `master`/`dev`:

| Workflow | Triggers on changes to | Checks |
|----------|------------------------|--------|
| `frontend.yml` | `frontend/` | Prettier, Terraform fmt/validate, HTML tidy |
| `assets.yml` | `assets/` | Terraform fmt/validate |
| `maintenance.yml` | `maintenance/` | Prettier, Terraform fmt/validate |
| `spotify.yml` | `spotify/` | Prettier, Terraform fmt/validate |
| `jupyter.yml` | `jupyter/` | Terraform fmt/validate |
| `health-checks.yml` | Scheduled weekly | Broken links, critical docs |
