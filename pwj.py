import json


def handle_json():
    # print("Handle json Here")
    json_data = open("repo.json").read()
    data = json.loads(json_data)
    for key in data["Github"]:
        print("Numele este: " + data["Github"][key]["name"] + " si URL-ul este: " + data["Github"][key]["url"])
        # print(data["Github"][key]["url"])


if __name__ == "__main__":
    handle_json()