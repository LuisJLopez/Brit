from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from .api_utils import Response
from .db_utils import Session, dbconnect
from .models import Item
from .settings import STATIC_DIR, TEMPLATES

app = FastAPI()

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@dbconnect
@app.get("/", response_class=HTMLResponse)
async def fetch_items(request: Request) -> TEMPLATES.TemplateResponse:
    session: Session = Session()
    response: Response = Response(session, request)
    return response.generic_response()


@dbconnect
@app.post("/add_item/")
async def add_item(
    request: Request, item_name: str = Form(), item_price: float = Form()
) -> TEMPLATES.TemplateResponse:
    session: Session = Session()

    new_item: Item = Item(name=item_name, price=item_price)
    session.add(new_item)
    session.commit()

    response: Response = Response(session, request)
    return response.generic_response()


@dbconnect
@app.post("/total/")
async def add_item(request: Request) -> TEMPLATES.TemplateResponse:
    session: Session = Session()
    response: Response = Response(session, request)
    return response.generic_response()
