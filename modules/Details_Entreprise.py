from .config import clearbit_API_Cle
from .utils import format_dict
import clearbit
import requests
clearbit.key = clearbit_API_Cle




def Details_Entreprise(domain, json_output=False):
    try:
        Entreprise = clearbit.Company.find(domain=domain,stream=True)
    except Exception as e:
        print(e)
    else:
        Details_Entreprise = None
        if Entreprise is not None:
            if json_output:
                Details_Entreprise = dict(Entreprise) #dictionnaire pour stocker les donnees

            else:
                format_dict(Entreprise)

        #Extraction Adresse Mail
        url = f'https://api.hunter.io/v2/domain-search?domain=stripe.com&api_key=1acc22706cbbedc9db8c2575e00dfa7325a299be'
        reponse = requests.get(url)
        json_reponse = reponse.json()
        if json_output:
             if reponse.ok:
                Details_Entreprise['Adresse Mail :'] = json_reponse
             else:
                Details_Entreprise['Erreur Extraction Mail'] = json_reponse
             print(Details_Entreprise)
        else:
            if reponse.ok:
                liste_mail = json_reponse['data']['emails']
                if liste_mail :
                    print("\nAdresse Mail::")
                    for mail in liste_mail :
                        print(mail['value'])
            else:
                print("\n Erreur lors de l'extraction des mails en utilisant la cle API_EMAIL_HUNTER")
                print(f"Erreur description::{json_reponse['erreur'][0]['details']}.")


