#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI 
#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel

#Creamos un objeto a partir de la clase FastAPI
app= FastAPI()

#Levantamos el server Uvicorn
#-uvicorn 3_crud:app --reload-
#{"id":3,"Name":"Alfredo", "LastName":"Garcia", "Age":30}
#Definimos nuestra entidad: User

class Auto(BaseModel):
    id:int
    Marca: str
    Modelo:str
    Anio:int
    
#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  
autos_list = [
    Auto(id=0, Marca="Audi", Modelo="rx", Anio="2032"),
    Auto(id=1, Marca="Toyota", Modelo="Camry", Anio="2021"),
    Auto(id=2, Marca="Honda", Modelo="Civic", Anio="2020"),
    Auto(id=3, Marca="Ford", Modelo="Mustang", Anio="2019"),
    Auto(id=4, Marca="Chevrolet", Modelo="Malibu", Anio="2018"),
    Auto(id=5, Marca="Volkswagen", Modelo="Jetta", Anio="2022"),
    Auto(id=6, Marca="Hyundai", Modelo="Elantra", Anio="2017"),
    Auto(id=7, Marca="Nissan", Modelo="Altima", Anio="2021"),
    Auto(id=8, Marca="Kia", Modelo="Optima", Anio="2020"),
    Auto(id=9, Marca="Subaru", Modelo="Outback", Anio="2019"),
    Auto(id=10, Marca="Mazda", Modelo="CX-5", Anio="2022"),
    Auto(id=11, Marca="Audi", Modelo="A4", Anio="2021"),
    Auto(id=12, Marca="Mercedes-Benz", Modelo="E-Class", Anio="2020"),
    Auto(id=13, Marca="Lexus", Modelo="RX", Anio="2022"),
    Auto(id=14, Marca="BMW", Modelo="3 Series", Anio="2021"),
    Auto(id=15, Marca="Chrysler", Modelo="300", Anio="2019"),
    Auto(id=16, Marca="Volvo", Modelo="XC60", Anio="2020"),
    Auto(id=17, Marca="Jeep", Modelo="Grand Cherokee", Anio="2021"),
    Auto(id=18, Marca="Tesla", Modelo="Model 3", Anio="2022"),
    Auto(id=19, Marca="Fiat", Modelo="500", Anio="2021"),
    Auto(id=20, Marca="GMC", Modelo="Sierra", Anio="2020"),
    Auto(id=21, Marca="Cadillac", Modelo="Escalade", Anio="2022"),
    Auto(id=22, Marca="Acura", Modelo="MDX", Anio="2021"),
    Auto(id=23, Marca="Buick", Modelo="Encore", Anio="2020"),
    Auto(id=24, Marca="Land Rover", Modelo="Discovery", Anio="2022"),
    Auto(id=25, Marca="Jaguar", Modelo="XF", Anio="2021"),
    Auto(id=26, Marca="Porsche", Modelo="911", Anio="2020"),
    Auto(id=27, Marca="Infiniti", Modelo="QX60", Anio="2022"),
    Auto(id=28, Marca="Mitsubishi", Modelo="Outlander", Anio="2021"),
    Auto(id=29, Marca="Subaru", Modelo="Forester", Anio="2020"),
    Auto(id=30, Marca="Nissan", Modelo="Rogue", Anio="2022"),
    Auto(id=31, Marca="Kia", Modelo="Sorento", Anio="2021"),
    Auto(id=32, Marca="Hyundai", Modelo="Tucson", Anio="2020"),
    Auto(id=33, Marca="Ford", Modelo="Escape", Anio="2022"),
    Auto(id=34, Marca="Chevrolet", Modelo="Equinox", Anio="2021"),
    Auto(id=35, Marca="Toyota", Modelo="Highlander", Anio="2020"),
    Auto(id=36, Marca="Honda", Modelo="CR-V", Anio="2022"),
    Auto(id=37, Marca="Mazda", Modelo="Mazda3", Anio="2021"),
    Auto(id=38, Marca="Audi", Modelo="Q5", Anio="2020"),
    Auto(id=39, Marca="Mercedes-Benz", Modelo="GLC", Anio="2022"),
    Auto(id=40, Marca="Lexus", Modelo="NX", Anio="2021"),
    Auto(id=41, Marca="BMW", Modelo="X5", Anio="2020"),
    Auto(id=42, Marca="Chrysler", Modelo="Pacifica", Anio="2022"),
    Auto(id=43, Marca="Volvo", Modelo="S60", Anio="2021"),
    Auto(id=44, Marca="Jeep", Modelo="Wrangler", Anio="2020"),
    Auto(id=45, Marca="Tesla", Modelo="Model S", Anio="2021"),
    Auto(id=46, Marca="Fiat", Modelo="Panda", Anio="2020"),
    Auto(id=47, Marca="GMC", Modelo="Terrain", Anio="2022"),
    Auto(id=48, Marca="Cadillac", Modelo="XT4", Anio="2021"),
    Auto(id=49, Marca="Acura", Modelo="TLX", Anio="2020"),
    Auto(id=50, Marca="Buick", Modelo="LaCrosse", Anio="2022"),
    Auto(id=51, Marca="Land Rover", Modelo="Range Rover", Anio="2021"),
    Auto(id=52, Marca="Jaguar", Modelo="F-PACE", Anio="2020"),
    Auto(id=53, Marca="Porsche", Modelo="Cayenne", Anio="2022"),
    Auto(id=54, Marca="Infiniti", Modelo="Q50", Anio="2021"),
    Auto(id=55, Marca="Mitsubishi", Modelo="Eclipse Cross", Anio="2020"),
    Auto(id=56, Marca="Subaru", Modelo="Crosstrek", Anio="2022"),
    Auto(id=57, Marca="Nissan", Modelo="Sentra", Anio="2021"),
    Auto(id=58, Marca="Kia", Modelo="Forte", Anio="2020"),
    Auto(id=59, Marca="Hyundai", Modelo="Sonata", Anio="2022"),
    Auto(id=60, Marca="Ford", Modelo="Fusion", Anio="2021"),
    Auto(id=61, Marca="Chevrolet", Modelo="Cruze", Anio="2020"),
    Auto(id=62, Marca="Toyota", Modelo="Corolla", Anio="2022"),
    Auto(id=63, Marca="Honda", Modelo="Accord", Anio="2021"),
    Auto(id=64, Marca="Mazda", Modelo="Mazda6", Anio="2020"),
    Auto(id=65, Marca="Audi", Modelo="A6", Anio="2022"),
    Auto(id=66, Marca="Mercedes-Benz", Modelo="CLS", Anio="2021"),
    Auto(id=67, Marca="Lexus", Modelo="LS", Anio="2020"),
    Auto(id=68, Marca="BMW", Modelo="7 Series", Anio="2022"),
    Auto(id=69, Marca="Chrysler", Modelo="300", Anio="2021"),
    Auto(id=70, Marca="Volvo", Modelo="S90", Anio="2020"),
    Auto(id=71, Marca="Jeep", Modelo="Compass", Anio="2022"),
    Auto(id=72, Marca="Tesla", Modelo="Model X", Anio="2021"),
    Auto(id=73, Marca="Fiat", Modelo="500X", Anio="2020"),
    Auto(id=74, Marca="GMC", Modelo="Yukon", Anio="2022"),
    Auto(id=75, Marca="Cadillac", Modelo="CT5", Anio="2021"),
    Auto(id=76, Marca="Acura", Modelo="ILX", Anio="2020"),
    Auto(id=77, Marca="Buick", Modelo="Enclave", Anio="2022"),
    Auto(id=78, Marca="Land Rover", Modelo="Defender", Anio="2021"),
    Auto(id=79, Marca="Jaguar", Modelo="XE", Anio="2020"),
    Auto(id=80, Marca="Porsche", Modelo="Panamera", Anio="2022"),
    Auto(id=81, Marca="Infiniti", Modelo="QX50", Anio="2021"),
    Auto(id=82, Marca="Mitsubishi", Modelo="Mirage", Anio="2020"),
    Auto(id=83, Marca="Subaru", Modelo="Impreza", Anio="2022"),
    Auto(id=84, Marca="Nissan", Modelo="Versa", Anio="2021"),
    Auto(id=85, Marca="Kia", Modelo="Rio", Anio="2020"),
    Auto(id=86, Marca="Hyundai", Modelo="Accent", Anio="2022"),
    Auto(id=87, Marca="Ford", Modelo="Fiesta", Anio="2021"),
    Auto(id=88, Marca="Chevrolet", Modelo="Spark", Anio="2020"),
    Auto(id=89, Marca="Toyota", Modelo="Yaris", Anio="2022"),
    Auto(id=90, Marca="Honda", Modelo="Fit", Anio="2021"),
    Auto(id=91, Marca="Mazda", Modelo="Mazda2", Anio="2020"),
    Auto(id=92, Marca="Audi", Modelo="A3", Anio="2022"),
    Auto(id=93, Marca="Mercedes-Benz", Modelo="A-Class", Anio="2021"),
    Auto(id=94, Marca="Lexus", Modelo="UX", Anio="2020"),
    Auto(id=95, Marca="BMW", Modelo="2 Series", Anio="2022"),
    Auto(id=96, Marca="Chrysler", Modelo="Voyager", Anio="2021"),
    Auto(id=97, Marca="Volvo", Modelo="V60", Anio="2020"),
    Auto(id=98, Marca="Jeep", Modelo="Renegade", Anio="2022"),
    Auto(id=99, Marca="Tesla", Modelo="Model Y", Anio="2021"),
    Auto(id=100, Marca="Fiat", Modelo="Punto", Anio="2020"),
    Auto(id=101, Marca="GMC", Modelo="Acadia", Anio="2022"),
    Auto(id=102, Marca="Cadillac", Modelo="XT6", Anio="2021"),
    Auto(id=103, Marca="Acura", Modelo="RDX", Anio="2020"),
    Auto(id=104, Marca="Buick", Modelo="Regal", Anio="2022"),
    Auto(id=105, Marca="Land Rover", Modelo="Velar", Anio="2021"),
    Auto(id=106, Marca="Jaguar", Modelo="XJ", Anio="2020"),
    Auto(id=107, Marca="Porsche", Modelo="Macan", Anio="2022"),
    Auto(id=108, Marca="Infiniti", Modelo="QX80", Anio="2021"),
    Auto(id=109, Marca="Mitsubishi", Modelo="Lancer", Anio="2020"),
    Auto(id=110, Marca="Subaru", Modelo="Legacy", Anio="2022"),
    Auto(id=111, Marca="Nissan", Modelo="Maxima", Anio="2021"),
    Auto(id=112, Marca="Kia", Modelo="Cadenza", Anio="2020"),
    Auto(id=113, Marca="Hyundai", Modelo="Veloster", Anio="2022"),
    Auto(id=114, Marca="Ford", Modelo="Taurus", Anio="2021"),
    Auto(id=115, Marca="Chevrolet", Modelo="Impala", Anio="2020"),
    Auto(id=116, Marca="Toyota", Modelo="Avalon", Anio="2022"),
    Auto(id=117, Marca="Honda", Modelo="Insight", Anio="2021"),
    Auto(id=118, Marca="Mazda", Modelo="MX-5 Miata", Anio="2020"),
    Auto(id=119, Marca="Audi", Modelo="TT", Anio="2022"),
    Auto(id=120, Marca="Mercedes-Benz", Modelo="SLC", Anio="2021"),
    Auto(id=121, Marca="Lexus", Modelo="LC", Anio="2020"),
    Auto(id=122, Marca="BMW", Modelo="Z4", Anio="2022"),
    Auto(id=123, Marca="Chrysler", Modelo="Crossfire", Anio="2021"),
    Auto(id=124, Marca="Volvo", Modelo="C30", Anio="2020"),
    Auto(id=125, Marca="Jeep", Modelo="Patriot", Anio="2022"),
    Auto(id=126, Marca="Tesla", Modelo="Roadster", Anio="2021"),
    Auto(id=127, Marca="Fiat", Modelo="Bravo", Anio="2020"),
    Auto(id=128, Marca="GMC", Modelo="Envoy", Anio="2022"),
    Auto(id=129, Marca="Cadillac", Modelo="XT5", Anio="2021"),
    Auto(id=130, Marca="Acura", Modelo="ILX", Anio="2020"),
    Auto(id=131, Marca="Buick", Modelo="Encore GX", Anio="2022"),
    Auto(id=132, Marca="Land Rover", Modelo="Discovery Sport", Anio="2021"),
    Auto(id=133, Marca="Jaguar", Modelo="F-TYPE", Anio="2020"),
    Auto(id=134, Marca="Porsche", Modelo="718 Cayman", Anio="2022"),
    Auto(id=135, Marca="Infiniti", Modelo="Q60", Anio="2021"),
    Auto(id=136, Marca="Mitsubishi", Modelo="Outlander Sport", Anio="2020"),
    Auto(id=137, Marca="Subaru", Modelo="BRZ", Anio="2022"),
    Auto(id=138, Marca="Nissan", Modelo="370Z", Anio="2021"),
    Auto(id=139, Marca="Kia", Modelo="Stinger", Anio="2020"),
    Auto(id=140, Marca="Hyundai", Modelo="Genesis", Anio="2022"),
    Auto(id=141, Marca="Ford", Modelo="GT", Anio="2021"),
    Auto(id=142, Marca="Chevrolet", Modelo="Camaro", Anio="2020"),
    Auto(id=143, Marca="Toyota", Modelo="86", Anio="2022"),
    Auto(id=144, Marca="Honda", Modelo="S2000", Anio="2021"),
    Auto(id=145, Marca="Mazda", Modelo="RX-8", Anio="2020"),
    Auto(id=146, Marca="Audi", Modelo="R8", Anio="2022"),
    Auto(id=147, Marca="Mercedes-Benz", Modelo="AMG GT", Anio="2021"),
    Auto(id=148, Marca="Lexus", Modelo="LFA", Anio="2020"),
    Auto(id=149, Marca="BMW", Modelo="i8", Anio="2022"),
    Auto(id=150, Marca="Chrysler", Modelo="Prowler", Anio="2021"),
    Auto(id=151, Marca="Volvo", Modelo="C70", Anio="2020"),
    Auto(id=152, Marca="Jeep", Modelo="Cherokee", Anio="2022"),
    Auto(id=153, Marca="Tesla", Modelo="Model Roadster", Anio="2021"),
    Auto(id=154, Marca="Fiat", Modelo="124 Spider", Anio="2020"),
    Auto(id=155, Marca="GMC", Modelo="Typhoon", Anio="2022"),
    Auto(id=156, Marca="Cadillac", Modelo="Eldorado", Anio="2021"),
    Auto(id=157, Marca="Acura", Modelo="Integra", Anio="2020"),
    Auto(id=158, Marca="Buick", Modelo="Skylark", Anio="2022"),
    Auto(id=159, Marca="Land Rover", Modelo="LR2", Anio="2021"),
    Auto(id=160, Marca="Jaguar", Modelo="XK", Anio="2020"),
    Auto(id=161, Marca="Porsche", Modelo="Panamera", Anio="2022"),
    Auto(id=162, Marca="Infiniti", Modelo="Q70", Anio="2021"),
    Auto(id=163, Marca="Mitsubishi", Modelo="Montero Sport", Anio="2020"),
    Auto(id=164, Marca="Subaru", Modelo="Baja", Anio="2022"),
    Auto(id=165, Marca="Nissan", Modelo="Cube", Anio="2021"),
    Auto(id=166, Marca="Kia", Modelo="Soul", Anio="2020"),
    Auto(id=167, Marca="Hyundai", Modelo="Tucson", Anio="2022"),
    Auto(id=168, Marca="Ford", Modelo="Escape", Anio="2021"),
    Auto(id=169, Marca="Chevrolet", Modelo="Trax", Anio="2020"),
    Auto(id=170, Marca="Toyota", Modelo="C-HR", Anio="2022"),
    Auto(id=171, Marca="Honda", Modelo="HR-V", Anio="2021"),
    Auto(id=172, Marca="Mazda", Modelo="CX-3", Anio="2020"),
    Auto(id=173, Marca="Audi", Modelo="Q3", Anio="2022"),
    Auto(id=174, Marca="Mercedes-Benz", Modelo="GLA", Anio="2021"),
    Auto(id=175, Marca="Lexus", Modelo="NX", Anio="2020"),
    Auto(id=176, Marca="BMW", Modelo="X1", Anio="2022"),
    Auto(id=177, Marca="Chrysler", Modelo="Pacifica", Anio="2021"),
    Auto(id=178, Marca="Volvo", Modelo="XC40", Anio="2020"),
    Auto(id=179, Marca="Jeep", Modelo="Cherokee", Anio="2022"),
    Auto(id=180, Marca="Tesla", Modelo="Model S", Anio="2021"),
    Auto(id=181, Marca="Fiat", Modelo="Ducato", Anio="2022"),
    Auto(id=182, Marca="GMC", Modelo="Savana", Anio="2021"),
    Auto(id=183, Marca="Cadillac", Modelo="XT4", Anio="2020"),
    Auto(id=184, Marca="Acura", Modelo="MDX", Anio="2022"),
    Auto(id=185, Marca="Buick", Modelo="Encore", Anio="2021"),
    Auto(id=186, Marca="Land Rover", Modelo="Discovery", Anio="2020"),
    Auto(id=187, Marca="Jaguar", Modelo="XF", Anio="2022"),
    Auto(id=188, Marca="Porsche", Modelo="911", Anio="2021"),
    Auto(id=189, Marca="Infiniti", Modelo="QX60", Anio="2020"),
    Auto(id=190, Marca="Mitsubishi", Modelo="Outlander", Anio="2022"),
    Auto(id=191, Marca="Subaru", Modelo="Forester", Anio="2021"),
    Auto(id=192, Marca="Nissan", Modelo="Rogue", Anio="2020"),
    Auto(id=193, Marca="Kia", Modelo="Sorento", Anio="2022"),
    Auto(id=194, Marca="Hyundai", Modelo="Tucson", Anio="2021"),
    Auto(id=195, Marca="Ford", Modelo="Escape", Anio="2020"),
    Auto(id=196, Marca="Chevrolet", Modelo="Equinox", Anio="2022"),
    Auto(id=197, Marca="Toyota", Modelo="Highlander", Anio="2021"),
    Auto(id=198, Marca="Honda", Modelo="CR-V", Anio="2020"),
    Auto(id=199, Marca="Mazda", Modelo="Mazda3", Anio="2022"),
    Auto(id=200, Marca="Ford", Modelo="Escape", Anio="2022"),
]

#***Get
@app.get("/autosclass/")
async def autosclass():
    return (autos_list)

#***Get con Filtro Query
@app.get("/autosclass1/")
async def autosclass(id:int):
    autos=filter (lambda auto: auto.id == id, autos_list)  
    try:
        return list(autos)[0]
    except:
        return{"error":"No se ha encontrado el auto"}
    
 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/?id=1
 
 
 #***Get con Filtro Query
@app.get("/autosclass2/")
async def autosclass(marca:str, modelo:str):
    autos=filter (lambda auto: auto.marca == marca, autos_list)#Función de orden superior
    autos1=filter (lambda auto: auto.modelo == modelo, autos_list)#Función de orden superior
    try:
        return list(autos1)[0]
    except:
        return{"error":"No se ha encontrado el auto"}

# *** Get con Filtro Query
@app.get("/autosclass3/")
async def autosclass(marca: str, modelo: str):
    filtered_autos = [auto for auto in autos_list if auto.Marca == marca and auto.Modelo == modelo]
    
    if filtered_autos:
        return filtered_autos[0]
    else:
        return {"error": "No se ha encontrado el auto"}

@app.get("/autosclass4/")
async def autosclass(modelo: str, anio: int):
    filtered_autos = [auto for auto in autos_list if auto.Modelo == modelo and auto.Anio == anio]
    
    if filtered_autos:
        return filtered_autos[0]
    else:
        return {"error": "No se ha encontrado el auto"}
