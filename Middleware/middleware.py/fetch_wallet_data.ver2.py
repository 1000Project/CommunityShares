import json

def fetch_latest_wallet_data():
    """
    Fetch the latest wallet data from the blockchain.
    """
    # Replace with actual blockchain API call
    latest_data = {
        "wallet1": {"balance": 1000, "last_tx": "2025-01-26"},
        "wallet2": {"balance": 500, "last_tx": "2025-01-27"},
    }
    return latest_data


def load_database(database_path):
    """
    Load the existing wallet database.
    """
    try:
        with open(database_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_to_database(data, database_path):
    """
    Save updated data to the wallet database.
    """
    with open(database_path, "w") as f:
        json.dump(data, f, indent=4)


def detect_changes(new_data, existing_data):
    """
    Detect wallets with changes compared to the existing database.
    """
    changes = {}
    for wallet, info in new_data.items():
        if wallet not in existing_data or existing_data[wallet] != info:
            changes[wallet] = info
    return changes


def update_database(database_path):
    """
    Fetch incremental updates and save changes to the database.
    """
    latest_data = fetch_latest_wallet_data()
    existing_data = load_database(database_path)
    changes = detect_changes(latest_data, existing_data)
    save_to_database({**existing_data, **changes}, database_path)
    return len(changes)  # Return the number of updated wallets


# Example usage
if __name__ == "__main__":
    database_path = "middleware/wallet_database.json"
    changes_count = update_database(database_path)
    print(f"Updated {changes_count} wallets in the database.")
