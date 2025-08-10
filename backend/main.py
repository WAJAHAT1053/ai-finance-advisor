from fastapi import FastAPI, UploadFile
import pandas as pd
import io

app = FastAPI()

@app.post("/upload-csv/")
async def upload_csv(file: UploadFile):
    content = await file.read()
    df = pd.read_csv(io.BytesIO(content))
    return {"rows": len(df), "columns": list(df.columns)}
