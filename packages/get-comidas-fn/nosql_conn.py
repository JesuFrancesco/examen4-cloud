import os
import borneo


def get_connection():
    signer = borneo.iam.SignatureProvider.create_with_resource_principal()
    region = borneo.Regions.US_ASHBURN_1
    compartment = os.getenv("COMPARTMENT_OCID")

    config = (
        borneo.NoSQLHandleConfig(region)
        .set_authorization_provider(signer)
        .set_default_compartment(compartment)
    )
    handle = borneo.NoSQLHandle(config)
    return handle
