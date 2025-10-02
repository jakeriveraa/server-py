from flask import Flask, jsonify, request
from http import HTTPStatus
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# http://127.0.0.1:5000
@app.route("/", methods=["GET"])
def index():
    return "welcome to Flask framework!"

# http://127.0.0.1:5000/cohort-60
@app.route("/cohort-60", methods=["GET"])
def hello_world():
    print("Cohort 60 end point accessed")
    return "Hello Cohort#60"

# http://127.0.0.1:5000/contact
@app.route("/contact", methods=["GET"])
def contact():
    information = {"email": "lololjajajaaj@ok.lol", "phone": "808-376-5793"}
    return information

# http://127.0.0.1:5000/course
@app.route("/course", methods=["GET"])
def course_information():
    return {
        "title": "introductory Web API Flask",
        "duration": "4 sessions",
        "level": "Beginner"
    }

# http://127.0.0.1:5000/user
@app.route("/user", methods=["GET"])
def user_info():

    return {
        "Favorite_technologies": [
            "Vue.js",
            "FastApi"
        ],
        "is_active": "true",
        "name": "carlos",
        "role": "student"
    }

student_names = ["zane","michael","reggie","tim","jake","jose"]

# http://127.0.0.1:5000/students
@app.route("/students", methods=["GET"])
def get_students():
    print("Students endpoint accessed")
    return student_names



@app.route("/students", methods=["POST"])
def add_student():
    student_names.append("Leo")
    return student_names


# -------- Assignment #1 --------
products = [
  {"id": 1, "name": "Gengar", "price": 25000},
  {"id": 2, "name": "Pikachu", "price": 2000},
  {"id": 3, "name": "Charizard", "price": 70000},
  {"id": 4, "name": "Mew", "price": 1000000000}
]
#products = [
 # {"id": 1, "title": "Cake", "price": 25, "category": "Electronics", "image": "https://picsum.photos/seed/1/300/300"},
  #{"id": 2, "title": "Ice-cream", "price": 5, "category": "Kitchen", "image": "https://picsum.photos/seed/2/300/300"},
  #{"id": 3, "title": "Cookie", "price": 3, "category": "Electronics", "image": "https://picsum.photos/seed/3/300/300"},
  #{"id": 4, "title": "Chocolate", "price": 10, "category": "Entertainment", "image": "https://picsum.photos/seed/4/300/300"}
#]

# http://127.0.0.1:5000/api/products
@app.route("/api/products", methods=["GET"])
def get_products():
    return products

# http://127.0.0.1:5000/api/products/count
@app.route("/api/products/count", methods=["GET"])
def get_product_count():
    count = len(products)
    return str(count)


# -------- Assignment #2 --------
@app.route("/api/products", methods=["POST"])
def create_product():
    data = request.get_json()
    data["id"] = len(products) + 1
    products.append(data)
    return jsonify({"message": "product added succsessfuly"}), HTTPStatus.CREATED


# UPDATE /api/products
@app.route("/api/products", methods=["PUT"])
def update_product(id):
    data = request.get_json()
    for product in products:
        if product["id"] == id:
            product["name"] = data.get("name")
            product["price"] = data.get("price")
            return jsonify({"message": "product updat3ed successfully"}), HTTPStatus.OK
    return jsonify({"message": "product not found"}), HTTPStatus.NOT_FOUND

# -------- session #4 --------
# Query Parameters
#A Query parameter is added to the end of the url to filter, sort or modify the response.
@app.route("/api/products/search", methods=["GET"])
def get_product_by_name():
    keyword = request.args.get("name")
    print(keyword)

    matched = []
    for product in products:
        if keyword in product["name"].lower():
            matched.append(product)
        #if product["name"].lower() == keyword:
            #matched.append(product)
    return jsonify({"results": matched}), HTTPStatus.OK

#session 2 

coupons = [
    {"_id": 1, "code": "WELCOME10", "discount": 10},
    {"_id": 2, "code": "FALL25", "discount": 25},
    {"_id": 3, "code": "VIP50", "discount": 50}
]

# read all coupons

# http://127.0.0.1:5000/api/coupons
@app.route("/api/coupons", methods=["GET"])
def get_coupons():
    return jsonify(coupons), HTTPStatus.OK


# create, add a new coupon

@app.route("/api/coupons", methods=["POST"])
def create_coupon():
    new_coupon = request.get_json()
    print(new_coupon)
    coupons.append(new_coupon)
    return jsonify(new_coupon), HTTPStatus.CREATED


# path parameter
# a path parameter is a dynamic segment of the url to pinpoint a specific item or resource.
# http://127.0.0.1:5000/greet/jake
@app.route("/greet/<string:name>", methods=["GET"])
def greet(name):
    return f"hello {name}", HTTPStatus.OK

# GET a coupon by id
@app.route("/api/coupons/<int:id>", methods=["GET"])
def get_coupon_by_id(id):
    for coupon in coupons:
        if coupon["_id"] == id:
            return jsonify(coupon), HTTPStatus.OK   
    return jsonify({"messag": "coupon not found"}), HTTPStatus.NOT_FOUND

# UPDATE - 

# DELETE - detele a coupon 
@app.route("/api/coupons/<int:id>", methods=["DELETE"])
def delete_coupon(id):
    for index, coupon in enumerate(coupons):
        if coupon["_id"] == id:
            coupons.pop(index)
            return jsonify({"message": "coupon not found"}), HTTPStatus.NO_CONTENT
    return "testing"







if __name__ == "__main__":
    app.run(debug=True)