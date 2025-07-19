[![CI/CD](https://github.com/Ulthran/ctbus_site/actions/workflows/main.yml/badge.svg)](https://github.com/Ulthran/ctbus_site/actions/workflows/main.yml)
[![Renovate enabled](https://img.shields.io/badge/renovate-enabled-brightgreen.svg)](https://www.mend.io/renovate/)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/07edb64af1c544439190dff82571e7a5)](https://app.codacy.com/gh/Ulthran/ctbus_site/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![Known Vulnerabilities](https://snyk.io/test/github/Ulthran/ctbus_site/badge.svg)](https://snyk.io/test/github/Ulthran/ctbus_site)

## About

This is a personal website for Charlie Bushman.

https://charliebushman.com

The static frontend is served via CloudFront at [https://vue.charliebushman.com](https://vue.charliebushman.com).

## Deployment

The site is now a Vue application deployed to an S3 bucket and served through a
CloudFront distribution. Infrastructure is managed with Terraform. All pages are
written as Vue single file components.

To deploy the site:

- `git clone git@github.com:Ulthran/ctbus_site.git && cd ctbus_site`
- Run `terraform init` once to configure the backend.
- For development subdomains run
  `terraform apply -var 'hostname=subdomain.charliebushman.com'`.
- For production run
  `terraform apply -var-file terraform/production.tfvars`.
  This deploys both `charliebushman.com` and `www.charliebushman.com`.
  
To run locally, start a simple web server from the `vue-frontend` directory:

- `cd vue-frontend && python3 -m http.server`

Then open the given address in your browser.

Some environment variables are defined in `zappa_settings.json` but others are secret and are defined in a json file uploaded to a bucket defined by `remote_env`. For local deployments, just put everything in a `.env` file.

## Contributing

If you have thoughts on how I could improve the site, I'd love to hear them. It is, for now and the foreseeable future, pretty simplistic in design, but I will also be using it as a testing ground for anything in the web app arena I want to learn more about.

## Security Vulnerabilities

If you discover a security vulnerability, please send an e-mail to me via [ctbushman@gmail.com](mailto:ctbushman@gmail.com).

## License

This site is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).
