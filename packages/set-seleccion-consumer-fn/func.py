import io
import json
import logging

from atp_conn import get_connection
from fdk import response


def handler(ctx, data: io.BytesIO = None):
    message = data.getvalue().decode("utf-8").strip().replace("[", "").replace("]", "")
    logging.getLogger().info("Msg recibido: %s", message)

    results = []
    status_code = 200

    try:
        with get_connection() as conn:
            cursor = conn.cursor()

            logging.getLogger().info("Procesando mensaje: %s", message)
            try:
                cursor.execute(
                    "INSERT INTO votacion (comida_votada) VALUES (:1)",
                    [message],
                )
                if cursor.rowcount == 1:
                    results.append({"status": "success", "message": message})
                else:
                    results.append({"status": "error", "message": message})
            except Exception as e:
                logging.getLogger().error("Error insertando '%s': %s", message, str(e))
                results.append({"status": "error", "message": str(e), "data": message})

            conn.commit()

    except Exception as e:
        logging.getLogger().error("Error general: %s", str(e))
        status_code = 500
        results = [{"status": "error", "message": str(e)}]

    return response.Response(
        ctx,
        response_data=json.dumps(results),
        headers={"Content-Type": "application/json"},
        status_code=status_code,
    )
