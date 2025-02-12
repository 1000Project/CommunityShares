# **Updated Community-Driven Scoring Model**

This document outlines the latest **scoring model** for the **1000 Project**, incorporating community feedback and revised metrics from the **Community-Driven Scoring Model** proposal. The model is designed to encourage responsible holding behavior, discourage manipulation, and optimize rewards distribution.

---

## **Scoring Criteria and Weight Distribution**

| **Criteria**              | **Weight (%)** | **Max Score (out of 1000)** |
| ------------------------- | -------------- | --------------------------- |
| **Holding Duration**      | **40%**        | **400 pts**                 |
| **Balance Stability**     | **10%**        | **100 pts**                 |
| **Cooldown Compliance**   | **15%**        | **150 pts**                 |
| **Transaction Behavior**  | **15%**        | **150 pts**                 |
| **P2P Transfer Patterns** | **10%**        | **100 pts**                 |
| **Accumulation History**  | **10%**        | **100 pts**                 |

**Total Possible Score:** 1000 Points

---

## **Weighted Criteria Breakdown**

### **1. Holding Duration (40% - 400 pts)**

Encourages long-term holding behavior by rewarding wallets based on the duration they have continuously held tokens.

| **Holding Period** | **Points Awarded** |
| ------------------ | ------------------ |
| 0 - 30 days        | 100 pts            |
| 31 - 90 days       | 250 pts            |
| 91+ days           | 400 pts            |

### **2. Balance Stability (10% - 100 pts)**

Rewards wallets that maintain a steady balance and do not engage in excessive selling.

| **Balance Stability**          | **Points Awarded** |
| ------------------------------ | ------------------ |
| No change (30+ days)           | 100 pts            |
| Small fluctuations (<10%)      | 75 pts             |
| Moderate fluctuations (10-20%) | 50 pts             |
| Large drops (>20%)             | 0 pts              |

### **3. Cooldown Compliance (15% - 150 pts)**

Encourages adherence to cooldown rules by penalizing wallets that breach them.

| **Cooldown Breaches** | **Points Awarded** |
| --------------------- | ------------------ |
| No breaches           | 150 pts            |
| 1 breach              | 75 pts             |
| 2+ breaches           | 0 pts              |

### **4. Transaction Behavior (15% - 150 pts)**

Rewards holders who engage in minimal trading and avoid frequent sell/buy behavior.

| **Transaction Frequency**  | **Points Awarded** |
| -------------------------- | ------------------ |
| No transactions (30+ days) | 150 pts            |
| Low transaction frequency  | 100 pts            |
| Medium frequency           | 50 pts             |
| High frequency             | 0 pts              |

### **5. P2P Transfer Patterns (10% - 100 pts)**

Penalizes wallets engaging in frequent peer-to-peer transfers indicative of bot-like behavior.

| **P2P Transfer Activity**   | **Points Awarded** |
| --------------------------- | ------------------ |
| No suspicious activity      | 100 pts            |
| Rare activity               | 50 pts             |
| Frequent bot-like transfers | 0 pts              |

### **6. Accumulation History (10% - 100 pts)**

Rewards wallets that accumulate tokens through multiple purchases instead of a single large buy.

| **Number of Purchases** | **Points Awarded** |
| ----------------------- | ------------------ |
| 10+ purchases           | 100 pts            |
| 5 - 9 purchases         | 75 pts             |
| 2 - 4 purchases         | 50 pts             |
| 0 - 1 purchases         | 0 pts              |

---

## **Changes from Previous Model**

- **Increased Weight for Holding Duration (30% → 40%)** to further incentivize long-term commitment.
- **Adjusted Balance Stability Weight (15% → 10%)** to better reflect impact.
- **Balanced Reward Distribution** by fine-tuning score caps per category.
- **Refined P2P Transfer Detection** to **penalize bot-like behavior** but avoid punishing normal user transactions.
- **More Gradual Scaling of Scores** to make each tier more impactful.

---

## **Implementation Notes**

- **Holders with a score above a set threshold** will qualify for rewards.
- The **score resets periodically** to prevent manipulation.
- The **contract implementation ensures fairness** by preventing score inflation.
- **Wallets engaging in bot-like activity** will receive penalties or disqualification.

---

## **Next Steps**

- **Deploy new scoring logic on testnet** and collect data on performance.
- **Community feedback round** after initial deployment.
- **Integrate scoring results into reward distribution contracts.**
- **Optimize calculations for on-chain efficiency.**

