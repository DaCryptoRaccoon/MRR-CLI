# MRR-CLI

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
⢸⣿⣿⠃⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣦⣄⠀⠀⠀⠀⣿⠿⣯⡙⢻⡏⠀⠀⠀⠀⠀⠀  ⠈⣿⣿⡇
⣾⣿⣿⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀In Bitcoin We⠀⠀⠀⠙⢿⣿⣿⣶⣶⣤⣿⣦⣼⣿⡄⠀⠀⠀⠀⠀⠀    ⣿⣿⣿
⣿⣿⡏⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀Trust⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠙⠛⠛⠛⠁⢸⣿⡀⠀⠀⠀⠀⠀⠀  ⢸⣿⣿
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
MiningRigRentals API Client

The MiningRigRentals API Client is a command-line interface (CLI) tool designed to interact with the MiningRigRentals platform, enabling users to manage their mining rentals directly through terminal commands. This tool offers a variety of functionalities from querying the platform for information about algorithms, servers, and pricing to managing accounts and rentals.

Features
Authentication Management: Securely connect to the MiningRigRentals API with your credentials.
Query Servers and Algorithms: Fetch data about supported servers and algorithms.
Account Management: View and manage account details including balances and transaction history.
Rental Management: Create, update, and manage mining rentals.
Dynamic Interaction: A command-line driven approach to interact with the API using straightforward commands.

Installation
Before you start using the MiningRigRentals API client, you need to set it up on your local machine:

API_BASE_URL="https://www.miningrigrentals.com/api/v2"
API_KEY="your_api_key_here"
API_SECRET="your_api_secret_here"

Run the CLI:

python mrr_cli.py
Usage
The client operates in an interactive command-line environment. Start the CLI, and you will be able to type commands directly.

Commands
whoami:

Test connectivity and return information about you.
Usage: whoami
get_servers:

Get a list of MRR rig servers.
Usage: get_servers
get_algos:

Get all algorithms and statistics for them.
Usage: get_algos
get_algo:

Get statistics for a specific algorithm by name.
Usage: get_algo <algo_name>
get_currencies:

Get a list of supported currencies.
Usage: get_currencies
get_account:

Retrieve detailed account information.
Usage: get_account
get_account_balance:

Retrieve account balances.
Usage: get_account_balance
get_account_transactions:

List or search transaction history.
Usage: get_account_transactions <optional_filters_in_JSON>
get_account_profile:

List all pool profiles, or filter by algorithm.
Usage: get_account_profile <optional_algo>
Extending Functionality
You can extend the client with more functionalities by adding new commands in the mrr_cli.py script following the patterns established in the existing command methods.

Contributing
Contributions are welcome! Please fork the repository and submit pull requests with any enhancements, bug fixes, or improvements. For major changes, please open an issue first to discuss what you would like to change.

License
This project is licensed under the MIT License - see the LICENSE file for details.
