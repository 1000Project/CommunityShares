# **Weighted Scoring Model for the 1000 Project**

## **Overview**
The **Weighted Scoring Model** is designed to evaluate token holder behavior and optimize reward distribution in the **1000 Project** ecosystem. By assigning weight to different metrics, the system ensures fairness, discourages gaming, and promotes long-term participation.

---

## **Weighted Criteria Breakdown**
The weighted scoring model assigns a total of **100 points** across various factors that reflect a holder’s contribution to the ecosystem.

| **Criteria**            | **Weight (%)** | **Metric Description** | **Scoring Breakdown** |
|-------------------------|---------------|------------------------|------------------------|
| **Holding Duration**    | 30%           | Number of days wallet has continuously held tokens. | 0-30 days: **10 pts**<br>31-90 days: **20 pts**<br>91+ days: **30 pts** |
| **Balance Stability**   | 15%           | Consistency of wallet balance over time (low volatility). | No change (30+ days): **15 pts**<br>Small fluctuations (<10% change): **10 pts**<br>Moderate fluctuations (10-20%): **5 pts**<br>Large drops (>20%): **0 pts** |
| **Cooldown Compliance** | 15%           | Whether the wallet has violated cooldown rules. | No cooldown breaches: **15 pts**<br>1 cooldown breach: **5 pts**<br>2+ breaches: **0 pts** |
| **Transaction Behavior**| 15%           | Frequency and nature of transactions (high stability = higher score). | No transactions in 30+ days: **15 pts**<br>Low transaction frequency: **10 pts**<br>Medium frequency (occasional buys/sells): **5 pts**<br>High frequency (frequent trades): **0 pts** |
| **P2P Transfer Patterns** | 10%        | Whether the wallet exhibits bot-like P2P transfers. | No suspicious activity: **10 pts**<br>Rare activity: **5 pts**<br>Frequent bot-like transfers: **0 pts** |
| **Accumulation History** | 15%         | Number of separate token purchases (encouraging organic buyers). | 10+ purchases: **15 pts**<br>5-9 purchases: **10 pts**<br>2-4 purchases: **5 pts**<br>0-1 purchases: **0 pts** |

---

## **Why These Adjustments?**
✔ **Lowered Balance Stability Weight (20% → 15%)**  
- Prevents redundancy with Holding Duration.  
- Avoids unfairly rewarding long-term holders twice.  

✔ **Added ‘Transaction Behavior’ as a Unique Factor (15%)**  
- Prevents day traders from scoring high.  
- Helps reward wallets with stable trading patterns.  

✔ **Added ‘Accumulation History’ (15%)**  
- Encourages investors who buy in multiple transactions rather than one lump sum.  
- Reduces gaming attempts from large initial purchases with no further engagement.  

✔ **Maintained Cooldown Compliance at 15%**  
- Penalizes those who violate selling restrictions.  
- Discourages quick sell-offs after rewards.  

✔ **P2P Transfer Patterns (10%)**  
- Helps detect bot activity without penalizing genuine users.  
- Keeps the system resistant to Sybil attacks.  

---

## **How This Model Works**
1. **Each wallet is scored daily** based on the six criteria.
2. **Scores determine eligibility for rewards.** Higher scores improve chances of selection.
3. **Chainlink VRF handles random selection**, ensuring fairness.
4. **Scores reset periodically**, allowing new entrants to compete fairly.

---

## **Community Feedback & Next Steps**
The **1000 Project** is a community-driven initiative. We encourage all participants to **review the scoring model** and provide feedback to refine our approach. 

👉 **Review the scoring model:** [GitHub Link](https://github.com/1000Project/CommunityShares)  
👉 **Participate in the poll on Telegram:** [Telegram Poll Link](https://t.me/The1000Project)

Your input will help shape the future of **1000**! 🚀
