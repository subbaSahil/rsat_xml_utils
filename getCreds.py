import base64

import json

from azure.identity import ClientSecretCredential

from azure.keyvault.secrets import SecretClient
 
def d365_preview_cred():

    encrypted_string = "eyJLZXlWYXVsdFVSTCI6ICJodHRwczovL2t2LXJzYXQtcG9jLXYyLnZhdWx0LmF6dXJlLm5ldC8iLCAiVGVuYW50SUQiOiAiYjE2YjUwNzgtM2MzNi00ODJlLWI5OGUtYjk4NjgyMmU4ZjdmIiwgIkNsaWVudElEIjogIjY5YzFjNDFmLTQzMzYtNDAzMi05NGNlLTAyZDcyZWE1Mjc0ZSIsICJDbGllbnRTZWNyZXQiOiAiSWM3OFF+bDQ0eX5BNDFvUmg2VVljbG9NeURpVnEtbX5wSkprdWJ4cyJ9"
 
    decoded_bytes = base64.b64decode(encrypted_string)

    keyvault_auth = json.loads(decoded_bytes.decode('utf-8'))
 
    try:

        credential = ClientSecretCredential(

            tenant_id=keyvault_auth["TenantID"],

            client_id=keyvault_auth["ClientID"],

            client_secret=keyvault_auth["ClientSecret"]

        )

        secret_client = SecretClient(

            vault_url=keyvault_auth["KeyVaultURL"],

            credential=credential

        )

        username = secret_client.get_secret("D365PreviewUsername").value

        password = secret_client.get_secret("D365PreviewPassword").value

        return {"username": username, "password": password}

    except Exception as e:

        raise RuntimeError(f"Failed to fetch secrets: {str(e)}")
 