import sender_stand_request
import data
import copy

#Nombre del kit
def get_kit_body(name):
    #kit= copy.deepcopy(data.kit_body)
    kit= data.kit_body.copy()
    kit['name'] = name
    return kit

 #Prueba positiva
def positive_assert(kit_body):
     auth_token=sender_stand_request.get_new_user_token()
     response= sender_stand_request.post_new_client_kit(kit_body,auth_token)
     #Imprimir detalles de la respuesta
     print('Status Code: ', response.status_code)
     print('Response text: ', response.text)
     #Confirmación
     assert response.status_code==201
     assert response.json()['name']==kit_body['name']
def negative_assert_code_400(kit_body):
    auth_token= sender_stand_request.get_new_user_token()
    response=sender_stand_request.post_new_client_kit(kit_body,auth_token)
    # Imprimir detalles de la respuesta
    print('Status Code: ', response.status_code)
    print('Response text: ', response.text)
    #Confirmación
    assert response.status_code==400

#Lista de comprobación
# Prueba 1. número permitido de caracteres (1)
def test_kit_name_1_char():
    positive_assert(get_kit_body(data.kit_name_test_1))
    # Paso la prueba Status Code:  201

#Prueba 2. número permitido de caracteres (511)
def test_kit_name_511_char():
   kit_body=get_kit_body(data.kit_name_test_2)
   positive_assert(kit_body)
    #paso la prueba Status Code:  201 pero toca cambiar el valor de kit_body en data.py

#Prueba 3. numero de caracteres es menor a la cantidad permitida
def test_kit_name_0_char():
   negative_assert_code_400(get_kit_body(data.kit_name_test_3))
#code404
#Prueba 4. El número de caracteres es 512
def test_kit_name_512_char():
   negative_assert_code_400(get_kit_body(data.kit_name_test_4))
#code 404
#Prueba 5. Caracteres especiales
def test_kit_name_special_char():
   positive_assert(get_kit_body(data.kit_name_test_5))
#Prueba 6. Se permite espacios
def test_kit_name_space_char():
   positive_assert(get_kit_body(data.kit_name_test_6))
    #Paso la Prueba PASSED             [100%]Status Code: 201
#Prueba 7. Se permiten números
def test_kit_name_number_char():
   positive_assert(get_kit_body(data.kit_name_test_7))
    #paso la prueba PASSED            [100%]Status Code: 201
#Prueba 8. El parametro no se pasa en la solicitud
def test_kit_name_missing():
    auth_token=sender_stand_request.get_new_user_token()
    response=sender_stand_request.post_new_client_kit(data.kit_name_test_8,auth_token)
    assert response.status_code==400
    #No paso la prueba

#Prueba 9. Se ha pasado un tipo de parametro diferente, numero
def test_kit_name_wrong_type():
    auth_token=sender_stand_request.get_new_user_token()
    response=sender_stand_request.post_new_client_kit(data.kit_name_test_9,auth_token)
    assert response.status_code==400
    #FAILED             [100%]Status Code: 404

