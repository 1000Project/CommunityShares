from fetch_wallet_data import update_database
from filter_eligible_wallets import filter_eligible_wallets
from score_wallets import score_wallets

def process_wallets():
    """
    Unified middleware function for processing wallets.
    """
    # Step 1: Update database with incremental changes
    database_path = "middleware/wallet_database.json"
    update_database(database_path)

    # Step 2: Load updated wallet data
    with open(database_path, "r") as f:
        wallets = json.load(f)

    # Step 3: Filter eligible wallets
    eligible_wallets = filter_eligible_wallets(wallets)

    # Step 4: Score eligible wallets
    scored_wallets = score_wallets(eligible_wallets)

    return scored_wallets


# Example usage
if __name__ == "__main__":
    final_result = process_wallets()
    print(f"Final processed wallets: {final_result}")
