import requests
import configuration
import data
import copy

#Crear Nuevo Usuario
def post_new_user():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=data.user_body,
                         headers={'Content-Type':'application/json'})
# Parametro de token de autenticación
def get_new_user_token():
    response = post_new_user()
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    return response.json()['authToken']
# Crear un nuevo kit
def post_new_client_kit(kit_body,auth_token):
    headers={'Authorization': f'Bearer {auth_token}'}
    return requests.post (configuration.URL_SERVICE + configuration.KITS_PATH,
                          json=data.kit_body,
                          headers=headers)
