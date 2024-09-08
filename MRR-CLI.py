# Set the API key and API Secret in the .env file.
import os
from dotenv import load_dotenv
from cmd import Cmd
import requests
import json
import hmac
import hashlib
import time

# Load environment variables from .env file
load_dotenv()

# Environment variables
API_BASE_URL = os.getenv("API_BASE_URL")
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

# ANSI color codes for red and orange
COLOR_RED = "\033[31m"
COLOR_ORANGE = "\033[33m"
COLOR_RESET = "\033[0m"

# Helper function to generate authentication headers
def generate_auth_headers(endpoint):
    nonce = str(int(time.time() * 1000))
    sign_string = API_KEY + nonce + endpoint
    sign = hmac.new(API_SECRET.encode(), sign_string.encode(), hashlib.sha1).hexdigest()
    return {
        'x-api-sign': sign,
        'x-api-key': API_KEY,
        'x-api-nonce': nonce
    }

# Persistent session to manage connections
session = requests.Session()
session.headers.update({'User-Agent': 'Raccoon MRR CLI'})

# Utility function to make API requests
def api_request(endpoint, method='get', data=None, params=None):
    url = f"{API_BASE_URL}{endpoint}"
    headers = generate_auth_headers(endpoint)
    if method == 'get':
        response = session.get(url, headers=headers, params=params)
    elif method == 'put':
        response = session.put(url, headers=headers, json=data)
    elif method == 'delete':
        response = session.delete(url, headers=headers, json=data)
    if response.status_code != 200:
        return {'error': response.json().get('message', 'Failed to process request')}
    return response.json()

class MRRCLI(Cmd):
    intro = COLOR_ORANGE +'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣴⣶⣶⣾⣿⣿⣿⣿⣿⣿⣷⣶⣶⣦⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⡿⠿⠿⢿⠛⠋⠉⠉⠙⠛⠛⠛⠿⠿⢿⣿⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⡿⢿⠹⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⢿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⡿⠛⣿⣯⣀⣀⠀⠙⢿⣦⣄⣀⡀⢀⣴⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⠟⠁⠀⠀⠈⠙⣛⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⠋⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣷⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣴⣿⣿⠟⠁⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠙⠛⢿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣦⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣾⣿⣿⣯⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣷⡀⠀⠀⠀
⠀⠀⢀⣾⣿⡿⠁⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣷⡀⠀⠀
⠀⠀⣾⣿⣿⠁⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠁⠀⠀⠈⠙⠻⣿⣿⣿⣿⣿⡿⠿⣿⣶⣤⣴⣶⣦⡀⠀⠀⠀⠈⢿⣿⣷⠀⠀
⠀⣸⣿⣿⠃⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⠀⠀⠀⠈⠙⢿⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⡓⠀⠀⠀⠀⠘⣿⣿⣇⠀
⢀⣿⣿⡏⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡝⢿⣿⣿⣿⣿⠿⠛⠉⠀⠀⠉⠛⠻⢿⣦⣄⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⢹⣿⣿⡀
⢸⣿⣿⠃⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣦⣄⠀⠀⠀⠀⣿⠿⣯⡙⢻⡏⠀⠀⠀⠀⠀⠀⠈⣿⣿⡇
⣾⣿⣿⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀In Bitcoin We⠀⠀⠀⠙⢿⣿⣿⣶⣶⣤⣿⣦⣼⣿⡄⠀⠀⠀⠀⠀⠀⣿⣿⣿
⣿⣿⡏⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀Trust⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠙⠛⠛⠛⠁⢸⣿⡀⠀⠀⠀⠀⠀⠀⢸⣿⣿
⣿⣿⡇⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠈⣿⣧⠀⠀⠀⠀⠀⢳⣄⢸⣿⣿
⢿⣿⣿⢀⣤⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⢹⣿⣆⠀⠀⠀⠀⢸⡿⣿⣿⣿
⢸⣿⣿⡄⠉⠛⠉⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⢻⣿⡷⢦⣤⣶⠟⢁⣿⣿⡇
⠘⣿⣿⣇⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠙⢿⣤⣤⣤⡴⣸⣿⣿⠃
⠀⢹⣿⣿⡄⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠈⠉⠁⢠⣿⣿⡏⠀
⠀⠀⢿⣿⣷⡀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⢀⣾⣿⡿⠀⠀
⠀⠀⠈⢿⣿⣷⡀⠀⠀⠀⠀⢸⣿⣿⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢀⣾⣿⡿⠁⠀⠀
⠀⠀⠀⠈⢿⣿⣷⡄⠀⣀⣀⣸⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⢠⣾⣿⡿⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠻⣿⣿⣦⡈⠛⠛⠋⠀⠀⠀⢹⡟⠀⠈⠉⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣴⣿⣿⠟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⢿⣿⣷⣄⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣶⣦⣤⣀⣀⡀⠀⠀⠀⠀⣀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀
Welcome to the Raccoon MRR API client. 
Type help or ? to list commands.
'''
    prompt = '(mrr) '

    # Commands for API endpoints
    def do_whoami(self, arg):
        "Test connectivity and return information about you"
        print(json.dumps(api_request('/whoami'), indent=2))

    def do_get_servers(self, arg):
        "Get a list of MRR rig servers"
        print(json.dumps(api_request('/info/servers'), indent=2))

    def do_get_algos(self, arg):
        "Get all algos and statistics for them"
        print(json.dumps(api_request('/info/algos'), indent=2))

    def do_get_algo(self, algo):
        "Get statistics for an algo by name"
        if algo:
            print(json.dumps(api_request(f'/info/algos/{algo}'), indent=2))
        else:
            print("Usage: get_algo <algo_name>")

    def do_get_currencies(self, arg):
        "Get a list of currencies"
        print(json.dumps(api_request('/info/currencies'), indent=2))

    def do_get_account(self, arg):
        "Retrieve account information"
        print(json.dumps(api_request('/account'), indent=2))

    def do_get_account_balance(self, arg):
        "Retrieve account balances"
        print(json.dumps(api_request('/account/balance'), indent=2))

    def do_get_account_transactions(self, arg):
        "List/search transaction history"
        filters = json.loads(arg) if arg else {}
        print(json.dumps(api_request('/account/transactions', params=filters), indent=2))

    def do_get_account_profile(self, arg):
        "List all pool profiles, or list by algo"
        params = json.loads(arg) if arg else {}
        print(json.dumps(api_request('/account/profile', params=params), indent=2))

    def do_create_account_profile(self, profile):
        "Create a pool profile"
        data = json.loads(profile) if profile else {}
        print(json.dumps(api_request('/account/profile', method='put', data=data), indent=2))

    def do_get_specific_profile(self, profile_id):
        "Get a specific pool profile"
        print(json.dumps(api_request(f'/account/profile/{profile_id}'), indent=2))

    def do_update_account_profile(self, args):
        "Update a specific pool profile"
        profile_id, profile_data = args.split(' ', 1)
        data = json.loads(profile_data)
        print(json.dumps(api_request(f'/account/profile/{profile_id}', method='put', data=data), indent=2))

    def do_delete_account_profile(self, profile_id):
        "Delete a specific pool profile"
        print(json.dumps(api_request(f'/account/profile/{profile_id}', method='delete'), indent=2))

    def do_test_pool(self, args):
        "Test a pool for connectivity and functionality"
        params = json.loads(args) if args else {}
        print(json.dumps(api_request('/account/pool/test', params=params), indent=2))

    def do_get_pricing(self, arg):
        "Retrieve current pricing information"
        try:
            result = api_request('/pricing')
            if 'error' in result:
                print(f"Error: {result['error']}")
            else:
                print(json.dumps(result, indent=2))
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def do_get_rental(self, arg):
        "Get information on rentals by rental ID. Usage: get_rental <ID1>[;<ID2>...]"
        try:
            result = api_request(f'/rental/{arg}')
            if 'error' in result:
                print(f"Error: {result['error']}")
            else:
                print(json.dumps(result, indent=2))
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def do_create_rental(self, args):
        "Create a new rental. Usage: create_rental <JSON data>"
        try:
            data = json.loads(args)
            result = api_request('/rental', method='put', data=data)
            if 'error' in result:
                print(f"Error: {result['error']}")
            else:
                print(json.dumps(result, indent=2))
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def do_apply_profile_to_rental(self, args):
        "Apply a pool profile to one or more rentals. Usage: apply_profile_to_rental <rental_ids> <profile_id>"
        rental_ids, profile_id = args.split()
        try:
            data = {'profile_id': profile_id}
            result = api_request(f'/rental/{rental_ids}/profile', method='put', data=data)
            if 'error' in result:
                print(f"Error: {result['error']}")
            else:
                print(json.dumps(result, indent=2))
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def do_get_rental_pools(self, arg):
        "List pools assigned to one or more rentals. Usage: get_rental_pools <rental_ids>"
        try:
            result = api_request(f'/rental/{arg}/pool')
            if 'error' in result:
                print(f"Error: {result['error']}")
            else:
                print(json.dumps(result, indent=2))
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def do_add_replace_pool_on_rental(self, args):
        "Add or replace a pool on one or more rentals. Usage: add_replace_pool_on_rental <rental_ids> <JSON data>"
        rental_ids, json_data = args.split(' ', 1)
        try:
            data = json.loads(json_data)
            result = api_request(f'/rental/{rental_ids}/pool', method='put', data=data)
            if 'error' in result:
                print(f"Error: {result['error']}")
            else:
                print(json.dumps(result, indent=2))
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def do_delete_pool_on_rental(self, arg):
        "Delete a pool on one or more rentals. Usage: delete_pool_on_rental <rental_ids>"
        try:
            result = api_request(f'/rental/{arg}/pool', method='delete')
            if 'error' in result:
                print(f"Error: {result['error']}")
            else:
                print(json.dumps(result, indent=2))
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def do_purchase_extension_on_rental(self, args):
        "Purchase an extension on one or more rentals. Usage: purchase_extension_on_rental <rental_ids> <JSON data>"
        rental_ids, json_data = args.split(' ', 1)
        try:
            data = json.loads(json_data)
            result = api_request(f'/rental/{rental_ids}/extend', method='put', data=data)
            if 'error' in result:
                print(f"Error: {result['error']}")
            else:
                print(json.dumps(result, indent=2))
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def do_get_rental_graph(self, arg):
        "Obtain rental graph information. Usage: get_rental_graph <rental_ids>"
        try:
            result = api_request(f'/rental/{arg}/graph')
            if 'error' in result:
                print(f"Error: {result['error']}")
            else:
                print(json.dumps(result, indent=2))
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def do_get_rental_log(self, arg):
        "Obtain 'Activity Log' detail messages on rentals. Usage: get_rental_log <rental_ids>"
        try:
            result = api_request(f'/rental/{arg}/log')
            if 'error' in result:
                print(f"Error: {result['error']}")
            else:
                print(json.dumps(result, indent=2))
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def do_get_rental_messages(self, arg):
        "Obtain messages on one or more of your rentals. Usage: get_rental_messages <rental_ids>"
        try:
            result = api_request(f'/rental/{arg}/message')
            if 'error' in result:
                print(f"Error: {result['error']}")
            else:
                print(json.dumps(result, indent=2))
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def do_send_message_to_rental(self, args):
        "Send a message to one or more of your rentals. Usage: send_message_to_rental <rental_ids> <message>"
        rental_ids, message = args.split(' ', 1)
        try:
            data = {'message': message}
            result = api_request(f'/rental/{rental_ids}/message', method='put', data=data)
            if 'error' in result:
                print(f"Error: {result['error']}")
            else:
                print(json.dumps(result, indent=2))
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def do_exit(self, arg):
        "Exit the application"
        print("Goodbye!")
        return True

if __name__ == '__main__':
    MRRCLI().cmdloop()
