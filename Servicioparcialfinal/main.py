from fastapi import FastAPI

app = FastAPI()

@app.get('/', tags=["Home"])
def home():
    return {"Welcome": "Architecture for Voice Recognition in Family Members"}



@app.get("/get_result", tags=["audio"])
async def get_audio():
    """Retorna resultados del audio introducido
    :return:  los diferentes resultados del modelo.
    """
    return {"message": "retorna los resultados del modelo"}


@app.post("/subir_audio", tags=["audio"])
async def post_audio():
    """Retorna resultados del audio introducido
    :return:  los diferentes resultados del modelo.
    """
    return {"message": "audio subido correctamente"}




