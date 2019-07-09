from fastapi import FastAPI
from starlette.responses import HTMLResponse

app = FastAPI()

@app.get("/", responce_class=HTMLResponse)
def read_root():
    return "<h1> HELLO <h1/>
