from flask import Flask
import flask_restful as restful
import json

app = Flask(__name__)
api = restful.Api(app)


class Greetings(restful.Resource):
    def get(self) -> dict:
        intro_dict = {
            "message": "Greetings fellow human!\nThis is a simple API to get the coffee flavors defined by the SCA (Specialty Coffee Association).\nCheck out & support the SCA on https://sca.coffee/",
            "purpose": "Well, I just wanted to check out how to build APIs with Flask.",
            "copyright": "'The Coffee Taster's Flavor Wheel' by the SCA and WCR (©2016-2020)",
            "link": "https://sca.coffee/research/coffee-tasters-flavor-wheel",
            "license": "https://creativecommons.org/licenses/by-nc-nd/4.0/",
            "disclaimer": "I'm not associated with the SCA. The original Flavor Wheel is distributed as PDF and I merely created a JSON version."
        }
        return intro_dict


class Flavors(restful.Resource):
    def get(self, general: str = "all", specific: str = "all") -> dict:

        # load locall saved json file
        with open("./resources/sca_coffee_flavors.json") as file:
            flavor_dict = json.load(file)

        # get subset of flavors associated with a general flavor
        # i.e. fruity
        if general != "all":
            flavor_dict = flavor_dict.get(general)

        # get a list of flavors associated with a specific flavor
        # i.e. berry
        if specific != "all":
            flavor_dict = flavor_dict.get(specific)

        return flavor_dict


api.add_resource(Greetings, "/")
api.add_resource(
    Flavors,
    "/flavors",  # json with all flavors
    "/flavors/<string:general>",  # json with flavors for one general flavor category
    "/flavors/<string:general>/<string:specific>",  # list of flavors for a specific flavor category
)


if __name__ == "__main__":
    app.run(debug=True)
