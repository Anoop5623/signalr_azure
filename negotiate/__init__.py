import azure.functions as func
import logging

def main(req: func.HttpRequest, connectionInfo) -> func.HttpResponse:
    logging.info("connection info")
    return func.HttpResponse(connectionInfo) 