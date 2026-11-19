# Exercise: Bakery Specials API

Exercise code for the lesson **Exercise: Bakery Specials API** in the Python Web APIs course on [ask-codey.com](https://www.ask-codey.com).

Maple Street Bakery's owner wants today's specials in the bakery's phone app. You'll finish the bakery's FastAPI app so the phone app has something to ask: a welcome message at `/` and today's specials at `/specials`. Tests send each request to the app and check what comes back.

## What's here

- `main.py`: the bakery's app, for you to finish. The comment at its top lists every request it should answer, with the status code and the body. For now it has no routes, so every request answers 404.
- `data.py`: today's three specials, in the list `SPECIALS`. Ready to use.
- `tests/test_bakery.py`: tests that send requests to your app and check each answer. You don't need to change this file.
- `requirements.txt`: the packages the app and the tests need (FastAPI and what it runs on, and pytest), at exact versions. Ready to use.
- `pytest.ini`: tells pytest where the tests are and where to find `main.py`. Ready to use.
- `.gitignore`: tells Git to leave out the virtual environment and the files Python and pytest make as they run. Ready to use.

## Before you start

The app and the tests need FastAPI and pytest, and they go in a virtual environment: a private set of packages for this folder only. In VS Code's terminal, in this folder, run these three commands.

On Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

On a Mac (zsh):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

- The first command makes the virtual environment, in a folder named `.venv`.
- The second turns it on for this terminal: the prompt starts with `(.venv)` from then on.
- The third installs the packages `requirements.txt` lists into it. It takes a minute: FastAPI brings several packages with it.

*Virtual Environments and pip* explains all three. The `.venv` folder is in `.gitignore`, so Git leaves it out: these commands make it again on any computer.

If PowerShell answers that running scripts is disabled on this system, run this once, then run the second command again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Each new terminal starts with the virtual environment off. If the prompt doesn't start with `(.venv)`, run the second command again. (VS Code often turns it on for you.)

## Run it

```bash
fastapi dev main.py
```

Then open `http://127.0.0.1:8000/docs` in your browser. The docs page lists every route the app has: none yet, until you add them. Click a route, then **Try it out** and **Execute**, to send it a real request. The app restarts each time you save a file. Stop it with **Ctrl+C**.

## Check your work

```bash
pytest
```

No server needs to be running: the tests hand each request straight to the app. At first every test fails: that is expected, because the app has no routes yet, so every request answers 404. Each route you finish turns its tests green. A failing test's message says what it sent, what it expected and what came back, for example *GET /specials should answer 200, but it answered 404 with {"detail":"Not Found"}*.

## The rules

- Write both routes in `main.py`, on `app`. Don't change `data.py` or the tests.
- `GET /` answers the welcome message in the comment at the top of `main.py`, word for word: a dictionary with the keys `bakery` and `message`.
- `GET /specials` answers the list `SPECIALS` from `data.py`. Return that list; don't copy the specials into `main.py`.
- The specials' address is exactly `/specials`, with no slash at the end.

## Tips

- Copy the shape of the lesson's routes: a decorator, `@app.get("...")`, right above a function that returns the answer.
- Each route needs a function with its own name, such as `welcome` and `list_specials`.
- A dictionary or a list that a route returns goes back as JSON: you don't convert anything yourself.
- Copy the welcome message from the comment, apostrophe and all: one different letter and the test says so.

## Hand it in

When it works, push your solution to a public repo of your own on GitHub, then paste that repo's address into **Submit your exercise** on the lesson page at [ask-codey.com](https://www.ask-codey.com). That's what completes the lesson. The lesson page shows the Git commands, step by step.
