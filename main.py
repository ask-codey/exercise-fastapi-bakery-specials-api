"""Maple Street Bakery's API: for you to finish.

Every request it should answer, with its status code and body:

  GET /           200, the welcome message, exactly:
                  {"bakery": "Maple Street Bakery", "message": "Welcome! Today's specials are at /specials."}
  GET /specials   200, the list SPECIALS from data.py, exactly as it is there:
                  [{"name": "Sourdough loaf", "price": 6.5}, {"name": "A dozen bagels", "price": 12.0},
                   {"name": "Cranberry scone", "price": 3.5}]

Run it with:  fastapi dev main.py
Then open http://127.0.0.1:8000/docs to try every route. Stop it with Ctrl+C.
"""
from fastapi import FastAPI

from data import SPECIALS

app = FastAPI(title="Maple Street Bakery")

# Add the two routes below: GET / first, then GET /specials.
