from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Welcome to Billing Service!",
        "version": "0.1.0",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "Billing Service",
        "environment": "development"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
