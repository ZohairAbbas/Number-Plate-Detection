from yolo_folio import detectandread
from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/index', response_class=HTMLResponse)
def get_basic_form(request: Request):
    data = ""
    return templates.TemplateResponse("index.html", {"request": request, "data": data})


@app.post('/index', response_class=HTMLResponse)
async def post_basic_form(request: Request, file: UploadFile = File(...)):
    content = await file.read()
    data = detectandread(file.filename)
    return templates.TemplateResponse("results.html", {"request": request, "data": data[0], "custom_model": data[1], "source": file.filename})
