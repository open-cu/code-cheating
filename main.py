from fastapi import FastAPI

app = FastAPI()


@app.get("/get/all_users")
async def root():
    return {"message": "Hello World"}


@app.get("/get/user/{id}")
async def say_hello(id: int):
    return {"message": f"Hello {id}"}
