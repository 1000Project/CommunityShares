import json

def load_wallet_data(database_path):
    """
    Load wallet data from the database.
    """
    with open(database_path, "r") as f:
        return json.load(f)


def filter_eligible_wallets(wallets, min_balance=1000):
    """
    Filter wallets based on eligibility criteria.
    """
    eligible_wallets = {}
    for wallet, info in wallets.items():
        if info["balance"] >= min_balance:  # Minimum balance check
            eligible_wallets[wallet] = info
    return eligible_wallets


# Example usage
if __name__ == "__main__":
    database_path = "middleware/wallet_database.json"
    wallets = load_wallet_data(database_path)
    eligible_wallets = filter_eligible_wallets(wallets)
    print(f"Eligible wallets: {list(eligible_wallets.keys())}")
