import io
import json
import logging

from queue_utils import publish_message
from fdk import response


def handler(ctx, data: io.BytesIO = None):
    body = json.loads(data.getvalue())

    logging.getLogger().info("JSON recibido: %s", body)

    comida = body.get("comida")

    res = publish_message(comida)

    logging.getLogger().info("Mensaje publicado: %s", res.data)

    return response.Response(
        ctx, response_data=res.data, headers={"Content-Type": "application/json"}
    )
