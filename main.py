from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    # Add actual prediction logic here — for now:
    print(f"Received file: {file.filename}, size: {len(contents)} bytes")
    result = "real"  # or "fake" from model
    return JSONResponse(content={"result": result})
