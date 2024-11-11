from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/clients")
def clients():
    with open("data/clients.json", "r") as f:
        clients_str = f.read()
    all_clients = json.loads(clients_str)
    return render_template("clients.html", clients=all_clients)

@app.route("/clients/add", methods=['GET', 'POST'])
def create():
    with open("data/clients.json", "r") as f:
        clients_str = f.read()
    all_clients = json.loads(clients_str)

    next_id = 1 if len(all_clients) == 0 else all_clients[-1]["id"] + 1

    if request.method == "POST":
        client_name = request.form["client_name"]
        if client_name == "":
            return "Name is required"
        
        all_clients.append({"id": next_id, "name": client_name})
        with open("data/clients.json", "w") as f:
            f.write(json.dumps(all_clients))
        
        return redirect(url_for("clients"))

    return render_template("add.html")

@app.route("/clients/<id>")
def client(id):
    with open("data/clients.json", "r") as f:
        clients_str = f.read()
    all_clients = json.loads(clients_str)
    client_by_id = next((client for client in all_clients if client["id"] == int(id)), None)
    return render_template("client.html", client=client_by_id)

@app.route("/clients/edit/<id>", methods=['GET', 'POST'])
def client_edit(id):
    with open("data/clients.json", "r") as f:
        clients_str = f.read()
    all_clients = json.loads(clients_str)

    client_by_id = next((client for client in all_clients if client["id"] == int(id)), None)
    client_index = all_clients.index(client_by_id) if client_by_id else None

    if request.method == 'POST' and client_index is not None:
        client_name = request.form["client_name"]
        all_clients[client_index] = {"id": client_by_id["id"], "name": client_name}

        with open("data/clients.json", "w") as f:
            f.write(json.dumps(all_clients))
        
        return redirect(url_for("clients"))

    return render_template("edit.html", client_id=id, client=client_by_id)

@app.route("/clients/delete")
def client_delete():
    with open("data/clients.json", "r") as f:
        clients_str = f.read()
    all_clients = json.loads(clients_str)

    client_id = request.args.get("id")
    client_by_id = next((client for client in all_clients if client["id"] == int(client_id)), None)
    if client_by_id:
        all_clients.remove(client_by_id)
        with open("data/clients.json", "w") as f:
            f.write(json.dumps(all_clients))

    return redirect(url_for("clients"))

if __name__ == "__main__":
    app.run()
