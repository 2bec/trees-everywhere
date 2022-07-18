# Trees Everywhere
## Requirements

- [Python 3.10](https://www.python.org/downloads/)

## How to start
1. Create a virtual environment with python: `python3 -m venv venv`
1. Activate this environment: `source venv/bin/activate`
1. Install dependencies: `pip install -r requirements.txt`
1. Run migrations: `python manage.py migrate`
1. Load some sample data: `python manage.py loaddata users accounts trees planted_trees`
1. Run app: `python manage.py runserver`

## Contributing

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
