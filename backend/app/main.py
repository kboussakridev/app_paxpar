from typing import Union

from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from pypdf import PdfReader, PdfWriter
from pypdf.annotations import FreeText
import time
from starlette.responses import FileResponse
import tkinter as tk
from fastapi.responses import JSONResponse
import os
app = FastAPI()


origins = [
    "http://localhost:3000",
]


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)



class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "karim"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.get("/backend_function")
def backend_function():
    return {"message": "Fonction backend exécutée avec succès"}

@app.get("/api/data")
def get_data():
    return {
        "message": f"Hello from FastAPI {time.time()}",
    }


@app.get("/api/chat")
def get_chat():
    return {
        "conversation": [
            "It's over Anakin, <br />I have the high ground.",
            "You underestimate my power!",
            "It's over Anakin, <br />I have the high ground.",
            "You underestimate my power!",
            "It's over Anakin, <br />I have the high ground.",
            "You underestimate my power!",
            "It's over Anakin, <br />I have the high ground.",
            "You underestimate my power!",
            "It's over Anakin, <br />I have the high ground.",
            "You underestimate my power!",
        ]
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

# Définit le répertoire d'upload
UPLOAD_DIRECTORY = "uploads"

# Vérifie si le répertoire d'upload existe, sinon le crée
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

# Définit une route POST pour télécharger des fichiers
@app.post("/upload")
async def upload_file(files: list[UploadFile] = File(...)):
    try:
        # Parcourt la liste des fichiers téléchargés
        for file in files:
            # Détermine l'emplacement où enregistrer chaque fichier
            file_location = os.path.join(UPLOAD_DIRECTORY, file.filename)
            # Ouvre chaque fichier et écrit son contenu dans le répertoire d'upload
            with open(file_location, "wb+") as file_object:
                file_object.write(file.file.read())
        # Retourne une réponse JSON indiquant que les fichiers ont été téléchargés avec succès
        return JSONResponse(content={"message": "Fichiers téléchargés avec succès"}, status_code=200)
    except Exception as e:
        # En cas d'erreur lors du téléchargement des fichiers, retourne une réponse JSON avec l'erreur
        return JSONResponse(content={"error": str(e)}, status_code=400)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)