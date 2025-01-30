def score_wallets(wallets):
    """
    Assign scores to wallets based on holding duration and balance stability.
    """
    scored_wallets = {}
    for wallet, info in wallets.items():
        score = 0

        # Example Scoring Logic
        holding_duration = info.get("holding_duration", 0)  # Days
        if holding_duration >= 91:
            score += 30
        elif holding_duration >= 31:
            score += 20
        else:
            score += 10

        balance_stability = info.get("balance_stability", 0)  # Percentage
        if balance_stability >= 90:
            score += 20
        elif balance_stability >= 80:
            score += 10

        scored_wallets[wallet] = {"info": info, "score": score}
    return scored_wallets


# Example usage
if __name__ == "__main__":
    eligible_wallets = {
        "wallet1": {"holding_duration": 100, "balance_stability": 95},
        "wallet2": {"holding_duration": 50, "balance_stability": 85},
    }
    scored_wallets = score_wallets(eligible_wallets)
    print(f"Scored wallets: {scored_wallets}")
