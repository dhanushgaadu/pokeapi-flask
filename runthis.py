import os
try:
    from flask import Flask,jsonify
    from requests import get
    from flask_cors import CORS
    import json
    import webbrowser

    app=Flask(__name__)
    CORS(app)
    @app.route("/<name>",methods=["GET"])
    def home(name):
        link=f"https://pokeapi.co/api/v2/pokemon/{name}"
        data=get_pokemon_data(link)
        return jsonify((data))
    @app.route("/")
    def index():
        return "Welcome to Pokemon API made by @dhanushgaadu"
    def get_pokemon_data(fulllink):
        api=get(fulllink).text
        ditto=dict(json.loads(api))
        lis={}
        lis.update({"name":ditto["species"]["name"]})
        for i in range(0,5):
            try:
                if ditto["stats"][i]["stat"]["name"]=="attack":
                    lis.update({"attack":ditto["stats"][i]["base_stat"]})
                elif ditto["stats"][i]["stat"]["name"]=="defense":
                    lis.update({"defence":ditto["stats"][i]["base_stat"]})
                elif ditto["stats"][i]["stat"]["name"]=="special-attack":
                    lis.update({"special_attack":ditto["stats"][i]["base_stat"]})
                elif ditto["stats"][i]["stat"]["name"]=="hp":
                    lis.update({"hp":ditto["stats"][i]["base_stat"]})
                else:
                    pass
            except IndexError:
                break 
        lis.update({"pic":ditto["sprites"]["other"]["official-artwork"]["front_default"]})
        return lis
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    webbrowser.open("index.html")
    app.run(host="0.0.0.0",port=80,debug=True)
except ModuleNotFoundError:
    os.system("python -m venv env")
    os.system("cd env/scripts")
    try:
        os.system("activate")
    except:
        os.system("./activate")
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    print("Some modules are missing please install them")
    if input("Do you want to install the requirements? (y/n): ").lower()=="y":
        os.system("pip install -r requirements.txt")
        os.system("python runthis.py")
    else:
        os.system("python runthis.py")
