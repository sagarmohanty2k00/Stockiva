from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {"message" : "hello"}

@app.get('/users')
def all_users():
    return {"users" : [
        {
            "name" : "sagar",
            "id" : 1,
        },
        {
            "name" : "mohanty",
            "id" : 2,
        }
    ]}

@app.post('/users/{id}')
def user(id):
    return {
            "name" : "sagar",
            "id" : 1,
        }