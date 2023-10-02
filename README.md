[![Tests](https://github.com/Ulthran/ctbus_site/actions/workflows/test.yml/badge.svg)](https://github.com/Ulthran/ctbus_site/actions/workflows/test.yml)
[![Super-Linter](https://github.com/Ulthran/ctbus_site/actions/workflows/linter.yml/badge.svg)](https://github.com/Ulthran/ctbus_site/actions/workflows/linter.yml)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/07edb64af1c544439190dff82571e7a5)](https://app.codacy.com/gh/Ulthran/ctbus_site/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

## About

This is a personal website for Charlie Bushman.

## Deployment

It is deployed as a serverless flask site using zappa on AWS.

-   `git clone git@github.com:Ulthran/ctbus_site.git && cd ctbus_site`
-   `python -m venv env`
-   `source env/bin/activate`
-   `pip install -r requirements.txt`
-   `pip install -r dev-requirements.txt` (for testing)
-   `zappa deploy`
-   `zappa update` (to update a previously deployed app)
-   `zappa tail` (to see logs)

To run locally,

-   `source env/bin/activate`
-   `export FLASK_DEBUG=1 && flask --app app/app run`

And go to the address given.

## Contributing

If you have thoughts on how I could improve the site, I'd love to hear them. It is, for now and the foreseeable future, pretty simplistic in design, but I will also be using it as a testing ground for anything in the web app arena I want to learn more about.

## Security Vulnerabilities

If you discover a security vulnerability, please send an e-mail to me via [ctbushman@gmail.com](mailto:ctbushman@gmail.com).

## License

This site is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).
