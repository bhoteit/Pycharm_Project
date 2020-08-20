import json
import requests
from .config import *

def Fetch_email(email_id,json_output=False):
    url = 'https://api.fullcontact.com/v3/person.enrich'
    headers = {'Authorization': f'Bearer{fullcontact_api_key}'}
    data = json.dumps({"email":  email_id})
    response = requests.post(url, data=data, headers=headers)

    if json_output:
        print(response.json())
        return

    if response.status_code == 401:
        print('Erreur Fullcontact_api_Cle')
        return

    if response.status_code == 403:
        print('Erreur authentification')
        return

    if response.status_code == 404:
        print('Erreur Profile')
        return


    print('Details_mail')
    attributs = ["fullName","ageRange","gender" , "location" ,   "title",
                 "organization" , "linkedin","bio","avatar", "details"]
    response = response.json()
    for attribut in attributs :
        try:
            valeur = response[attribut]
            if valeur is not None:
                print(f'{attribut.capitalize()}::{valeur}')
        except KeyError:
            pass
    print('\nPlus de details:')
    print(('-' * 20 ))
    details = ['emails','phones', 'employment','education','interests' ]
    for attribut in details:
        try:
            valeur_liste = response['details'][attribut]
            if valeur_liste:
                print(f'{attribut.capitalize()}::')
                print(('-' * 20))
                for valeur in valeur_liste :
                    if isinstance(valeur, str):
                        print(valeur, end=' ')
                    else:
                        for data in valeur:
                            print(f'{data.capitalize()}::{valeur[data]}')
                        print()
                print()
        except KeyError:
            pass
        