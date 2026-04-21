from fastapi import FastAPI, Request
from products_data import Product
import abc
print(abc.__file__)

app = FastAPI()

# Path parameter example
@app.get("/product/{product_id}")
def get_product(product_id: int):
    for item in Product:
        if item["id"] == product_id:
            return item
    return {"error": "Product not found"}


# now 2nd way is query parameter 

# so waht is query mentnet 
@app.get("/greet")
def greet(name:str):
    return f"Hello {name}"

#http://127.0.0.1:8000/greet?name=jigar


# nowe righht now only 1 uqeyr paprment if letsupped there is one more paorment so i pased in that and dispaly there but wht if i want more then 100 query pamrnet then 


#for that we have request 

@app.get("/products")
def get_product(request: Request):
    print(request)
    query_params = request.query_params
    return {"query_params": query_params}
    #