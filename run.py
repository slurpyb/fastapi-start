import uvicorn 
from config import PORT, BIND, WORKERS, RELOAD

if __name__ == "__main__":
    uvicorn.run("app:App", host=BIND, port=int(PORT), reload=RELOAD, debug=RELOAD, workers=int(WORKERS))