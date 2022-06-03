from flask import Flask , request , jsonify

app = Flask(__name__)

contacts = [ {'id': 1, 'Name': u'Rajesh Shukla', 'Contact': u'3333456987', 'done': False },
{'id': 2, 'Name': u'Mukesh Singh', 'Contact': u'5426789632', 'done': False},
{'id': 3, 'Name': u'Harshita Pasi', 'Contact': u'4563289657', 'done': False}]

@app.route("/add-contact", methods = ["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status": "ERROR",
            "message": "Please provide the data"
        } , 400)
    contact = {
        "id": contacts[-1]["id"] + 1,
        "Name": request.json["Name"],
        "Contact": request.json.get["Contact",""],
        "done": False
    }
    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message":"Task added successfully"
    })

if __name__ == "__main__":
    app.run(debug=True)