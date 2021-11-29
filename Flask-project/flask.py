
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