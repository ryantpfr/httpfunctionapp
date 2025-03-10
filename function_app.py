import azure.functions as func
import logging
import os
# import requests

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    text = requests.get("https://www.google.com").text
    # text = "dsdsdsd"

    return func.HttpResponse(text)