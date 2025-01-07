from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

cars = [
        { "id": "9009", "mark": "Toyota", "model": "Yaris", "description": "Economic car, nothing unusual", "yearModel": 2008, "mileage": 220_000  },
        { "id": "101010", "mark": "Honda", "model": "Civic", "description": "Decent car, fast and economic", "yearModel": 2014, "mileage": 80_000  },
        { "id": "42069360", "mark": "Lamborghini", "model": "Aventador", "description": "Non Economic car, burn fuel and do donuts", "yearModel": 2013, "mileage": 55000  },
    ]

@app.get("/cars", response_class=HTMLResponse)
async def read_cars(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"cars": cars}
    )

@app.get("/cars/create", response_class=HTMLResponse)
async def create_car(request: Request):
    return templates.TemplateResponse(
        request=request, name="create.html"
    )

@app.post("/cars/create")
async def create_car(request: Request):
    data = await request.form()
    cars.append({
        "id": data["id"],
        "mark": data["mark"],
        "model": data["model"],
        "description": data["description"],
        "yearModel": int(data["yearModel"]),
        "mileage": int(data["mileage"]),
    })
    # print(data["id"])
    return {"message": "Car created successfully"}