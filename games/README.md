# Games Service

Static site for the games experience, deployed to S3/CloudFront via Terraform.

## Deploy (production)

From `games/`:

```sh
terraform init
terraform apply
```

## Run locally

From `games/`:

```sh
node dev-server.js
```

Then visit `http://localhost:4173`.

Optional environment overrides:

```sh
ASSETS_BASE_URL=http://localhost:4173/assets ENV_NAME=local node dev-server.js
```
