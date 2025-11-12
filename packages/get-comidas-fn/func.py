import io
import json
import logging

import borneo
from nosql_conn import get_connection

from fdk import response


def handler(ctx, data: io.BytesIO = None):

    logging.getLogger().debug("Retornando comidas desde Oracle NoSQL DB")
    handle = get_connection()
    pSQL = "SELECT * FROM comidas"
    lista = []
    request = borneo.QueryRequest().set_statement(pSQL)
    while True:
        result = handle.query(request)
        lista.append(result.get_results())
        if request.is_done():
            break
    handle.close()

    res = json.dumps(lista)
    logging.getLogger().debug("Comidas obtenidas: " + res)

    return response.Response(
        ctx,
        response_data=res,
        headers={"Content-Type": "application/json"},
    )
