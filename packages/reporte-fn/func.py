import io
import json
import logging

from atp_conn import get_connection
from fdk import response


def handler(ctx, data: io.BytesIO = None):
    logging.getLogger().debug("Retornando votos desde Oracle ATP DB")
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT comida_votada, COUNT(1) as votos FROM votacion GROUP BY comida_votada ORDER BY votos DESC"
        )
        result = cursor.fetchall()
        res = [{"tipo_comida": row[0], "votos": row[1]} for row in result]

    return response.Response(
        ctx,
        response_data=json.dumps(res),
        headers={"Content-Type": "application/json"},
    )
