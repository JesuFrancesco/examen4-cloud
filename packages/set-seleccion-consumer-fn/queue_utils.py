import os
import oci


def consume_message():
    oci_configuration = {}
    oci_signer = oci.auth.signers.get_resource_principals_signer()
    oci_service_endpoint = os.getenv("OCI_QUEUE_ENDPOINT")
    oci_queue_id = os.getenv("OCI_QUEUE_ID")

    oci_queue_client = oci.queue.QueueClient(
        config=oci_configuration,
        signer=oci_signer,
        service_endpoint=oci_service_endpoint,
    )

    message = oci_queue_client.get_messages(
        queue_id=oci_queue_id, visibility_in_seconds=25, timeout_in_seconds=5, limit=1
    )
    return message
