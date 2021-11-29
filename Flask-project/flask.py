
from flask import Flask,Response, request
import pymongo
import json
from bson.objectid import ObjectId

app=Flask(__name__)

try:
    client = pymongo.MongoClient("mongodb+srv://jayadeep:jayadeep@cluster0.jd9mv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.get_database('suta')
    register = db.sutatable
    region=db.sutacategory
except:
    print("Error cannot connect to db")


"""
funtion: insert_product:: This function used to insert product details uses post method
               and does not take any parameters 
returns:: This function returns response in json format as user created and returns product unique id
"""
@app.route("/products",methods=["POST"])
def insert_product():
    try:
        user={"productname":request.form["productname"],"originalprice":request.form["originalprice"],"offerprice":request.form["offerprice"],
        "image":request.form["image"],"quantity":request.form["quantity"]}
        dbresponse=register.products.insert_one(user)
        print(dbresponse.inserted_id)
        # for attr in dir(dbresponse):
        #     print(attr)
        return Response(
            response=json.dumps(
                {"message":"user created", 
                "id":f"{dbresponse.inserted_id}"}),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)

"""
funtion: get_some_products:: This function used to display inserted product details uses get method
               and does not take any parameters 
returns:: This function returns response in json format and display existing users
"""
@app.route("/products",methods=["GET"])
def get_some_products():
    try:
        data=list(register.products.find())
        for user in data:
            user['_id'] = str(user["_id"])
        
        return Response(response=json.dumps(data),
    status=500,
    mimetype="application/json")
    except Exception as ex:
        print(ex)
    return Response(response=json.dumps({"message":"cannot read users"}),
    status=500,
    mimetype="application/json")


"""
funtion: search:: This function used to search details using id uses method get
                 and does not take any parameters 
returns:: This function returns response in json format 
"""
@app.route("/products/<id>",methods=["GET"])
def search(id):
    try:
        data=list(register.products.find_one({"_id":ObjectId(id)}))
        # for attr in dir(data):
        #     print(f"********{attr}********")
        for user in data:
            user['_id'] = str(user["_id"])
        
        return Response(response=json.dumps(data),
    status=500,
    mimetype="application/json")
    except Exception as ex:
        print(ex)
    return Response(response=json.dumps({"message":"no users found"}),
    status=500,
    mimetype="application/json")


"""
funtion: update_some_product:: This function used to update inserted product details uses patch method
               and  take parameters as id 
returns:: This function returns response in json format and update user
"""
@app.route("/products/<id>",methods=["PATCH"])
def update_user_product(id):
    try:
        dbResponse=register.products.update_one({"_id":ObjectId(id)},{"$set":{"originalprice":request.form["originalprice"]}})
        for attr in dir(dbResponse):
            print(f"********{attr}********")
        return Response(
            response=json.dumps(
                {"message":"user updated"}),
            status=200,
            mimetype="application/json"
        )

    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps(
                {"message":"sorry cannot update user"}),
            status=200,
            mimetype="application/json"
        )
"""
funtion: delete_user_products:: This function used to delete exusting product details uses delete method
               and take parameters as id  
returns:: This function returns response in json format and user deleted with unique id
"""
@app.route("/products/<id>",methods=["DELETE"])
def delete_user_product(id):
    try:
        dbResponse = register.products.delete_one({"_id":ObjectId(id)})
        for attr in dir(dbResponse):
            print(f"****{attr}****")
        return Response(
            response=json.dumps(
                {"message":"user deleted","id":f"{id}"}),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print("ex")
        return Response(
            response=json.dumps(
                {"message":"sorry cannot delete a user"}),
            status=200,
            mimetype="application/json"
        )


"""
funtion: categorytable:: This function used to  inserted category details uses post method
               and does not take any parameters 
returns:: This function returns response in json format and display euser created
"""
@app.route("/categorytable",methods=["POST"])
def categorytable():
    try:
        user={"categoryname":request.form["categoryname"],"categoryimage":request.form["categoryimage"]}
        dbresponse=region.categorytable.insert_one(user)
        print(dbresponse.inserted_id)
        # for attr in dir(dbresponse):
        #     print(attr)
        return Response(
            response=json.dumps(
                {"message":"user created", 
                "id":f"{dbresponse.inserted_id}"}),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)


"""
funtion: get_some_category:: This function used to display inserted category details uses get method
               and does not take any parameters 
returns:: This function returns response in json format and display existing users
"""
@app.route("/categorytable",methods=["GET"])
def get_some_category():
    try:
        data=list(region.categorytable.find())
        for user in data:
            user['_id'] = str(user["_id"])
        
        return Response(response=json.dumps(data),
    status=500,
    mimetype="application/json")
    except Exception as ex:
        print(ex)
    return Response(response=json.dumps({"message":"cannot read users"}),
    status=500,
    mimetype="application/json")



"""
funtion: search:: This function used to search details using id uses method get
                 and does not take any parameters 
returns:: This function returns response in json format 
"""

@app.route("/categorytable/<id>",methods=["GET"])
def search(id):
    try:
        data=list(register.categorytable.find_one({"_id":ObjectId(id)}))
        # for attr in dir(data):
        #     print(f"********{attr}********")
        for user in data:
            user['_id'] = str(user["_id"])
        
        return Response(response=json.dumps(data),
    status=500,
    mimetype="application/json")
    except Exception as ex:
        print(ex)
    return Response(response=json.dumps({"message":"no users found"}),
    status=500,
    mimetype="application/json")
"""
funtion: update_user_category:: This function used to update inserted category details uses patch method
               and take id as parameters 
returns:: This function returns response in json format and display updated user
"""   
@app.route("/categorytable/<id>",methods=["PATCH"])
def update_user_category(id):
    try:
        dbResponse=region.categorytable.update_one({"_id":ObjectId(id)},{"$set":{"categoryimage":request.form["categoryimage"]}})
        for attr in dir(dbResponse):
            print(f"********{attr}********")
        return Response(
            response=json.dumps(
                {"message":"user updated"}),
            status=200,
            mimetype="application/json"
        )

    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps(
                {"message":"sorry cannot update user"}),
            status=200,
            mimetype="application/json"
        )

    
"""
funtion: delete_user_category:: This function used to delete inserted category details uses delete method
               and  take id as parameters 
returns:: This function returns response in json format and display unique id with message
"""
@app.route("/categorytable/<id>",methods=["DELETE"])
def delete_user_category(id):
    try:
        dbResponse = region.categorytable.delete_one({"_id":ObjectId(id)})
        for attr in dir(dbResponse):
            print(f"****{attr}****")
        return Response(
            response=json.dumps(
                {"message":"user deleted","id":f"{id}"}),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print("ex")
        return Response(
            response=json.dumps(
                {"message":"sorry cannot delete a user"}),
            status=200,
            mimetype="application/json"
        )



if __name__ == "__main__":
    app.run(debug="True")