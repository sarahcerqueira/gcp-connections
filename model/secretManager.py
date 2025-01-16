from google.cloud.secretmanager import SecretManagerServiceClient
from google.cloud.secretmanager_v1 import AccessSecretVersionResponse
from model import util

class GcpSecrets:

    __secretManagerClient: SecretManagerServiceClient

    def __init__(self):
        self.__secretManagerClient = SecretManagerServiceClient()

    def __getSecretCompletePath(self, secretName:str, gcpProject:str)->str:
        return f"projects/{gcpProject}/secrets/{secretName}/versions/latest"

    def __getSecretRequest(self, secretName:str, gcpProject:str)->dict:
        return {"name": self.__getSecretCompletePath(secretName,gcpProject )}

    def __requestSecret(self, secretName:str, gcpProject:str)->AccessSecretVersionResponse:
        return self.__secretManagerClient.access_secret_version(request= self.__getSecretRequest(secretName,gcpProject ))

    def getSecret(self, secretName:str, gcpProject:str)->str:
        return self.__requestSecret(secretName, gcpProject).payload.data.decode('utf-8')


class DataBaseCredencials:

    def __getCredentialFromGCP(self)->str:
        return GcpSecrets().getSecret("data-base", "9364527392")

    def __extractCredentials(self, data:str)->tuple:
        dictData = util.convertStringToJson(data)
        return dictData["client_id"], dictData["client_secret"]

    @property
    def credential(self)->tuple:
        return self.__extractCredentials(
            self.__getCredentialFromGCP()
        )