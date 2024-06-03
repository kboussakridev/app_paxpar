from typing import Union

from fastapi import FastAPI
from pypdf import PdfReader, PdfWriter
from pypdf.annotations import FreeText
import time
from starlette.responses import FileResponse
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    # "http://localhost.tiangolo.com",
    # "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
    "http://localhost:3000/camille",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}


app = FastAPI()


@app.get("/")
def hello():
    return {"Hello": "World"}


@app.get("/camille")
def hello_cam():
    return {"Hello": "camille"}


@app.get("/karim")
def hello_k():
    return {"Hello": "karim"}


@app.get("/items/{item_id}")
def read_item(
    item_id: int,
    y: int,
    q: Union[str, None] = None,
):
    return {
        "item_id": item_id,
        "y": y,
        "hello": "Karim",
        "q": q,
    }


@app.get("/invoice/{num}")
def invoice_get(num: int):
    """
    Build an invoice from the given number.
    Lorem ipsum ....
    """
    # build the PDF
    # ...

    # Fill the writer with the pages you want
    # pdf_path = os.path.join(RESOURCE_ROOT, "crazyones.pdf")
    # reader = PdfReader(pdf_path)
    # page = reader.pages[0]
    writer = PdfWriter()
    # writer.add_page(page)
    writer.add_blank_page(800.0, 800.0)

    # Create the annotation and add it
    annotation = FreeText(
        text=f"Invoice #{num}, {time.time()} seconds",
        rect=(50, 550, 200, 650),
        font="Arial",
        bold=True,
        italic=True,
        font_size="20pt",
        font_color="00ff00",
        border_color="ff0000",
        background_color="cdcdcd",
    )
    writer.add_annotation(page_number=0, annotation=annotation)

    # Write the annotated file to disk
    with open("file.pdf", "wb") as fp:
        writer.write(fp)

    # return f"invoice {num}"
    return FileResponse(
        "file.pdf",
        # media_type="application/octet-stream",
        # filename=file_name,
    )
