import json
import pandas as pd


with open('test.json', 'r') as file:
    fhir_data = json.load(file)

type = fhir_data['entry'][0]['resource']['resourceType']
id = fhir_data['entry'][0]['resource']['id']
first_name = ' '.join(fhir_data['entry'][0]['resource']['name'][0]['given'])
last_name = fhir_data['entry'][0]['resource']['name'][0]['family']
telecom_directory = fhir_data['entry'][0]['resource']['telecom']
phone_numbers = []
for item in telecom_directory:
    phone_numbers.append(item['value'])

gender = fhir_data['entry'][0]['resource']['gender']
birthDate = fhir_data['entry'][0]['resource']['birthDate']
address_line = ' '.join(fhir_data['entry'][0]['resource']['address'][0]['line'])
address_city = fhir_data['entry'][0]['resource']['address'][0]['city']
address_state = fhir_data['entry'][0]['resource']['address'][0]['state']
address_postal_code = fhir_data['entry'][0]['resource']['address'][0]['postalCode']
address_country = fhir_data['entry'][0]['resource']['address'][0]['country']

combined_address = address_line + ' ' + address_city + ' ' + address_state + ' ' + address_postal_code + ' ' + address_country

data = [[id, first_name, last_name, phone_numbers, gender, birthDate, combined_address]]

df = pd.DataFrame(data, columns=['patient_id', 'first_name', 'last_name', 'phone_number', 'gender', 'birthDate', 'address'])

print(df)


# print(id)
# print(first_name)
# print(last_name)
# print(phone_numbers)
# print(gender)
# print(birthDate)
# print(address_line, address_city, address_state, address_postal_code, address_country)


# Extract relevant data from FHIR JSON
# patient_data = []
# for patient in fhir_data['entry']:
#     patient_info = patient['resource']

#     patient_dict = {
#         'id': patient_info['id'],
#         'name': patient_info['name'],
#         'gender': patient_info['gender'],
#         'birthDate': patient_info['birthDate']
#     }
#     patient_data.append(patient_dict)

#  # Convert data to Pandas DataFrame
# patient_df = pd.DataFrame(patient_data)

# print(patient_df)
