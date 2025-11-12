import io
import json
import logging

from atp_conn import get_connection
from queue_utils import consume_message
from fdk import response


def handler(ctx, data: io.BytesIO = None):
    message = consume_message()

    logging.getLogger().info("JSON recibido: %s", message.data)

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO votacion (comida_votada) VALUES (%s)", (message.data,)
        )
        conn.commit()

    return response.Response(
        ctx, response_data=message.data, headers={"Content-Type": "application/json"}
    )
