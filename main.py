# main.py

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

from calculator import run_projection
from excel_writer import generate_excel

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def form_page(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/calculate")
def calculate(
    current_age: int = Form(...),
    current_salary: float = Form(...),
    current_service: float = Form(...),
    discount_rate: float = Form(...)
):

    ages, service, salary, gratuity, discount, pv = run_projection(
        current_age,
        current_salary,
        current_service,
        discount_rate=discount_rate
    )

    excel_file = generate_excel(ages, service, salary, gratuity, discount, pv)

    return StreamingResponse(
        excel_file,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": "attachment; filename=GratuityProjection.xlsx"}
    )