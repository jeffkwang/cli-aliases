# How to contribute to cli-aliases
Thank you for considering contributing!

## Reporting issues
Include the following information in your post:

- Describe what you expected to happen.
- If possible, include a minimal reproducible example to help us identify the issue. This also helps check that the issue is not with your own code.
- Describe what actually happened. Include the full traceback if there was an exception.
- List your Python version. If possible, check if this issue is already fixed in the latest releases or the latest code in the repository.

## Building from source
After downloading the source files or forking cli-aliases to your GitHub account, you can build the project from source. 

- Navigate to project directory.
- Create a virtualenv.
```
python -m venv env
cd env/Scripts
activate
```
- Install the development dependencies, then install cli-aliases in editable mode
```
python -m pip install -r requirements.txt && python -m pip install -e .
```

## Start coding
If you're submitting a feature addition or change, branch off of the "main" branch.
```
git fetch origin
git checkout -b your-branch-name origin/main
```
Using your favorite editor, make your changes, committing as you go.

Include tests that cover any code changes you make. Make sure the test fails without your patch. Run the tests as described below.

Push your commits to your fork on GitHub and create a pull request. Link to the issue being addressed with fixes #123 in the pull request.
```
git push --set-upstream fork your-branch-name
```