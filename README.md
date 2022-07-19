# Trees Everywhere
## Requirements

- [Python 3.10](https://www.python.org/downloads/)

## Contributing
### Running it locally
1. Clone the repository `git clone git@github.com:2bec/trees-everywhere.git && cd trees-everywhere`
1. Create a virtual environment with python: `python3 -m venv venv`
1. Activate this environment: `source venv/bin/activate`
1. Install dependencies: `pip install -r requirements.txt`
1. Install develop dependencies: `pip install -r requirements_dev.txt`
1. Run migrations: `python manage.py migrate`
1. Load some sample data: `python manage.py loaddata users accounts trees planted_trees`
1. Run app: `python manage.py runserver`

### Access admin
1. Go to `http://127.0.0.1:8000/admin`
1. For username `admin` and password `Admin-123`

### Access web
1. Go to `http://127.0.0.1:8000`
1. Make your login. You can create some user in the admin or use default users created with the `loaddata` command
1. Default users:
    * username: `teste-1`, password: `Admin-123`
    * username: `teste-2`, password: `Admin-123`

Each of the users already has one or more trees planted. You can plant more trees clicking the button `Plant a Tree` after login.

### About tests
1. I preferred to use Django TestCase and fixtures

To run all tests `make test`

### Code Lint
1. I preferred to use [Flake8](https://flake8.pycqa.org/en/latest/)

To run lint `make lint`

### Changes

General workflow is:

1. Checkout from develop
1. Create a branch using naming convention for branchs
1. Make changes and commit using naming convention for commits
1. Push branch to origin
1. Create a pull request using naming convention
1. Use a template for PR's and fill all important areas
1. Wait for review

### Branch naming convention

Branch names must match one of these patterns:

- feature/[A-z]\*
- fix/[A-z]\*
- hotfix/[A-z]\*
- doc/[A-z]\*
- refactor/[A-z]\*
- test/[A-z]\*

### Commit naming convention

Commits messages must match one of these patterns:

- improvements: [A-z]\*
- fix: [A-z]\*
- hotfix: [A-z]\*
- docs: [A-z]\*
- refactor: [A-z]\*
- tests: [A-z]\*

### Pull Request title naming convention

Pull Requests title must match one of these patterns:

- [Feature] [A-z]\*
- [Fix] [A-z]\*
- [Hotfix] [A-z]\*
- [Doc] [A-z]\*
- [Refactor] [A-z]\*
- [Test] [A-z]\*
