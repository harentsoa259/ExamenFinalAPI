# installation de fastapi -> pip install fastapi
# Demarer le serveur -> uvicorn main:app --reload

# pour tester l'API curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/items?item=apple'


from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/ping")
def root():
    return {"pong"}

