import os
import oci


def publish_message(message_content):
    oci_configuration = {}
    oci_signer = oci.auth.signers.get_resource_principals_signer()
    oci_service_endpoint = os.getenv("OCI_QUEUE_ENDPOINT")
    oci_queue_id = os.getenv("OCI_QUEUE_ID")

    oci_queue_client = oci.queue.QueueClient(
        config=oci_configuration,
        signer=oci_signer,
        service_endpoint=oci_service_endpoint,
    )

    publish_message_response = oci_queue_client.put_messages(
        queue_id=oci_queue_id,
        put_messages_details=oci.queue.models.PutMessagesDetails(
            messages=[oci.queue.models.PutMessagesDetailsEntry(content=message_content)]
        ),
    )
    return publish_message_response


# ==========
# EXAMPLE
# ==========
# if __name__ == "__main__":
#     response = publish_message(
#         message_content="Hola desde la Universidad de Lima",
#     )
#     print(response.data)
#     response = publish_message(
#         message_content='[{"ID_PERSONA": 89, "ID_EMPRESA": 4, "MONTO": 780}, {"ID_PERSONA": 66, "ID_EMPRESA": 5, "MONTO": 1447}, {"ID_PERSONA": 50, "ID_EMPRESA": 3, "MONTO": 736}]',
#     )
#     print(response.data)
