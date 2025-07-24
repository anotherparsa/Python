from flask import Flask

app = Flask(__name__)

stores = [
    {
        "name" : "my store",
        "items" : [
            {
                "name" : "chair",
                "price" : 10
            }
        ]
    }
]

@app.get("/stores")
def get_stores():
    return {"stores" : stores}