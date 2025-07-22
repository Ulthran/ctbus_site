[![CI/CD](https://github.com/Ulthran/ctbus_site/actions/workflows/main.yml/badge.svg)](https://github.com/Ulthran/ctbus_site/actions/workflows/main.yml)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/07edb64af1c544439190dff82571e7a5)](https://app.codacy.com/gh/Ulthran/ctbus_site/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![Known Vulnerabilities](https://snyk.io/test/github/Ulthran/ctbus_site/badge.svg)](https://snyk.io/test/github/Ulthran/ctbus_site)

## About

This is a personal website for Charlie Bushman.

https://charliebushman.com

## Deployment

The project is split into several small services that share a Terraform backend.
Each service can be deployed on its own.

To deploy a service:

- `git clone git@github.com:Ulthran/ctbus_site.git && cd ctbus_site`
- Initialize Terraform in the desired service directory. For example:

```
terraform -chdir=frontend/terraform init
terraform -chdir=frontend/terraform apply -var 'hostname=subdomain.example.com'
```

Use similar commands for `assets/terraform` and `spotify/terraform`.
  
To run locally, start the included Python development server:

- `python3 dev_server.py`

Then open the given address in your browser.

## Contributing

If you have thoughts on how I could improve the site, I'd love to hear them. It is, for now and the foreseeable future, pretty simplistic in design, but I will also be using it as a testing ground for anything in the web app arena I want to learn more about.

## Security Vulnerabilities

If you discover a security vulnerability, please send an e-mail to me via [ctbushman@gmail.com](mailto:ctbushman@gmail.com).

## License

This site is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).
