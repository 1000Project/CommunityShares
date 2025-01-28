README for the 1000 Project Middleware

Overview

The middleware for the 1000 Project is a modular system designed to streamline off-chain computations, optimize cost efficiency, and support the reward and burn logic. This document outlines the updated workflow, individual script functionalities, and setup instructions.

Updated Workflow

Data Collection (Off-Chain)

Script: fetch_wallet_data.py

Fetch incremental wallet data updates from the blockchain.

Store changes in the middleware database for further processing.

Filter Eligible Wallets (Off-Chain)

Script: filter_eligible_wallets.py

Exclude wallets that:

Hold less than the minimum required balance.

Are flagged for cooldown periods or suspected behavior.

Are contract or blacklisted wallets.

Score Eligible Wallets (Off-Chain)

Script: score_wallets.py

Assign weighted scores based on criteria:

Holding duration.

Balance stability.

Other dynamic metrics.

Store wallet scores in the middleware database.

Select Wallets Using Chainlink VRF (On-Chain)

Script: call_chainlink_vrf.py

Randomly select 10% of eligible wallets (max 1,000).

Use Chainlink VRF for randomness verification.

Execute Daily Operations (On-Chain)

Script: export_selected_wallets.py

On Reward Days:

Distribute 1% of the reward wallet to selected wallets.

Log transactions for transparency.

On Burn Days:

Execute token burns (1% of the reward wallet).

Post-Execution Updates (Off-Chain)

Update middleware database to reflect new balances and cooldown flags.

Notify holders via Telegram/Discord bots of rewards, cooldowns, or updates.

Script Descriptions

fetch_wallet_data.py

Purpose: Fetch wallet data from the blockchain with incremental updates.

Key Features: Reduces overhead by only updating modified or new wallet data.

filter_eligible_wallets.py

Purpose: Apply eligibility filters to wallet data.

Filters: Minimum balance, cooldown flags, blacklist exclusion.

score_wallets.py

Purpose: Assign scores to eligible wallets based on weighted criteria.

Scoring Logic: Holding duration, balance stability, dynamic metrics.

call_chainlink_vrf.py

Purpose: Use Chainlink VRF to randomly select wallets.

Output: List of randomly selected wallets.

export_selected_wallets.py

Purpose: Distribute rewards or execute burns based on daily operations.

Includes: Logging transactions on-chain.

setupanddependencies.py

Purpose: Install required Python libraries and set up dependencies.

mainfunction.py

Purpose: Orchestrates all middleware scripts for seamless workflow execution.

Setup Instructions

Clone the Repository:

git clone <repository-url>
cd <repository-folder>

Install Dependencies:
Run the setupanddependencies.py script to install required Python libraries.

python3 setupanddependencies.py

Run the Middleware:
Execute the main function to trigger the workflow.

python3 mainfunction.py

Configure Settings:

Update blockchain URLs, APIs, and wallet data settings in the respective scripts.

Modify scoring weights and filters in score_wallets.py and filter_eligible_wallets.py as needed.

Changelog

Latest Updates

Incremental Data Updates:

Optimized fetch_wallet_data.py for change-detection logic.

Streamlined Filtering:

Combined multiple checks into filter_eligible_wallets.py.

Weighted Scoring Mechanism:

Added score_wallets.py for scoring eligible wallets.

Cost Optimization:

Prioritized off-chain computations to reduce on-chain gas costs.

Next Steps

Testing: Validate individual script functionality and full workflow integration.

Documentation: Keep this README updated with further changes.

Feedback: Collaborate with the dev team to refine scripts and processes.

