from fastapi import FastAPI, Header
from starlette.responses import HTMLResponse

app = FastAPI()

def format_home_page():
    return "dog"


@app.get("/", response_class=HTMLResponse)
def read_root(*, user_agent: str = Header(None), host: str = Header(None)):
    welcome_msg = """
    <h1> HELLO </h1>
    <p> <b> You are : </b>""" + user_agent + "</p>" + \
    "<b> I am: </b>" + host

    return welcome_msg 
