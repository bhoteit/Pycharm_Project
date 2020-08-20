import argparse
from modules import (Fetch_email, Details_Entreprise)
#Definir Argument
parser = argparse.ArgumentParser()
parser.add_argument("-m","--email",metavar='',help="Recherhce Mail")
parser.add_argument("-d","--domain",metavar='',help="Recherche Nom de Domaine")
parser.add_argument("-j","--json",metavar='',help="Afficher Sortie JSON")
args = parser.parse_args()

if args.domain:
    domain = args.domain
    Details_Entreprise(domain, args.json)
    exit()
elif args.email:
    email_id = args.email
    Fetch_email(email_id, args.json)
    exit()
else:
    print("""
    
██╗░░░░░██████╗░  ███╗░░░███╗██╗░█████╗░░██████╗░███████╗
██║░░░░░╚════██╗  ████╗░████║██║██╔══██╗██╔════╝░██╔════╝
██║░░░░░░█████╔╝  ██╔████╔██║██║███████║██║░░██╗░█████╗░░
██║░░░░░░╚═══██╗  ██║╚██╔╝██║██║██╔══██║██║░░╚██╗██╔══╝░░
███████╗██████╔╝  ██║░╚═╝░██║██║██║░░██║╚██████╔╝███████╗
╚══════╝╚═════╝░  ╚═╝░░░░░╚═╝╚═╝╚═╝░░╚═╝░╚═════╝░╚══════╝

░█████╗░░██████╗██╗███╗░░██╗████████╗
██╔══██╗██╔════╝██║████╗░██║╚══██╔══╝
██║░░██║╚█████╗░██║██╔██╗██║░░░██║░░░
██║░░██║░╚═══██╗██║██║╚████║░░░██║░░░
╚█████╔╝██████╔╝██║██║░╚███║░░░██║░░░
░╚════╝░╚═════╝░╚═╝╚═╝░░╚══╝░░░╚═╝░░░


Usage: osint-spy.py [options]
            Options:
            -h,            --help 
             --email                                  Obtenir des renseignement sur un adresse mail 
             --json                                   Afficher les sorties JSON
              --domain                                Obtenir des renseignements sur un nom de domaine   


""")

