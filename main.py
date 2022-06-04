from fastapi import FastAPI

from routers import mount

app = FastAPI()

app.include_router(mount.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
