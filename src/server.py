"""
Main module of the server file
"""

# 3rd party moudles
from flask import render_template
import connexion


# local modules
import config

def create_app(config_filename=None):


    # Get the application instance
    connex_app = config.connex_app

    # Read the swagger.yml file to configure the endpoints
    connex_app.add_api("swagger.yml")

    # # create the application instance
    # app = connexion.App(__name__, specification_dir="./")
    #
    # # Cead the swagger.yml file to configure the endpoints
    # app.add_api("swagger.yml")


    return connex_app



if __name__ == "__main__":
    connex_app = create_app()
    connex_app.run(debug=True)


    # Create a URL route in our application for "/"
    @connex_app.route("/")
    def home():
        """
        This function just responds to the browser URL
        localhost:5000/

        :return:        the rendered template "home.html"
        """
        return render_template("home.html")