# Conexões com o GCP em Python

### Pré-Requisito

- Ter o gcloud configurado na sua máquina.
- Ter um projeto no GCP o qual você tenha acesso e algum segredo cadastrado no secret manager:
- Faça login no gcloud com os seguintes comandos:
 
  `` gcloud auth login``
  
    `` gcloud auth application-default login``
  
- Configure a variável de ambiente (windows):
  
  name: GOOGLE_APPLICATION_CREDENTIALS
  
  value: %APPDATA%\gcloud\application_default_credentials.json

### Adaptação do código

No arquivo model.secretManager.py altere a classe DataBaseCredencials de acordo com as suas necessidades:
  - Na linha 28, altere "data-base" pelo nome do segredo cadastrado no GCP e o parâmetro "9364527392" pelo nome do seu projeto no GCP.
  - Execute o arquivo main.py
