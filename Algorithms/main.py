import requests

# figd_BdfmoNt6S1BQeV5o_fkR_gL9hzwzieCRDq94Fn8h
# https://www.figma.com/design/WCJFFzKTC79QgoANAjMOSY/Untitled?node-id=0-1&t=FCU7HEu2QWq72nbR-1
file_id = 'WCJFFzKTC79QgoANAjMOSY'
access_token = 'figd_BdfmoNt6S1BQeV5o_fkR_gL9hzwzieCRDq94Fn8h'

url = f'https://api.figma.com/v1/files/{file_id}'

headers = {
   'X-Figma-Token': access_token
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
   design_data = response.json()
   print("Данные файла Figma:", design_data)
else:
   print("Ошибка:", response.status_code, response.text)