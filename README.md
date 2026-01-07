[![CI/CD](https://github.com/Ulthran/ctbus_site/actions/workflows/health-checks.yml/badge.svg)](https://github.com/Ulthran/ctbus_site/actions/workflows/health-checks.yml)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/07edb64af1c544439190dff82571e7a5)](https://app.codacy.com/gh/Ulthran/ctbus_site/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![Known Vulnerabilities](https://snyk.io/test/github/Ulthran/ctbus_site/badge.svg)](https://snyk.io/test/github/Ulthran/ctbus_site)

## About

This is a personal website for Charlie Bushman. It is a serverless, microservice grid comprised of a static assets CDN, the Vue frontend CDN, an additional API for accessing third party data sources (plus misc tasks). Each service is managed with Terraform.

<https://charliebushman.com>

## Deployment

To deploy a service:

- `git clone git@github.com:Ulthran/ctbus_site.git && cd ctbus_site`
- Move into the desired service directory and initialize `cd frontend/terraform && terraform init`
- Select your workspace `terraform workspace select dev`
- Deploy stack/apply changes `terraform apply`

NOTE: The frontend service requires deployed versions of each other service (pulled from the remote Terraform state files).
  
To run locally, start the included Python development server:

- `python3 dev_server.py`

Then open the given address in your browser.

### Games SPA local development

Run the React single-page app locally with placeholder values filled for assets and environment:

- `npm run dev:games -- --port 4173`

The server injects `ASSETS_BASE_URL` (defaulting to `http://localhost:<port>/assets`) and `ENV_NAME` (defaulting to `local`).

## Security Vulnerabilities

If you discover a security vulnerability, please send an e-mail to me via [ctbushman@gmail.com](mailto:ctbushman@gmail.com).

## License

This site is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).
