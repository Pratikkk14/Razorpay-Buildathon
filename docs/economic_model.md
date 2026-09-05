# Economic Allocation Model

## Mathematical Formulation

### 1. Incremental Lift
For any candidate intervention action $a \in \{\text{RETRY}, \text{PAYMENT\_LINK}, \text{REMINDER}, \text{ALTERNATE\_METHOD}, \text{HUMAN\_ESCALATION}\}$:

$$\Delta P(a) = P(\text{recovery} \mid a) - P(\text{recovery} \mid \text{no action})$$

Where $P(\text{recovery} \mid \text{no action})$ represents the customer's natural recovery probability without any merchant intervention.

---

### 2. Expected Incremental Revenue
Given a payment amount $V$ in INR:

$$\text{EIR}(a) = \Delta P(a) \times V$$

---

### 3. Comprehensive Cost Structure
Every intervention incurs three distinct costs:

$$\text{Cost}_{\text{total}}(a) = C_{\text{action}}(a) + C_{\text{incentive}}(a) + C_{\text{friction}}(a)$$

- $C_{\text{action}}(a)$: Direct infrastructure/channel dispatch fees (e.g. ₹2.00 per SMS/WhatsApp link, ₹0.50 per retry attempt, ₹150.00 for support agent labor).
- $C_{\text{incentive}}(a)$: Any customer discount, fee waiver, or cash incentive offered.
- $C_{\text{friction}}(a)$: Estimated cost of customer annoyance, app notification fatigue, and brand reputation wear.

---

### 4. Expected Net Incremental Contribution (Objective Target)

$$\text{ENIC}(a) = \text{EIR}(a) - \text{Cost}_{\text{total}}(a)$$

$$\text{ENIC}(a) = \left[ (P(\text{recovery} \mid a) - P(\text{recovery} \mid \text{no action})) \times V \right] - \text{Cost}_{\text{total}}(a)$$

---

### 5. Policy Decision Selection

$$\text{Action}^* = \arg\max_{a \in \mathcal{A}_{\text{valid}}} \text{ENIC}(a)$$

$$\text{Decision} = \begin{cases} 
\text{ACT}(a^*) & \text{if } \text{ENIC}(a^*) > 0 \text{ and } \mathcal{P}_{\text{valid}}(a^*) = \text{True} \\
\text{WAIT} & \text{if Quiet Hours or Cooldown applies to optimum } a^* \\
\text{DONT\_ACT} & \text{if } \max_{a} \text{ENIC}(a) \le 0 \\
\text{ESCALATE} & \text{if } V \ge \text{Threshold}_{\text{VIP}} \text{ or manual review triggered}
\end{cases}$$
