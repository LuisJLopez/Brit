from typing import List

from fastapi import Request

from .db_utils import Session
from .models import Item
from .settings import ROOT_PAGE, TEMPLATES


class Response:
    def __init__(self, session: Session, request: Request) -> None:
        self.session = session
        self.request = request

    def generic_response(self) -> TEMPLATES.TemplateResponse:
        items: List[Item] = self.session.query(Item).all()
        total: float = sum([item.price for item in items])

        return TEMPLATES.TemplateResponse(
            ROOT_PAGE,
            {"request": self.request, "items": items, "total": "{:.2f}".format(total)},
        )
