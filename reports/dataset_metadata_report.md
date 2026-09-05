# Dataset Metadata Report
_Generated: 2026-09-05T17:44:26_
_DATA_DIR: `/content/`_
_Files analyzed: 19_

> This report is READ-ONLY: no source dataset was modified. No merging, feature engineering, or ML schema decisions were made. Flags below are candidates for human review only.

## .config/.last_update_check.json

**ERROR reading file:** `ValueError: Mixing dicts with non-Series may lead to ambiguous ordering.`

- type: json | size: 134.00 B

## bandit_model_metrics.json

### 1. File Information
- type: json | size: 1.99 KB | rows: 5 | columns: 5

### 2-3. Column Schema & Unique Values

#### `model_type`  (`object`)
- unique: 1 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: CONSTANT, categorical-like (name)
- top 1 values:
  - `LinUCB`: 5 (100.0%) 

#### `best_alpha`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: CONSTANT
- all values (n=1): 5×5

#### `training_samples`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: CONSTANT
- all values (n=1): 38500×5

#### `validation_samples`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: CONSTANT
- all values (n=1): 8250×5

- **tuning_history** -- ERROR analyzing column: TypeError: unhashable type: 'dict'

### 4. Data Quality Flags
- **constant columns**: model_type, best_alpha, training_samples, validation_samples
- **near constant columns**: none
- **extremely high cardinality columns**: none
- **likely id columns**: none
- **likely timestamp columns**: none
- **likely categorical columns**: model_type
- **likely target outcome columns**: none
- **columns with possible post outcome info**: none

### 5. Relationships / Duplicates
- duplicate rows: not computed

### 9. Dataset-Specific Summary
**Potentially useful for:**
- behavioral information (behavior/score/history-like columns present)
**Potential limitations:**
- no obvious temporal information detected
- no obvious target/outcome column detected
- 4 constant column(s) present

## customer_recovery_and_behavioral_dataset.csv

### 1. File Information
- type: csv | size: 12.15 MB | rows: 20,000 | columns: 45

### 2-3. Column Schema & Unique Values

#### `case_id`  (`object`)
- unique: 20,000 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: extremely-high-cardinality, id-like (name)
- top 20 values:
  - `case_019984`: 1 (0.005%) 
  - `case_019983`: 1 (0.005%) 
  - `case_019982`: 1 (0.005%) 
  - `case_019981`: 1 (0.005%) 
  - `case_019980`: 1 (0.005%) 
  - `case_019979`: 1 (0.005%) 
  - `case_019978`: 1 (0.005%) 
  - `case_019977`: 1 (0.005%) 
  - `case_019976`: 1 (0.005%) 
  - `case_019975`: 1 (0.005%) 
  - `case_019974`: 1 (0.005%) 
  - `case_019973`: 1 (0.005%) 
  - `case_019972`: 1 (0.005%) 
  - `case_019971`: 1 (0.005%) 
  - `case_019970`: 1 (0.005%) 
  - `case_019969`: 1 (0.005%) 
  - `case_000032`: 1 (0.005%) 
  - `case_000031`: 1 (0.005%) 
  - `case_000030`: 1 (0.005%) 
  - `case_000029`: 1 (0.005%) 

#### `created_at`  (`object`)
- unique: 8,704 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: timestamp-like
- datetime range: 2026-08-27 19:31:53.775847+00:00 -> 2026-09-03 19:30:53.775847+00:00 | unique dates: 8

#### `customer_id`  (`object`)
- unique: 17,922 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: id-like (name)
- top 20 values:
  - `cust_45451`: 4 (0.02%) 
  - `cust_75669`: 4 (0.02%) 
  - `cust_39724`: 4 (0.02%) 
  - `cust_21201`: 4 (0.02%) 
  - `cust_22525`: 4 (0.02%) 
  - `cust_26404`: 3 (0.015%) 
  - `cust_89585`: 3 (0.015%) 
  - `cust_62037`: 3 (0.015%) 
  - `cust_87520`: 3 (0.015%) 
  - `cust_49772`: 3 (0.015%) 
  - `cust_36238`: 3 (0.015%) 
  - `cust_90691`: 3 (0.015%) 
  - `cust_77267`: 3 (0.015%) 
  - `cust_85369`: 3 (0.015%) 
  - `cust_17808`: 3 (0.015%) 
  - `cust_24094`: 3 (0.015%) 
  - `cust_74028`: 3 (0.015%) 
  - `cust_84635`: 3 (0.015%) 
  - `cust_47316`: 3 (0.015%) 
  - `cust_51914`: 3 (0.015%) 

#### `customer_name`  (`object`)
- unique: 15 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- top 15 values:
  - `Siddharth Jain`: 1381 (6.905%) 
  - `Rahul Gupta`: 1377 (6.885%) 
  - `Vikram Singh`: 1373 (6.865%) 
  - `Pooja Deshmukh`: 1368 (6.84%) 
  - `Aditya Nair`: 1356 (6.78%) 
  - `Meera Sen`: 1352 (6.76%) 
  - `Ananya Iyer`: 1346 (6.73%) 
  - `Amit Saxena`: 1336 (6.68%) 
  - `Rohan Mehta`: 1332 (6.66%) 
  - `Tanvi Joshi`: 1322 (6.61%) 
  - `Diya Patel`: 1312 (6.56%) 
  - `Karan Verma`: 1312 (6.56%) 
  - `Sneha Rao`: 1300 (6.5%) 
  - `Neha Kulkarni`: 1291 (6.455%) 
  - `Aarav Sharma`: 1242 (6.21%) 

#### `order_id`  (`object`)
- unique: 19,974 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: extremely-high-cardinality, id-like (name)
- top 20 values:
  - `order_3569789`: 2 (0.01%) 
  - `order_2920308`: 2 (0.01%) 
  - `order_6233968`: 2 (0.01%) 
  - `order_5952764`: 2 (0.01%) 
  - `order_7206978`: 2 (0.01%) 
  - `order_7754735`: 2 (0.01%) 
  - `order_2131522`: 2 (0.01%) 
  - `order_1437496`: 2 (0.01%) 
  - `order_2972763`: 2 (0.01%) 
  - `order_3533489`: 2 (0.01%) 
  - `order_1911901`: 2 (0.01%) 
  - `order_3864366`: 2 (0.01%) 
  - `order_7872579`: 2 (0.01%) 
  - `order_5660954`: 2 (0.01%) 
  - `order_3701840`: 2 (0.01%) 
  - `order_1584044`: 2 (0.01%) 
  - `order_1436293`: 2 (0.01%) 
  - `order_3779093`: 2 (0.01%) 
  - `order_1732398`: 2 (0.01%) 
  - `order_1721598`: 2 (0.01%) 

#### `domain`  (`object`)
- unique: 4 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- top 4 values:
  - `PAYMENT_FAILURE`: 15337 (76.685%) 
  - `CHECKOUT_ABANDONMENT`: 2701 (13.505%) 
  - `SUBSCRIPTION_FAILURE`: 1585 (7.925%) 
  - `B2B_RECEIVABLE`: 377 (1.885%) 

#### `amount_inr`  (`int64`)
- unique: 23 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=23): 99×958, 149×1041, 299×1006, 499×977, 799×1574, 999×1566, 1499×1587, 2499×1578, 3999×1587, 4999×1017, 6999×989, 8999×1004, 12499×1107, 15999×998, 19999×474, 24999×470, 28999×489, 35000×472, 49999×510, 65000×144, 85000×148, 99999×153, 125000×151

#### `payment_method`  (`object`)
- unique: 6 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: categorical-like (name)
- top 6 values:
  - `upi`: 9158 (45.79%) 
  - `card`: 5887 (29.435%) 
  - `netbanking`: 2379 (11.895%) 
  - `subscription`: 1585 (7.925%) 
  - `paylater`: 614 (3.07%) 
  - `b2b_invoice`: 377 (1.885%) 

#### `issuer_or_rail`  (`object`)
- unique: 7 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- top 7 values:
  - `hdfc`: 5562 (27.81%) 
  - `sbi`: 4831 (24.155%) 
  - `icici`: 4038 (20.19%) 
  - `axis`: 2351 (11.755%) 
  - `kotak`: 1542 (7.71%) 
  - `federal`: 843 (4.215%) 
  - `yesbank`: 833 (4.165%) 

#### `card_network`  (`object`)
- unique: 4 | missing: 14,113 (70.565%) | zeros: n/a | negative: n/a
- top 4 values:
  - `rupay`: 1515 (7.575%) 
  - `mastercard`: 1477 (7.385%) 
  - `visa`: 1466 (7.33%) 
  - `amex`: 1429 (7.145%) 

#### `failure_source`  (`object`)
- unique: 5 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: target-like (name)
- top 5 values:
  - `CUSTOMER`: 6630 (33.15%) 
  - `INSTRUMENT`: 5075 (25.375%) 
  - `ISSUER`: 3323 (16.615%) 
  - `GATEWAY`: 3278 (16.39%) 
  - `BUSINESS`: 1694 (8.47%) 

#### `failure_step`  (`object`)
- unique: 4 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: target-like (name)
- top 4 values:
  - `AUTHORIZATION`: 8344 (41.72%) 
  - `INITIATION`: 6653 (33.265%) 
  - `AUTHENTICATION`: 3360 (16.8%) 
  - `CAPTURE`: 1643 (8.215%) 

#### `failure_code`  (`object`)
- unique: 12 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: target-like (name), categorical-like (name)
- top 12 values:
  - `card_expired`: 1744 (8.72%) 
  - `insufficient_funds`: 1697 (8.485%) 
  - `risk_check_failed`: 1694 (8.47%) 
  - `mandate_revoked`: 1689 (8.445%) 
  - `otp_timeout`: 1686 (8.43%) 
  - `issuer_technical_error`: 1683 (8.415%) 
  - `incorrect_upi_pin`: 1674 (8.37%) 
  - `capture_timeout`: 1643 (8.215%) 
  - `invalid_vpa`: 1642 (8.21%) 
  - `bank_downtime`: 1640 (8.2%) 
  - `gateway_timeout`: 1635 (8.175%) 
  - `payment_cancelled`: 1573 (7.865%) 

#### `failure_reason`  (`object`)
- unique: 12 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: target-like (name)
- top 12 values:
  - `Card expiry date has elapsed`: 1744 (8.72%) 
  - `Insufficient funds or credit limit exceeded`: 1697 (8.485%) 
  - `Transaction blocked due to elevated fraud risk score`: 1694 (8.47%) 
  - `Customer revoked e-mandate standing instruction`: 1689 (8.445%) 
  - `OTP timeout or user dropped 3D Secure session`: 1686 (8.43%) 
  - `Bank servers timed out during authorization`: 1683 (8.415%) 
  - `Incorrect UPI PIN entered by user`: 1674 (8.37%) 
  - `Auto-capture failed after authorization hold`: 1643 (8.215%) 
  - `Invalid or unregistered UPI Virtual Payment Address`: 1642 (8.21%) 
  - `Issuer core banking system scheduled downtime`: 1640 (8.2%) 
  - `Acquiring gateway timed out waiting for switch response`: 1635 (8.175%) 
  - `Customer manually cancelled transaction in payment app`: 1573 (7.865%) 

#### `is_recoverable`  (`bool`)
- unique: 2 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- top 2 values:
  - `True`: 16617 (83.085%) 
  - `False`: 3383 (16.915%) 

#### `is_rail_degraded`  (`bool`)
- unique: 2 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- top 2 values:
  - `False`: 18549 (92.745%) 
  - `True`: 1451 (7.255%) 

#### `previous_purchase_count`  (`int64`)
- unique: 16 | missing: 0 (0.0%) | zeros: 1,251 | negative: 0
- all values (n=16): 0×1251, 1×1219, 2×1270, 3×1257, 4×1262, 5×1312, 6×1231, 7×1241, 8×1276, 9×1203, 10×1272, 11×1223, 12×1299, 13×1225, 14×1267, 15×1192

#### `previous_payment_success_rate`  (`float64`)
- unique: 5 | missing: 0 (0.0%) | zeros: 3,977 | negative: 0
- flags: target-like (name)
- all values (n=5): 0.0×3977, 0.6×4018, 0.85×3966, 0.95×4016, 1.0×4023

#### `customer_ltv_inr`  (`float64`)
- unique: 18,714 | missing: 0 (0.0%) | zeros: 1,251 | negative: 0
- min=0 max=67,452.9 mean=19,678.3383 median=16,141.325 std=15,223.3179
- quantiles: p1=0 p5=0 p25=7,564.525 p50=16,141.325 p75=29,344.315 p95=49,545.73 p99=60,504.1608

#### `checkout_funnel_progress`  (`float64`)
- unique: 5 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=5): 0.4×3986, 0.6×3993, 0.8×3989, 0.95×4037, 1.0×3995

#### `customer_session_active`  (`bool`)
- unique: 2 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- top 2 values:
  - `True`: 13019 (65.095%) 
  - `False`: 6981 (34.905%) 

#### `time_since_failure_minutes`  (`float64`)
- unique: 596 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: timestamp-like, target-like (name)
- min=0.5 max=60 mean=30.0949 median=30.3 std=17.1333
- quantiles: p1=1.1 p5=3.3 p25=15.1 p50=30.3 p75=44.7 p95=57 p99=59.4

#### `contact_count_24h`  (`int64`)
- unique: 3 | missing: 0 (0.0%) | zeros: 11,934 | negative: 0
- all values (n=3): 0×11934, 1×4022, 2×4044

#### `opted_out_dnd`  (`bool`)
- unique: 2 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- top 2 values:
  - `False`: 19484 (97.42%) 
  - `True`: 516 (2.58%) 

#### `customer_psychology_archetype`  (`object`)
- unique: 6 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: categorical-like (name)
- top 6 values:
  - `Loyal Repeat Buyer`: 12163 (60.815%) 
  - `Window Shopper Abandoner`: 3613 (18.065%) 
  - `Friction-Averse 1-Tap Speed`: 1985 (9.925%) 
  - `Anxious & Security Conscious`: 1207 (6.035%) 
  - `Chronic Deal Hunter`: 698 (3.49%) 
  - `First-Time Skeptical`: 334 (1.67%) 

#### `frequently_abandons_checkout`  (`bool`)
- unique: 2 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- top 2 values:
  - `False`: 18208 (91.04%) 
  - `True`: 1792 (8.96%) 

#### `historical_checkout_abandonment_count`  (`int64`)
- unique: 7 | missing: 0 (0.0%) | zeros: 12,962 | negative: 0
- all values (n=7): 0×12962, 1×4516, 2×1276, 3×679, 4×315, 5×114, 6×138

#### `checkout_abandonment_risk_score`  (`float64`)
- unique: 41 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=0.05 max=0.98 mean=0.2114 median=0.17 std=0.1637
- quantiles: p1=0.05 p5=0.05 p25=0.07 p50=0.17 p75=0.28 p95=0.538 p99=0.84

#### `primary_abandonment_trigger`  (`object`)
- unique: 7 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- top 7 values:
  - `bank_technical_glitch`: 5190 (25.95%) 
  - `window_shopping_comparison`: 4691 (23.455%) 
  - `instrument_input_error`: 3386 (16.93%) 
  - `session_distraction_and_timeout`: 2812 (14.06%) 
  - `unexpected_amount_or_liquidity`: 1697 (8.485%) 
  - `payment_friction_otp_timeout`: 1686 (8.43%) 
  - `price_shock_at_shipping_or_taxes`: 538 (2.69%) 

#### `dropoff_stage_affinity`  (`object`)
- unique: 7 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- top 7 values:
  - `bank_authorization_handshake`: 5190 (25.95%) 
  - `payment_selection`: 4691 (23.455%) 
  - `payment_method_input`: 3386 (16.93%) 
  - `gateway_redirection`: 2812 (14.06%) 
  - `authorization_processing`: 1697 (8.485%) 
  - `otp_authentication_gateway`: 1686 (8.43%) 
  - `cart_checkout_review`: 538 (2.69%) 

#### `hesitation_dwell_time_seconds`  (`int64`)
- unique: 202 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: timestamp-like
- min=5 max=210 mean=36.0297 median=19 std=39.2414
- quantiles: p1=6 p5=8 p25=13 p50=19 p75=44 p95=128 p99=188

#### `security_anxiety_index`  (`float64`)
- unique: 91 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=0.05 max=0.95 mean=0.2726 median=0.21 std=0.2009
- quantiles: p1=0.05 p5=0.07 p25=0.13 p50=0.21 p75=0.36 p95=0.75 p99=0.9

#### `price_sensitivity_index`  (`float64`)
- unique: 89 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=0.1 max=0.98 mean=0.385 median=0.3 std=0.2292
- quantiles: p1=0.1 p5=0.12 p25=0.2 p50=0.3 p75=0.59 p95=0.81 p99=0.91

#### `discount_responsiveness`  (`object`)
- unique: 3 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- top 3 values:
  - `Low`: 12163 (60.815%) 
  - `High`: 4311 (21.555%) 
  - `Moderate`: 3526 (17.63%) 

#### `brand_trust_score`  (`float64`)
- unique: 80 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=0.2 max=0.99 mean=0.7836 median=0.87 std=0.1893
- quantiles: p1=0.36 p5=0.44 p25=0.61 p50=0.87 p75=0.93 p95=0.98 p99=0.99

#### `device_category`  (`object`)
- unique: 4 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: categorical-like (name)
- top 4 values:
  - `Android App`: 10980 (54.9%) 
  - `iOS App`: 4936 (24.68%) 
  - `Mobile Chrome`: 3026 (15.13%) 
  - `Desktop Web`: 1058 (5.29%) 

#### `preferred_recovery_channel`  (`object`)
- unique: 4 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: target-like (name), categorical-like (name)
- top 4 values:
  - `WhatsApp`: 10052 (50.26%) 
  - `SMS`: 4973 (24.865%) 
  - `In-App Push`: 4010 (20.05%) 
  - `Email`: 965 (4.825%) 

#### `optimal_psychology_nudge`  (`object`)
- unique: 7 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- top 7 values:
  - `Frictionless Priority Alternate Payment Link`: 11864 (59.32%) 
  - `Standard Multi-Rail Payment Link with Push Reminder`: 3511 (17.555%) 
  - `Instant 1-Tap WhatsApp UPI Intent Deep-Link`: 1925 (9.625%) 
  - `Reassure No-Debit & Reserve Cart Items (Bilingual Hinglish Voice)`: 1175 (5.875%) 
  - `Bounded 5% Recovery Incentive & Stock Hold Countdown`: 684 (3.42%) 
  - `DO_NOT_CONTACT_DND_GUARD`: 516 (2.58%) 
  - `Display Razorpay Verified Trust Badge & 24h Order Reservation`: 325 (1.625%) 

#### `model_psychological_diagnosis`  (`object`)
- unique: 6 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- top 6 values:
  - `High trust VIP customer with habitual checkout behavior. Drops are almost purely technical; responds immediately to standard payment links without extra incentive.`: 12163 (60.815%) 
  - `Casual browser with low purchase urgency. Frequently initiates checkout to check final landed price; needs scarcity nudges or stock-hold reservation alerts.`: 3613 (18.065%) 
  - `Impatience-driven modern digital shopper. Expects zero latency; will abandon instantly if redirected through clumsy screens. Converts best via 1-tap WhatsApp UPI intent.`: 1985 (9.925%) 
  - `High fear of double-debit and OTP fraud. Prolonged screen hesitation. Requires explicit reassurance that account has not been debited and card details remain secure.`: 1207 (6.035%) 
  - `Comparison shopper seeking coupons and maximum value. High cart abandonment rate. Highly responsive to small bounded 5% recovery incentives or cashbacks.`: 698 (3.49%) 
  - `Unfamiliar with merchant checkout. Skeptical of payment gateway reliability; needs reserved-order comfort and clear Razorpay trust marks.`: 334 (1.67%) 

#### `ml_predicted_recovery_probability`  (`float64`)
- unique: 3,139 | missing: 0 (0.0%) | zeros: 7 | negative: 0
- flags: target-like (name)
- min=0 max=0.7427 mean=0.4433 median=0.564 std=0.2327
- quantiles: p1=0.0102 p5=0.0501 p25=0.1105 p50=0.564 p75=0.5976 p95=0.6441 p99=0.6775

#### `algorithmic_intent_score`  (`float64`)
- unique: 13 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=13): 35.0×39, 45.0×193, 50.0×501, 55.0×337, 60.0×1644, 65.0×798, 70.0×1605, 75.0×2065, 80.0×1521, 85.0×2259, 90.0×4617, 95.0×628, 100.0×3793

#### `recommended_recovery_action`  (`object`)
- unique: 3 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: target-like (name)
- top 3 values:
  - `STANDARD_PAYMENT_LINK`: 8426 (42.13%) 
  - `CUSTOMER_RETRY`: 7763 (38.815%) 
  - `STOP`: 3811 (19.055%) 

#### `expected_recovery_value_inr`  (`float64`)
- unique: 553 | missing: 0 (0.0%) | zeros: 3,811 | negative: 0
- flags: target-like (name)
- min=0 max=106,248 mean=5,201.289 median=889.9 std=11,259.9139
- quantiles: p1=0 p5=0 p25=93.49 p50=889.9 p75=4,985.29 p95=23,623.5 p99=63,748.5

#### `ground_truth_recovered_ai_policy`  (`bool`)
- unique: 2 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: target-like (name)
- top 2 values:
  - `False`: 11120 (55.6%) 
  - `True`: 8880 (44.4%) 

#### `ground_truth_recovered_static`  (`bool`)
- unique: 2 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: target-like (name)
- top 2 values:
  - `False`: 16661 (83.305%) 
  - `True`: 3339 (16.695%) 

### 4. Data Quality Flags
- **constant columns**: none
- **near constant columns**: none
- **extremely high cardinality columns**: case_id, order_id
- **likely id columns**: case_id, customer_id, order_id
- **likely timestamp columns**: created_at, time_since_failure_minutes, hesitation_dwell_time_seconds
- **likely categorical columns**: case_id, customer_id, customer_name, order_id, domain, payment_method, issuer_or_rail, card_network, failure_source, failure_step, failure_code, failure_reason, is_recoverable, is_rail_degraded, customer_session_active, opted_out_dnd, customer_psychology_archetype, frequently_abandons_checkout, primary_abandonment_trigger, dropoff_stage_affinity, discount_responsiveness, device_category, preferred_recovery_channel, optimal_psychology_nudge, model_psychological_diagnosis, recommended_recovery_action, ground_truth_recovered_ai_policy, ground_truth_recovered_static
- **likely target outcome columns**: failure_source, failure_step, failure_code, failure_reason, previous_payment_success_rate, time_since_failure_minutes, preferred_recovery_channel, ml_predicted_recovery_probability, recommended_recovery_action, expected_recovery_value_inr, ground_truth_recovered_ai_policy, ground_truth_recovered_static
- **columns with possible post outcome info**: none

### 5. Relationships / Duplicates
- duplicate rows: 0 (0.0%)
- candidate ID columns (unique counts):
  - `case_id`: 20,000 unique
  - `customer_id`: 17,922 unique
  - `order_id`: 19,974 unique
- inferred entity relationships:
  - `customer_id` -> 17,922 unique entities
  - `order_id` -> 19,974 unique entities
  - `case_id` -> 20,000 unique entities

### 8. Temporal Information
- `created_at`: 2026-08-27 19:31:53.775847+00:00 -> 2026-09-03 19:30:53.775847+00:00 | unique dates: 8 | missing: 0

### 9. Dataset-Specific Summary
**Potentially useful for:**
- customer/payment context (entity id columns present)
- behavioral information (behavior/score/history-like columns present)
- sequential/temporal information (timestamp-like columns present)
- outcome information (candidate target columns present)
**Potential limitations:**
- none obviously detected

## episodes.parquet

### 1. File Information
- type: parquet | size: 5.22 MB | rows: 199,757 | columns: 29

### 2-3. Column Schema & Unique Values

#### `behavior_prob`  (`float64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: CONSTANT
- all values (n=1): 1.0×199757

#### `failure_reason`  (`object`)
- unique: 6 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: target-like (name)
- top 6 values:
  - `temporary_bank_failure`: 87664 (43.885%) 
  - `insufficient_funds`: 56324 (28.196%) 
  - `invalid_payment_method`: 27484 (13.759%) 
  - `network_error`: 13882 (6.949%) 
  - `authentication_failed`: 7612 (3.811%) 
  - `card_expired`: 6791 (3.4%) 

#### `amount`  (`float64`)
- unique: 6 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=6): 999.0×34342, 2499.0×33606, 4999.0×34213, 9999.0×34488, 24999.0×34484, 59999.0×28624

#### `attempt_count`  (`int64`)
- unique: 3 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=3): 1×153370, 2×39858, 3×6529

#### `hours_since_first_failure`  (`float64`)
- unique: 77 | missing: 0 (0.0%) | zeros: 100,000 | negative: 0
- flags: target-like (name)
- min=0 max=168 mean=18.0598 median=0 std=28.6168
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=36 p95=84 p99=121

#### `interventions_count`  (`int64`)
- unique: 5 | missing: 0 (0.0%) | zeros: 105,268 | negative: 0
- all values (n=5): 0×105268, 1×52633, 2×23963, 3×14215, 4×3678

#### `consecutive_failures`  (`int64`)
- unique: 5 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: target-like (name)
- all values (n=5): 1×105268, 2×52633, 3×23963, 4×14215, 5×3678

#### `is_weekend`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 144,055 | negative: 0
- all values (n=2): 0×144055, 1×55702

#### `customer_ltv`  (`float64`)
- unique: 100,000 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=5,000.4411 max=149,997.801 mean=52,163.8913 median=46,829.2961 std=29,419.3458
- quantiles: p1=7,030.3378 p5=12,531.3029 p25=27,647.6363 p50=46,829.2961 p75=74,699.0382 p95=98,380.9632 p99=136,301.4424

#### `customer_failure_rate`  (`float64`)
- unique: 4 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: target-like (name)
- all values (n=4): 0.02×15866, 0.04×123024, 0.15×40435, 0.35×20432

#### `subscription_paid_count`  (`int64`)
- unique: 9 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=9): 1×22429, 2×22114, 3×21540, 4×22265, 5×22374, 6×22205, 7×22022, 8×22050, 9×22758

#### `customer_archetype`  (`object`)
- unique: 4 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: categorical-like (name)
- top 4 values:
  - `reliable`: 123024 (61.587%) 
  - `occasional`: 40435 (20.242%) 
  - `high_risk`: 20432 (10.228%) 
  - `reliable_dormant`: 15866 (7.943%) 

#### `opted_out`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 199,757 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×199757

#### `account_tenure_days`  (`int64`)
- unique: 2,168 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=30 max=2,199 mean=662.5621 median=598 std=415.6152
- quantiles: p1=65 p5=149 p25=336 p50=598 p75=911 p95=1,447 p99=2,048

#### `lifetime_success_rate`  (`float64`)
- unique: 116 | missing: 0 (0.0%) | zeros: 4,595 | negative: 0
- flags: timestamp-like, target-like (name)
- min=0 max=1 mean=0.8547 median=0.9474 std=0.2134
- quantiles: p1=0 p5=0.3333 p25=0.8462 p50=0.9474 p75=0.9677 p95=1 p99=1

#### `days_since_last_success`  (`int64`)
- unique: 145 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: target-like (name)
- min=5 max=149 mean=37.1284 median=31 std=27.1504
- quantiles: p1=5 p5=8 p25=19 p50=31 p75=44 p95=91 p99=137

#### `historical_ltv`  (`float64`)
- unique: 100,000 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=5,000.4411 max=149,997.801 mean=52,163.8913 median=46,829.2961 std=29,419.3458
- quantiles: p1=7,030.3378 p5=12,531.3029 p25=27,647.6363 p50=46,829.2961 p75=74,699.0382 p95=98,380.9632 p99=136,301.4424

#### `is_first_ever_failure`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 183,891 | negative: 0
- flags: target-like (name)
- all values (n=2): 0×183891, 1×15866

#### `action`  (`object`)
- unique: 7 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: target-like (name)
- top 7 values:
  - `ESCALATE_TO_HUMAN`: 44117 (22.085%) 
  - `RETRY`: 40378 (20.214%) 
  - `PAYMENT_LINK`: 39552 (19.8%) 
  - `REQUEST_ALTERNATE_METHOD`: 29280 (14.658%) 
  - `STOP_RECOVERY`: 16650 (8.335%) 
  - `WAIT`: 16479 (8.25%) 
  - `SEND_REMINDER`: 13301 (6.659%) 

#### `allowed_actions`  (`object`)
- unique: 3 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: target-like (name)
- top 3 values:
  - `ESCALATE_TO_HUMAN,PAYMENT_LINK,REQUEST_ALTERNATE_METHOD,RETRY,SEND_REMINDER,STOP_RECOVERY,WAIT`: 134539 (67.351%) 
  - `ESCALATE_TO_HUMAN,PAYMENT_LINK,REQUEST_ALTERNATE_METHOD,SEND_REMINDER,STOP_RECOVERY,WAIT`: 47325 (23.691%) 
  - `ESCALATE_TO_HUMAN,STOP_RECOVERY,WAIT`: 17893 (8.957%) 

#### `reward`  (`float64`)
- unique: 500 | missing: 0 (0.0%) | zeros: 107,475 | negative: 10,184
- min=-910 max=59,999 mean=7,120.676 median=0 std=15,825.1094
- quantiles: p1=-240 p5=-5 p25=0 p50=0 p75=4,914 p95=59,829 p99=59,964

#### `done`  (`bool`)
- unique: 2 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- top 2 values:
  - `True`: 100000 (50.061%) 
  - `False`: 99757 (49.939%) 

#### `resolved`  (`bool`)
- unique: 2 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- top 2 values:
  - `False`: 117659 (58.901%) 
  - `True`: 82098 (41.099%) 

#### `recovered_amount`  (`float64`)
- unique: 7 | missing: 0 (0.0%) | zeros: 117,659 | negative: 0
- flags: target-like (name)
- all values (n=7): 0.0×117659, 999.0×13628, 2499.0×13411, 4999.0×13577, 9999.0×13669, 24999.0×13916, 59999.0×13897

#### `episode_id`  (`object`)
- unique: 100,000 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: id-like (name)
- top 20 values:
  - `ep_0038169`: 7 (0.004%) 
  - `ep_0038172`: 7 (0.004%) 
  - `ep_0052081`: 7 (0.004%) 
  - `ep_0061863`: 7 (0.004%) 
  - `ep_0077347`: 7 (0.004%) 
  - `ep_0033308`: 7 (0.004%) 
  - `ep_0015649`: 7 (0.004%) 
  - `ep_0066193`: 7 (0.004%) 
  - `ep_0029971`: 7 (0.004%) 
  - `ep_0040107`: 7 (0.004%) 
  - `ep_0007322`: 7 (0.004%) 
  - `ep_0020710`: 7 (0.004%) 
  - `ep_0073383`: 7 (0.004%) 
  - `ep_0029880`: 7 (0.004%) 
  - `ep_0029874`: 7 (0.004%) 
  - `ep_0039200`: 7 (0.004%) 
  - `ep_0090754`: 7 (0.004%) 
  - `ep_0061737`: 7 (0.004%) 
  - `ep_0025628`: 7 (0.004%) 
  - `ep_0010256`: 7 (0.004%) 

#### `timestep`  (`int64`)
- unique: 7 | missing: 0 (0.0%) | zeros: 100,000 | negative: 0
- flags: timestamp-like
- all values (n=7): 0×100000, 1×52884, 2×25244, 3×14312, 4×5679, 5×1402, 6×236

#### `episode_length`  (`int64`)
- unique: 7 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=7): 1×47116, 2×55280, 3×32796, 4×34532, 5×21385, 6×6996, 7×1652

#### `episode_return`  (`float64`)
- unique: 500 | missing: 0 (0.0%) | zeros: 8,118 | negative: 34,282
- min=-910 max=59,999 mean=12,688.0233 median=4,674 std=18,846.7986
- quantiles: p1=-600 p5=-240 p25=789 p50=4,674 p75=24,394 p95=59,829 p99=59,964

#### `provenance`  (`object`)
- unique: 1 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: CONSTANT
- top 1 values:
  - `SYNTHETIC_TRAINING_DATA`: 199757 (100.0%) 

### 4. Data Quality Flags
- **constant columns**: behavior_prob, opted_out, provenance
- **near constant columns**: none
- **extremely high cardinality columns**: none
- **likely id columns**: episode_id
- **likely timestamp columns**: lifetime_success_rate, timestep
- **likely categorical columns**: failure_reason, customer_archetype, action, allowed_actions, done, resolved, episode_id, provenance
- **likely target outcome columns**: failure_reason, hours_since_first_failure, consecutive_failures, customer_failure_rate, lifetime_success_rate, days_since_last_success, is_first_ever_failure, action, allowed_actions, recovered_amount
- **columns with possible post outcome info**: none

### 5. Relationships / Duplicates
- duplicate rows: 0 (0.0%)
- candidate ID columns (unique counts):
  - `episode_id`: 100,000 unique

### 6. Target / Outcome Analysis
**`action`** (categorical)
- `ESCALATE_TO_HUMAN`: 44,117 (22.085%)
- `RETRY`: 40,378 (20.214%)
- `PAYMENT_LINK`: 39,552 (19.8%)
- `REQUEST_ALTERNATE_METHOD`: 29,280 (14.658%)
- `STOP_RECOVERY`: 16,650 (8.335%)
- `WAIT`: 16,479 (8.25%)
- `SEND_REMINDER`: 13,301 (6.659%)
**`recovered_amount`** (numeric)
- min=0 max=59,999 mean=7,175.5603 median=0 std=15,859.3433

### 7. Cross-tabulations
**action_vs_recovered_amount**
```json
[{"action": "ESCALATE_TO_HUMAN", "count": 44117, "mean": 13547.8358002584, "median": 2499.0, "std": 21306.2052894379}, {"action": "PAYMENT_LINK", "count": 39552, "mean": 9842.7335659385, "median": 999.0, "std": 17715.9135396447}, {"action": "REQUEST_ALTERNATE_METHOD", "count": 29280, "mean": 7710.8610314208, "median": 0.0, "std": 16262.4877239913}, {"action": "RETRY", "count": 40378, "mean": 2506.2639556194, "median": 0.0, "std": 6136.7830905748}, {"action": "SEND_REMINDER", "count": 13301, "mean": 2482.8218930907, "median": 0.0, "std": 9873.2843947203}, {"action": "STOP_RECOVERY", "count": 16650, "mean": 0.0, "median": 0.0, "std": 0.0}, {"action": "WAIT", "count": 16479, "mean": 5241.9916863887, "median": 0.0, "std": 13646.6545914078}]
```

### 9. Dataset-Specific Summary
**Potentially useful for:**
- behavioral information (behavior/score/history-like columns present)
- sequential/temporal information (timestamp-like columns present)
- treatment/action information
- outcome information (candidate target columns present)
**Potential limitations:**
- 3 constant column(s) present

## episodes_test.parquet

### 1. File Information
- type: parquet | size: 813.10 KB | rows: 30,061 | columns: 29

### 2-3. Column Schema & Unique Values

#### `behavior_prob`  (`float64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: CONSTANT
- all values (n=1): 1.0×30061

#### `failure_reason`  (`object`)
- unique: 6 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: target-like (name)
- top 6 values:
  - `temporary_bank_failure`: 13391 (44.546%) 
  - `insufficient_funds`: 8355 (27.793%) 
  - `invalid_payment_method`: 4113 (13.682%) 
  - `network_error`: 2090 (6.953%) 
  - `authentication_failed`: 1158 (3.852%) 
  - `card_expired`: 954 (3.174%) 

#### `amount`  (`float64`)
- unique: 6 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=6): 999.0×5120, 2499.0×5081, 4999.0×5186, 9999.0×5087, 24999.0×5253, 59999.0×4334

#### `attempt_count`  (`int64`)
- unique: 3 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=3): 1×22982, 2×6122, 3×957

#### `hours_since_first_failure`  (`float64`)
- unique: 75 | missing: 0 (0.0%) | zeros: 15,000 | negative: 0
- flags: target-like (name)
- min=0 max=168 mean=18.3164 median=1 std=29.0087
- quantiles: p1=0 p5=0 p25=0 p50=1 p75=36 p95=84 p99=121

#### `interventions_count`  (`int64`)
- unique: 5 | missing: 0 (0.0%) | zeros: 15,798 | negative: 0
- all values (n=5): 0×15798, 1×7923, 2×3594, 3×2159, 4×587

#### `consecutive_failures`  (`int64`)
- unique: 5 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: target-like (name)
- all values (n=5): 1×15798, 2×7923, 3×3594, 4×2159, 5×587

#### `is_weekend`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 21,866 | negative: 0
- all values (n=2): 0×21866, 1×8195

#### `customer_ltv`  (`float64`)
- unique: 15,000 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=5,000.4411 max=149,873.8379 mean=51,931.3781 median=46,493.5412 std=29,649.3365
- quantiles: p1=6,909.9851 p5=12,272.682 p25=27,204.3965 p50=46,493.5412 p75=73,949.8028 p95=98,392.9809 p99=138,722.6377

#### `customer_failure_rate`  (`float64`)
- unique: 4 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: target-like (name)
- all values (n=4): 0.02×2437, 0.04×18413, 0.15×6103, 0.35×3108

#### `subscription_paid_count`  (`int64`)
- unique: 9 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=9): 1×3326, 2×3319, 3×3228, 4×3290, 5×3427, 6×3355, 7×3399, 8×3186, 9×3531

#### `customer_archetype`  (`object`)
- unique: 4 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: categorical-like (name)
- top 4 values:
  - `reliable`: 18413 (61.252%) 
  - `occasional`: 6103 (20.302%) 
  - `high_risk`: 3108 (10.339%) 
  - `reliable_dormant`: 2437 (8.107%) 

#### `opted_out`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 30,061 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×30061

#### `account_tenure_days`  (`int64`)
- unique: 1,807 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=30 max=2,199 mean=662.0083 median=597 std=418.1554
- quantiles: p1=66 p5=146 p25=335 p50=597 p75=905 p95=1,462 p99=2,072

#### `lifetime_success_rate`  (`float64`)
- unique: 116 | missing: 0 (0.0%) | zeros: 741 | negative: 0
- flags: timestamp-like, target-like (name)
- min=0 max=1 mean=0.8541 median=0.9474 std=0.2149
- quantiles: p1=0 p5=0.3333 p25=0.8462 p50=0.9474 p75=0.9677 p95=1 p99=1

#### `days_since_last_success`  (`int64`)
- unique: 145 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: target-like (name)
- min=5 max=149 mean=37.2071 median=32 std=26.8167
- quantiles: p1=5 p5=8 p25=19 p50=32 p75=44 p95=89 p99=136

#### `historical_ltv`  (`float64`)
- unique: 15,000 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=5,000.4411 max=149,873.8379 mean=51,931.3781 median=46,493.5412 std=29,649.3365
- quantiles: p1=6,909.9851 p5=12,272.682 p25=27,204.3965 p50=46,493.5412 p75=73,949.8028 p95=98,392.9809 p99=138,722.6377

#### `is_first_ever_failure`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 27,624 | negative: 0
- flags: target-like (name)
- all values (n=2): 0×27624, 1×2437

#### `action`  (`object`)
- unique: 7 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: target-like (name)
- top 7 values:
  - `ESCALATE_TO_HUMAN`: 6770 (22.521%) 
  - `RETRY`: 6170 (20.525%) 
  - `PAYMENT_LINK`: 5790 (19.261%) 
  - `REQUEST_ALTERNATE_METHOD`: 4349 (14.467%) 
  - `STOP_RECOVERY`: 2486 (8.27%) 
  - `WAIT`: 2465 (8.2%) 
  - `SEND_REMINDER`: 2031 (6.756%) 

#### `allowed_actions`  (`object`)
- unique: 3 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: target-like (name)
- top 3 values:
  - `ESCALATE_TO_HUMAN,PAYMENT_LINK,REQUEST_ALTERNATE_METHOD,RETRY,SEND_REMINDER,STOP_RECOVERY,WAIT`: 20173 (67.107%) 
  - `ESCALATE_TO_HUMAN,PAYMENT_LINK,REQUEST_ALTERNATE_METHOD,SEND_REMINDER,STOP_RECOVERY,WAIT`: 7142 (23.758%) 
  - `ESCALATE_TO_HUMAN,STOP_RECOVERY,WAIT`: 2746 (9.135%) 

#### `reward`  (`float64`)
- unique: 443 | missing: 0 (0.0%) | zeros: 16,233 | negative: 1,515
- min=-910 max=59,999 mean=7,093.5696 median=0 std=15,773.19
- quantiles: p1=-245 p5=-5 p25=0 p50=0 p75=4,889 p95=59,829 p99=59,964

#### `done`  (`bool`)
- unique: 2 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- top 2 values:
  - `False`: 15061 (50.101%) 
  - `True`: 15000 (49.899%) 

#### `resolved`  (`bool`)
- unique: 2 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- top 2 values:
  - `False`: 17748 (59.04%) 
  - `True`: 12313 (40.96%) 

#### `recovered_amount`  (`float64`)
- unique: 7 | missing: 0 (0.0%) | zeros: 17,748 | negative: 0
- flags: target-like (name)
- all values (n=7): 0.0×17748, 999.0×2048, 2499.0×1999, 4999.0×2040, 9999.0×2026, 24999.0×2131, 59999.0×2069

#### `episode_id`  (`object`)
- unique: 15,000 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: id-like (name)
- top 20 values:
  - `ep_0069694`: 7 (0.023%) 
  - `ep_0008365`: 7 (0.023%) 
  - `ep_0084079`: 7 (0.023%) 
  - `ep_0002499`: 7 (0.023%) 
  - `ep_0039849`: 7 (0.023%) 
  - `ep_0081638`: 7 (0.023%) 
  - `ep_0034976`: 7 (0.023%) 
  - `ep_0068692`: 7 (0.023%) 
  - `ep_0007528`: 7 (0.023%) 
  - `ep_0012214`: 7 (0.023%) 
  - `ep_0093265`: 7 (0.023%) 
  - `ep_0027649`: 7 (0.023%) 
  - `ep_0066193`: 7 (0.023%) 
  - `ep_0040214`: 7 (0.023%) 
  - `ep_0091433`: 7 (0.023%) 
  - `ep_0049790`: 7 (0.023%) 
  - `ep_0075659`: 7 (0.023%) 
  - `ep_0092652`: 7 (0.023%) 
  - `ep_0061610`: 7 (0.023%) 
  - `ep_0006821`: 7 (0.023%) 

#### `timestep`  (`int64`)
- unique: 7 | missing: 0 (0.0%) | zeros: 15,000 | negative: 0
- flags: timestamp-like
- all values (n=7): 0×15000, 1×7955, 2×3802, 3×2168, 4×887, 5×212, 6×37

#### `episode_length`  (`int64`)
- unique: 7 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=7): 1×7045, 2×8306, 3×4902, 4×5124, 5×3375, 6×1050, 7×259

#### `episode_return`  (`float64`)
- unique: 443 | missing: 0 (0.0%) | zeros: 1,228 | negative: 5,065
- min=-910 max=59,999 mean=12,774.301 median=4,744 std=18,884.9652
- quantiles: p1=-600 p5=-245 p25=789 p50=4,744 p75=24,484 p95=59,829 p99=59,964

#### `provenance`  (`object`)
- unique: 1 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: CONSTANT
- top 1 values:
  - `HELD_OUT_OFFLINE_EVAL`: 30061 (100.0%) 

### 4. Data Quality Flags
- **constant columns**: behavior_prob, opted_out, provenance
- **near constant columns**: none
- **extremely high cardinality columns**: none
- **likely id columns**: episode_id
- **likely timestamp columns**: lifetime_success_rate, timestep
- **likely categorical columns**: failure_reason, customer_archetype, action, allowed_actions, done, resolved, episode_id, provenance
- **likely target outcome columns**: failure_reason, hours_since_first_failure, consecutive_failures, customer_failure_rate, lifetime_success_rate, days_since_last_success, is_first_ever_failure, action, allowed_actions, recovered_amount
- **columns with possible post outcome info**: none

### 5. Relationships / Duplicates
- duplicate rows: 0 (0.0%)
- candidate ID columns (unique counts):
  - `episode_id`: 15,000 unique

### 6. Target / Outcome Analysis
**`action`** (categorical)
- `ESCALATE_TO_HUMAN`: 6,770 (22.521%)
- `RETRY`: 6,170 (20.525%)
- `PAYMENT_LINK`: 5,790 (19.261%)
- `REQUEST_ALTERNATE_METHOD`: 4,349 (14.467%)
- `STOP_RECOVERY`: 2,486 (8.27%)
- `WAIT`: 2,465 (8.2%)
- `SEND_REMINDER`: 2,031 (6.756%)
**`recovered_amount`** (numeric)
- min=0 max=59,999 mean=7,149.0698 median=0 std=15,807.8041

### 7. Cross-tabulations
**action_vs_recovered_amount**
```json
[{"action": "ESCALATE_TO_HUMAN", "count": 6770, "mean": 13276.4895125554, "median": 2499.0, "std": 21127.5488494627}, {"action": "PAYMENT_LINK", "count": 5790, "mean": 9951.6701208981, "median": 999.0, "std": 17889.3287932882}, {"action": "REQUEST_ALTERNATE_METHOD", "count": 4349, "mean": 7468.6327891469, "median": 0.0, "std": 15934.7742410084}, {"action": "RETRY", "count": 6170, "mean": 2585.1252836305, "median": 0.0, "std": 6286.5307571791}, {"action": "SEND_REMINDER", "count": 2031, "mean": 2712.5411127523, "median": 0.0, "std": 10439.5604746371}, {"action": "STOP_RECOVERY", "count": 2486, "mean": 0.0, "median": 0.0, "std": 0.0}, {"action": "WAIT", "count": 2465, "mean": 5462.7606490872, "median": 0.0, "std": 13747.9838310622}]
```

### 9. Dataset-Specific Summary
**Potentially useful for:**
- behavioral information (behavior/score/history-like columns present)
- sequential/temporal information (timestamp-like columns present)
- treatment/action information
- outcome information (candidate target columns present)
**Potential limitations:**
- 3 constant column(s) present

## episodes_train.parquet

### 1. File Information
- type: parquet | size: 3.72 MB | rows: 139,910 | columns: 29

### 2-3. Column Schema & Unique Values

#### `behavior_prob`  (`float64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: CONSTANT
- all values (n=1): 1.0×139910

#### `failure_reason`  (`object`)
- unique: 6 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: target-like (name)
- top 6 values:
  - `temporary_bank_failure`: 61341 (43.843%) 
  - `insufficient_funds`: 39466 (28.208%) 
  - `invalid_payment_method`: 19180 (13.709%) 
  - `network_error`: 9750 (6.969%) 
  - `authentication_failed`: 5351 (3.825%) 
  - `card_expired`: 4822 (3.447%) 

#### `amount`  (`float64`)
- unique: 6 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=6): 999.0×24132, 2499.0×23442, 4999.0×23919, 9999.0×24289, 24999.0×24178, 59999.0×19950

#### `attempt_count`  (`int64`)
- unique: 3 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=3): 1×107398, 2×27867, 3×4645

#### `hours_since_first_failure`  (`float64`)
- unique: 77 | missing: 0 (0.0%) | zeros: 70,000 | negative: 0
- flags: target-like (name)
- min=0 max=168 mean=18.0165 median=0 std=28.5159
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=36 p95=80 p99=120

#### `interventions_count`  (`int64`)
- unique: 5 | missing: 0 (0.0%) | zeros: 73,679 | negative: 0
- all values (n=5): 0×73679, 1×36866, 2×16811, 3×9989, 4×2565

#### `consecutive_failures`  (`int64`)
- unique: 5 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: target-like (name)
- all values (n=5): 1×73679, 2×36866, 3×16811, 4×9989, 5×2565

#### `is_weekend`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 100,971 | negative: 0
- all values (n=2): 0×100971, 1×38939

#### `customer_ltv`  (`float64`)
- unique: 70,000 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=5,003.023 max=149,997.801 mean=52,221.9403 median=46,872.7126 std=29,416.2081
- quantiles: p1=7,128.7468 p5=12,530.2647 p25=27,691.5092 p50=46,872.7126 p75=74,848.1233 p95=98,441.5806 p99=135,900.3886

#### `customer_failure_rate`  (`float64`)
- unique: 4 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: target-like (name)
- all values (n=4): 0.02×11072, 0.04×86239, 0.15×28237, 0.35×14362

#### `subscription_paid_count`  (`int64`)
- unique: 9 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=9): 1×15898, 2×15511, 3×15045, 4×15626, 5×15562, 6×15521, 7×15294, 8×15545, 9×15908

#### `customer_archetype`  (`object`)
- unique: 4 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: categorical-like (name)
- top 4 values:
  - `reliable`: 86239 (61.639%) 
  - `occasional`: 28237 (20.182%) 
  - `high_risk`: 14362 (10.265%) 
  - `reliable_dormant`: 11072 (7.914%) 

#### `opted_out`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 139,910 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×139910

#### `account_tenure_days`  (`int64`)
- unique: 2,156 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=30 max=2,199 mean=662.5776 median=598 std=414.9496
- quantiles: p1=65 p5=148 p25=336 p50=598 p75=913 p95=1,443 p99=2,045.91

#### `lifetime_success_rate`  (`float64`)
- unique: 116 | missing: 0 (0.0%) | zeros: 3,232 | negative: 0
- flags: timestamp-like, target-like (name)
- min=0 max=1 mean=0.8544 median=0.9474 std=0.2141
- quantiles: p1=0 p5=0.3333 p25=0.8462 p50=0.9474 p75=0.9677 p95=1 p99=1

#### `days_since_last_success`  (`int64`)
- unique: 145 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: target-like (name)
- min=5 max=149 mean=37.111 median=31 std=27.2143
- quantiles: p1=5 p5=8 p25=19 p50=31 p75=43 p95=91 p99=137

#### `historical_ltv`  (`float64`)
- unique: 70,000 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=5,003.023 max=149,997.801 mean=52,221.9403 median=46,872.7126 std=29,416.2081
- quantiles: p1=7,128.7468 p5=12,530.2647 p25=27,691.5092 p50=46,872.7126 p75=74,848.1233 p95=98,441.5806 p99=135,900.3886

#### `is_first_ever_failure`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 128,838 | negative: 0
- flags: target-like (name)
- all values (n=2): 0×128838, 1×11072

#### `action`  (`object`)
- unique: 7 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: target-like (name)
- top 7 values:
  - `ESCALATE_TO_HUMAN`: 30848 (22.048%) 
  - `RETRY`: 28247 (20.189%) 
  - `PAYMENT_LINK`: 27772 (19.85%) 
  - `REQUEST_ALTERNATE_METHOD`: 20484 (14.641%) 
  - `STOP_RECOVERY`: 11603 (8.293%) 
  - `WAIT`: 11593 (8.286%) 
  - `SEND_REMINDER`: 9363 (6.692%) 

#### `allowed_actions`  (`object`)
- unique: 3 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: target-like (name)
- top 3 values:
  - `ESCALATE_TO_HUMAN,PAYMENT_LINK,REQUEST_ALTERNATE_METHOD,RETRY,SEND_REMINDER,STOP_RECOVERY,WAIT`: 94332 (67.423%) 
  - `ESCALATE_TO_HUMAN,PAYMENT_LINK,REQUEST_ALTERNATE_METHOD,SEND_REMINDER,STOP_RECOVERY,WAIT`: 33024 (23.604%) 
  - `ESCALATE_TO_HUMAN,STOP_RECOVERY,WAIT`: 12554 (8.973%) 

#### `reward`  (`float64`)
- unique: 493 | missing: 0 (0.0%) | zeros: 75,267 | negative: 7,110
- min=-910 max=59,999 mean=7,116.6807 median=0 std=15,816.5016
- quantiles: p1=-235 p5=-5 p25=0 p50=0 p75=4,919 p95=59,829 p99=59,964

#### `done`  (`bool`)
- unique: 2 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- top 2 values:
  - `True`: 70000 (50.032%) 
  - `False`: 69910 (49.968%) 

#### `resolved`  (`bool`)
- unique: 2 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- top 2 values:
  - `False`: 82377 (58.879%) 
  - `True`: 57533 (41.121%) 

#### `recovered_amount`  (`float64`)
- unique: 7 | missing: 0 (0.0%) | zeros: 82,377 | negative: 0
- flags: target-like (name)
- all values (n=7): 0.0×82377, 999.0×9575, 2499.0×9345, 4999.0×9528, 9999.0×9639, 24999.0×9723, 59999.0×9723

#### `episode_id`  (`object`)
- unique: 70,000 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: id-like (name)
- top 20 values:
  - `ep_0072294`: 7 (0.005%) 
  - `ep_0056951`: 7 (0.005%) 
  - `ep_0062435`: 7 (0.005%) 
  - `ep_0060114`: 7 (0.005%) 
  - `ep_0073383`: 7 (0.005%) 
  - `ep_0025628`: 7 (0.005%) 
  - `ep_0000279`: 7 (0.005%) 
  - `ep_0072312`: 7 (0.005%) 
  - `ep_0059480`: 7 (0.005%) 
  - `ep_0060092`: 7 (0.005%) 
  - `ep_0050987`: 7 (0.005%) 
  - `ep_0061863`: 7 (0.005%) 
  - `ep_0077596`: 7 (0.005%) 
  - `ep_0038705`: 7 (0.005%) 
  - `ep_0000449`: 7 (0.005%) 
  - `ep_0020410`: 7 (0.005%) 
  - `ep_0037227`: 7 (0.005%) 
  - `ep_0030402`: 7 (0.005%) 
  - `ep_0018710`: 7 (0.005%) 
  - `ep_0085510`: 7 (0.005%) 

#### `timestep`  (`int64`)
- unique: 7 | missing: 0 (0.0%) | zeros: 70,000 | negative: 0
- flags: timestamp-like
- all values (n=7): 0×70000, 1×37034, 2×17707, 3×10044, 4×3957, 5×994, 6×174

#### `episode_length`  (`int64`)
- unique: 7 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=7): 1×32966, 2×38654, 3×22989, 4×24348, 5×14815, 6×4920, 7×1218

#### `episode_return`  (`float64`)
- unique: 493 | missing: 0 (0.0%) | zeros: 5,645 | negative: 23,950
- min=-910 max=59,999 mean=12,695.9233 median=4,679 std=18,838.4223
- quantiles: p1=-595 p5=-240 p25=789 p50=4,679 p75=24,394 p95=59,829 p99=59,964

#### `provenance`  (`object`)
- unique: 1 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: CONSTANT
- top 1 values:
  - `SYNTHETIC_TRAINING_DATA`: 139910 (100.0%) 

### 4. Data Quality Flags
- **constant columns**: behavior_prob, opted_out, provenance
- **near constant columns**: none
- **extremely high cardinality columns**: none
- **likely id columns**: episode_id
- **likely timestamp columns**: lifetime_success_rate, timestep
- **likely categorical columns**: failure_reason, customer_archetype, action, allowed_actions, done, resolved, episode_id, provenance
- **likely target outcome columns**: failure_reason, hours_since_first_failure, consecutive_failures, customer_failure_rate, lifetime_success_rate, days_since_last_success, is_first_ever_failure, action, allowed_actions, recovered_amount
- **columns with possible post outcome info**: none

### 5. Relationships / Duplicates
- duplicate rows: 0 (0.0%)
- candidate ID columns (unique counts):
  - `episode_id`: 70,000 unique

### 6. Target / Outcome Analysis
**`action`** (categorical)
- `ESCALATE_TO_HUMAN`: 30,848 (22.048%)
- `RETRY`: 28,247 (20.189%)
- `PAYMENT_LINK`: 27,772 (19.85%)
- `REQUEST_ALTERNATE_METHOD`: 20,484 (14.641%)
- `STOP_RECOVERY`: 11,603 (8.293%)
- `WAIT`: 11,593 (8.286%)
- `SEND_REMINDER`: 9,363 (6.692%)
**`recovered_amount`** (numeric)
- min=0 max=59,999 mean=7,171.5029 median=0 std=15,850.8626

### 7. Cross-tabulations
**action_vs_recovered_amount**
```json
[{"action": "ESCALATE_TO_HUMAN", "count": 30848, "mean": 13587.367252334, "median": 2499.0, "std": 21326.6283515763}, {"action": "PAYMENT_LINK", "count": 27772, "mean": 9781.1857266311, "median": 999.0, "std": 17642.345540557}, {"action": "REQUEST_ALTERNATE_METHOD", "count": 20484, "mean": 7749.1895625854, "median": 0.0, "std": 16301.704982051}, {"action": "RETRY", "count": 28247, "mean": 2485.2877119694, "median": 0.0, "std": 6100.5700641657}, {"action": "SEND_REMINDER", "count": 9363, "mean": 2451.8464167468, "median": 0.0, "std": 9838.2340734479}, {"action": "STOP_RECOVERY", "count": 11603, "mean": 0.0, "median": 0.0, "std": 0.0}, {"action": "WAIT", "count": 11593, "mean": 5234.6944708013, "median": 0.0, "std": 13595.9599918017}]
```

### 9. Dataset-Specific Summary
**Potentially useful for:**
- behavioral information (behavior/score/history-like columns present)
- sequential/temporal information (timestamp-like columns present)
- treatment/action information
- outcome information (candidate target columns present)
**Potential limitations:**
- 3 constant column(s) present

## episodes_val.parquet

### 1. File Information
- type: parquet | size: 808.78 KB | rows: 29,786 | columns: 29

### 2-3. Column Schema & Unique Values

#### `behavior_prob`  (`float64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: CONSTANT
- all values (n=1): 1.0×29786

#### `failure_reason`  (`object`)
- unique: 6 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: target-like (name)
- top 6 values:
  - `temporary_bank_failure`: 12932 (43.416%) 
  - `insufficient_funds`: 8503 (28.547%) 
  - `invalid_payment_method`: 4191 (14.07%) 
  - `network_error`: 2042 (6.856%) 
  - `authentication_failed`: 1103 (3.703%) 
  - `card_expired`: 1015 (3.408%) 

#### `amount`  (`float64`)
- unique: 6 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=6): 999.0×5090, 2499.0×5083, 4999.0×5108, 9999.0×5112, 24999.0×5053, 59999.0×4340

#### `attempt_count`  (`int64`)
- unique: 3 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=3): 1×22990, 2×5869, 3×927

#### `hours_since_first_failure`  (`float64`)
- unique: 74 | missing: 0 (0.0%) | zeros: 15,000 | negative: 0
- flags: target-like (name)
- min=0 max=168 mean=18.0043 median=0 std=28.6908
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=36 p95=84 p99=121

#### `interventions_count`  (`int64`)
- unique: 5 | missing: 0 (0.0%) | zeros: 15,791 | negative: 0
- all values (n=5): 0×15791, 1×7844, 2×3558, 3×2067, 4×526

#### `consecutive_failures`  (`int64`)
- unique: 5 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: target-like (name)
- all values (n=5): 1×15791, 2×7844, 3×3558, 4×2067, 5×526

#### `is_weekend`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 21,218 | negative: 0
- all values (n=2): 0×21218, 1×8568

#### `customer_ltv`  (`float64`)
- unique: 15,000 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=5,007.4837 max=149,967.7754 mean=52,125.885 median=46,941.7408 std=29,200.0116
- quantiles: p1=6,923.0147 p5=12,682.7896 p25=27,818.357 p50=46,941.7408 p75=74,734.7208 p95=98,156.8583 p99=135,137.2537

#### `customer_failure_rate`  (`float64`)
- unique: 4 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: target-like (name)
- all values (n=4): 0.02×2357, 0.04×18372, 0.15×6095, 0.35×2962

#### `subscription_paid_count`  (`int64`)
- unique: 9 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=9): 1×3205, 2×3284, 3×3267, 4×3349, 5×3385, 6×3329, 7×3329, 8×3319, 9×3319

#### `customer_archetype`  (`object`)
- unique: 4 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: categorical-like (name)
- top 4 values:
  - `reliable`: 18372 (61.68%) 
  - `occasional`: 6095 (20.463%) 
  - `high_risk`: 2962 (9.944%) 
  - `reliable_dormant`: 2357 (7.913%) 

#### `opted_out`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 29,786 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×29786

#### `account_tenure_days`  (`int64`)
- unique: 1,801 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=30 max=2,197 mean=663.0482 median=597 std=416.1809
- quantiles: p1=65 p5=157 p25=333 p50=597 p75=911 p95=1,456.5 p99=2,046

#### `lifetime_success_rate`  (`float64`)
- unique: 116 | missing: 0 (0.0%) | zeros: 622 | negative: 0
- flags: timestamp-like, target-like (name)
- min=0 max=1 mean=0.8569 median=0.9474 std=0.2085
- quantiles: p1=0 p5=0.4 p25=0.8462 p50=0.9474 p75=0.9677 p95=1 p99=1

#### `days_since_last_success`  (`int64`)
- unique: 145 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: target-like (name)
- min=5 max=149 mean=37.1306 median=31 std=27.1858
- quantiles: p1=5 p5=8 p25=18 p50=31 p75=44 p95=91 p99=138

#### `historical_ltv`  (`float64`)
- unique: 15,000 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=5,007.4837 max=149,967.7754 mean=52,125.885 median=46,941.7408 std=29,200.0116
- quantiles: p1=6,923.0147 p5=12,682.7896 p25=27,818.357 p50=46,941.7408 p75=74,734.7208 p95=98,156.8583 p99=135,137.2537

#### `is_first_ever_failure`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 27,429 | negative: 0
- flags: target-like (name)
- all values (n=2): 0×27429, 1×2357

#### `action`  (`object`)
- unique: 7 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: target-like (name)
- top 7 values:
  - `ESCALATE_TO_HUMAN`: 6499 (21.819%) 
  - `PAYMENT_LINK`: 5990 (20.11%) 
  - `RETRY`: 5961 (20.013%) 
  - `REQUEST_ALTERNATE_METHOD`: 4447 (14.93%) 
  - `STOP_RECOVERY`: 2561 (8.598%) 
  - `WAIT`: 2421 (8.128%) 
  - `SEND_REMINDER`: 1907 (6.402%) 

#### `allowed_actions`  (`object`)
- unique: 3 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: target-like (name)
- top 3 values:
  - `ESCALATE_TO_HUMAN,PAYMENT_LINK,REQUEST_ALTERNATE_METHOD,RETRY,SEND_REMINDER,STOP_RECOVERY,WAIT`: 20034 (67.26%) 
  - `ESCALATE_TO_HUMAN,PAYMENT_LINK,REQUEST_ALTERNATE_METHOD,SEND_REMINDER,STOP_RECOVERY,WAIT`: 7159 (24.035%) 
  - `ESCALATE_TO_HUMAN,STOP_RECOVERY,WAIT`: 2593 (8.705%) 

#### `reward`  (`float64`)
- unique: 438 | missing: 0 (0.0%) | zeros: 15,975 | negative: 1,559
- min=-910 max=59,999 mean=7,166.7989 median=0 std=15,918.0101
- quantiles: p1=-240.75 p5=-5 p25=0 p50=0 p75=4,894 p95=59,829 p99=59,964

#### `done`  (`bool`)
- unique: 2 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- top 2 values:
  - `True`: 15000 (50.359%) 
  - `False`: 14786 (49.641%) 

#### `resolved`  (`bool`)
- unique: 2 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- top 2 values:
  - `False`: 17534 (58.867%) 
  - `True`: 12252 (41.133%) 

#### `recovered_amount`  (`float64`)
- unique: 7 | missing: 0 (0.0%) | zeros: 17,534 | negative: 0
- flags: target-like (name)
- all values (n=7): 0.0×17534, 999.0×2005, 2499.0×2067, 4999.0×2009, 9999.0×2004, 24999.0×2062, 59999.0×2105

#### `episode_id`  (`object`)
- unique: 15,000 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: id-like (name)
- top 20 values:
  - `ep_0038668`: 7 (0.024%) 
  - `ep_0006141`: 7 (0.024%) 
  - `ep_0038172`: 7 (0.024%) 
  - `ep_0085848`: 7 (0.024%) 
  - `ep_0099123`: 7 (0.024%) 
  - `ep_0039200`: 7 (0.024%) 
  - `ep_0033308`: 7 (0.024%) 
  - `ep_0039600`: 7 (0.024%) 
  - `ep_0067876`: 7 (0.024%) 
  - `ep_0049130`: 7 (0.024%) 
  - `ep_0052081`: 7 (0.024%) 
  - `ep_0079855`: 7 (0.024%) 
  - `ep_0065150`: 7 (0.024%) 
  - `ep_0074820`: 7 (0.024%) 
  - `ep_0097149`: 7 (0.024%) 
  - `ep_0075205`: 7 (0.024%) 
  - `ep_0075712`: 7 (0.024%) 
  - `ep_0009035`: 7 (0.024%) 
  - `ep_0071666`: 7 (0.024%) 
  - `ep_0061737`: 7 (0.024%) 

#### `timestep`  (`int64`)
- unique: 7 | missing: 0 (0.0%) | zeros: 15,000 | negative: 0
- flags: timestamp-like
- all values (n=7): 0×15000, 1×7895, 2×3735, 3×2100, 4×835, 5×196, 6×25

#### `episode_length`  (`int64`)
- unique: 7 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=7): 1×7105, 2×8320, 3×4905, 4×5060, 5×3195, 6×1026, 7×175

#### `episode_return`  (`float64`)
- unique: 438 | missing: 0 (0.0%) | zeros: 1,245 | negative: 5,267
- min=-910 max=59,999 mean=12,563.8413 median=4,624 std=18,847.5944
- quantiles: p1=-600 p5=-240 p25=759 p50=4,624 p75=9,999 p95=59,829 p99=59,964

#### `provenance`  (`object`)
- unique: 1 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: CONSTANT
- top 1 values:
  - `SYNTHETIC_TRAINING_DATA`: 29786 (100.0%) 

### 4. Data Quality Flags
- **constant columns**: behavior_prob, opted_out, provenance
- **near constant columns**: none
- **extremely high cardinality columns**: none
- **likely id columns**: episode_id
- **likely timestamp columns**: lifetime_success_rate, timestep
- **likely categorical columns**: failure_reason, customer_archetype, action, allowed_actions, done, resolved, episode_id, provenance
- **likely target outcome columns**: failure_reason, hours_since_first_failure, consecutive_failures, customer_failure_rate, lifetime_success_rate, days_since_last_success, is_first_ever_failure, action, allowed_actions, recovered_amount
- **columns with possible post outcome info**: none

### 5. Relationships / Duplicates
- duplicate rows: 0 (0.0%)
- candidate ID columns (unique counts):
  - `episode_id`: 15,000 unique

### 6. Target / Outcome Analysis
**`action`** (categorical)
- `ESCALATE_TO_HUMAN`: 6,499 (21.819%)
- `PAYMENT_LINK`: 5,990 (20.11%)
- `RETRY`: 5,961 (20.013%)
- `REQUEST_ALTERNATE_METHOD`: 4,447 (14.93%)
- `STOP_RECOVERY`: 2,561 (8.598%)
- `WAIT`: 2,421 (8.128%)
- `SEND_REMINDER`: 1,907 (6.402%)
**`recovered_amount`** (numeric)
- min=0 max=59,999 mean=7,221.3539 median=0 std=15,951.2747

### 7. Cross-tabulations
**action_vs_recovered_amount**
```json
[{"action": "ESCALATE_TO_HUMAN", "count": 6499, "mean": 13642.8578242807, "median": 2499.0, "std": 21395.4402794259}, {"action": "PAYMENT_LINK", "count": 5990, "mean": 10022.7943238731, "median": 999.0, "std": 17888.2803696117}, {"action": "REQUEST_ALTERNATE_METHOD", "count": 4447, "mean": 7771.2003597931, "median": 0.0, "std": 16399.8472567885}, {"action": "RETRY", "count": 5961, "mean": 2524.036403288, "median": 0.0, "std": 6151.3020087241}, {"action": "SEND_REMINDER", "count": 1907, "mean": 2390.2490823283, "median": 0.0, "std": 9415.7886864552}, {"action": "STOP_RECOVERY", "count": 2561, "mean": 0.0, "median": 0.0, "std": 0.0}, {"action": "WAIT", "count": 2421, "mean": 5052.1532424618, "median": 0.0, "std": 13787.245898577}]
```

### 9. Dataset-Specific Summary
**Potentially useful for:**
- behavioral information (behavior/score/history-like columns present)
- sequential/temporal information (timestamp-like columns present)
- treatment/action information
- outcome information (candidate target columns present)
**Potential limitations:**
- 3 constant column(s) present

## historical_records.csv

### 1. File Information
- type: csv | size: 161.04 KB | rows: 1,000 | columns: 23

### 2-3. Column Schema & Unique Values

#### `record_id`  (`object`)
- unique: 1,000 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: extremely-high-cardinality, id-like (name)
- top 20 values:
  - `rec_001000`: 1 (0.1%) 
  - `rec_000001`: 1 (0.1%) 
  - `rec_000002`: 1 (0.1%) 
  - `rec_000003`: 1 (0.1%) 
  - `rec_000004`: 1 (0.1%) 
  - `rec_000005`: 1 (0.1%) 
  - `rec_000006`: 1 (0.1%) 
  - `rec_000007`: 1 (0.1%) 
  - `rec_000984`: 1 (0.1%) 
  - `rec_000983`: 1 (0.1%) 
  - `rec_000982`: 1 (0.1%) 
  - `rec_000981`: 1 (0.1%) 
  - `rec_000980`: 1 (0.1%) 
  - `rec_000979`: 1 (0.1%) 
  - `rec_000978`: 1 (0.1%) 
  - `rec_000977`: 1 (0.1%) 
  - `rec_000976`: 1 (0.1%) 
  - `rec_000975`: 1 (0.1%) 
  - `rec_000974`: 1 (0.1%) 
  - `rec_000973`: 1 (0.1%) 

#### `customer_id`  (`int64`)
- unique: 998 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: extremely-high-cardinality, id-like (name)
- min=1,190 max=99,998 mean=51,709.639 median=52,787 std=28,463.1948
- quantiles: p1=2,216.73 p5=6,357.5 p25=27,803.75 p50=52,787 p75=75,767.25 p95=95,595.75 p99=99,076.21

#### `customer_archetype`  (`object`)
- unique: 3 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: categorical-like (name)
- top 3 values:
  - `reliable`: 709 (70.9%) 
  - `occasional`: 201 (20.1%) 
  - `high_risk`: 90 (9.0%) 

#### `customer_ltv`  (`float64`)
- unique: 1,000 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: extremely-high-cardinality
- min=5,007.25 max=99,881.91 mean=49,982.9368 median=45,288.87 std=25,764.6936
- quantiles: p1=8,920.7301 p5=14,603.445 p25=28,158.8175 p50=45,288.87 p75=72,111.3025 p95=94,226.342 p99=99,233.3655

#### `customer_failure_rate`  (`float64`)
- unique: 3 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: target-like (name)
- all values (n=3): 0.04×709, 0.15×201, 0.35×90

#### `customer_opted_out`  (`bool`)
- unique: 1 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: CONSTANT
- top 1 values:
  - `False`: 1000 (100.0%) 

#### `subscription_id`  (`object`)
- unique: 998 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: extremely-high-cardinality, id-like (name)
- top 20 values:
  - `sub_sim_92527`: 2 (0.2%) 
  - `sub_sim_78634`: 2 (0.2%) 
  - `sub_sim_13098`: 1 (0.1%) 
  - `sub_sim_35517`: 1 (0.1%) 
  - `sub_sim_41268`: 1 (0.1%) 
  - `sub_sim_82207`: 1 (0.1%) 
  - `sub_sim_41910`: 1 (0.1%) 
  - `sub_sim_32182`: 1 (0.1%) 
  - `sub_sim_49454`: 1 (0.1%) 
  - `sub_sim_23176`: 1 (0.1%) 
  - `sub_sim_66464`: 1 (0.1%) 
  - `sub_sim_97163`: 1 (0.1%) 
  - `sub_sim_13231`: 1 (0.1%) 
  - `sub_sim_8674`: 1 (0.1%) 
  - `sub_sim_24268`: 1 (0.1%) 
  - `sub_sim_72839`: 1 (0.1%) 
  - `sub_sim_83359`: 1 (0.1%) 
  - `sub_sim_94490`: 1 (0.1%) 
  - `sub_sim_38079`: 1 (0.1%) 
  - `sub_sim_39501`: 1 (0.1%) 

#### `subscription_paid_count`  (`int64`)
- unique: 9 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=9): 1×101, 2×117, 3×113, 4×106, 5×108, 6×130, 7×104, 8×118, 9×103

#### `subscription_remaining_count`  (`int64`)
- unique: 9 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=9): 2×113, 3×120, 4×96, 5×113, 6×128, 7×115, 8×109, 9×116, 10×90

#### `amount`  (`float64`)
- unique: 6 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=6): 999.0×174, 2499.0×172, 4999.0×174, 9999.0×165, 24999.0×150, 59999.0×165

#### `failure_reason`  (`object`)
- unique: 6 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: target-like (name)
- top 6 values:
  - `temporary_bank_failure`: 404 (40.4%) 
  - `insufficient_funds`: 294 (29.4%) 
  - `invalid_payment_method`: 150 (15.0%) 
  - `network_error`: 79 (7.9%) 
  - `card_expired`: 45 (4.5%) 
  - `authentication_failed`: 28 (2.8%) 

#### `attempt_count`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: CONSTANT
- all values (n=1): 1×1000

#### `hours_since_first_failure`  (`float64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 1,000 | negative: 0
- flags: CONSTANT, target-like (name)
- all values (n=1): 0.0×1000

#### `interventions_count`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 1,000 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×1000

#### `is_weekend`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 718 | negative: 0
- all values (n=2): 0×718, 1×282

#### `action_taken`  (`object`)
- unique: 7 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: target-like (name)
- top 7 values:
  - `RETRY`: 456 (45.6%) 
  - `PAYMENT_LINK`: 201 (20.1%) 
  - `REQUEST_ALTERNATE_METHOD`: 109 (10.9%) 
  - `SEND_REMINDER`: 108 (10.8%) 
  - `WAIT`: 61 (6.1%) 
  - `ESCALATE_TO_HUMAN`: 35 (3.5%) 
  - `STOP_RECOVERY`: 30 (3.0%) 

#### `recovered`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 649 | negative: 0
- flags: target-like (name)
- all values (n=2): 0×649, 1×351

#### `recovered_amount`  (`float64`)
- unique: 7 | missing: 0 (0.0%) | zeros: 649 | negative: 0
- flags: target-like (name)
- all values (n=7): 0.0×649, 999.0×57, 2499.0×55, 4999.0×64, 9999.0×63, 24999.0×51, 59999.0×61

#### `recovery_time_hours`  (`float64`)
- unique: 7 | missing: 0 (0.0%) | zeros: 30 | negative: 0
- flags: timestamp-like, target-like (name)
- all values (n=7): 0.0×30, 1.0×456, 6.0×16, 12.0×108, 24.0×246, 36.0×109, 48.0×35

#### `action_cost`  (`float64`)
- unique: 6 | missing: 0 (0.0%) | zeros: 91 | negative: 0
- flags: target-like (name)
- all values (n=6): 0.0×91, 5.0×456, 10.0×108, 15.0×201, 20.0×109, 150.0×35

#### `friction`  (`float64`)
- unique: 6 | missing: 0 (0.0%) | zeros: 91 | negative: 0
- all values (n=6): 0.0×91, 0.2×456, 0.8×35, 1.0×201, 1.2×108, 1.5×109

#### `reward`  (`float64`)
- unique: 37 | missing: 0 (0.0%) | zeros: 91 | negative: 558
- min=-230 max=59,974 mean=5,998.864 median=-25 std=14,920.0938
- quantiles: p1=-230 p5=-130 p25=-75 p50=-25 p75=2,474 p95=59,829 p99=59,974

#### `provenance`  (`object`)
- unique: 1 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: CONSTANT
- top 1 values:
  - `SYNTHETIC_TRAINING_DATA`: 1000 (100.0%) 

### 4. Data Quality Flags
- **constant columns**: customer_opted_out, attempt_count, hours_since_first_failure, interventions_count, provenance
- **near constant columns**: none
- **extremely high cardinality columns**: record_id, customer_id, customer_ltv, subscription_id
- **likely id columns**: record_id, customer_id, subscription_id
- **likely timestamp columns**: recovery_time_hours
- **likely categorical columns**: record_id, customer_archetype, customer_opted_out, subscription_id, failure_reason, action_taken, provenance
- **likely target outcome columns**: customer_failure_rate, failure_reason, hours_since_first_failure, action_taken, recovered, recovered_amount, recovery_time_hours, action_cost
- **columns with possible post outcome info**: none

### 5. Relationships / Duplicates
- duplicate rows: 0 (0.0%)
- candidate ID columns (unique counts):
  - `record_id`: 1,000 unique
  - `customer_id`: 998 unique
  - `subscription_id`: 998 unique
- inferred entity relationships:
  - `customer_id` -> 998 unique entities

### 6. Target / Outcome Analysis
**`recovered`** (binary)
- 0: 649 (64.9%)
- 1: 351 (35.1%)
**`recovered_amount`** (numeric)
- min=0 max=59,999 mean=6,079.149 median=0 std=14,934.208

### 9. Dataset-Specific Summary
**Potentially useful for:**
- customer/payment context (entity id columns present)
- sequential/temporal information (timestamp-like columns present)
- outcome information (candidate target columns present)
**Potential limitations:**
- 5 constant column(s) present

## historical_records.parquet

### 1. File Information
- type: parquet | size: 1.70 MB | rows: 55,000 | columns: 23

### 2-3. Column Schema & Unique Values

#### `record_id`  (`object`)
- unique: 55,000 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: extremely-high-cardinality, id-like (name)
- top 20 values:
  - `rec_055000`: 1 (0.002%) 
  - `rec_000001`: 1 (0.002%) 
  - `rec_000002`: 1 (0.002%) 
  - `rec_000003`: 1 (0.002%) 
  - `rec_000004`: 1 (0.002%) 
  - `rec_000005`: 1 (0.002%) 
  - `rec_000006`: 1 (0.002%) 
  - `rec_000007`: 1 (0.002%) 
  - `rec_054984`: 1 (0.002%) 
  - `rec_054983`: 1 (0.002%) 
  - `rec_054982`: 1 (0.002%) 
  - `rec_054981`: 1 (0.002%) 
  - `rec_054980`: 1 (0.002%) 
  - `rec_054979`: 1 (0.002%) 
  - `rec_054978`: 1 (0.002%) 
  - `rec_054977`: 1 (0.002%) 
  - `rec_054976`: 1 (0.002%) 
  - `rec_054975`: 1 (0.002%) 
  - `rec_054974`: 1 (0.002%) 
  - `rec_054973`: 1 (0.002%) 

#### `customer_id`  (`int64`)
- unique: 42,055 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: id-like (name)
- min=1,003 max=99,998 mean=50,532.1102 median=50,713.5 std=28,555.827
- quantiles: p1=2,002.96 p5=5,969 p25=25,883 p50=50,713.5 p75=75,122.75 p95=94,964.1 p99=98,948

#### `customer_archetype`  (`object`)
- unique: 3 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: categorical-like (name)
- top 3 values:
  - `reliable`: 38392 (69.804%) 
  - `occasional`: 10945 (19.9%) 
  - `high_risk`: 5663 (10.296%) 

#### `customer_ltv`  (`float64`)
- unique: 54,838 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: extremely-high-cardinality
- min=5,001.81 max=99,999.04 mean=49,568.4613 median=45,560.965 std=26,092.0295
- quantiles: p1=6,946.2976 p5=12,481.8085 p25=27,210.035 p50=45,560.965 p75=71,791.1375 p95=94,286.344 p99=98,941.8481

#### `customer_failure_rate`  (`float64`)
- unique: 3 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: target-like (name)
- all values (n=3): 0.04×38392, 0.15×10945, 0.35×5663

#### `customer_opted_out`  (`bool`)
- unique: 1 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: CONSTANT
- top 1 values:
  - `False`: 55000 (100.0%) 

#### `subscription_id`  (`object`)
- unique: 42,055 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: id-like (name)
- top 20 values:
  - `sub_sim_50013`: 6 (0.011%) 
  - `sub_sim_74377`: 5 (0.009%) 
  - `sub_sim_79032`: 5 (0.009%) 
  - `sub_sim_78404`: 5 (0.009%) 
  - `sub_sim_91482`: 5 (0.009%) 
  - `sub_sim_15477`: 5 (0.009%) 
  - `sub_sim_84624`: 5 (0.009%) 
  - `sub_sim_98663`: 5 (0.009%) 
  - `sub_sim_77990`: 5 (0.009%) 
  - `sub_sim_72635`: 5 (0.009%) 
  - `sub_sim_31716`: 5 (0.009%) 
  - `sub_sim_4662`: 5 (0.009%) 
  - `sub_sim_70276`: 5 (0.009%) 
  - `sub_sim_75029`: 5 (0.009%) 
  - `sub_sim_59461`: 5 (0.009%) 
  - `sub_sim_29114`: 5 (0.009%) 
  - `sub_sim_91289`: 5 (0.009%) 
  - `sub_sim_91471`: 5 (0.009%) 
  - `sub_sim_46646`: 5 (0.009%) 
  - `sub_sim_63590`: 5 (0.009%) 

#### `subscription_paid_count`  (`int64`)
- unique: 9 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=9): 1×6139, 2×6159, 3×6141, 4×5946, 5×6107, 6×6210, 7×6199, 8×6107, 9×5992

#### `subscription_remaining_count`  (`int64`)
- unique: 9 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=9): 2×6135, 3×6119, 4×6141, 5×6025, 6×6048, 7×6044, 8×6218, 9×6150, 10×6120

#### `amount`  (`float64`)
- unique: 6 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=6): 999.0×9072, 2499.0×9343, 4999.0×9277, 9999.0×9102, 24999.0×9188, 59999.0×9018

#### `failure_reason`  (`object`)
- unique: 6 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: target-like (name)
- top 6 values:
  - `temporary_bank_failure`: 21765 (39.573%) 
  - `insufficient_funds`: 16462 (29.931%) 
  - `invalid_payment_method`: 8288 (15.069%) 
  - `network_error`: 3824 (6.953%) 
  - `card_expired`: 2911 (5.293%) 
  - `authentication_failed`: 1750 (3.182%) 

#### `attempt_count`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: CONSTANT
- all values (n=1): 1×55000

#### `hours_since_first_failure`  (`float64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 55,000 | negative: 0
- flags: CONSTANT, target-like (name)
- all values (n=1): 0.0×55000

#### `interventions_count`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 55,000 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×55000

#### `is_weekend`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 39,558 | negative: 0
- all values (n=2): 0×39558, 1×15442

#### `action_taken`  (`object`)
- unique: 7 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: target-like (name)
- top 7 values:
  - `RETRY`: 26600 (48.364%) 
  - `PAYMENT_LINK`: 10814 (19.662%) 
  - `REQUEST_ALTERNATE_METHOD`: 6538 (11.887%) 
  - `SEND_REMINDER`: 5047 (9.176%) 
  - `WAIT`: 2503 (4.551%) 
  - `ESCALATE_TO_HUMAN`: 1968 (3.578%) 
  - `STOP_RECOVERY`: 1530 (2.782%) 

#### `recovered`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 36,179 | negative: 0
- flags: target-like (name)
- all values (n=2): 0×36179, 1×18821

#### `recovered_amount`  (`float64`)
- unique: 7 | missing: 0 (0.0%) | zeros: 36,179 | negative: 0
- flags: target-like (name)
- all values (n=7): 0.0×36179, 999.0×3049, 2499.0×3101, 4999.0×3192, 9999.0×3022, 24999.0×3123, 59999.0×3334

#### `recovery_time_hours`  (`float64`)
- unique: 7 | missing: 0 (0.0%) | zeros: 1,530 | negative: 0
- flags: timestamp-like, target-like (name)
- all values (n=7): 0.0×1530, 1.0×26600, 6.0×637, 12.0×5047, 24.0×12680, 36.0×6538, 48.0×1968

#### `action_cost`  (`float64`)
- unique: 6 | missing: 0 (0.0%) | zeros: 4,033 | negative: 0
- flags: target-like (name)
- all values (n=6): 0.0×4033, 5.0×26600, 10.0×5047, 15.0×10814, 20.0×6538, 150.0×1968

#### `friction`  (`float64`)
- unique: 6 | missing: 0 (0.0%) | zeros: 4,033 | negative: 0
- all values (n=6): 0.0×4033, 0.2×26600, 0.8×1968, 1.0×10814, 1.2×5047, 1.5×6538

#### `reward`  (`float64`)
- unique: 37 | missing: 0 (0.0%) | zeros: 4,033 | negative: 32,146
- min=-230 max=59,974 mean=6,011.3002 median=-25 std=14,950.573
- quantiles: p1=-230 p5=-170 p25=-75 p50=-25 p75=2,384 p95=59,829 p99=59,974

#### `provenance`  (`object`)
- unique: 1 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: CONSTANT
- top 1 values:
  - `SYNTHETIC_TRAINING_DATA`: 55000 (100.0%) 

### 4. Data Quality Flags
- **constant columns**: customer_opted_out, attempt_count, hours_since_first_failure, interventions_count, provenance
- **near constant columns**: none
- **extremely high cardinality columns**: record_id, customer_ltv
- **likely id columns**: record_id, customer_id, subscription_id
- **likely timestamp columns**: recovery_time_hours
- **likely categorical columns**: record_id, customer_archetype, customer_opted_out, subscription_id, failure_reason, action_taken, provenance
- **likely target outcome columns**: customer_failure_rate, failure_reason, hours_since_first_failure, action_taken, recovered, recovered_amount, recovery_time_hours, action_cost
- **columns with possible post outcome info**: none

### 5. Relationships / Duplicates
- duplicate rows: 0 (0.0%)
- candidate ID columns (unique counts):
  - `record_id`: 55,000 unique
  - `customer_id`: 42,055 unique
  - `subscription_id`: 42,055 unique
- inferred entity relationships:
  - `customer_id` -> 42,055 unique entities

### 6. Target / Outcome Analysis
**`recovered`** (binary)
- 0: 36,179 (65.78%)
- 1: 18,821 (34.22%)
**`recovered_amount`** (numeric)
- min=0 max=59,999 mean=6,092.3214 median=0 std=14,964.721

### 9. Dataset-Specific Summary
**Potentially useful for:**
- customer/payment context (entity id columns present)
- sequential/temporal information (timestamp-like columns present)
- outcome information (candidate target columns present)
**Potential limitations:**
- 5 constant column(s) present

## live_persona_state.json

### 1. File Information
- type: json | size: 57.84 KB | rows: 50 | columns: 9

### 2-3. Column Schema & Unique Values

#### `phone`  (`int64`)
- unique: 50 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: extremely-high-cardinality
- min=919,000,001,546 max=919,000,001,595 mean=919,000,001,570.5 median=919,000,001,570.5 std=14.5774
- quantiles: p1=919,000,001,546.49 p5=919,000,001,548.45 p25=919,000,001,558.25 p50=919,000,001,570.5 p75=919,000,001,582.75 p95=919,000,001,592.55 p99=919,000,001,594.51

#### `persona`  (`object`)
- unique: 6 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- top 6 values:
  - `considering_cancellation`: 13 (26.0%) 
  - `needs_payment_help`: 10 (20.0%) 
  - `accidental_failure`: 8 (16.0%) 
  - `forgetful_promises_then_pays`: 7 (14.0%) 
  - `suspicious_payer`: 6 (12.0%) 
  - `ignores_completely`: 6 (12.0%) 

#### `status`  (`object`)
- unique: 2 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: categorical-like (name)
- top 2 values:
  - `resolved`: 47 (94.0%) 
  - `stalled`: 3 (6.0%) 

#### `outcome`  (`object`)
- unique: 5 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: target-like (name)
- top 5 values:
  - `recovered`: 22 (44.0%) 
  - `retained_paused`: 12 (24.0%) 
  - `human_escalated`: 7 (14.0%) 
  - `timeout`: 6 (12.0%) 
  - `active`: 3 (6.0%) 

#### `replies_sent`  (`int64`)
- unique: 10 | missing: 0 (0.0%) | zeros: 8 | negative: 0
- all values (n=10): 0×8, 1×17, 2×1, 3×13, 4×4, 5×1, 6×1, 7×1, 8×1, 10×3

#### `temperature`  (`float64`)
- unique: 19 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=19): 0.7000000000000001×1, 0.71×2, 0.72×2, 0.73×1, 0.75×1, 0.76×4, 0.78×1, 0.79×4, 0.8×1, 0.81×2, 0.8200000000000001×4, 0.8300000000000001×3, 0.84×5, 0.85×6, 0.86×3, 0.87×2, 0.88×2, 0.89×5, 0.9×1

- **seen_interventions** -- ERROR analyzing column: TypeError: unhashable type: 'list'

#### `conversation_summary`  (`object`)
- unique: 45 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- top 20 values:
  - ``: 6 (12.0%) 
  - `Agent notified that the payment of INR 999.00 failed due to insufficient funds and warned that cancelling would result in loss of all premium features, including advanced analytics, priority support, and exclusive content, asking if the user wants to keep the subscription or needs help updating payment. Agent then offered to pause the Razorpay Premium Annual Subscription for one month and asked if the user would like to proceed. User was told the subscription was paused for a month and given a payment link to resume anytime. User now asks for clarification on what would be lost if they cancel and inquires about any discounts or flexible plans.`: 1 (2.0%) 
  - `Agent informed the customer that the INR 1499.00 payment failed and the auto‑pay mandate was revoked (invoice 919000001548). The customer requested a UPI link or an easy way to update the payment method. Agent provided a UPI payment link (https://rzp.io/i/3ade2d61) and asked the customer to update and inform when done. Customer thanked the agent and said they would update the payment method right away using the UPI option. Agent reiterated thanks and reminded the customer to let them know once the payment is completed, sending the same payment link again. Latest agent message: "Thanks! You can pay here: https://rzp.io/i/3ade2d61. Let us know once it’s completed."`: 1 (2.0%) 
  - `Agent sent a payment recovery notice about a declined INR 999.00 transaction (reference 919000001549). User asked for clarification about the product/service and sign‑up date. Agent replied that the charge is for a Razorpay Premium Annual Subscription, could not provide the signup date, and offered a payment link. User requested specifics about what the subscription includes and asked for confirmation of the email linked to the account. Agent responded that the subscription gives full access to all premium features for a year, cannot view the email on file, and forwarded the request to support.`: 1 (2.0%) 
  - `Agent notified user that the INR 999.00 transaction was declined. User asked for a UPI link or instructions to update payment method, preferring UPI over re‑entering card details. Agent provided a UPI payment link (https://rzp.io/i/98b54934). User now acknowledges receipt and plans to complete the payment using the provided link.`: 1 (2.0%) 
  - `Agent informed me that the payment of INR 499 (transaction ID 919000001550) failed because my card has expired. I acknowledged the issue, said I’ll update my card details, and will pay the amount right away.`: 1 (2.0%) 
  - `Agent notified that the INR 1499 auto‑pay was revoked, causing a payment failure. Customer asked for guidance on updating payment details and expressed intent to pay promptly. Agent provided a link to update payment info.`: 1 (2.0%) 
  - `Agent sent a payment recovery notice for INR 499.00 (transaction ID 919000001553) due to an expired card. Customer thanked the agent, noted the card expiration, and asked for a link to update payment details. Agent provided a link (https://rzp.io/i/2928cf9b) to update card details and asked to be notified once done to reactivate the Razorpay Pro Monthly Plan. Customer now confirms they have updated the card and requests reactivation.`: 1 (2.0%) 
  - `Agent informed me that the INR 2999.00 payment for invoice 919000001554 failed due to incorrect details and sent a payment link. I acknowledged and promised to pay tonight. Agent followed up, reminding me to use the same link. I reiterated my promise to pay tonight. Agent sent another reminder, confirming they will watch for my payment tonight and shared the payment link again. I responded with another promise to handle the payment tonight. Agent thanked me and said they'd look out for my payment tonight, providing the payment link again. Latest agent message: "Thanks! We'll look out for your payment tonight. You can pay here: https://rzp.io/i/71cb26a9". My reply: "Got it, thanks! I'll take care of it tonight after I finish up some work."`: 1 (2.0%) 
  - `Agent sent a payment recovery notice for INR 999.00 (invoice 919000001555) due to insufficient funds. Customer replied promising to pay tonight. Agent followed up, acknowledging the plan and providing the payment link, asking to be informed of any issues.`: 1 (2.0%) 
  - `Agent sent a payment recovery notice indicating a declined transaction of INR 999.00 (transaction ID 919000001557). The user asked for details about the product/service and subscription date. Agent replied that it is for the Razorpay Premium Annual Subscription and suggested checking email or account for the sign‑up date. User requested the exact start date and a copy of the confirmation or invoice. Agent responded that they don’t have access to the signup date or original invoice, but have forwarded the request to support and will get back shortly. User now asks for an estimated response time and reiterates need for invoice before confirming payment.`: 1 (2.0%) 
  - `Agent notified of a failed INR 499.00 payment due to an expired card (transaction ID 919000001558). Customer thanked the agent, confirmed the card expiration, and requested a link to update payment details. Agent provided the update link: https://rzp.io/i/b49295c8. Customer now confirms they have updated the card using the link and asks for confirmation that the payment succeeded.`: 1 (2.0%) 
  - `Agent sent a payment recovery notice stating the auto‑pay mandate was revoked for INR 1499.00 due to a payment failure. User responded requesting a UPI link or instructions to update the payment method, indicating willingness to pay but needing an alternative to the failed card. Agent provided a UPI payment link: https://rzp.io/i/09e9845f. User replied thanking the agent, confirming they have opened the link and will pay immediately.`: 1 (2.0%) 
  - `Agent notified that a 999 INR charge was declined. User requested a UPI payment link or instructions to update payment method, preferring UPI over re‑entering card details. Agent responded with a UPI link (https://rzp.io/i/a0375d51) and offered further help, reiterating the link and asking to be informed once payment is completed. User now acknowledges the link and intends to pay immediately via UPI.`: 1 (2.0%) 
  - `Agent sent a payment recovery notice for a failed INR 2999 payment (invoice 919000001561) due to incorrect payment details. User asked for clarification about the product/service and sign‑up date. Agent replied that the charge is for the Razorpay Business Suite Subscription, but did not have the exact signup date, suggesting the user check their email or account and providing a payment link. User requested the exact subscription date and email confirmation before proceeding. Agent responded they do not have access to that information and have forwarded the request to support.`: 1 (2.0%) 
  - `Agent notified me that a payment of INR 499.00 failed due to a technical error. I asked what would be lost if I cancel. Agent replied that canceling would lose access to premium features, priority support, future updates, and that reports would be removed after 30 days. The agent also offered to downgrade me to a cheaper plan if I specify which one. I asked for clarification on data loss and possible downgrade options. Agent responded that reports are kept for 30 days then deleted permanently, and that they will forward my question about cheaper plans and their features to the support team for a follow‑up.`: 1 (2.0%) 
  - `Agent notified me of a payment failure for INR 2999 (transaction ID 919000001563). I acknowledged the issue and asked for a link to update payment details. Agent sent a link (https://rzp.io/i/94c94d5d) to update the card. I responded that I clicked the link, updated my card, and the payment is now completed.`: 1 (2.0%) 
  - `Agent notified that the auto‑pay mandate was revoked for INR 1499.00 (transaction ID 919000001564). User acknowledged the notice, mentioned the card issue, and requested a UPI payment link or a way to update payment details. Agent provided a UPI payment link (https://rzp.io/i/61a2d44f) and mentioned the option to update the payment method in the app. User responded with gratitude and intent to pay using the provided link.`: 1 (2.0%) 
  - `Agent sent a payment recovery notice about a failed INR 999 charge (transaction ID 919000001565) due to insufficient funds. User asked what would be lost if they cancel and if a pause option is available. Agent explained that cancelling would lose access to premium features and support, and offered a pause of up to 1 month with no charges but also no access, providing a payment link. User expressed desire to pause for a month to reassess. Agent confirmed the subscription is paused for a month and will reactivate automatically after 30 days.`: 1 (2.0%) 
  - `Agent sent a payment recovery notice about a technical error processing INR 499 (reference 919000001566). Customer asked for a link to update card details. Agent provided the link https://rzp.io/i/a70df4ea. Customer confirmed updating the card and completing the payment.`: 1 (2.0%) 

- **scenario** -- ERROR analyzing column: TypeError: unhashable type: 'dict'

### 4. Data Quality Flags
- **constant columns**: none
- **near constant columns**: none
- **extremely high cardinality columns**: phone
- **likely id columns**: none
- **likely timestamp columns**: none
- **likely categorical columns**: persona, status, outcome, conversation_summary
- **likely target outcome columns**: outcome
- **columns with possible post outcome info**: none

### 5. Relationships / Duplicates
- duplicate rows: not computed

### 6. Target / Outcome Analysis
**`outcome`** (categorical)
- `recovered`: 22 (44.0%)
- `retained_paused`: 12 (24.0%)
- `human_escalated`: 7 (14.0%)
- `timeout`: 6 (12.0%)
- `active`: 3 (6.0%)

### 9. Dataset-Specific Summary
**Potentially useful for:**
- outcome information (candidate target columns present)
**Potential limitations:**
- no obvious temporal information detected

## sample_data/anscombe.json

### 1. File Information
- type: json | size: 1.66 KB | rows: 44 | columns: 3

### 2-3. Column Schema & Unique Values

#### `Series`  (`object`)
- unique: 4 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- top 4 values:
  - `I`: 11 (25.0%) 
  - `II`: 11 (25.0%) 
  - `III`: 11 (25.0%) 
  - `IV`: 11 (25.0%) 

#### `X`  (`int64`)
- unique: 12 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=12): 4×3, 5×3, 6×3, 7×3, 8×13, 9×3, 10×3, 11×3, 12×3, 13×3, 14×3, 19×1

#### `Y`  (`float64`)
- unique: 43 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: extremely-high-cardinality
- min=3.1 max=12.74 mean=7.5005 median=7.52 std=1.9592
- quantiles: p1=3.5988 p5=4.7505 p25=6.1175 p50=7.52 p75=8.7475 p95=10.708 p99=12.6368

### 4. Data Quality Flags
- **constant columns**: none
- **near constant columns**: none
- **extremely high cardinality columns**: Y
- **likely id columns**: none
- **likely timestamp columns**: none
- **likely categorical columns**: Series
- **likely target outcome columns**: none
- **columns with possible post outcome info**: none

### 5. Relationships / Duplicates
- duplicate rows: 0 (0.0%)

### 9. Dataset-Specific Summary
**Potentially useful for:**
- general tabular features (no strong signal columns detected)
**Potential limitations:**
- no obvious temporal information detected
- no obvious target/outcome column detected

## sample_data/california_housing_test.csv

### 1. File Information
- type: csv | size: 294.08 KB | rows: 3,000 | columns: 9

### 2-3. Column Schema & Unique Values

#### `longitude`  (`float64`)
- unique: 607 | missing: 0 (0.0%) | zeros: 0 | negative: 3,000
- min=-124.18 max=-114.49 mean=-119.5892 median=-118.485 std=1.9949
- quantiles: p1=-123.2101 p5=-122.47 p25=-121.81 p50=-118.485 p75=-118.02 p95=-117.1 p99=-116.48

#### `latitude`  (`float64`)
- unique: 587 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=32.56 max=41.92 mean=35.6354 median=34.27 std=2.1297
- quantiles: p1=32.69 p5=32.82 p25=33.93 p50=34.27 p75=37.69 p95=38.97 p99=40.6

#### `housing_median_age`  (`float64`)
- unique: 52 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=1 max=52 mean=28.8453 median=29 std=12.5554
- quantiles: p1=4 p5=8 p25=18 p50=29 p75=37 p95=52 p99=52

#### `total_rooms`  (`float64`)
- unique: 2,215 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=6 max=30,450 mean=2,599.5787 median=2,106 std=2,155.5933
- quantiles: p1=105.99 p5=585.9 p25=1,401 p50=2,106 p75=3,129 p95=6,016.45 p99=10,724.28

#### `total_bedrooms`  (`float64`)
- unique: 1,055 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=2 max=5,419 mean=529.9507 median=437 std=415.6544
- quantiles: p1=26 p5=130.95 p25=291 p50=437 p75=636 p95=1,220.1 p99=2,100.12

#### `population`  (`float64`)
- unique: 1,802 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=5 max=11,935 mean=1,402.7987 median=1,155 std=1,030.543
- quantiles: p1=62.96 p5=346.95 p25=780 p50=1,155 p75=1,742.75 p95=3,238.3 p99=5,226.11

#### `households`  (`float64`)
- unique: 1,026 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=2 max=4,930 mean=489.912 median=409.5 std=365.4227
- quantiles: p1=21.99 p5=122.95 p25=273 p50=409.5 p75=597.25 p95=1,113 p99=1,840.04

#### `median_income`  (`float64`)
- unique: 2,578 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=0.4999 max=15.0001 mean=3.8073 median=3.4871 std=1.8545
- quantiles: p1=1.0349 p5=1.5624 p25=2.544 p50=3.4871 p75=4.6565 p95=6.9755 p99=10.38

#### `median_house_value`  (`float64`)
- unique: 1,784 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=22,500 max=500,001 mean=205,846.275 median=177,650 std=113,119.6875
- quantiles: p1=51,597 p5=67,785 p25=121,200 p50=177,650 p75=263,975 p95=465,640 p99=500,001

### 4. Data Quality Flags
- **constant columns**: none
- **near constant columns**: none
- **extremely high cardinality columns**: none
- **likely id columns**: none
- **likely timestamp columns**: none
- **likely categorical columns**: none
- **likely target outcome columns**: none
- **columns with possible post outcome info**: none

### 5. Relationships / Duplicates
- duplicate rows: 0 (0.0%)

### 9. Dataset-Specific Summary
**Potentially useful for:**
- general tabular features (no strong signal columns detected)
**Potential limitations:**
- no obvious temporal information detected
- no obvious target/outcome column detected

## sample_data/california_housing_train.csv

### 1. File Information
- type: csv | size: 1.63 MB | rows: 17,000 | columns: 9

### 2-3. Column Schema & Unique Values

#### `longitude`  (`float64`)
- unique: 827 | missing: 0 (0.0%) | zeros: 0 | negative: 17,000
- min=-124.35 max=-114.31 mean=-119.5621 median=-118.49 std=2.0052
- quantiles: p1=-123.2301 p5=-122.47 p25=-121.79 p50=-118.49 p75=-118 p95=-117.07 p99=-116.25

#### `latitude`  (`float64`)
- unique: 840 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=32.54 max=41.95 mean=35.6252 median=34.25 std=2.1373
- quantiles: p1=32.68 p5=32.82 p25=33.93 p50=34.25 p75=37.72 p95=38.96 p99=40.6301

#### `housing_median_age`  (`float64`)
- unique: 52 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=1 max=52 mean=28.5894 median=29 std=12.5869
- quantiles: p1=4 p5=8 p25=18 p50=29 p75=37 p95=52 p99=52

#### `total_rooms`  (`float64`)
- unique: 5,533 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=2 max=37,937 mean=2,643.6644 median=2,127 std=2,179.9471
- quantiles: p1=186.99 p5=626.95 p25=1,462 p50=2,127 p75=3,151.25 p95=6,269.05 p99=11,294.14

#### `total_bedrooms`  (`float64`)
- unique: 1,848 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=1 max=6,445 mean=539.4108 median=434 std=421.4995
- quantiles: p1=41 p5=138 p25=297 p50=434 p75=648.25 p95=1,283 p99=2,269.05

#### `population`  (`float64`)
- unique: 3,683 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=3 max=35,682 mean=1,429.5739 median=1,167 std=1,147.853
- quantiles: p1=94.99 p5=350.95 p25=790 p50=1,167 p75=1,721 p95=3,297.05 p99=5,871.28

#### `households`  (`float64`)
- unique: 1,740 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=1 max=6,082 mean=501.2219 median=409 std=384.5208
- quantiles: p1=34 p5=126 p25=282 p50=409 p75=605.25 p95=1,172.1 p99=2,036.02

#### `median_income`  (`float64`)
- unique: 11,175 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=0.4999 max=15.0001 mean=3.8836 median=3.5446 std=1.9082
- quantiles: p1=1.0955 p5=1.6034 p25=2.5664 p50=3.5446 p75=4.767 p95=7.3645 p99=10.6351

#### `median_house_value`  (`float64`)
- unique: 3,694 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- min=14,999 max=500,001 mean=207,300.9124 median=180,400 std=115,983.7644
- quantiles: p1=50,000 p5=66,000 p25=119,400 p50=180,400 p75=265,000 p95=495,500 p99=500,001

### 4. Data Quality Flags
- **constant columns**: none
- **near constant columns**: none
- **extremely high cardinality columns**: none
- **likely id columns**: none
- **likely timestamp columns**: none
- **likely categorical columns**: none
- **likely target outcome columns**: none
- **columns with possible post outcome info**: none

### 5. Relationships / Duplicates
- duplicate rows: 0 (0.0%)

### 9. Dataset-Specific Summary
**Potentially useful for:**
- general tabular features (no strong signal columns detected)
**Potential limitations:**
- no obvious temporal information detected
- no obvious target/outcome column detected

## sample_data/mnist_test.csv

### 1. File Information
- type: csv | size: 17.44 MB | rows: 9,999 | columns: 785
- NOTE: column detail truncated to first 300 columns


### 2-3. Column Schema & Unique Values

#### `7`  (`int64`)
- unique: 10 | missing: 0 (0.0%) | zeros: 980 | negative: 0
- all values (n=10): 0×980, 1×1135, 2×1032, 3×1010, 4×982, 5×892, 6×958, 7×1027, 8×974, 9×1009

#### `0`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.1`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.2`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.3`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.4`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.5`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.6`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.7`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.8`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.9`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.10`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.11`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.12`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.13`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.14`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.15`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.16`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.17`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.18`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.19`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.20`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.21`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.22`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.23`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.24`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.25`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.26`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.27`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.28`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.29`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.30`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.31`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.32`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.33`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 9,998 | negative: 0
- flags: near-constant
- all values (n=2): 0×9998, 38×1

#### `0.34`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 9,998 | negative: 0
- flags: near-constant
- all values (n=2): 0×9998, 236×1

#### `0.35`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 9,998 | negative: 0
- flags: near-constant
- all values (n=2): 0×9998, 158×1

#### `0.36`  (`int64`)
- unique: 3 | missing: 0 (0.0%) | zeros: 9,997 | negative: 0
- flags: near-constant
- all values (n=3): 0×9997, 170×1, 233×1

#### `0.37`  (`int64`)
- unique: 6 | missing: 0 (0.0%) | zeros: 9,993 | negative: 0
- flags: near-constant
- all values (n=6): 0×9993, 13×2, 37×1, 106×1, 144×1, 198×1

#### `0.38`  (`int64`)
- unique: 12 | missing: 0 (0.0%) | zeros: 9,988 | negative: 0
- flags: near-constant
- all values (n=12): 0×9988, 4×1, 15×1, 21×1, 22×1, 24×1, 28×1, 44×1, 192×1, 218×1, 224×1, 255×1

#### `0.39`  (`int64`)
- unique: 20 | missing: 0 (0.0%) | zeros: 9,980 | negative: 0
- flags: near-constant
- all values (n=20): 0×9980, 16×1, 21×1, 22×1, 28×1, 32×1, 41×1, 43×1, 83×1, 108×1, 110×1, 162×1, 167×1, 170×1, 186×1, 212×1, 214×1, 232×1, 243×1, 253×1

#### `0.40`  (`int64`)
- unique: 21 | missing: 0 (0.0%) | zeros: 9,979 | negative: 0
- flags: near-constant
- all values (n=21): 0×9979, 5×1, 6×1, 32×1, 39×1, 69×1, 76×1, 131×1, 150×1, 151×1, 170×1, 178×1, 204×1, 217×1, 220×1, 225×1, 229×1, 239×1, 243×1, 249×1, 255×1

#### `0.41`  (`int64`)
- unique: 20 | missing: 0 (0.0%) | zeros: 9,976 | negative: 0
- flags: near-constant
- all values (n=20): 0×9976, 2×1, 3×1, 13×2, 19×1, 23×1, 29×2, 41×1, 92×1, 100×1, 128×1, 139×1, 148×1, 154×1, 159×1, 163×1, 174×1, 235×2, 253×2, 255×1

#### `0.42`  (`int64`)
- unique: 17 | missing: 0 (0.0%) | zeros: 9,981 | negative: 0
- flags: near-constant
- all values (n=17): 0×9981, 20×1, 42×1, 64×1, 110×1, 114×1, 157×1, 161×1, 164×1, 167×1, 181×1, 193×1, 223×1, 231×1, 236×1, 254×2, 255×2

#### `0.43`  (`int64`)
- unique: 16 | missing: 0 (0.0%) | zeros: 9,983 | negative: 0
- flags: near-constant
- all values (n=16): 0×9983, 6×1, 11×1, 27×1, 84×1, 85×1, 107×1, 137×1, 142×1, 161×1, 169×1, 170×1, 228×1, 253×1, 254×2, 255×1

#### `0.44`  (`int64`)
- unique: 11 | missing: 0 (0.0%) | zeros: 9,989 | negative: 0
- flags: near-constant
- all values (n=11): 0×9989, 14×1, 32×1, 36×1, 47×1, 50×1, 54×1, 63×1, 86×1, 118×1, 191×1

#### `0.45`  (`int64`)
- unique: 7 | missing: 0 (0.0%) | zeros: 9,993 | negative: 0
- flags: near-constant
- all values (n=7): 0×9993, 2×1, 71×1, 145×1, 180×1, 246×1, 253×1

#### `0.46`  (`int64`)
- unique: 7 | missing: 0 (0.0%) | zeros: 9,993 | negative: 0
- flags: near-constant
- all values (n=7): 0×9993, 45×1, 50×1, 173×1, 207×1, 211×1, 254×1

#### `0.47`  (`int64`)
- unique: 4 | missing: 0 (0.0%) | zeros: 9,996 | negative: 0
- flags: near-constant
- all values (n=4): 0×9996, 13×1, 235×1, 254×1

#### `0.48`  (`int64`)
- unique: 3 | missing: 0 (0.0%) | zeros: 9,997 | negative: 0
- flags: near-constant
- all values (n=3): 0×9997, 34×1, 158×1

#### `0.49`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.50`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.51`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.52`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.53`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.54`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.55`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.56`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.57`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.58`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.59`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.60`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.61`  (`int64`)
- unique: 5 | missing: 0 (0.0%) | zeros: 9,995 | negative: 0
- flags: near-constant
- all values (n=5): 0×9995, 50×1, 67×1, 128×1, 192×1

#### `0.62`  (`int64`)
- unique: 7 | missing: 0 (0.0%) | zeros: 9,992 | negative: 0
- flags: near-constant
- all values (n=7): 0×9992, 16×1, 45×1, 168×1, 187×1, 191×1, 254×2

#### `0.63`  (`int64`)
- unique: 14 | missing: 0 (0.0%) | zeros: 9,986 | negative: 0
- flags: near-constant
- all values (n=14): 0×9986, 5×1, 22×1, 32×1, 40×1, 59×1, 81×1, 91×1, 128×1, 177×1, 190×1, 199×1, 213×1, 216×1

#### `0.64`  (`int64`)
- unique: 22 | missing: 0 (0.0%) | zeros: 9,972 | negative: 0
- flags: near-constant
- all values (n=22): 0×9972, 1×1, 15×1, 26×1, 27×1, 32×1, 34×3, 35×1, 45×2, 59×1, 62×1, 100×1, 118×1, 128×3, 133×1, 168×1, 178×1, 186×1, 195×1, 251×1, 253×1, 255×2

#### `0.65`  (`int64`)
- unique: 42 | missing: 0 (0.0%) | zeros: 9,947 | negative: 0
- flags: near-constant
- min=0 max=255 mean=0.6073 median=0 std=10.3537
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.66`  (`int64`)
- unique: 72 | missing: 0 (0.0%) | zeros: 9,904 | negative: 0
- flags: near-constant
- min=0 max=255 mean=1.2157 median=0 std=14.9601
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.67`  (`int64`)
- unique: 112 | missing: 0 (0.0%) | zeros: 9,840 | negative: 0
- min=0 max=255 mean=2.1474 median=0 std=20.2592
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=72.02

#### `0.68`  (`int64`)
- unique: 117 | missing: 0 (0.0%) | zeros: 9,784 | negative: 0
- min=0 max=255 mean=2.8169 median=0 std=23.1452
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=142.04

#### `0.69`  (`int64`)
- unique: 146 | missing: 0 (0.0%) | zeros: 9,749 | negative: 0
- min=0 max=255 mean=3.3341 median=0 std=24.7969
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=162.02

#### `0.70`  (`int64`)
- unique: 148 | missing: 0 (0.0%) | zeros: 9,736 | negative: 0
- min=0 max=255 mean=3.8547 median=0 std=27.5815
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=197.02

#### `0.71`  (`int64`)
- unique: 144 | missing: 0 (0.0%) | zeros: 9,727 | negative: 0
- min=0 max=255 mean=3.8546 median=0 std=27.2288
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=192.02

#### `0.72`  (`int64`)
- unique: 143 | missing: 0 (0.0%) | zeros: 9,755 | negative: 0
- min=0 max=255 mean=3.4894 median=0 std=25.8039
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=178.02

#### `0.73`  (`int64`)
- unique: 120 | missing: 0 (0.0%) | zeros: 9,801 | negative: 0
- min=0 max=255 mean=2.7635 median=0 std=22.9817
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=142.02

#### `0.74`  (`int64`)
- unique: 97 | missing: 0 (0.0%) | zeros: 9,850 | negative: 0
- min=0 max=255 mean=2.1146 median=0 std=20.2374
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=85

#### `0.75`  (`int64`)
- unique: 72 | missing: 0 (0.0%) | zeros: 9,894 | negative: 0
- min=0 max=255 mean=1.5364 median=0 std=17.6583
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=5.02

#### `0.76`  (`int64`)
- unique: 53 | missing: 0 (0.0%) | zeros: 9,931 | negative: 0
- flags: near-constant
- min=0 max=255 mean=1.0104 median=0 std=14.098
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.77`  (`int64`)
- unique: 28 | missing: 0 (0.0%) | zeros: 9,965 | negative: 0
- flags: near-constant
- all values (n=28): 0×9965, 18×2, 22×1, 27×1, 29×1, 34×2, 38×1, 44×1, 48×1, 64×1, 71×1, 75×1, 80×1, 89×1, 94×1, 102×1, 134×1, 142×1, 152×1, 184×1, 191×1, 192×1, 199×1, 211×1, 225×1, 253×1, 254×4, 255×3

#### `0.78`  (`int64`)
- unique: 12 | missing: 0 (0.0%) | zeros: 9,986 | negative: 0
- flags: near-constant
- all values (n=12): 0×9986, 9×1, 15×1, 82×1, 159×1, 170×1, 177×1, 180×1, 217×1, 249×1, 254×1, 255×3

#### `0.79`  (`int64`)
- unique: 8 | missing: 0 (0.0%) | zeros: 9,992 | negative: 0
- flags: near-constant
- all values (n=8): 0×9992, 3×1, 35×1, 57×1, 112×1, 171×1, 177×1, 234×1

#### `0.80`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 9,998 | negative: 0
- flags: near-constant
- all values (n=2): 0×9998, 5×1

#### `0.81`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.82`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.83`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.84`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.85`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.86`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.87`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.88`  (`int64`)
- unique: 3 | missing: 0 (0.0%) | zeros: 9,997 | negative: 0
- flags: near-constant
- all values (n=3): 0×9997, 65×1, 139×1

#### `0.89`  (`int64`)
- unique: 10 | missing: 0 (0.0%) | zeros: 9,990 | negative: 0
- flags: near-constant
- all values (n=10): 0×9990, 1×1, 4×1, 9×1, 52×1, 57×1, 114×1, 128×1, 150×1, 217×1

#### `0.90`  (`int64`)
- unique: 22 | missing: 0 (0.0%) | zeros: 9,970 | negative: 0
- flags: near-constant
- all values (n=22): 0×9970, 1×3, 2×2, 7×2, 10×1, 18×1, 28×1, 29×1, 31×2, 32×1, 66×1, 67×1, 79×1, 114×1, 121×1, 122×1, 128×1, 146×2, 161×1, 225×1, 253×1, 255×3

#### `0.91`  (`int64`)
- unique: 53 | missing: 0 (0.0%) | zeros: 9,937 | negative: 0
- flags: near-constant
- min=0 max=255 mean=0.5676 median=0 std=9.4876
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.92`  (`int64`)
- unique: 81 | missing: 0 (0.0%) | zeros: 9,890 | negative: 0
- min=0 max=255 mean=1.2866 median=0 std=15.2804
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=10

#### `0.93`  (`int64`)
- unique: 134 | missing: 0 (0.0%) | zeros: 9,791 | negative: 0
- min=0 max=255 mean=2.5981 median=0 std=21.9448
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=123.08

#### `0.94`  (`int64`)
- unique: 152 | missing: 0 (0.0%) | zeros: 9,675 | negative: 0
- min=0 max=255 mean=4.6365 median=0 std=30.0548
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=228.02

#### `0.95`  (`int64`)
- unique: 188 | missing: 0 (0.0%) | zeros: 9,530 | negative: 0
- min=0 max=255 mean=6.9002 median=0 std=36.648
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=253

#### `0.96`  (`int64`)
- unique: 206 | missing: 0 (0.0%) | zeros: 9,385 | negative: 0
- min=0 max=255 mean=9.3806 median=0 std=42.6774
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=44 p99=253

#### `0.97`  (`int64`)
- unique: 203 | missing: 0 (0.0%) | zeros: 9,287 | negative: 0
- min=0 max=255 mean=11.4625 median=0 std=47.1832
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=107 p99=253

#### `0.98`  (`int64`)
- unique: 231 | missing: 0 (0.0%) | zeros: 9,209 | negative: 0
- min=0 max=255 mean=12.6115 median=0 std=49.4526
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=127 p99=254

#### `0.99`  (`int64`)
- unique: 226 | missing: 0 (0.0%) | zeros: 9,165 | negative: 0
- min=0 max=255 mean=13.1891 median=0 std=50.8286
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=132 p99=254

#### `0.100`  (`int64`)
- unique: 222 | missing: 0 (0.0%) | zeros: 9,230 | negative: 0
- min=0 max=255 mean=12.0641 median=0 std=48.3715
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=122.1 p99=254

#### `0.101`  (`int64`)
- unique: 212 | missing: 0 (0.0%) | zeros: 9,329 | negative: 0
- min=0 max=255 mean=9.9028 median=0 std=43.677
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=64 p99=253

#### `0.102`  (`int64`)
- unique: 197 | missing: 0 (0.0%) | zeros: 9,471 | negative: 0
- min=0 max=255 mean=7.8468 median=0 std=39.1518
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=10 p99=253

#### `0.103`  (`int64`)
- unique: 166 | missing: 0 (0.0%) | zeros: 9,631 | negative: 0
- min=0 max=255 mean=5.5463 median=0 std=33.179
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=244.02

#### `0.104`  (`int64`)
- unique: 134 | missing: 0 (0.0%) | zeros: 9,751 | negative: 0
- min=0 max=255 mean=3.4418 median=0 std=25.6248
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=169.02

#### `0.105`  (`int64`)
- unique: 90 | missing: 0 (0.0%) | zeros: 9,867 | negative: 0
- min=0 max=255 mean=1.8194 median=0 std=18.9772
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=38.02

#### `0.106`  (`int64`)
- unique: 62 | missing: 0 (0.0%) | zeros: 9,920 | negative: 0
- flags: near-constant
- min=0 max=255 mean=1.0549 median=0 std=14.322
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.107`  (`int64`)
- unique: 38 | missing: 0 (0.0%) | zeros: 9,958 | negative: 0
- flags: near-constant
- min=0 max=254 mean=0.4305 median=0 std=8.5428
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.108`  (`int64`)
- unique: 13 | missing: 0 (0.0%) | zeros: 9,986 | negative: 0
- flags: near-constant
- all values (n=13): 0×9986, 2×1, 3×1, 27×1, 36×1, 48×2, 64×1, 80×1, 109×1, 163×1, 241×1, 254×1, 255×1

#### `0.109`  (`int64`)
- unique: 5 | missing: 0 (0.0%) | zeros: 9,995 | negative: 0
- flags: near-constant
- all values (n=5): 0×9995, 58×1, 63×1, 96×1, 234×1

#### `0.110`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 9,998 | negative: 0
- flags: near-constant
- all values (n=2): 0×9998, 163×1

#### `0.111`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.112`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.113`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.114`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.115`  (`int64`)
- unique: 5 | missing: 0 (0.0%) | zeros: 9,994 | negative: 0
- flags: near-constant
- all values (n=5): 0×9994, 1×1, 9×2, 55×1, 114×1

#### `0.116`  (`int64`)
- unique: 13 | missing: 0 (0.0%) | zeros: 9,986 | negative: 0
- flags: near-constant
- all values (n=13): 0×9986, 1×1, 4×2, 6×1, 7×1, 19×1, 47×1, 66×1, 103×1, 159×1, 201×1, 202×1, 206×1

#### `0.117`  (`int64`)
- unique: 27 | missing: 0 (0.0%) | zeros: 9,968 | negative: 0
- flags: near-constant
- all values (n=27): 0×9968, 3×1, 4×1, 5×2, 7×3, 13×1, 14×1, 15×2, 16×1, 21×2, 28×1, 29×1, 32×1, 45×1, 57×1, 86×1, 88×1, 103×1, 113×1, 117×1, 122×1, 144×1, 165×1, 168×1, 221×1, 231×1, 255×1

#### `0.118`  (`int64`)
- unique: 83 | missing: 0 (0.0%) | zeros: 9,885 | negative: 0
- min=0 max=254 mean=0.9783 median=0 std=12.4415
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=7

#### `0.119`  (`int64`)
- unique: 122 | missing: 0 (0.0%) | zeros: 9,762 | negative: 0
- min=0 max=255 mean=2.529 median=0 std=21.1462
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=99.02

#### `0.120`  (`int64`)
- unique: 168 | missing: 0 (0.0%) | zeros: 9,581 | negative: 0
- min=0 max=255 mean=5.0396 median=0 std=30.4132
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=221.08

#### `0.121`  (`int64`)
- unique: 211 | missing: 0 (0.0%) | zeros: 9,286 | negative: 0
- min=0 max=255 mean=9.4444 median=0 std=41.2755
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=68 p99=253

#### `0.122`  (`int64`)
- unique: 236 | missing: 0 (0.0%) | zeros: 8,928 | negative: 0
- min=0 max=255 mean=15.3823 median=0 std=53.2959
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=156 p99=254

#### `0.123`  (`int64`)
- unique: 249 | missing: 0 (0.0%) | zeros: 8,438 | negative: 0
- min=0 max=255 mean=23.045 median=0 std=65.0083
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=233 p99=254

#### `0.124`  (`int64`)
- unique: 252 | missing: 0 (0.0%) | zeros: 8,025 | negative: 0
- min=0 max=255 mean=31.0166 median=0 std=73.6484
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=252 p99=254

#### `0.125`  (`int64`)
- unique: 251 | missing: 0 (0.0%) | zeros: 7,576 | negative: 0
- min=0 max=255 mean=38.9409 median=0 std=81.0848
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=253 p99=255

#### `0.126`  (`int64`)
- unique: 252 | missing: 0 (0.0%) | zeros: 7,286 | negative: 0
- min=0 max=255 mean=45.7366 median=0 std=86.7748
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=28 p95=253 p99=255

#### `0.127`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 7,162 | negative: 0
- min=0 max=255 mean=47.9742 median=0 std=88.7072
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=38 p95=254 p99=255

#### `0.128`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 7,278 | negative: 0
- min=0 max=255 mean=44.8108 median=0 std=85.944
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=23.5 p95=253 p99=255

#### `0.129`  (`int64`)
- unique: 255 | missing: 0 (0.0%) | zeros: 7,569 | negative: 0
- min=0 max=255 mean=37.8008 median=0 std=79.6726
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=253 p99=255

#### `0.130`  (`int64`)
- unique: 252 | missing: 0 (0.0%) | zeros: 8,042 | negative: 0
- min=0 max=255 mean=28.5547 median=0 std=70.6883
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=251 p99=255

#### `0.131`  (`int64`)
- unique: 243 | missing: 0 (0.0%) | zeros: 8,573 | negative: 0
- min=0 max=255 mean=20.7006 median=0 std=61.5039
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=213 p99=255

#### `0.132`  (`int64`)
- unique: 233 | missing: 0 (0.0%) | zeros: 9,033 | negative: 0
- min=0 max=255 mean=13.6112 median=0 std=50.1181
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=133 p99=254

#### `0.133`  (`int64`)
- unique: 210 | missing: 0 (0.0%) | zeros: 9,410 | negative: 0
- min=0 max=255 mean=7.9209 median=0 std=38.3267
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=21 p99=252

#### `0.134`  (`int64`)
- unique: 164 | missing: 0 (0.0%) | zeros: 9,651 | negative: 0
- min=0 max=255 mean=4.3927 median=0 std=28.4246
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=197

#### `0.135`  (`int64`)
- unique: 122 | missing: 0 (0.0%) | zeros: 9,815 | negative: 0
- min=0 max=255 mean=2.1196 median=0 std=19.4716
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=92.04

#### `0.136`  (`int64`)
- unique: 62 | missing: 0 (0.0%) | zeros: 9,924 | negative: 0
- flags: near-constant
- min=0 max=255 mean=0.7951 median=0 std=11.7339
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.137`  (`int64`)
- unique: 17 | missing: 0 (0.0%) | zeros: 9,980 | negative: 0
- flags: near-constant
- all values (n=17): 0×9980, 9×1, 14×2, 31×2, 38×2, 44×1, 49×1, 81×1, 106×1, 112×1, 153×1, 159×1, 177×1, 210×1, 238×1, 254×1, 255×1

#### `0.138`  (`int64`)
- unique: 8 | missing: 0 (0.0%) | zeros: 9,992 | negative: 0
- flags: near-constant
- all values (n=8): 0×9992, 31×1, 37×1, 54×1, 76×1, 152×1, 230×1, 246×1

#### `0.139`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.140`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.141`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 9,998 | negative: 0
- flags: near-constant
- all values (n=2): 0×9998, 24×1

#### `0.142`  (`int64`)
- unique: 3 | missing: 0 (0.0%) | zeros: 9,997 | negative: 0
- flags: near-constant
- all values (n=3): 0×9997, 1×1, 13×1

#### `0.143`  (`int64`)
- unique: 13 | missing: 0 (0.0%) | zeros: 9,986 | negative: 0
- flags: near-constant
- all values (n=13): 0×9986, 4×1, 5×2, 8×1, 9×1, 10×1, 11×1, 23×1, 28×1, 40×1, 57×1, 75×1, 80×1

#### `0.144`  (`int64`)
- unique: 47 | missing: 0 (0.0%) | zeros: 9,944 | negative: 0
- flags: near-constant
- min=0 max=254 mean=0.4779 median=0 std=8.3762
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.145`  (`int64`)
- unique: 93 | missing: 0 (0.0%) | zeros: 9,863 | negative: 0
- min=0 max=255 mean=1.4315 median=0 std=15.6559
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=33.02

#### `0.146`  (`int64`)
- unique: 148 | missing: 0 (0.0%) | zeros: 9,685 | negative: 0
- min=0 max=255 mean=3.6429 median=0 std=25.4745
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=162

#### `0.147`  (`int64`)
- unique: 195 | missing: 0 (0.0%) | zeros: 9,436 | negative: 0
- min=0 max=255 mean=7.297 median=0 std=36.6673
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=13 p99=248

#### `0.148`  (`int64`)
- unique: 229 | missing: 0 (0.0%) | zeros: 9,015 | negative: 0
- min=0 max=255 mean=13.1477 median=0 std=49.4209
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=125 p99=253

#### `0.149`  (`int64`)
- unique: 248 | missing: 0 (0.0%) | zeros: 8,433 | negative: 0
- min=0 max=255 mean=22.5657 median=0 std=63.8523
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=227.1 p99=254

#### `0.150`  (`int64`)
- unique: 252 | missing: 0 (0.0%) | zeros: 7,706 | negative: 0
- min=0 max=255 mean=35.1423 median=0 std=78.0496
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=252 p99=254

#### `0.151`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 6,987 | negative: 0
- min=0 max=255 mean=49.5439 median=0 std=89.8174
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=49 p95=253 p99=255

#### `0.152`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 6,250 | negative: 0
- min=0 max=255 mean=63.8272 median=0 std=98.5059
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=131 p95=253 p99=255

#### `0.153`  (`int64`)
- unique: 255 | missing: 0 (0.0%) | zeros: 5,620 | negative: 0
- min=0 max=255 mean=78.0182 median=0 std=104.9772
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=191 p95=254 p99=255

#### `0.154`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 5,189 | negative: 0
- min=0 max=255 mean=88.8999 median=0 std=108.6543
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=222 p95=254 p99=255

#### `0.155`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 4,988 | negative: 0
- min=0 max=255 mean=93.3499 median=2 std=109.681
- quantiles: p1=0 p5=0 p25=0 p50=2 p75=232 p95=254 p99=255

#### `0.156`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 5,077 | negative: 0
- min=0 max=255 mean=90.1996 median=0 std=108.5238
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=223 p95=254 p99=255

#### `0.157`  (`int64`)
- unique: 255 | missing: 0 (0.0%) | zeros: 5,455 | negative: 0
- min=0 max=255 mean=80.3113 median=0 std=105.1489
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=192 p95=254 p99=255

#### `0.158`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 6,083 | negative: 0
- min=0 max=255 mean=64.7679 median=0 std=98.1321
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=132 p95=253 p99=255

#### `0.159`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 6,940 | negative: 0
- min=0 max=255 mean=48.3171 median=0 std=88.2447
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=47 p95=253 p99=255

#### `0.160`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 7,809 | negative: 0
- min=0 max=255 mean=33.269 median=0 std=75.7179
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=252 p99=255

#### `0.161`  (`int64`)
- unique: 245 | missing: 0 (0.0%) | zeros: 8,569 | negative: 0
- min=0 max=255 mean=20.4438 median=0 std=60.9212
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=212.1 p99=254

#### `0.162`  (`int64`)
- unique: 224 | missing: 0 (0.0%) | zeros: 9,120 | negative: 0
- min=0 max=255 mean=12.048 median=0 std=47.2735
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=110 p99=253

#### `0.163`  (`int64`)
- unique: 185 | missing: 0 (0.0%) | zeros: 9,498 | negative: 0
- min=0 max=255 mean=6.2015 median=0 std=33.716
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=1 p99=234

#### `0.164`  (`int64`)
- unique: 137 | missing: 0 (0.0%) | zeros: 9,758 | negative: 0
- min=0 max=255 mean=2.8441 median=0 std=22.4375
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=134.02

#### `0.165`  (`int64`)
- unique: 66 | missing: 0 (0.0%) | zeros: 9,918 | negative: 0
- flags: near-constant
- min=0 max=254 mean=0.7662 median=0 std=10.845
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.166`  (`int64`)
- unique: 21 | missing: 0 (0.0%) | zeros: 9,979 | negative: 0
- flags: near-constant
- all values (n=21): 0×9979, 13×1, 36×1, 54×1, 55×1, 56×1, 67×1, 70×1, 76×1, 91×1, 92×1, 100×1, 104×1, 125×1, 133×1, 151×1, 177×1, 199×1, 213×1, 231×1, 232×1

#### `0.167`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.168`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.169`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.170`  (`int64`)
- unique: 3 | missing: 0 (0.0%) | zeros: 9,997 | negative: 0
- flags: near-constant
- all values (n=3): 0×9997, 13×1, 26×1

#### `0.171`  (`int64`)
- unique: 23 | missing: 0 (0.0%) | zeros: 9,975 | negative: 0
- flags: near-constant
- all values (n=23): 0×9975, 1×1, 4×1, 7×1, 14×1, 15×2, 30×1, 31×1, 48×1, 53×1, 83×1, 122×2, 128×1, 136×1, 139×1, 163×1, 168×1, 172×1, 190×1, 208×1, 222×1, 226×1, 254×1

#### `0.172`  (`int64`)
- unique: 80 | missing: 0 (0.0%) | zeros: 9,881 | negative: 0
- min=0 max=255 mean=1.3554 median=0 std=15.5089
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=25.04

#### `0.173`  (`int64`)
- unique: 143 | missing: 0 (0.0%) | zeros: 9,734 | negative: 0
- min=0 max=255 mean=3.3806 median=0 std=25.3979
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=174.02

#### `0.174`  (`int64`)
- unique: 198 | missing: 0 (0.0%) | zeros: 9,444 | negative: 0
- min=0 max=255 mean=7.182 median=0 std=36.9194
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=13 p99=252

#### `0.175`  (`int64`)
- unique: 239 | missing: 0 (0.0%) | zeros: 8,978 | negative: 0
- min=0 max=255 mean=14.1009 median=0 std=51.3157
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=140 p99=253

#### `0.176`  (`int64`)
- unique: 250 | missing: 0 (0.0%) | zeros: 8,308 | negative: 0
- min=0 max=255 mean=24.6231 median=0 std=66.5688
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=238.1 p99=254

#### `0.177`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 7,458 | negative: 0
- min=0 max=255 mean=39.4433 median=0 std=81.6758
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=4 p95=253 p99=254

#### `0.178`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 6,495 | negative: 0
- min=0 max=255 mean=56.9897 median=0 std=94.1504
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=95 p95=253 p99=255

#### `0.179`  (`int64`)
- unique: 255 | missing: 0 (0.0%) | zeros: 5,471 | negative: 0
- min=0 max=255 mean=76.0466 median=0 std=103.3746
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=180 p95=253 p99=255

#### `0.180`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 4,719 | negative: 0
- min=0 max=255 mean=94.445 median=18 std=108.6146
- quantiles: p1=0 p5=0 p25=0 p50=18 p75=230 p95=254 p99=255

#### `0.181`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 4,066 | negative: 0
- min=0 max=255 mean=110.2932 median=71 std=111.4508
- quantiles: p1=0 p5=0 p25=0 p50=71 p75=251 p95=254 p99=255

#### `0.182`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 3,645 | negative: 0
- min=0 max=255 mean=122.435 median=122 std=112.1827
- quantiles: p1=0 p5=0 p25=0 p50=122 p75=252 p95=254 p99=255

#### `0.183`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 3,518 | negative: 0
- min=0 max=255 mean=127.3024 median=139 std=112.4677
- quantiles: p1=0 p5=0 p25=0 p50=139 p75=252 p95=254 p99=255

#### `0.184`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 3,623 | negative: 0
- min=0 max=255 mean=122.6923 median=122 std=112.1349
- quantiles: p1=0 p5=0 p25=0 p50=122 p75=252 p95=254 p99=255

#### `0.185`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 4,031 | negative: 0
- min=0 max=255 mean=111.9081 median=76 std=112.3098
- quantiles: p1=0 p5=0 p25=0 p50=76 p75=252 p95=254 p99=255

#### `0.186`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 4,711 | negative: 0
- min=0 max=255 mean=95.1309 median=15 std=109.4951
- quantiles: p1=0 p5=0 p25=0 p50=15 p75=233 p95=254 p99=255

#### `0.187`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 5,687 | negative: 0
- min=0 max=255 mean=73.7067 median=0 std=102.6845
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=170 p95=253 p99=255

#### `0.188`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 6,811 | negative: 0
- min=0 max=255 mean=52.5627 median=0 std=92.1088
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=64 p95=253 p99=255

#### `0.189`  (`int64`)
- unique: 254 | missing: 0 (0.0%) | zeros: 7,811 | negative: 0
- min=0 max=255 mean=33.4776 median=0 std=76.2543
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=252 p99=254

#### `0.190`  (`int64`)
- unique: 249 | missing: 0 (0.0%) | zeros: 8,642 | negative: 0
- min=0 max=255 mean=19.6753 median=0 std=60.1891
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=209 p99=254

#### `0.191`  (`int64`)
- unique: 217 | missing: 0 (0.0%) | zeros: 9,213 | negative: 0
- min=0 max=255 mean=10.2504 median=0 std=43.4459
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=75 p99=253

#### `0.192`  (`int64`)
- unique: 180 | missing: 0 (0.0%) | zeros: 9,601 | negative: 0
- min=0 max=255 mean=5.2557 median=0 std=31.3404
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=222.02

#### `0.193`  (`int64`)
- unique: 101 | missing: 0 (0.0%) | zeros: 9,853 | negative: 0
- min=0 max=255 mean=1.7222 median=0 std=17.3065
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=54.02

#### `0.194`  (`int64`)
- unique: 30 | missing: 0 (0.0%) | zeros: 9,965 | negative: 0
- flags: near-constant
- all values (n=30): 0×9965, 5×1, 7×1, 22×3, 24×1, 28×1, 31×1, 46×1, 55×1, 61×1, 63×1, 65×1, 67×1, 94×1, 100×1, 111×1, 112×1, 113×1, 128×2, 143×1, 152×1, 170×1, 172×1, 191×1, 196×1, 224×1, 237×1, 247×1, 251×1, 253×3

#### `0.195`  (`int64`)
- unique: 5 | missing: 0 (0.0%) | zeros: 9,995 | negative: 0
- flags: near-constant
- all values (n=5): 0×9995, 61×1, 79×1, 85×1, 152×1

#### `0.196`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.197`  (`int64`)
- unique: 3 | missing: 0 (0.0%) | zeros: 9,997 | negative: 0
- flags: near-constant
- all values (n=3): 0×9997, 25×1, 128×1

#### `0.198`  (`int64`)
- unique: 14 | missing: 0 (0.0%) | zeros: 9,986 | negative: 0
- flags: near-constant
- all values (n=14): 0×9986, 3×1, 10×1, 20×1, 21×1, 47×1, 58×1, 64×1, 123×1, 125×1, 138×1, 174×1, 189×1, 191×1

#### `0.199`  (`int64`)
- unique: 53 | missing: 0 (0.0%) | zeros: 9,938 | negative: 0
- flags: near-constant
- min=0 max=255 mean=0.7319 median=0 std=11.32
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.200`  (`int64`)
- unique: 125 | missing: 0 (0.0%) | zeros: 9,793 | negative: 0
- min=0 max=255 mean=2.6584 median=0 std=22.3473
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=124.02

#### `0.201`  (`int64`)
- unique: 166 | missing: 0 (0.0%) | zeros: 9,553 | negative: 0
- min=0 max=255 mean=6.0119 median=0 std=33.8055
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=249.02

#### `84`  (`int64`)
- unique: 228 | missing: 0 (0.0%) | zeros: 9,134 | negative: 0
- min=0 max=255 mean=11.8474 median=0 std=46.909
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=106.1 p99=253

#### `185`  (`int64`)
- unique: 249 | missing: 0 (0.0%) | zeros: 8,461 | negative: 0
- min=0 max=255 mean=22.1495 median=0 std=63.3016
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=224 p99=254

#### `159`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 7,486 | negative: 0
- min=0 max=255 mean=37.4935 median=0 std=79.2968
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=1 p95=252 p99=254

#### `151`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 6,375 | negative: 0
- min=0 max=255 mean=57.0685 median=0 std=93.5598
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=94 p95=253 p99=255

#### `60`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 5,184 | negative: 0
- min=0 max=255 mean=78.5112 median=0 std=103.209
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=185 p95=253 p99=255

#### `36`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 4,205 | negative: 0
- min=0 max=255 mean=99.961 median=43 std=108.0891
- quantiles: p1=0 p5=0 p25=0 p50=43 p75=233 p95=254 p99=255

#### `0.202`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 3,575 | negative: 0
- min=0 max=255 mean=116.4303 median=98 std=110.5917
- quantiles: p1=0 p5=0 p25=0 p50=98 p75=252 p95=254 p99=255

#### `0.203`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 3,189 | negative: 0
- min=0 max=255 mean=127.9943 median=133 std=110.9267
- quantiles: p1=0 p5=0 p25=0 p50=133 p75=252 p95=254 p99=255

#### `0.204`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 2,939 | negative: 0
- min=0 max=255 mean=135.0903 median=155 std=110.5919
- quantiles: p1=0 p5=0 p25=0 p50=155 p75=253 p95=254 p99=255

#### `0.205`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 2,858 | negative: 0
- min=0 max=255 mean=136.6448 median=161 std=110.2943
- quantiles: p1=0 p5=0 p25=0 p50=161 p75=253 p95=254 p99=255

#### `0.206`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 2,930 | negative: 0
- min=0 max=255 mean=133.4454 median=151 std=109.9851
- quantiles: p1=0 p5=0 p25=0 p50=151 p75=252 p95=254 p99=255

#### `0.207`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 3,188 | negative: 0
- min=0 max=255 mean=126.597 median=130 std=110.7485
- quantiles: p1=0 p5=0 p25=0 p50=130 p75=252 p95=254 p99=255

#### `0.208`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 3,768 | negative: 0
- min=0 max=255 mean=113.2448 median=85 std=110.9986
- quantiles: p1=0 p5=0 p25=0 p50=85 p75=252 p95=254 p99=255

#### `0.209`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 4,753 | negative: 0
- min=0 max=255 mean=92.9967 median=15 std=108.4977
- quantiles: p1=0 p5=0 p25=0 p50=15 p75=228 p95=254 p99=255

#### `0.210`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 5,968 | negative: 0
- min=0 max=255 mean=67.6828 median=0 std=100.0156
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=142 p95=253 p99=255

#### `0.211`  (`int64`)
- unique: 255 | missing: 0 (0.0%) | zeros: 7,218 | negative: 0
- min=0 max=255 mean=44.4236 median=0 std=86.0573
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=22 p95=253 p99=255

#### `0.212`  (`int64`)
- unique: 255 | missing: 0 (0.0%) | zeros: 8,232 | negative: 0
- min=0 max=255 mean=25.6086 median=0 std=67.5171
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=241 p99=254

#### `0.213`  (`int64`)
- unique: 238 | missing: 0 (0.0%) | zeros: 9,020 | negative: 0
- min=0 max=255 mean=13.7272 median=0 std=50.5785
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=139 p99=253

#### `0.214`  (`int64`)
- unique: 200 | missing: 0 (0.0%) | zeros: 9,493 | negative: 0
- min=0 max=255 mean=6.62 median=0 std=34.8539
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=2 p99=235.04

#### `0.215`  (`int64`)
- unique: 130 | missing: 0 (0.0%) | zeros: 9,788 | negative: 0
- min=0 max=255 mean=2.5387 median=0 std=21.1659
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=124

#### `0.216`  (`int64`)
- unique: 45 | missing: 0 (0.0%) | zeros: 9,946 | negative: 0
- flags: near-constant
- min=0 max=255 mean=0.526 median=0 std=9.4538
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.217`  (`int64`)
- unique: 4 | missing: 0 (0.0%) | zeros: 9,994 | negative: 0
- flags: near-constant
- all values (n=4): 0×9994, 3×3, 130×1, 146×1

#### `0.218`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 9,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×9999

#### `0.219`  (`int64`)
- unique: 9 | missing: 0 (0.0%) | zeros: 9,990 | negative: 0
- flags: near-constant
- all values (n=9): 0×9990, 19×1, 22×2, 28×1, 36×1, 37×1, 80×1, 157×1, 255×1

#### `0.220`  (`int64`)
- unique: 27 | missing: 0 (0.0%) | zeros: 9,971 | negative: 0
- flags: near-constant
- all values (n=27): 0×9971, 3×1, 4×1, 8×1, 9×1, 25×1, 48×2, 70×1, 71×1, 75×1, 79×1, 98×1, 101×1, 104×1, 111×1, 128×1, 133×1, 134×1, 147×1, 222×1, 225×1, 230×1, 231×1, 233×1, 249×1, 253×1, 255×2

#### `0.221`  (`int64`)
- unique: 69 | missing: 0 (0.0%) | zeros: 9,900 | negative: 0
- flags: near-constant
- min=0 max=255 mean=1.2061 median=0 std=14.9133
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.222`  (`int64`)
- unique: 138 | missing: 0 (0.0%) | zeros: 9,715 | negative: 0
- min=0 max=255 mean=3.7196 median=0 std=26.476
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=189.02

#### `0.223`  (`int64`)
- unique: 195 | missing: 0 (0.0%) | zeros: 9,413 | negative: 0
- min=0 max=255 mean=8.2276 median=0 std=39.6131
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=26 p99=252

#### `222`  (`int64`)
- unique: 240 | missing: 0 (0.0%) | zeros: 8,908 | negative: 0
- min=0 max=255 mean=15.8658 median=0 std=54.5695
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=165 p99=253

#### `254`  (`int64`)
- unique: 250 | missing: 0 (0.0%) | zeros: 8,028 | negative: 0
- min=0 max=255 mean=28.9839 median=0 std=71.6183
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=251 p99=254

#### `254.1`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 6,875 | negative: 0
- min=0 max=255 mean=49.3708 median=0 std=89.358
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=50 p95=253 p99=254

#### `254.2`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 5,593 | negative: 0
- min=0 max=255 mean=73.6785 median=0 std=102.3655
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=170 p95=253 p99=255

#### `254.3`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 4,393 | negative: 0
- min=0 max=255 mean=98.0196 median=32 std=108.9248
- quantiles: p1=0 p5=0 p25=0 p50=32 p75=234 p95=254 p99=255

#### `241`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 3,768 | negative: 0
- min=0 max=255 mean=114.6056 median=86 std=111.7165
- quantiles: p1=0 p5=0 p25=0 p50=86 p75=252 p95=254 p99=255

#### `198`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 3,513 | negative: 0
- min=0 max=255 mean=121.9957 median=117 std=111.9059
- quantiles: p1=0 p5=0 p25=0 p50=117 p75=252 p95=254 p99=255

#### `198.1`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 3,435 | negative: 0
- min=0 max=255 mean=123.4612 median=121 std=112.0042
- quantiles: p1=0 p5=0 p25=0 p50=121 p75=252 p95=254 p99=255

#### `198.2`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 3,451 | negative: 0
- min=0 max=255 mean=123.2741 median=118 std=112.1912
- quantiles: p1=0 p5=0 p25=0 p50=118 p75=252 p95=254 p99=255

#### `198.3`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 3,393 | negative: 0
- min=0 max=255 mean=122.3812 median=117 std=111.0904
- quantiles: p1=0 p5=0 p25=0 p50=117 p75=252 p95=254 p99=255

#### `198.4`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 3,290 | negative: 0
- min=0 max=255 mean=123.0889 median=121 std=110.5991
- quantiles: p1=0 p5=0 p25=0 p50=121 p75=252 p95=254 p99=255

#### `198.5`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 3,330 | negative: 0
- min=0 max=255 mean=123.9638 median=125 std=111.2451
- quantiles: p1=0 p5=0 p25=0 p50=125 p75=252 p95=254 p99=255

#### `198.6`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 3,681 | negative: 0
- min=0 max=255 mean=117.5201 median=102 std=111.5671
- quantiles: p1=0 p5=0 p25=0 p50=102 p75=252 p95=254 p99=255

#### `198.7`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 4,459 | negative: 0
- min=0 max=255 mean=100.5363 median=36 std=110.291
- quantiles: p1=0 p5=0 p25=0 p50=36 p75=240 p95=254 p99=255

#### `170`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 5,660 | negative: 0
- min=0 max=255 mean=75.0332 median=0 std=103.4996
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=180 p95=253 p99=255

#### `52`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 6,967 | negative: 0
- min=0 max=255 mean=49.458 median=0 std=89.9676
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=49 p95=253 p99=255

#### `0.224`  (`int64`)
- unique: 252 | missing: 0 (0.0%) | zeros: 8,099 | negative: 0
- min=0 max=255 mean=28.8176 median=0 std=71.8632
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=252 p99=254

#### `0.225`  (`int64`)
- unique: 235 | missing: 0 (0.0%) | zeros: 8,933 | negative: 0
- min=0 max=255 mean=14.7878 median=0 std=52.235
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=147.1 p99=253

#### `0.226`  (`int64`)
- unique: 198 | missing: 0 (0.0%) | zeros: 9,458 | negative: 0
- min=0 max=255 mean=6.9682 median=0 std=35.7652
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=8.1 p99=239.02

#### `0.227`  (`int64`)
- unique: 128 | missing: 0 (0.0%) | zeros: 9,793 | negative: 0
- min=0 max=255 mean=2.8098 median=0 std=22.8298
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=143

#### `0.228`  (`int64`)
- unique: 59 | missing: 0 (0.0%) | zeros: 9,935 | negative: 0
- flags: near-constant
- min=0 max=248 mean=0.7285 median=0 std=10.9359
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.229`  (`int64`)
- unique: 7 | missing: 0 (0.0%) | zeros: 9,993 | negative: 0
- flags: near-constant
- all values (n=7): 0×9993, 1×1, 14×1, 20×1, 26×1, 190×1, 211×1

#### `0.230`  (`int64`)
- unique: 3 | missing: 0 (0.0%) | zeros: 9,997 | negative: 0
- flags: near-constant
- all values (n=3): 0×9997, 19×1, 140×1

#### `0.231`  (`int64`)
- unique: 13 | missing: 0 (0.0%) | zeros: 9,987 | negative: 0
- flags: near-constant
- all values (n=13): 0×9987, 11×1, 13×1, 36×1, 47×1, 128×1, 145×1, 146×1, 159×1, 191×1, 221×1, 230×1, 247×1

#### `0.232`  (`int64`)
- unique: 26 | missing: 0 (0.0%) | zeros: 9,967 | negative: 0
- flags: near-constant
- all values (n=26): 0×9967, 2×1, 10×1, 13×1, 16×1, 20×1, 25×1, 39×1, 45×1, 64×1, 96×1, 112×1, 113×1, 133×1, 141×1, 155×1, 161×1, 181×1, 197×1, 198×1, 203×1, 212×1, 247×1, 253×4, 254×3, 255×3

#### `0.233`  (`int64`)
- unique: 83 | missing: 0 (0.0%) | zeros: 9,874 | negative: 0
- min=0 max=255 mean=1.6614 median=0 std=17.83
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=38.04

#### `0.234`  (`int64`)
- unique: 144 | missing: 0 (0.0%) | zeros: 9,702 | negative: 0
- min=0 max=255 mean=4.2667 median=0 std=29.0881
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=222.06

#### `0.235`  (`int64`)
- unique: 204 | missing: 0 (0.0%) | zeros: 9,364 | negative: 0
- min=0 max=255 mean=9.2181 median=0 std=42.2614
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=45.2 p99=253

#### `67`  (`int64`)
- unique: 240 | missing: 0 (0.0%) | zeros: 8,745 | negative: 0
- min=0 max=255 mean=18.2849 median=0 std=58.6583
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=202 p99=253

#### `114`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 7,773 | negative: 0
- min=0 max=255 mean=33.7067 median=0 std=76.6658
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=252 p99=254

#### `72`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 6,404 | negative: 0
- min=0 max=255 mean=58.0073 median=0 std=95.1321
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=93.5 p95=253 p99=255

#### `114.1`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 5,069 | negative: 0
- min=0 max=255 mean=86.2104 median=0 std=107.0125
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=213 p95=254 p99=255

#### `163`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 4,144 | negative: 0
- min=0 max=255 mean=107.7781 median=58 std=111.405
- quantiles: p1=0 p5=0 p25=0 p50=58 p75=248 p95=254 p99=255

#### `227`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 3,847 | negative: 0
- min=0 max=255 mean=114.8359 median=87 std=112.276
- quantiles: p1=0 p5=0 p25=0 p50=87 p75=252 p95=254 p99=255

#### `254.4`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 3,998 | negative: 0
- min=0 max=255 mean=109.9506 median=70 std=111.1956
- quantiles: p1=0 p5=0 p25=0 p50=70 p75=249 p95=254 p99=255

#### `225`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 4,211 | negative: 0
- min=0 max=255 mean=101.7437 median=42 std=109.8425
- quantiles: p1=0 p5=0 p25=0 p50=42 p75=242 p95=254 p99=255

#### `254.5`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 4,423 | negative: 0
- min=0 max=255 mean=98.6924 median=31 std=109.7252
- quantiles: p1=0 p5=0 p25=0 p50=31 p75=239 p95=254 p99=255

#### `254.6`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 4,243 | negative: 0
- min=0 max=255 mean=99.2934 median=39 std=108.4792
- quantiles: p1=0 p5=0 p25=0 p50=39 p75=233 p95=254 p99=255

#### `254.7`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 3,951 | negative: 0
- min=0 max=255 mean=105.0361 median=58 std=109.1878
- quantiles: p1=0 p5=0 p25=0 p50=58 p75=241 p95=254 p99=255

#### `250`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 3,767 | negative: 0
- min=0 max=255 mean=113.4697 median=84 std=111.1677
- quantiles: p1=0 p5=0 p25=0 p50=84 p75=252 p95=254 p99=255

#### `229`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 3,897 | negative: 0
- min=0 max=255 mean=113.1504 median=79 std=112.0389
- quantiles: p1=0 p5=0 p25=0 p50=79 p75=252 p95=254 p99=255

#### `254.8`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 4,546 | negative: 0
- min=0 max=255 mean=98.7131 median=29 std=110.22
- quantiles: p1=0 p5=0 p25=0 p50=29 p75=240 p95=254 p99=255

#### `254.9`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 5,743 | negative: 0
- min=0 max=255 mean=74.6371 median=0 std=103.5626
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=178 p95=254 p99=255

#### `140`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 7,034 | negative: 0
- min=0 max=255 mean=49.3926 median=0 std=90.3678
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=46 p95=253 p99=255

#### `0.236`  (`int64`)
- unique: 252 | missing: 0 (0.0%) | zeros: 8,128 | negative: 0
- min=0 max=255 mean=28.9751 median=0 std=72.1084
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=252 p99=254

#### `0.237`  (`int64`)
- unique: 235 | missing: 0 (0.0%) | zeros: 8,992 | negative: 0
- min=0 max=255 mean=14.321 median=0 std=52.067
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=140.1 p99=253

#### `0.238`  (`int64`)
- unique: 195 | missing: 0 (0.0%) | zeros: 9,523 | negative: 0
- min=0 max=255 mean=6.017 median=0 std=33.1125
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=236

#### `0.239`  (`int64`)
- unique: 107 | missing: 0 (0.0%) | zeros: 9,838 | negative: 0
- min=0 max=255 mean=2.0407 median=0 std=18.9714
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=86.04

#### `0.240`  (`int64`)
- unique: 49 | missing: 0 (0.0%) | zeros: 9,946 | negative: 0
- flags: near-constant
- min=0 max=254 mean=0.5271 median=0 std=9.3112
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.241`  (`int64`)
- unique: 8 | missing: 0 (0.0%) | zeros: 9,992 | negative: 0
- flags: near-constant
- all values (n=8): 0×9992, 5×1, 18×1, 26×1, 33×1, 83×1, 168×1, 219×1

#### `0.242`  (`int64`)
- unique: 3 | missing: 0 (0.0%) | zeros: 9,997 | negative: 0
- flags: near-constant
- all values (n=3): 0×9997, 57×1, 226×1

#### `0.243`  (`int64`)
- unique: 10 | missing: 0 (0.0%) | zeros: 9,990 | negative: 0
- flags: near-constant
- all values (n=10): 0×9990, 2×1, 22×1, 44×1, 81×1, 101×1, 209×1, 217×1, 233×1, 255×1

#### `0.244`  (`int64`)
- unique: 30 | missing: 0 (0.0%) | zeros: 9,966 | negative: 0
- flags: near-constant
- all values (n=30): 0×9966, 7×1, 9×1, 13×1, 23×1, 39×1, 42×1, 44×1, 62×1, 63×1, 91×1, 113×1, 114×1, 133×2, 135×1, 139×1, 141×1, 150×1, 169×1, 177×1, 178×1, 182×1, 191×1, 194×1, 199×2, 216×1, 227×1, 231×1, 253×3, 254×1

#### `0.245`  (`int64`)
- unique: 79 | missing: 0 (0.0%) | zeros: 9,882 | negative: 0
- min=0 max=255 mean=1.477 median=0 std=16.6454
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=14.02

#### `0.246`  (`int64`)
- unique: 133 | missing: 0 (0.0%) | zeros: 9,736 | negative: 0
- min=0 max=255 mean=3.7897 median=0 std=27.302
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=191

#### `0.247`  (`int64`)
- unique: 199 | missing: 0 (0.0%) | zeros: 9,358 | negative: 0
- min=0 max=255 mean=8.7274 median=0 std=41.0301
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=33 p99=253

#### `0.248`  (`int64`)
- unique: 236 | missing: 0 (0.0%) | zeros: 8,650 | negative: 0
- min=0 max=255 mean=18.9681 median=0 std=58.9563
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=197.1 p99=253

#### `0.249`  (`int64`)
- unique: 253 | missing: 0 (0.0%) | zeros: 7,569 | negative: 0
- min=0 max=255 mean=36.8013 median=0 std=79.6015
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=253 p99=254

#### `0.250`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 6,103 | negative: 0
- min=0 max=255 mean=63.8925 median=0 std=97.926
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=128 p95=253 p99=255

#### `0.251`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 4,876 | negative: 0
- min=0 max=255 mean=92.0973 median=9 std=108.9193
- quantiles: p1=0 p5=0 p25=0 p50=9 p75=229 p95=254 p99=255

#### `0.252`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 4,190 | negative: 0
- min=0 max=255 mean=107.7699 median=57 std=112.1082
- quantiles: p1=0 p5=0 p25=0 p50=57 p75=251 p95=254 p99=255

#### `17`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 4,231 | negative: 0
- min=0 max=255 mean=104.9173 median=50 std=110.8457
- quantiles: p1=0 p5=0 p25=0 p50=50 p75=245 p95=254 p99=255

#### `66`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 4,669 | negative: 0
- min=0 max=255 mean=90.2618 median=14 std=107.1822
- quantiles: p1=0 p5=0 p25=0 p50=14 p75=220.5 p95=254 p99=255

#### `14`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 5,083 | negative: 0
- min=0 max=255 mean=80.3092 median=0 std=103.5303
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=188 p95=254 p99=255

#### `67.1`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 5,123 | negative: 0
- min=0 max=255 mean=79.8016 median=0 std=103.472
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=186 p95=254 p99=255

#### `67.2`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 4,881 | negative: 0
- min=0 max=255 mean=84.5459 median=6 std=104.9659
- quantiles: p1=0 p5=0 p25=0 p50=6 p75=201 p95=254 p99=255

#### `67.3`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 4,418 | negative: 0
- min=0 max=255 mean=94.4852 median=28 std=107.4297
- quantiles: p1=0 p5=0 p25=0 p50=28 p75=227 p95=254 p99=255

#### `59`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 4,017 | negative: 0
- min=0 max=255 mean=107.8448 median=64 std=110.6456
- quantiles: p1=0 p5=0 p25=0 p50=64 p75=247 p95=254 p99=255

#### `21`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 4,033 | negative: 0
- min=0 max=255 mean=108.9505 median=66 std=110.9377
- quantiles: p1=0 p5=0 p25=0 p50=66 p75=249 p95=254 p99=255

### 4. Data Quality Flags
- **constant columns**: 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.10, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.20, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.30, 0.31, 0.32, 0.49, 0.50, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.60, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.111, 0.112, 0.113, 0.114, 0.139, 0.140, 0.167, 0.168, 0.169, 0.196, 0.218
- **near constant columns**: 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.40, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.76, 0.77, 0.78, 0.79, 0.80, 0.88, 0.89, 0.90, 0.91, 0.106, 0.107, 0.108, 0.109, 0.110, 0.115, 0.116, 0.117, 0.136, 0.137, 0.138, 0.141, 0.142, 0.143, 0.144, 0.165, 0.166, 0.170, 0.171, 0.194, 0.195, 0.197, 0.198, 0.199, 0.216, 0.217, 0.219, 0.220, 0.221, 0.228, 0.229, 0.230, 0.231, 0.232, 0.240, 0.241, 0.242, 0.243, 0.244
- **extremely high cardinality columns**: none
- **likely id columns**: none
- **likely timestamp columns**: none
- **likely categorical columns**: none
- **likely target outcome columns**: none
- **columns with possible post outcome info**: none

### 5. Relationships / Duplicates
- duplicate rows: 0 (0.0%)

### 9. Dataset-Specific Summary
**Potentially useful for:**
- general tabular features (no strong signal columns detected)
**Potential limitations:**
- no obvious temporal information detected
- no obvious target/outcome column detected
- 63 constant column(s) present

## sample_data/mnist_train_small.csv

### 1. File Information
- type: csv | size: 34.83 MB | rows: 19,999 | columns: 785
- NOTE: column detail truncated to first 300 columns


### 2-3. Column Schema & Unique Values

#### `6`  (`int64`)
- unique: 10 | missing: 0 (0.0%) | zeros: 1,962 | negative: 0
- all values (n=10): 0×1962, 1×2243, 2×1989, 3×2021, 4×1924, 5×1761, 6×2038, 7×2126, 8×1912, 9×2023

#### `0`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.1`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.2`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.3`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.4`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.5`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.6`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.7`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.8`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.9`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.10`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.11`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.12`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 19,998 | negative: 0
- flags: near-constant
- all values (n=2): 0×19998, 10×1

#### `0.13`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 19,998 | negative: 0
- flags: near-constant
- all values (n=2): 0×19998, 216×1

#### `0.14`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 19,998 | negative: 0
- flags: near-constant
- all values (n=2): 0×19998, 216×1

#### `0.15`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 19,998 | negative: 0
- flags: near-constant
- all values (n=2): 0×19998, 9×1

#### `0.16`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.17`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.18`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.19`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.20`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.21`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.22`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.23`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.24`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.25`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.26`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.27`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.28`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.29`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.30`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.31`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.32`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.33`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.34`  (`int64`)
- unique: 4 | missing: 0 (0.0%) | zeros: 19,996 | negative: 0
- flags: near-constant
- all values (n=4): 0×19996, 2×1, 114×1, 132×1

#### `0.35`  (`int64`)
- unique: 9 | missing: 0 (0.0%) | zeros: 19,990 | negative: 0
- flags: near-constant
- all values (n=9): 0×19990, 3×1, 13×2, 30×1, 37×1, 47×1, 51×1, 163×1, 212×1

#### `0.36`  (`int64`)
- unique: 8 | missing: 0 (0.0%) | zeros: 19,992 | negative: 0
- flags: near-constant
- all values (n=8): 0×19992, 22×1, 111×1, 133×1, 146×1, 249×1, 252×1, 253×1

#### `0.37`  (`int64`)
- unique: 14 | missing: 0 (0.0%) | zeros: 19,986 | negative: 0
- flags: near-constant
- all values (n=14): 0×19986, 4×1, 7×1, 49×1, 52×1, 62×1, 64×1, 84×1, 113×1, 133×1, 144×1, 170×1, 198×1, 230×1

#### `0.38`  (`int64`)
- unique: 17 | missing: 0 (0.0%) | zeros: 19,981 | negative: 0
- flags: near-constant
- all values (n=17): 0×19981, 3×1, 24×1, 32×1, 49×1, 52×1, 55×1, 113×1, 120×1, 133×1, 158×1, 163×1, 173×1, 208×1, 253×3, 254×1, 255×1

#### `0.39`  (`int64`)
- unique: 23 | missing: 0 (0.0%) | zeros: 19,972 | negative: 0
- flags: near-constant
- all values (n=23): 0×19972, 1×1, 20×1, 46×2, 47×1, 60×2, 77×1, 89×2, 113×1, 128×2, 130×1, 168×1, 169×1, 193×1, 195×1, 203×1, 208×1, 212×1, 228×1, 234×1, 240×1, 253×1, 255×2

#### `0.40`  (`int64`)
- unique: 34 | missing: 0 (0.0%) | zeros: 19,965 | negative: 0
- flags: near-constant
- min=0 max=255 mean=0.2416 median=0 std=6.8123
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.41`  (`int64`)
- unique: 29 | missing: 0 (0.0%) | zeros: 19,966 | negative: 0
- flags: near-constant
- all values (n=29): 0×19966, 4×1, 9×1, 11×1, 18×1, 22×1, 24×1, 25×1, 29×1, 60×1, 63×1, 64×1, 72×1, 83×1, 84×1, 91×2, 100×1, 104×1, 107×1, 116×1, 123×1, 139×1, 155×1, 177×2, 211×1, 219×1, 243×1, 254×3, 255×2

#### `0.42`  (`int64`)
- unique: 23 | missing: 0 (0.0%) | zeros: 19,972 | negative: 0
- flags: near-constant
- all values (n=23): 0×19972, 19×2, 21×1, 24×1, 56×1, 64×2, 107×1, 128×1, 129×1, 130×1, 132×1, 150×1, 151×1, 179×1, 193×1, 216×1, 221×1, 224×1, 230×2, 232×1, 253×2, 254×2, 255×1

#### `0.43`  (`int64`)
- unique: 27 | missing: 0 (0.0%) | zeros: 19,968 | negative: 0
- flags: near-constant
- all values (n=27): 0×19968, 11×1, 19×1, 25×1, 33×1, 37×1, 38×1, 41×1, 53×1, 61×1, 62×1, 68×1, 86×1, 95×2, 102×1, 112×1, 113×1, 122×1, 134×1, 147×1, 149×1, 151×1, 193×1, 242×1, 250×1, 253×3, 255×3

#### `0.44`  (`int64`)
- unique: 26 | missing: 0 (0.0%) | zeros: 19,971 | negative: 0
- flags: near-constant
- all values (n=26): 0×19971, 10×1, 11×1, 14×1, 22×1, 27×1, 28×1, 31×1, 32×1, 46×1, 51×1, 53×1, 78×1, 92×1, 98×1, 99×1, 146×1, 157×2, 158×1, 165×1, 168×1, 182×2, 207×1, 213×1, 220×1, 253×2

#### `0.45`  (`int64`)
- unique: 22 | missing: 0 (0.0%) | zeros: 19,975 | negative: 0
- flags: near-constant
- all values (n=22): 0×19975, 4×1, 17×1, 26×2, 27×1, 53×1, 62×1, 82×1, 96×1, 114×1, 130×1, 145×1, 169×1, 186×1, 193×1, 221×1, 226×1, 228×1, 231×1, 234×1, 247×1, 254×3

#### `0.46`  (`int64`)
- unique: 24 | missing: 0 (0.0%) | zeros: 19,975 | negative: 0
- flags: near-constant
- all values (n=24): 0×19975, 13×1, 14×1, 21×1, 23×1, 31×1, 44×1, 49×1, 59×1, 68×1, 77×1, 85×1, 140×1, 147×1, 152×1, 200×1, 210×1, 223×1, 239×1, 240×1, 248×1, 253×1, 254×1, 255×2

#### `0.47`  (`int64`)
- unique: 14 | missing: 0 (0.0%) | zeros: 19,986 | negative: 0
- flags: near-constant
- all values (n=14): 0×19986, 9×1, 13×1, 57×1, 61×1, 62×1, 65×1, 75×1, 107×1, 131×1, 148×1, 166×1, 195×1, 248×1

#### `0.48`  (`int64`)
- unique: 4 | missing: 0 (0.0%) | zeros: 19,996 | negative: 0
- flags: near-constant
- all values (n=4): 0×19996, 168×1, 218×1, 229×1

#### `0.49`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 19,998 | negative: 0
- flags: near-constant
- all values (n=2): 0×19998, 54×1

#### `0.50`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.51`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.52`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.53`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.54`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.55`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.56`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.57`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.58`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.59`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 19,998 | negative: 0
- flags: near-constant
- all values (n=2): 0×19998, 29×1

#### `0.60`  (`int64`)
- unique: 5 | missing: 0 (0.0%) | zeros: 19,995 | negative: 0
- flags: near-constant
- all values (n=5): 0×19995, 10×1, 26×1, 58×1, 128×1

#### `0.61`  (`int64`)
- unique: 5 | missing: 0 (0.0%) | zeros: 19,995 | negative: 0
- flags: near-constant
- all values (n=5): 0×19995, 6×1, 13×1, 38×1, 62×1

#### `0.62`  (`int64`)
- unique: 11 | missing: 0 (0.0%) | zeros: 19,989 | negative: 0
- flags: near-constant
- all values (n=11): 0×19989, 2×1, 19×1, 47×1, 53×1, 64×1, 73×1, 85×1, 95×1, 181×1, 212×1

#### `0.63`  (`int64`)
- unique: 25 | missing: 0 (0.0%) | zeros: 19,973 | negative: 0
- flags: near-constant
- all values (n=25): 0×19973, 2×1, 4×1, 13×2, 23×1, 26×1, 37×1, 48×1, 55×1, 58×1, 71×1, 72×1, 73×1, 76×1, 103×1, 132×1, 173×1, 174×1, 191×1, 194×1, 203×1, 222×1, 251×1, 253×1, 254×2

#### `0.64`  (`int64`)
- unique: 39 | missing: 0 (0.0%) | zeros: 19,950 | negative: 0
- flags: near-constant
- min=0 max=255 mean=0.3078 median=0 std=7.7336
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.65`  (`int64`)
- unique: 67 | missing: 0 (0.0%) | zeros: 19,913 | negative: 0
- flags: near-constant
- min=0 max=255 mean=0.571 median=0 std=10.2315
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.66`  (`int64`)
- unique: 96 | missing: 0 (0.0%) | zeros: 19,848 | negative: 0
- flags: near-constant
- min=0 max=255 mean=0.986 median=0 std=13.8597
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.67`  (`int64`)
- unique: 126 | missing: 0 (0.0%) | zeros: 19,776 | negative: 0
- min=0 max=255 mean=1.4575 median=0 std=16.5013
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=14

#### `0.68`  (`int64`)
- unique: 149 | missing: 0 (0.0%) | zeros: 19,713 | negative: 0
- min=0 max=255 mean=2.0382 median=0 std=19.817
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=79

#### `0.69`  (`int64`)
- unique: 175 | missing: 0 (0.0%) | zeros: 19,609 | negative: 0
- min=0 max=255 mean=2.6239 median=0 std=22.3109
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=139

#### `0.70`  (`int64`)
- unique: 190 | missing: 0 (0.0%) | zeros: 19,537 | negative: 0
- min=0 max=255 mean=3.1939 median=0 std=24.6718
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=172

#### `0.71`  (`int64`)
- unique: 202 | missing: 0 (0.0%) | zeros: 19,475 | negative: 0
- min=0 max=255 mean=3.6537 median=0 std=26.1434
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=185

#### `0.72`  (`int64`)
- unique: 204 | missing: 0 (0.0%) | zeros: 19,469 | negative: 0
- min=0 max=255 mean=3.7074 median=0 std=26.4153
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=183.02

#### `0.73`  (`int64`)
- unique: 180 | missing: 0 (0.0%) | zeros: 19,510 | negative: 0
- min=0 max=255 mean=3.5609 median=0 std=26.6902
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=196

#### `0.74`  (`int64`)
- unique: 180 | missing: 0 (0.0%) | zeros: 19,591 | negative: 0
- min=0 max=255 mean=2.9559 median=0 std=23.8102
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=156

#### `0.75`  (`int64`)
- unique: 152 | missing: 0 (0.0%) | zeros: 19,706 | negative: 0
- min=0 max=255 mean=2.0656 median=0 std=19.9136
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=77.02

#### `0.76`  (`int64`)
- unique: 107 | missing: 0 (0.0%) | zeros: 19,823 | negative: 0
- flags: near-constant
- min=0 max=255 mean=1.356 median=0 std=16.4961
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.77`  (`int64`)
- unique: 76 | missing: 0 (0.0%) | zeros: 19,891 | negative: 0
- flags: near-constant
- min=0 max=255 mean=0.7345 median=0 std=11.9042
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.78`  (`int64`)
- unique: 40 | missing: 0 (0.0%) | zeros: 19,950 | negative: 0
- flags: near-constant
- min=0 max=255 mean=0.3494 median=0 std=8.2914
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.79`  (`int64`)
- unique: 23 | missing: 0 (0.0%) | zeros: 19,974 | negative: 0
- flags: near-constant
- all values (n=23): 0×19974, 2×2, 5×1, 7×1, 12×2, 19×1, 25×1, 27×2, 35×1, 39×1, 46×1, 51×1, 57×1, 117×1, 122×1, 128×1, 163×1, 190×1, 201×1, 203×1, 239×1, 250×1, 254×1

#### `0.80`  (`int64`)
- unique: 9 | missing: 0 (0.0%) | zeros: 19,991 | negative: 0
- flags: near-constant
- all values (n=9): 0×19991, 7×1, 18×1, 36×1, 115×1, 128×1, 219×1, 254×1, 255×1

#### `0.81`  (`int64`)
- unique: 4 | missing: 0 (0.0%) | zeros: 19,995 | negative: 0
- flags: near-constant
- all values (n=4): 0×19995, 9×1, 55×1, 165×2

#### `0.82`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.83`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.84`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.85`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.86`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.87`  (`int64`)
- unique: 3 | missing: 0 (0.0%) | zeros: 19,996 | negative: 0
- flags: near-constant
- all values (n=3): 0×19996, 65×2, 84×1

#### `0.88`  (`int64`)
- unique: 5 | missing: 0 (0.0%) | zeros: 19,995 | negative: 0
- flags: near-constant
- all values (n=5): 0×19995, 6×1, 17×1, 28×1, 52×1

#### `0.89`  (`int64`)
- unique: 18 | missing: 0 (0.0%) | zeros: 19,980 | negative: 0
- flags: near-constant
- all values (n=18): 0×19980, 1×2, 2×2, 8×1, 13×1, 14×1, 16×1, 25×1, 33×1, 40×1, 44×1, 45×1, 51×1, 73×1, 92×1, 118×1, 125×1, 134×1

#### `0.90`  (`int64`)
- unique: 41 | missing: 0 (0.0%) | zeros: 19,953 | negative: 0
- flags: near-constant
- min=0 max=255 mean=0.2035 median=0 std=5.7122
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.91`  (`int64`)
- unique: 77 | missing: 0 (0.0%) | zeros: 19,892 | negative: 0
- flags: near-constant
- min=0 max=255 mean=0.6306 median=0 std=10.6804
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.92`  (`int64`)
- unique: 119 | missing: 0 (0.0%) | zeros: 19,788 | negative: 0
- min=0 max=255 mean=1.2339 median=0 std=15.2544
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=5

#### `0.93`  (`int64`)
- unique: 155 | missing: 0 (0.0%) | zeros: 19,668 | negative: 0
- min=0 max=255 mean=2.277 median=0 std=21.0584
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=91

#### `0.94`  (`int64`)
- unique: 195 | missing: 0 (0.0%) | zeros: 19,479 | negative: 0
- min=0 max=255 mean=3.6779 median=0 std=26.7409
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=190.02

#### `0.95`  (`int64`)
- unique: 221 | missing: 0 (0.0%) | zeros: 19,241 | negative: 0
- min=0 max=255 mean=5.6106 median=0 std=33.424
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=250

#### `0.96`  (`int64`)
- unique: 237 | missing: 0 (0.0%) | zeros: 18,975 | negative: 0
- min=0 max=255 mean=7.4986 median=0 std=38.2267
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=4.1 p99=253

#### `0.97`  (`int64`)
- unique: 247 | missing: 0 (0.0%) | zeros: 18,689 | negative: 0
- min=0 max=255 mean=9.6655 median=0 std=43.0666
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=57 p99=253

#### `0.98`  (`int64`)
- unique: 251 | missing: 0 (0.0%) | zeros: 18,415 | negative: 0
- min=0 max=255 mean=12.1723 median=0 std=48.1652
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=118.1 p99=254

#### `0.99`  (`int64`)
- unique: 250 | missing: 0 (0.0%) | zeros: 18,249 | negative: 0
- min=0 max=255 mean=13.6951 median=0 std=51.4971
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=145 p99=254

#### `0.100`  (`int64`)
- unique: 252 | missing: 0 (0.0%) | zeros: 18,251 | negative: 0
- min=0 max=255 mean=13.4778 median=0 std=50.6241
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=139 p99=254

#### `0.101`  (`int64`)
- unique: 251 | missing: 0 (0.0%) | zeros: 18,413 | negative: 0
- min=0 max=255 mean=12.0943 median=0 std=48.2419
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=120.1 p99=253

#### `0.102`  (`int64`)
- unique: 250 | missing: 0 (0.0%) | zeros: 18,682 | negative: 0
- min=0 max=255 mean=9.8719 median=0 std=43.5837
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=62 p99=253

#### `0.103`  (`int64`)
- unique: 230 | missing: 0 (0.0%) | zeros: 19,041 | negative: 0
- min=0 max=255 mean=7.2895 median=0 std=38.0078
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=253

#### `0.104`  (`int64`)
- unique: 215 | missing: 0 (0.0%) | zeros: 19,387 | negative: 0
- min=0 max=255 mean=4.5278 median=0 std=29.5817
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=208.02

#### `0.105`  (`int64`)
- unique: 164 | missing: 0 (0.0%) | zeros: 19,646 | negative: 0
- min=0 max=255 mean=2.3131 median=0 std=21.1884
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=92.12

#### `0.106`  (`int64`)
- unique: 111 | missing: 0 (0.0%) | zeros: 19,829 | negative: 0
- flags: near-constant
- min=0 max=255 mean=1.1073 median=0 std=14.3438
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.107`  (`int64`)
- unique: 59 | missing: 0 (0.0%) | zeros: 19,924 | negative: 0
- flags: near-constant
- min=0 max=255 mean=0.4063 median=0 std=8.6577
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.108`  (`int64`)
- unique: 27 | missing: 0 (0.0%) | zeros: 19,971 | negative: 0
- flags: near-constant
- all values (n=27): 0×19971, 5×1, 10×1, 17×1, 18×1, 25×1, 32×1, 33×1, 42×1, 54×1, 57×1, 66×1, 78×1, 93×1, 98×1, 113×1, 114×1, 117×1, 128×1, 170×2, 175×1, 191×1, 206×1, 232×1, 253×1, 254×1, 255×2

#### `0.109`  (`int64`)
- unique: 8 | missing: 0 (0.0%) | zeros: 19,991 | negative: 0
- flags: near-constant
- all values (n=8): 0×19991, 29×2, 60×1, 115×1, 130×1, 164×1, 191×1, 192×1

#### `0.110`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 19,998 | negative: 0
- flags: near-constant
- all values (n=2): 0×19998, 47×1

#### `0.111`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.112`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.113`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 19,998 | negative: 0
- flags: near-constant
- all values (n=2): 0×19998, 38×1

#### `0.114`  (`int64`)
- unique: 3 | missing: 0 (0.0%) | zeros: 19,997 | negative: 0
- flags: near-constant
- all values (n=3): 0×19997, 22×1, 32×1

#### `0.115`  (`int64`)
- unique: 6 | missing: 0 (0.0%) | zeros: 19,994 | negative: 0
- flags: near-constant
- all values (n=6): 0×19994, 7×1, 18×1, 33×1, 53×1, 71×1

#### `0.116`  (`int64`)
- unique: 25 | missing: 0 (0.0%) | zeros: 19,972 | negative: 0
- flags: near-constant
- all values (n=25): 0×19972, 1×1, 3×1, 4×1, 5×1, 6×1, 7×2, 8×1, 14×2, 17×1, 19×1, 21×1, 23×1, 25×1, 26×2, 33×1, 36×1, 42×1, 61×1, 62×1, 89×1, 91×1, 114×1, 197×1, 211×1

#### `0.117`  (`int64`)
- unique: 71 | missing: 0 (0.0%) | zeros: 19,903 | negative: 0
- flags: near-constant
- min=0 max=255 mean=0.4101 median=0 std=7.8189
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.118`  (`int64`)
- unique: 112 | missing: 0 (0.0%) | zeros: 19,777 | negative: 0
- min=0 max=255 mean=1.0708 median=0 std=13.6093
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=7.02

#### `0.119`  (`int64`)
- unique: 177 | missing: 0 (0.0%) | zeros: 19,568 | negative: 0
- min=0 max=255 mean=2.4587 median=0 std=21.117
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=114.02

#### `0.120`  (`int64`)
- unique: 214 | missing: 0 (0.0%) | zeros: 19,210 | negative: 0
- min=0 max=255 mean=4.7464 median=0 std=29.5355
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=214

#### `0.121`  (`int64`)
- unique: 242 | missing: 0 (0.0%) | zeros: 18,765 | negative: 0
- min=0 max=255 mean=8.3325 median=0 std=39.4537
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=34 p99=253

#### `24`  (`int64`)
- unique: 249 | missing: 0 (0.0%) | zeros: 18,116 | negative: 0
- min=0 max=255 mean=13.2464 median=0 std=49.5369
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=131 p99=253

#### `67`  (`int64`)
- unique: 255 | missing: 0 (0.0%) | zeros: 17,376 | negative: 0
- min=0 max=255 mean=19.6098 median=0 std=60.0487
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=203 p99=254

#### `67.1`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 16,505 | negative: 0
- min=0 max=255 mean=26.7804 median=0 std=69.0016
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=246 p99=254

#### `18`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 15,576 | negative: 0
- min=0 max=255 mean=34.9827 median=0 std=77.6255
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=253 p99=255

#### `0.122`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 14,872 | negative: 0
- min=0 max=255 mean=42.3529 median=0 std=84.289
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=7 p95=253 p99=255

#### `0.123`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 14,494 | negative: 0
- min=0 max=255 mean=45.7571 median=0 std=86.5952
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=29 p95=253 p99=255

#### `0.124`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 14,556 | negative: 0
- min=0 max=255 mean=44.3143 median=0 std=85.5746
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=20 p95=253 p99=255

#### `0.125`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 15,052 | negative: 0
- min=0 max=255 mean=39.0832 median=0 std=81.2739
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=253 p99=255

#### `0.126`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 15,922 | negative: 0
- min=0 max=255 mean=31.7837 median=0 std=74.8224
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=252 p99=255

#### `0.127`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 16,908 | negative: 0
- min=0 max=255 mean=23.3389 median=0 std=65.0475
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=230 p99=254

#### `0.128`  (`int64`)
- unique: 253 | missing: 0 (0.0%) | zeros: 17,859 | negative: 0
- min=0 max=255 mean=14.9509 median=0 std=52.1937
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=152 p99=254

#### `0.129`  (`int64`)
- unique: 247 | missing: 0 (0.0%) | zeros: 18,719 | negative: 0
- min=0 max=255 mean=8.3635 median=0 std=39.2202
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=38 p99=252

#### `0.130`  (`int64`)
- unique: 215 | missing: 0 (0.0%) | zeros: 19,269 | negative: 0
- min=0 max=255 mean=4.3646 median=0 std=28.1824
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=194.02

#### `0.131`  (`int64`)
- unique: 167 | missing: 0 (0.0%) | zeros: 19,660 | negative: 0
- min=0 max=255 mean=1.9323 median=0 std=18.6021
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=67.02

#### `0.132`  (`int64`)
- unique: 96 | missing: 0 (0.0%) | zeros: 19,856 | negative: 0
- flags: near-constant
- min=0 max=255 mean=0.7069 median=0 std=10.6576
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.133`  (`int64`)
- unique: 35 | missing: 0 (0.0%) | zeros: 19,958 | negative: 0
- flags: near-constant
- min=0 max=253 mean=0.1822 median=0 std=5.0708
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.134`  (`int64`)
- unique: 10 | missing: 0 (0.0%) | zeros: 19,990 | negative: 0
- flags: near-constant
- all values (n=10): 0×19990, 9×1, 15×1, 61×1, 77×1, 147×1, 165×1, 195×1, 206×1, 221×1

#### `0.135`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 19,998 | negative: 0
- flags: near-constant
- all values (n=2): 0×19998, 59×1

#### `0.136`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.137`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.138`  (`int64`)
- unique: 5 | missing: 0 (0.0%) | zeros: 19,995 | negative: 0
- flags: near-constant
- all values (n=5): 0×19995, 47×1, 53×1, 64×1, 76×1

#### `0.139`  (`int64`)
- unique: 21 | missing: 0 (0.0%) | zeros: 19,978 | negative: 0
- flags: near-constant
- all values (n=21): 0×19978, 4×1, 5×1, 7×2, 10×1, 11×1, 12×1, 18×1, 19×1, 29×1, 36×1, 50×1, 55×1, 61×1, 64×1, 67×1, 82×1, 85×1, 86×1, 101×1, 222×1

#### `0.140`  (`int64`)
- unique: 70 | missing: 0 (0.0%) | zeros: 19,893 | negative: 0
- flags: near-constant
- min=0 max=255 mean=0.4014 median=0 std=7.4938
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.141`  (`int64`)
- unique: 135 | missing: 0 (0.0%) | zeros: 19,717 | negative: 0
- min=0 max=255 mean=1.5779 median=0 std=17.2239
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=32.02

#### `0.142`  (`int64`)
- unique: 206 | missing: 0 (0.0%) | zeros: 19,385 | negative: 0
- min=0 max=255 mean=3.5852 median=0 std=25.7237
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=166.04

#### `0.143`  (`int64`)
- unique: 241 | missing: 0 (0.0%) | zeros: 18,865 | negative: 0
- min=0 max=255 mean=7.1927 median=0 std=36.5242
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=13 p99=251

#### `0.144`  (`int64`)
- unique: 253 | missing: 0 (0.0%) | zeros: 18,093 | negative: 0
- min=0 max=255 mean=13.0229 median=0 std=49.228
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=128 p99=253

#### `0.145`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 17,077 | negative: 0
- min=0 max=255 mean=21.2125 median=0 std=62.0812
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=219 p99=254

#### `131`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 15,905 | negative: 0
- min=0 max=255 mean=31.5372 median=0 std=74.6239
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=252 p99=254

#### `252`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 14,514 | negative: 0
- min=0 max=255 mean=43.8881 median=0 std=85.7293
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=19 p95=253 p99=254

#### `252.1`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 13,082 | negative: 0
- min=0 max=255 mean=57.7901 median=0 std=94.9345
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=102 p95=253 p99=255

#### `66`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 11,675 | negative: 0
- min=0 max=255 mean=73.0585 median=0 std=102.7687
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=169 p95=254 p99=255

#### `0.146`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 10,729 | negative: 0
- min=0 max=255 mean=84.2894 median=0 std=107.0562
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=209 p95=254 p99=255

#### `0.147`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 10,198 | negative: 0
- min=0 max=255 mean=89.974 median=0 std=108.5727
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=222 p95=254 p99=255

#### `0.148`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 10,281 | negative: 0
- min=0 max=255 mean=88.2855 median=0 std=107.9001
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=217 p95=254 p99=255

#### `0.149`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 10,951 | negative: 0
- min=0 max=255 mean=79.4402 median=0 std=104.7439
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=191 p95=254 p99=255

#### `0.150`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 12,184 | negative: 0
- min=0 max=255 mean=65.5721 median=0 std=98.8304
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=137 p95=253 p99=255

#### `0.151`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 13,840 | negative: 0
- min=0 max=255 mean=49.4934 median=0 std=89.4551
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=51 p95=253 p99=255

#### `0.152`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 15,494 | negative: 0
- min=0 max=255 mean=33.7784 median=0 std=75.9818
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=252 p99=255

#### `0.153`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 16,958 | negative: 0
- min=0 max=255 mean=21.201 median=0 std=61.6514
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=214 p99=254

#### `0.154`  (`int64`)
- unique: 253 | missing: 0 (0.0%) | zeros: 18,120 | negative: 0
- min=0 max=255 mean=12.2484 median=0 std=47.2639
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=110 p99=253

#### `0.155`  (`int64`)
- unique: 236 | missing: 0 (0.0%) | zeros: 18,971 | negative: 0
- min=0 max=255 mean=6.2641 median=0 std=33.615
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=3 p99=234.02

#### `0.156`  (`int64`)
- unique: 192 | missing: 0 (0.0%) | zeros: 19,501 | negative: 0
- min=0 max=255 mean=2.7374 median=0 std=21.5949
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=123.04

#### `0.157`  (`int64`)
- unique: 116 | missing: 0 (0.0%) | zeros: 19,825 | negative: 0
- flags: near-constant
- min=0 max=255 mean=0.7815 median=0 std=10.7097
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.158`  (`int64`)
- unique: 28 | missing: 0 (0.0%) | zeros: 19,972 | negative: 0
- flags: near-constant
- all values (n=28): 0×19972, 2×1, 7×1, 9×1, 16×1, 21×1, 23×1, 28×1, 29×1, 31×1, 36×1, 37×1, 39×1, 57×1, 64×1, 82×1, 89×1, 98×1, 103×1, 104×1, 108×1, 116×1, 119×1, 129×1, 138×1, 146×1, 165×1, 253×1

#### `0.159`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.160`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.161`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 19,999 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×19999

#### `0.162`  (`int64`)
- unique: 9 | missing: 0 (0.0%) | zeros: 19,991 | negative: 0
- flags: near-constant
- all values (n=9): 0×19991, 19×1, 22×1, 33×1, 41×1, 55×1, 61×1, 74×1, 177×1

#### `0.163`  (`int64`)
- unique: 38 | missing: 0 (0.0%) | zeros: 19,951 | negative: 0
- flags: near-constant
- min=0 max=254 mean=0.1738 median=0 std=5.2422
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.164`  (`int64`)
- unique: 118 | missing: 0 (0.0%) | zeros: 19,787 | negative: 0
- min=0 max=254 mean=1.0695 median=0 std=13.5102
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=5

#### `0.165`  (`int64`)
- unique: 191 | missing: 0 (0.0%) | zeros: 19,458 | negative: 0
- min=0 max=255 mean=3.3991 median=0 std=25.3905
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=171.06

#### `0.166`  (`int64`)
- unique: 233 | missing: 0 (0.0%) | zeros: 18,855 | negative: 0
- min=0 max=255 mean=7.4587 median=0 std=37.3019
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=18.1 p99=252

#### `0.167`  (`int64`)
- unique: 251 | missing: 0 (0.0%) | zeros: 17,993 | negative: 0
- min=0 max=255 mean=14.3647 median=0 std=52.1235
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=150 p99=253

#### `0.168`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 16,786 | negative: 0
- min=0 max=255 mean=24.1036 median=0 std=66.3895
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=241 p99=254

#### `159`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 15,310 | negative: 0
- min=0 max=255 mean=37.1675 median=0 std=80.5426
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=253 p99=254

#### `250`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 13,524 | negative: 0
- min=0 max=255 mean=52.6538 median=0 std=92.1354
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=64 p95=253 p99=255

#### `232`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 11,668 | negative: 0
- min=0 max=255 mean=70.136 median=0 std=101.0958
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=156 p95=253 p99=255

#### `30`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 10,000 | negative: 0
- min=0 max=255 mean=87.9374 median=0 std=107.2991
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=216 p95=254 p99=255

#### `32`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 8,540 | negative: 0
- min=0 max=255 mean=105.0926 median=52 std=110.7946
- quantiles: p1=0 p5=0 p25=0 p50=52 p75=247 p95=254 p99=255

#### `0.169`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 7,574 | negative: 0
- min=0 max=255 mean=117.7192 median=105 std=111.9066
- quantiles: p1=0 p5=0 p25=0 p50=105 p75=252 p95=254 p99=255

#### `0.170`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 7,120 | negative: 0
- min=0 max=255 mean=123.1963 median=125 std=112.0889
- quantiles: p1=0 p5=0 p25=0 p50=125 p75=252 p95=254 p99=255

#### `0.171`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 7,361 | negative: 0
- min=0 max=255 mean=121.4451 median=118 std=112.4098
- quantiles: p1=0 p5=0 p25=0 p50=118 p75=252 p95=254 p99=255

#### `0.172`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 8,059 | negative: 0
- min=0 max=255 mean=111.7396 median=73 std=112.1713
- quantiles: p1=0 p5=0 p25=0 p50=73 p75=252 p95=254 p99=255

#### `0.173`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 9,489 | negative: 0
- min=0 max=255 mean=95.7385 median=15 std=109.9575
- quantiles: p1=0 p5=0 p25=0 p50=15 p75=236 p95=254 p99=255

#### `0.174`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 11,402 | negative: 0
- min=0 max=255 mean=74.5985 median=0 std=103.6227
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=177 p95=253 p99=255

#### `0.175`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 13,526 | negative: 0
- min=0 max=255 mean=53.4916 median=0 std=92.8635
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=69 p95=253 p99=255

#### `0.176`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 15,492 | negative: 0
- min=0 max=255 mean=35.0831 median=0 std=78.0269
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=252 p99=254

#### `0.177`  (`int64`)
- unique: 255 | missing: 0 (0.0%) | zeros: 17,128 | negative: 0
- min=0 max=255 mean=20.9221 median=0 std=62.0074
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=220 p99=254

#### `0.178`  (`int64`)
- unique: 253 | missing: 0 (0.0%) | zeros: 18,296 | negative: 0
- min=0 max=255 mean=11.2456 median=0 std=45.3922
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=93 p99=253

#### `0.179`  (`int64`)
- unique: 236 | missing: 0 (0.0%) | zeros: 19,167 | negative: 0
- min=0 max=255 mean=5.2607 median=0 std=30.8297
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=212

#### `0.180`  (`int64`)
- unique: 167 | missing: 0 (0.0%) | zeros: 19,673 | negative: 0
- min=0 max=255 mean=1.7881 median=0 std=17.2226
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=64

#### `0.181`  (`int64`)
- unique: 59 | missing: 0 (0.0%) | zeros: 19,933 | negative: 0
- flags: near-constant
- min=0 max=254 mean=0.294 median=0 std=6.6778
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.182`  (`int64`)
- unique: 8 | missing: 0 (0.0%) | zeros: 19,992 | negative: 0
- flags: near-constant
- all values (n=8): 0×19992, 12×1, 33×1, 38×1, 51×1, 78×1, 113×1, 172×1

#### `0.183`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 19,998 | negative: 0
- flags: near-constant
- all values (n=2): 0×19998, 47×1

#### `0.184`  (`int64`)
- unique: 6 | missing: 0 (0.0%) | zeros: 19,994 | negative: 0
- flags: near-constant
- all values (n=6): 0×19994, 5×1, 58×1, 64×1, 128×1, 191×1

#### `0.185`  (`int64`)
- unique: 19 | missing: 0 (0.0%) | zeros: 19,980 | negative: 0
- flags: near-constant
- all values (n=19): 0×19980, 7×1, 9×1, 16×2, 34×1, 51×1, 67×1, 72×1, 77×1, 85×1, 95×1, 109×1, 110×1, 118×1, 120×1, 121×1, 122×1, 198×1, 255×1

#### `0.186`  (`int64`)
- unique: 77 | missing: 0 (0.0%) | zeros: 19,883 | negative: 0
- flags: near-constant
- min=0 max=255 mean=0.5212 median=0 std=9.147
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.187`  (`int64`)
- unique: 175 | missing: 0 (0.0%) | zeros: 19,589 | negative: 0
- min=0 max=255 mean=2.2973 median=0 std=20.0563
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=96.02

#### `0.188`  (`int64`)
- unique: 229 | missing: 0 (0.0%) | zeros: 19,047 | negative: 0
- min=0 max=255 mean=6.029 median=0 std=33.462
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=238.04

#### `0.189`  (`int64`)
- unique: 250 | missing: 0 (0.0%) | zeros: 18,180 | negative: 0
- min=0 max=255 mean=12.4959 median=0 std=48.4141
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=116.1 p99=253

#### `0.190`  (`int64`)
- unique: 255 | missing: 0 (0.0%) | zeros: 16,914 | negative: 0
- min=0 max=255 mean=22.4229 median=0 std=63.9072
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=230 p99=254

#### `15`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 15,243 | negative: 0
- min=0 max=255 mean=36.4002 median=0 std=79.0838
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=253 p99=254

#### `222`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 13,303 | negative: 0
- min=0 max=255 mean=53.8798 median=0 std=92.2037
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=73.5 p95=253 p99=255

#### `252.2`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 11,077 | negative: 0
- min=0 max=255 mean=73.5276 median=0 std=101.7626
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=168 p95=253 p99=255

#### `108`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 9,143 | negative: 0
- min=0 max=255 mean=93.3955 median=20 std=107.6124
- quantiles: p1=0 p5=0 p25=0 p50=20 p75=224.5 p95=254 p99=255

#### `0.191`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 7,568 | negative: 0
- min=0 max=255 mean=110.3933 median=77 std=109.8408
- quantiles: p1=0 p5=0 p25=0 p50=77 p75=248 p95=254 p99=255

#### `0.192`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 6,519 | negative: 0
- min=0 max=255 mean=125.0272 median=128 std=110.5519
- quantiles: p1=0 p5=0 p25=0 p50=128 p75=252 p95=254 p99=255

#### `0.193`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 5,977 | negative: 0
- min=0 max=255 mean=133.3466 median=152 std=110.5983
- quantiles: p1=0 p5=0 p25=0 p50=152 p75=253 p95=254 p99=255

#### `0.194`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 5,745 | negative: 0
- min=0 max=255 mean=135.665 median=157 std=110.1191
- quantiles: p1=0 p5=0 p25=0 p50=157 p75=253 p95=254 p99=255

#### `0.195`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 5,862 | negative: 0
- min=0 max=255 mean=133.7989 median=154 std=110.5034
- quantiles: p1=0 p5=0 p25=0 p50=154 p75=252 p95=254 p99=255

#### `0.196`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 6,430 | negative: 0
- min=0 max=255 mean=126.8184 median=133 std=110.7795
- quantiles: p1=0 p5=0 p25=0 p50=133 p75=252 p95=254 p99=255

#### `0.197`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 7,589 | negative: 0
- min=0 max=255 mean=112.8679 median=84 std=110.9224
- quantiles: p1=0 p5=0 p25=0 p50=84 p75=251 p95=254 p99=255

#### `0.198`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 9,553 | negative: 0
- min=0 max=255 mean=93.0246 median=13 std=108.5682
- quantiles: p1=0 p5=0 p25=0 p50=13 p75=228 p95=254 p99=255

#### `0.199`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 11,878 | negative: 0
- min=0 max=255 mean=68.8206 median=0 std=100.4654
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=150 p95=253 p99=255

#### `0.200`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 14,245 | negative: 0
- min=0 max=255 mean=46.4065 median=0 std=87.983
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=28 p95=253 p99=255

#### `0.201`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 16,248 | negative: 0
- min=0 max=255 mean=28.3397 median=0 std=71.2545
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=251 p99=254

#### `0.202`  (`int64`)
- unique: 254 | missing: 0 (0.0%) | zeros: 17,829 | negative: 0
- min=0 max=255 mean=15.488 median=0 std=53.5345
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=157.1 p99=253

#### `0.203`  (`int64`)
- unique: 244 | missing: 0 (0.0%) | zeros: 18,912 | negative: 0
- min=0 max=255 mean=7.0542 median=0 std=35.8377
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=10 p99=237

#### `0.204`  (`int64`)
- unique: 186 | missing: 0 (0.0%) | zeros: 19,574 | negative: 0
- min=0 max=255 mean=2.5662 median=0 std=21.4385
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=122.08

#### `0.205`  (`int64`)
- unique: 71 | missing: 0 (0.0%) | zeros: 19,910 | negative: 0
- flags: near-constant
- min=0 max=253 mean=0.5118 median=0 std=9.1991
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.206`  (`int64`)
- unique: 9 | missing: 0 (0.0%) | zeros: 19,991 | negative: 0
- flags: near-constant
- all values (n=9): 0×19991, 10×1, 12×1, 21×1, 95×1, 151×1, 171×1, 196×1, 253×1

#### `0.207`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 19,998 | negative: 0
- flags: near-constant
- all values (n=2): 0×19998, 191×1

#### `0.208`  (`int64`)
- unique: 8 | missing: 0 (0.0%) | zeros: 19,992 | negative: 0
- flags: near-constant
- all values (n=8): 0×19992, 2×1, 7×1, 21×1, 92×1, 201×1, 248×1, 252×1

#### `0.209`  (`int64`)
- unique: 55 | missing: 0 (0.0%) | zeros: 19,935 | negative: 0
- flags: near-constant
- min=0 max=255 mean=0.2991 median=0 std=7.2872
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.210`  (`int64`)
- unique: 135 | missing: 0 (0.0%) | zeros: 19,778 | negative: 0
- min=0 max=255 mean=1.3722 median=0 std=15.7501
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=15

#### `0.211`  (`int64`)
- unique: 201 | missing: 0 (0.0%) | zeros: 19,413 | negative: 0
- min=0 max=255 mean=3.8192 median=0 std=27.0944
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=194

#### `0.212`  (`int64`)
- unique: 244 | missing: 0 (0.0%) | zeros: 18,747 | negative: 0
- min=0 max=255 mean=8.5726 median=0 std=40.5356
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=31.1 p99=252

#### `0.213`  (`int64`)
- unique: 254 | missing: 0 (0.0%) | zeros: 17,668 | negative: 0
- min=0 max=255 mean=17.0317 median=0 std=56.3564
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=181 p99=253

#### `0.214`  (`int64`)
- unique: 255 | missing: 0 (0.0%) | zeros: 16,068 | negative: 0
- min=0 max=255 mean=30.0209 median=0 std=73.1901
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=252 p99=254

#### `147`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 14,127 | negative: 0
- min=0 max=255 mean=47.346 median=0 std=88.4466
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=36 p95=253 p99=254

#### `252.3`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 11,809 | negative: 0
- min=0 max=255 mean=68.338 median=0 std=100.4802
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=151 p95=253 p99=255

#### `183`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 9,609 | negative: 0
- min=0 max=255 mean=90.1373 median=9 std=107.4731
- quantiles: p1=0 p5=0 p25=0 p50=9 p75=221 p95=254 p99=255

#### `5`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 7,957 | negative: 0
- min=0 max=255 mean=107.8778 median=64 std=110.5125
- quantiles: p1=0 p5=0 p25=0 p50=64 p75=247 p95=254 p99=255

#### `0.215`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 7,072 | negative: 0
- min=0 max=255 mean=119.2118 median=108 std=110.9882
- quantiles: p1=0 p5=0 p25=0 p50=108 p75=252 p95=254 p99=255

#### `0.216`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 6,761 | negative: 0
- min=0 max=255 mean=124.337 median=127 std=111.475
- quantiles: p1=0 p5=0 p25=0 p50=127 p75=252 p95=254 p99=255

#### `0.217`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 6,699 | negative: 0
- min=0 max=255 mean=124.1327 median=126 std=111.2049
- quantiles: p1=0 p5=0 p25=0 p50=126 p75=252 p95=254 p99=255

#### `0.218`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 6,617 | negative: 0
- min=0 max=255 mean=123.3522 median=122 std=110.6212
- quantiles: p1=0 p5=0 p25=0 p50=122 p75=252 p95=254 p99=255

#### `0.219`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 6,600 | negative: 0
- min=0 max=255 mean=123.8568 median=125 std=110.7786
- quantiles: p1=0 p5=0 p25=0 p50=125 p75=252 p95=254 p99=255

#### `0.220`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 6,698 | negative: 0
- min=0 max=255 mean=122.7219 median=117 std=111.1076
- quantiles: p1=0 p5=0 p25=0 p50=117 p75=252 p95=254 p99=255

#### `0.221`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 7,413 | negative: 0
- min=0 max=255 mean=115.6481 median=94 std=111.2494
- quantiles: p1=0 p5=0 p25=0 p50=94 p75=252 p95=254 p99=255

#### `20`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 9,029 | negative: 0
- min=0 max=255 mean=99.8496 median=32 std=110.2134
- quantiles: p1=0 p5=0 p25=0 p50=32 p75=240 p95=254 p99=255

#### `89`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 11,293 | negative: 0
- min=0 max=255 mean=76.6391 median=0 std=104.3419
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=187 p95=253 p99=255

#### `89.1`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 13,746 | negative: 0
- min=0 max=255 mean=52.6555 median=0 std=92.6966
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=63 p95=253 p99=254

#### `73`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 15,926 | negative: 0
- min=0 max=255 mean=32.0664 median=0 std=75.615
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=252 p99=254

#### `0.222`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 17,678 | negative: 0
- min=0 max=255 mean=16.7743 median=0 std=55.5833
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=177.1 p99=253

#### `0.223`  (`int64`)
- unique: 248 | missing: 0 (0.0%) | zeros: 18,870 | negative: 0
- min=0 max=255 mean=7.2756 median=0 std=36.5782
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=14 p99=243.02

#### `0.224`  (`int64`)
- unique: 201 | missing: 0 (0.0%) | zeros: 19,563 | negative: 0
- min=0 max=255 mean=2.6904 median=0 std=21.8015
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=134

#### `0.225`  (`int64`)
- unique: 70 | missing: 0 (0.0%) | zeros: 19,918 | negative: 0
- flags: near-constant
- min=0 max=254 mean=0.4558 median=0 std=8.6254
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.226`  (`int64`)
- unique: 4 | missing: 0 (0.0%) | zeros: 19,996 | negative: 0
- flags: near-constant
- all values (n=4): 0×19996, 132×1, 139×1, 221×1

#### `0.227`  (`int64`)
- unique: 3 | missing: 0 (0.0%) | zeros: 19,997 | negative: 0
- flags: near-constant
- all values (n=3): 0×19997, 31×1, 77×1

#### `0.228`  (`int64`)
- unique: 13 | missing: 0 (0.0%) | zeros: 19,986 | negative: 0
- flags: near-constant
- all values (n=13): 0×19986, 1×1, 15×1, 20×1, 58×2, 68×1, 71×1, 90×1, 106×1, 137×1, 209×1, 239×1, 254×1

#### `0.229`  (`int64`)
- unique: 71 | missing: 0 (0.0%) | zeros: 19,911 | negative: 0
- flags: near-constant
- min=0 max=255 mean=0.532 median=0 std=9.8265
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.230`  (`int64`)
- unique: 127 | missing: 0 (0.0%) | zeros: 19,729 | negative: 0
- min=0 max=255 mean=1.8711 median=0 std=19.5387
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=37.02

#### `0.231`  (`int64`)
- unique: 211 | missing: 0 (0.0%) | zeros: 19,333 | negative: 0
- min=0 max=255 mean=4.6277 median=0 std=30.0964
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=226.04

#### `0.232`  (`int64`)
- unique: 244 | missing: 0 (0.0%) | zeros: 18,576 | negative: 0
- min=0 max=255 mean=9.8884 median=0 std=43.4572
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=59 p99=253

#### `0.233`  (`int64`)
- unique: 255 | missing: 0 (0.0%) | zeros: 17,337 | negative: 0
- min=0 max=255 mean=19.7845 median=0 std=60.5979
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=211 p99=253

#### `48`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 15,560 | negative: 0
- min=0 max=255 mean=35.0269 median=0 std=78.6201
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=252 p99=254

#### `247`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 13,290 | negative: 0
- min=0 max=255 mean=55.2042 median=0 std=93.9521
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=78 p95=253 p99=255

#### `252.4`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 10,875 | negative: 0
- min=0 max=255 mean=78.5041 median=0 std=104.5798
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=192 p95=254 p99=255

#### `159.1`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 9,001 | negative: 0
- min=0 max=255 mean=98.7263 median=27 std=110.0704
- quantiles: p1=0 p5=0 p25=0 p50=27 p75=238 p95=254 p99=255

#### `0.234`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 7,994 | negative: 0
- min=0 max=255 mean=110.0509 median=69 std=111.247
- quantiles: p1=0 p5=0 p25=0 p50=69 p75=250 p95=254 p99=255

#### `0.235`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 7,847 | negative: 0
- min=0 max=255 mean=111.0335 median=72 std=111.2896
- quantiles: p1=0 p5=0 p25=0 p50=72 p75=250 p95=254 p99=255

#### `0.236`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 8,177 | negative: 0
- min=0 max=255 mean=105.571 median=55 std=110.282
- quantiles: p1=0 p5=0 p25=0 p50=55 p75=245 p95=254 p99=255

#### `0.237`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 8,559 | negative: 0
- min=0 max=255 mean=99.6222 median=40 std=109.0691
- quantiles: p1=0 p5=0 p25=0 p50=40 p75=238 p95=254 p99=255

#### `0.238`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 8,471 | negative: 0
- min=0 max=255 mean=99.7531 median=40 std=108.8828
- quantiles: p1=0 p5=0 p25=0 p50=40 p75=236 p95=254 p99=255

#### `0.239`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 8,052 | negative: 0
- min=0 max=255 mean=104.8899 median=57 std=109.528
- quantiles: p1=0 p5=0 p25=0 p50=57 p75=244 p95=254 p99=255

#### `0.240`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 7,593 | negative: 0
- min=0 max=255 mean=111.8611 median=80 std=110.6663
- quantiles: p1=0 p5=0 p25=0 p50=80 p75=250 p95=254 p99=255

#### `79`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 7,852 | negative: 0
- min=0 max=255 mean=111.1374 median=73 std=111.3251
- quantiles: p1=0 p5=0 p25=0 p50=73 p75=251 p95=254 p99=255

#### `236`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 9,142 | negative: 0
- min=0 max=255 mean=98.6966 median=29 std=109.9135
- quantiles: p1=0 p5=0 p25=0 p50=29 p75=239 p95=254 p99=255

#### `252.5`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 11,358 | negative: 0
- min=0 max=255 mean=76.4148 median=0 std=104.514
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=187 p95=254 p99=255

#### `252.6`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 13,810 | negative: 0
- min=0 max=255 mean=52.729 median=0 std=92.832
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=63.5 p95=253 p99=254

#### `249`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 16,000 | negative: 0
- min=0 max=255 mean=31.6604 median=0 std=75.1307
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=252 p99=254

#### `198`  (`int64`)
- unique: 254 | missing: 0 (0.0%) | zeros: 17,767 | negative: 0
- min=0 max=255 mean=15.6835 median=0 std=53.6389
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=160 p99=253

#### `16`  (`int64`)
- unique: 234 | missing: 0 (0.0%) | zeros: 19,023 | negative: 0
- min=0 max=255 mean=6.1823 median=0 std=33.4946
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=233

#### `0.241`  (`int64`)
- unique: 171 | missing: 0 (0.0%) | zeros: 19,658 | negative: 0
- min=0 max=255 mean=1.94 median=0 std=18.2905
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=72.02

#### `0.242`  (`int64`)
- unique: 57 | missing: 0 (0.0%) | zeros: 19,933 | negative: 0
- flags: near-constant
- min=0 max=255 mean=0.314 median=0 std=7.0869
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.243`  (`int64`)
- unique: 5 | missing: 0 (0.0%) | zeros: 19,995 | negative: 0
- flags: near-constant
- all values (n=5): 0×19995, 25×1, 56×1, 116×1, 125×1

#### `0.244`  (`int64`)
- unique: 3 | missing: 0 (0.0%) | zeros: 19,997 | negative: 0
- flags: near-constant
- all values (n=3): 0×19997, 1×1, 185×1

#### `0.245`  (`int64`)
- unique: 14 | missing: 0 (0.0%) | zeros: 19,985 | negative: 0
- flags: near-constant
- all values (n=14): 0×19985, 2×1, 3×1, 6×1, 15×1, 43×1, 45×1, 54×1, 112×1, 121×1, 150×1, 178×1, 223×1, 254×2

#### `0.246`  (`int64`)
- unique: 64 | missing: 0 (0.0%) | zeros: 19,913 | negative: 0
- flags: near-constant
- min=0 max=254 mean=0.5721 median=0 std=10.4636
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=0

#### `0.247`  (`int64`)
- unique: 127 | missing: 0 (0.0%) | zeros: 19,748 | negative: 0
- min=0 max=255 mean=1.7778 median=0 std=18.7231
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=43

#### `0.248`  (`int64`)
- unique: 215 | missing: 0 (0.0%) | zeros: 19,363 | negative: 0
- min=0 max=255 mean=4.3437 median=0 std=29.1735
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=0 p99=222

#### `0.249`  (`int64`)
- unique: 245 | missing: 0 (0.0%) | zeros: 18,551 | negative: 0
- min=0 max=255 mean=10.0186 median=0 std=43.7551
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=62 p99=253

#### `41`  (`int64`)
- unique: 254 | missing: 0 (0.0%) | zeros: 17,218 | negative: 0
- min=0 max=255 mean=20.7976 median=0 std=62.3196
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=226 p99=254

#### `193`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 15,167 | negative: 0
- min=0 max=255 mean=37.438 median=0 std=80.5369
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=0 p95=253 p99=254

#### `252.7`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 12,778 | negative: 0
- min=0 max=255 mean=60.0888 median=0 std=96.5004
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=109 p95=253 p99=255

#### `199`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 10,481 | negative: 0
- min=0 max=255 mean=83.984 median=0 std=106.7816
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=209 p95=254 p99=255

#### `22`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 8,936 | negative: 0
- min=0 max=255 mean=100.3359 median=32 std=110.4846
- quantiles: p1=0 p5=0 p25=0 p50=32 p75=241 p95=254 p99=255

#### `0.250`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 8,605 | negative: 0
- min=0 max=255 mean=103.1486 median=41 std=110.7483
- quantiles: p1=0 p5=0 p25=0 p50=41 p75=243 p95=254 p99=255

#### `0.251`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 9,063 | negative: 0
- min=0 max=255 mean=94.4055 median=23 std=108.1749
- quantiles: p1=0 p5=0 p25=0 p50=23 p75=227.5 p95=254 p99=255

#### `0.252`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 9,803 | negative: 0
- min=0 max=255 mean=83.5646 median=5 std=104.3931
- quantiles: p1=0 p5=0 p25=0 p50=5 p75=198 p95=254 p99=255

#### `0.253`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 10,215 | negative: 0
- min=0 max=255 mean=79.2283 median=0 std=103.0931
- quantiles: p1=0 p5=0 p25=0 p50=0 p75=186 p95=254 p99=255

#### `0.254`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 9,878 | negative: 0
- min=0 max=255 mean=84.1964 median=4 std=105.1474
- quantiles: p1=0 p5=0 p25=0 p50=4 p75=202 p95=254 p99=255

#### `12`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 8,926 | negative: 0
- min=0 max=255 mean=94.2113 median=25 std=107.3852
- quantiles: p1=0 p5=0 p25=0 p50=25 p75=224 p95=254 p99=255

#### `135`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 8,132 | negative: 0
- min=0 max=255 mean=104.788 median=56 std=109.7066
- quantiles: p1=0 p5=0 p25=0 p50=56 p75=242 p95=254 p99=255

#### `248`  (`int64`)
- unique: 256 | missing: 0 (0.0%) | zeros: 8,280 | negative: 0
- min=0 max=255 mean=106.3019 median=58 std=110.6608
- quantiles: p1=0 p5=0 p25=0 p50=58 p75=247 p95=254 p99=255

### 4. Data Quality Flags
- **constant columns**: 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.10, 0.11, 0.16, 0.17, 0.18, 0.19, 0.20, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.30, 0.31, 0.32, 0.33, 0.50, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.82, 0.83, 0.84, 0.85, 0.86, 0.111, 0.112, 0.136, 0.137, 0.159, 0.160, 0.161
- **near constant columns**: 0.12, 0.13, 0.14, 0.15, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.40, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.59, 0.60, 0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.76, 0.77, 0.78, 0.79, 0.80, 0.81, 0.87, 0.88, 0.89, 0.90, 0.91, 0.106, 0.107, 0.108, 0.109, 0.110, 0.113, 0.114, 0.115, 0.116, 0.117, 0.132, 0.133, 0.134, 0.135, 0.138, 0.139, 0.140, 0.157, 0.158, 0.162, 0.163, 0.181, 0.182, 0.183, 0.184, 0.185, 0.186, 0.205, 0.206, 0.207, 0.208, 0.209, 0.225, 0.226, 0.227, 0.228, 0.229, 0.242, 0.243, 0.244, 0.245, 0.246
- **extremely high cardinality columns**: none
- **likely id columns**: none
- **likely timestamp columns**: none
- **likely categorical columns**: none
- **likely target outcome columns**: none
- **columns with possible post outcome info**: none

### 5. Relationships / Duplicates
- duplicate rows: 0 (0.0%)

### 9. Dataset-Specific Summary
**Potentially useful for:**
- general tabular features (no strong signal columns detected)
**Potential limitations:**
- no obvious temporal information detected
- no obvious target/outcome column detected
- 51 constant column(s) present

## scenarios.json

### 1. File Information
- type: json | size: 7.63 KB | rows: 10 | columns: 1

### 2-3. Column Schema & Unique Values

- **scenarios** -- ERROR analyzing column: TypeError: unhashable type: 'dict'

### 4. Data Quality Flags
- **constant columns**: none
- **near constant columns**: none
- **extremely high cardinality columns**: none
- **likely id columns**: none
- **likely timestamp columns**: none
- **likely categorical columns**: none
- **likely target outcome columns**: none
- **columns with possible post outcome info**: none

### 5. Relationships / Duplicates
- duplicate rows: 0 (0.0%)

### 9. Dataset-Specific Summary
**Potentially useful for:**
- general tabular features (no strong signal columns detected)
**Potential limitations:**
- no obvious temporal information detected
- no obvious target/outcome column detected

## test.parquet

### 1. File Information
- type: parquet | size: 288.09 KB | rows: 8,250 | columns: 23

### 2-3. Column Schema & Unique Values

#### `record_id`  (`object`)
- unique: 8,250 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: extremely-high-cardinality, id-like (name)
- top 20 values:
  - `rec_004902`: 1 (0.012%) 
  - `rec_047500`: 1 (0.012%) 
  - `rec_039793`: 1 (0.012%) 
  - `rec_049281`: 1 (0.012%) 
  - `rec_008213`: 1 (0.012%) 
  - `rec_053398`: 1 (0.012%) 
  - `rec_040865`: 1 (0.012%) 
  - `rec_028064`: 1 (0.012%) 
  - `rec_019066`: 1 (0.012%) 
  - `rec_036281`: 1 (0.012%) 
  - `rec_006008`: 1 (0.012%) 
  - `rec_003390`: 1 (0.012%) 
  - `rec_014880`: 1 (0.012%) 
  - `rec_030584`: 1 (0.012%) 
  - `rec_001372`: 1 (0.012%) 
  - `rec_044428`: 1 (0.012%) 
  - `rec_049579`: 1 (0.012%) 
  - `rec_000095`: 1 (0.012%) 
  - `rec_007741`: 1 (0.012%) 
  - `rec_037880`: 1 (0.012%) 

#### `customer_id`  (`int64`)
- unique: 7,944 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: extremely-high-cardinality, id-like (name)
- min=1,019 max=99,983 mean=50,416.2352 median=50,231 std=28,557.9719
- quantiles: p1=1,869.03 p5=5,706.6 p25=26,031.75 p50=50,231 p75=75,083 p95=94,710.7 p99=99,041.63

#### `customer_archetype`  (`object`)
- unique: 3 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: categorical-like (name)
- top 3 values:
  - `reliable`: 5770 (69.939%) 
  - `occasional`: 1663 (20.158%) 
  - `high_risk`: 817 (9.903%) 

#### `customer_ltv`  (`float64`)
- unique: 8,247 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: extremely-high-cardinality
- min=5,009.68 max=99,991.43 mean=49,975.1416 median=45,638.87 std=26,347.1941
- quantiles: p1=6,873.7361 p5=12,400.868 p25=27,599.405 p50=45,638.87 p75=72,688.935 p95=94,407.082 p99=98,914.3686

#### `customer_failure_rate`  (`float64`)
- unique: 3 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: target-like (name)
- all values (n=3): 0.04×5770, 0.15×1663, 0.35×817

#### `customer_opted_out`  (`bool`)
- unique: 1 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: CONSTANT
- top 1 values:
  - `False`: 8250 (100.0%) 

#### `subscription_id`  (`object`)
- unique: 7,944 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: extremely-high-cardinality, id-like (name)
- top 20 values:
  - `sub_sim_48769`: 4 (0.048%) 
  - `sub_sim_55568`: 3 (0.036%) 
  - `sub_sim_34739`: 3 (0.036%) 
  - `sub_sim_75029`: 3 (0.036%) 
  - `sub_sim_82070`: 3 (0.036%) 
  - `sub_sim_27223`: 3 (0.036%) 
  - `sub_sim_9532`: 2 (0.024%) 
  - `sub_sim_60683`: 2 (0.024%) 
  - `sub_sim_24396`: 2 (0.024%) 
  - `sub_sim_89149`: 2 (0.024%) 
  - `sub_sim_95403`: 2 (0.024%) 
  - `sub_sim_67749`: 2 (0.024%) 
  - `sub_sim_19003`: 2 (0.024%) 
  - `sub_sim_43529`: 2 (0.024%) 
  - `sub_sim_77990`: 2 (0.024%) 
  - `sub_sim_74657`: 2 (0.024%) 
  - `sub_sim_93361`: 2 (0.024%) 
  - `sub_sim_97398`: 2 (0.024%) 
  - `sub_sim_2216`: 2 (0.024%) 
  - `sub_sim_5505`: 2 (0.024%) 

#### `subscription_paid_count`  (`int64`)
- unique: 9 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=9): 1×926, 2×966, 3×881, 4×890, 5×915, 6×915, 7×942, 8×880, 9×935

#### `subscription_remaining_count`  (`int64`)
- unique: 9 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=9): 2×976, 3×939, 4×919, 5×902, 6×915, 7×864, 8×911, 9×861, 10×963

#### `amount`  (`float64`)
- unique: 6 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=6): 999.0×1370, 2499.0×1416, 4999.0×1374, 9999.0×1390, 24999.0×1366, 59999.0×1334

#### `failure_reason`  (`object`)
- unique: 6 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: target-like (name)
- top 6 values:
  - `temporary_bank_failure`: 3264 (39.564%) 
  - `insufficient_funds`: 2469 (29.927%) 
  - `invalid_payment_method`: 1244 (15.079%) 
  - `network_error`: 574 (6.958%) 
  - `card_expired`: 437 (5.297%) 
  - `authentication_failed`: 262 (3.176%) 

#### `attempt_count`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: CONSTANT
- all values (n=1): 1×8250

#### `hours_since_first_failure`  (`float64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 8,250 | negative: 0
- flags: CONSTANT, target-like (name)
- all values (n=1): 0.0×8250

#### `interventions_count`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 8,250 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×8250

#### `is_weekend`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 5,895 | negative: 0
- all values (n=2): 0×5895, 1×2355

#### `action_taken`  (`object`)
- unique: 7 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: target-like (name)
- top 7 values:
  - `RETRY`: 3943 (47.794%) 
  - `PAYMENT_LINK`: 1625 (19.697%) 
  - `REQUEST_ALTERNATE_METHOD`: 997 (12.085%) 
  - `SEND_REMINDER`: 760 (9.212%) 
  - `WAIT`: 373 (4.521%) 
  - `ESCALATE_TO_HUMAN`: 310 (3.758%) 
  - `STOP_RECOVERY`: 242 (2.933%) 

#### `recovered`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 5,427 | negative: 0
- flags: target-like (name)
- all values (n=2): 0×5427, 1×2823

#### `recovered_amount`  (`float64`)
- unique: 7 | missing: 0 (0.0%) | zeros: 5,427 | negative: 0
- flags: target-like (name)
- all values (n=7): 0.0×5427, 999.0×456, 2499.0×454, 4999.0×474, 9999.0×478, 24999.0×461, 59999.0×500

#### `recovery_time_hours`  (`float64`)
- unique: 7 | missing: 0 (0.0%) | zeros: 242 | negative: 0
- flags: timestamp-like, target-like (name)
- all values (n=7): 0.0×242, 1.0×3943, 6.0×85, 12.0×760, 24.0×1913, 36.0×997, 48.0×310

#### `action_cost`  (`float64`)
- unique: 6 | missing: 0 (0.0%) | zeros: 615 | negative: 0
- flags: target-like (name)
- all values (n=6): 0.0×615, 5.0×3943, 10.0×760, 15.0×1625, 20.0×997, 150.0×310

#### `friction`  (`float64`)
- unique: 6 | missing: 0 (0.0%) | zeros: 615 | negative: 0
- all values (n=6): 0.0×615, 0.2×3943, 0.8×310, 1.0×1625, 1.2×760, 1.5×997

#### `reward`  (`float64`)
- unique: 37 | missing: 0 (0.0%) | zeros: 615 | negative: 4,812
- min=-230 max=59,974 mean=6,011.0469 median=-25 std=14,940.179
- quantiles: p1=-230 p5=-170 p25=-75 p50=-25 p75=2,384 p95=59,829 p99=59,974

#### `provenance`  (`object`)
- unique: 1 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: CONSTANT
- top 1 values:
  - `HELD_OUT_OFFLINE_EVAL`: 8250 (100.0%) 

### 4. Data Quality Flags
- **constant columns**: customer_opted_out, attempt_count, hours_since_first_failure, interventions_count, provenance
- **near constant columns**: none
- **extremely high cardinality columns**: record_id, customer_id, customer_ltv, subscription_id
- **likely id columns**: record_id, customer_id, subscription_id
- **likely timestamp columns**: recovery_time_hours
- **likely categorical columns**: record_id, customer_archetype, customer_opted_out, subscription_id, failure_reason, action_taken, provenance
- **likely target outcome columns**: customer_failure_rate, failure_reason, hours_since_first_failure, action_taken, recovered, recovered_amount, recovery_time_hours, action_cost
- **columns with possible post outcome info**: none

### 5. Relationships / Duplicates
- duplicate rows: 0 (0.0%)
- candidate ID columns (unique counts):
  - `record_id`: 8,250 unique
  - `customer_id`: 7,944 unique
  - `subscription_id`: 7,944 unique
- inferred entity relationships:
  - `customer_id` -> 7,944 unique entities

### 6. Target / Outcome Analysis
**`recovered`** (binary)
- 0: 5,427 (65.782%)
- 1: 2,823 (34.218%)
**`recovered_amount`** (numeric)
- min=0 max=59,999 mean=6,092.5063 median=0 std=14,954.3259

### 9. Dataset-Specific Summary
**Potentially useful for:**
- customer/payment context (entity id columns present)
- sequential/temporal information (timestamp-like columns present)
- outcome information (candidate target columns present)
**Potential limitations:**
- 5 constant column(s) present

## train.parquet

### 1. File Information
- type: parquet | size: 1.24 MB | rows: 38,500 | columns: 23

### 2-3. Column Schema & Unique Values

#### `record_id`  (`object`)
- unique: 38,500 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: extremely-high-cardinality, id-like (name)
- top 20 values:
  - `rec_005483`: 1 (0.003%) 
  - `rec_045710`: 1 (0.003%) 
  - `rec_047410`: 1 (0.003%) 
  - `rec_037223`: 1 (0.003%) 
  - `rec_049498`: 1 (0.003%) 
  - `rec_048805`: 1 (0.003%) 
  - `rec_041229`: 1 (0.003%) 
  - `rec_008288`: 1 (0.003%) 
  - `rec_010561`: 1 (0.003%) 
  - `rec_021932`: 1 (0.003%) 
  - `rec_040776`: 1 (0.003%) 
  - `rec_019910`: 1 (0.003%) 
  - `rec_029682`: 1 (0.003%) 
  - `rec_036039`: 1 (0.003%) 
  - `rec_038509`: 1 (0.003%) 
  - `rec_045939`: 1 (0.003%) 
  - `rec_037524`: 1 (0.003%) 
  - `rec_001374`: 1 (0.003%) 
  - `rec_039698`: 1 (0.003%) 
  - `rec_008842`: 1 (0.003%) 

#### `customer_id`  (`int64`)
- unique: 31,720 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: id-like (name)
- min=1,003 max=99,998 mean=50,620.2931 median=50,818 std=28,584.5723
- quantiles: p1=2,064.98 p5=5,988.6 p25=25,971.75 p50=50,818 p75=75,188.25 p95=95,072.3 p99=98,978.06

#### `customer_archetype`  (`object`)
- unique: 3 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: categorical-like (name)
- top 3 values:
  - `reliable`: 26872 (69.797%) 
  - `occasional`: 7645 (19.857%) 
  - `high_risk`: 3983 (10.345%) 

#### `customer_ltv`  (`float64`)
- unique: 38,422 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: extremely-high-cardinality
- min=5,001.81 max=99,999.04 mean=49,541.37 median=45,582.795 std=26,065.1532
- quantiles: p1=6,892.691 p5=12,495.2425 p25=27,246.83 p50=45,582.795 p75=71,746.765 p95=94,292.058 p99=98,955.7513

#### `customer_failure_rate`  (`float64`)
- unique: 3 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: target-like (name)
- all values (n=3): 0.04×26872, 0.15×7645, 0.35×3983

#### `customer_opted_out`  (`bool`)
- unique: 1 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: CONSTANT
- top 1 values:
  - `False`: 38500 (100.0%) 

#### `subscription_id`  (`object`)
- unique: 31,720 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: id-like (name)
- top 20 values:
  - `sub_sim_50013`: 6 (0.016%) 
  - `sub_sim_79032`: 5 (0.013%) 
  - `sub_sim_70276`: 4 (0.01%) 
  - `sub_sim_2217`: 4 (0.01%) 
  - `sub_sim_85115`: 4 (0.01%) 
  - `sub_sim_8068`: 4 (0.01%) 
  - `sub_sim_78912`: 4 (0.01%) 
  - `sub_sim_59461`: 4 (0.01%) 
  - `sub_sim_73240`: 4 (0.01%) 
  - `sub_sim_26304`: 4 (0.01%) 
  - `sub_sim_65514`: 4 (0.01%) 
  - `sub_sim_62009`: 4 (0.01%) 
  - `sub_sim_37272`: 4 (0.01%) 
  - `sub_sim_83333`: 4 (0.01%) 
  - `sub_sim_65356`: 4 (0.01%) 
  - `sub_sim_72543`: 4 (0.01%) 
  - `sub_sim_1331`: 4 (0.01%) 
  - `sub_sim_54223`: 4 (0.01%) 
  - `sub_sim_79773`: 4 (0.01%) 
  - `sub_sim_34355`: 4 (0.01%) 

#### `subscription_paid_count`  (`int64`)
- unique: 9 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=9): 1×4292, 2×4275, 3×4364, 4×4199, 5×4252, 6×4314, 7×4347, 8×4285, 9×4172

#### `subscription_remaining_count`  (`int64`)
- unique: 9 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=9): 2×4285, 3×4270, 4×4280, 5×4163, 6×4248, 7×4251, 8×4384, 9×4384, 10×4235

#### `amount`  (`float64`)
- unique: 6 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=6): 999.0×6332, 2499.0×6558, 4999.0×6503, 9999.0×6351, 24999.0×6425, 59999.0×6331

#### `failure_reason`  (`object`)
- unique: 6 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: target-like (name)
- top 6 values:
  - `temporary_bank_failure`: 15236 (39.574%) 
  - `insufficient_funds`: 11524 (29.932%) 
  - `invalid_payment_method`: 5801 (15.068%) 
  - `network_error`: 2677 (6.953%) 
  - `card_expired`: 2037 (5.291%) 
  - `authentication_failed`: 1225 (3.182%) 

#### `attempt_count`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: CONSTANT
- all values (n=1): 1×38500

#### `hours_since_first_failure`  (`float64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 38,500 | negative: 0
- flags: CONSTANT, target-like (name)
- all values (n=1): 0.0×38500

#### `interventions_count`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 38,500 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×38500

#### `is_weekend`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 27,655 | negative: 0
- all values (n=2): 0×27655, 1×10845

#### `action_taken`  (`object`)
- unique: 7 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: target-like (name)
- top 7 values:
  - `RETRY`: 18628 (48.384%) 
  - `PAYMENT_LINK`: 7627 (19.81%) 
  - `REQUEST_ALTERNATE_METHOD`: 4579 (11.894%) 
  - `SEND_REMINDER`: 3501 (9.094%) 
  - `WAIT`: 1736 (4.509%) 
  - `ESCALATE_TO_HUMAN`: 1367 (3.551%) 
  - `STOP_RECOVERY`: 1062 (2.758%) 

#### `recovered`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 25,325 | negative: 0
- flags: target-like (name)
- all values (n=2): 0×25325, 1×13175

#### `recovered_amount`  (`float64`)
- unique: 7 | missing: 0 (0.0%) | zeros: 25,325 | negative: 0
- flags: target-like (name)
- all values (n=7): 0.0×25325, 999.0×2105, 2499.0×2179, 4999.0×2239, 9999.0×2110, 24999.0×2202, 59999.0×2340

#### `recovery_time_hours`  (`float64`)
- unique: 7 | missing: 0 (0.0%) | zeros: 1,062 | negative: 0
- flags: timestamp-like, target-like (name)
- all values (n=7): 0.0×1062, 1.0×18628, 6.0×448, 12.0×3501, 24.0×8915, 36.0×4579, 48.0×1367

#### `action_cost`  (`float64`)
- unique: 6 | missing: 0 (0.0%) | zeros: 2,798 | negative: 0
- flags: target-like (name)
- all values (n=6): 0.0×2798, 5.0×18628, 10.0×3501, 15.0×7627, 20.0×4579, 150.0×1367

#### `friction`  (`float64`)
- unique: 6 | missing: 0 (0.0%) | zeros: 2,798 | negative: 0
- all values (n=6): 0.0×2798, 0.2×18628, 0.8×1367, 1.0×7627, 1.2×3501, 1.5×4579

#### `reward`  (`float64`)
- unique: 37 | missing: 0 (0.0%) | zeros: 2,798 | negative: 22,527
- min=-230 max=59,974 mean=6,030.239 median=-25 std=14,970.554
- quantiles: p1=-230 p5=-170 p25=-75 p50=-25 p75=2,384 p95=59,829 p99=59,974

#### `provenance`  (`object`)
- unique: 1 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: CONSTANT
- top 1 values:
  - `SYNTHETIC_TRAINING_DATA`: 38500 (100.0%) 

### 4. Data Quality Flags
- **constant columns**: customer_opted_out, attempt_count, hours_since_first_failure, interventions_count, provenance
- **near constant columns**: none
- **extremely high cardinality columns**: record_id, customer_ltv
- **likely id columns**: record_id, customer_id, subscription_id
- **likely timestamp columns**: recovery_time_hours
- **likely categorical columns**: record_id, customer_archetype, customer_opted_out, subscription_id, failure_reason, action_taken, provenance
- **likely target outcome columns**: customer_failure_rate, failure_reason, hours_since_first_failure, action_taken, recovered, recovered_amount, recovery_time_hours, action_cost
- **columns with possible post outcome info**: none

### 5. Relationships / Duplicates
- duplicate rows: 0 (0.0%)
- candidate ID columns (unique counts):
  - `record_id`: 38,500 unique
  - `customer_id`: 31,720 unique
  - `subscription_id`: 31,720 unique
- inferred entity relationships:
  - `customer_id` -> 31,720 unique entities

### 6. Target / Outcome Analysis
**`recovered`** (binary)
- 0: 25,325 (65.779%)
- 1: 13,175 (34.221%)
**`recovered_amount`** (numeric)
- min=0 max=59,999 mean=6,111.2812 median=0 std=14,984.6797

### 9. Dataset-Specific Summary
**Potentially useful for:**
- customer/payment context (entity id columns present)
- sequential/temporal information (timestamp-like columns present)
- outcome information (candidate target columns present)
**Potential limitations:**
- 5 constant column(s) present

## val.parquet

### 1. File Information
- type: parquet | size: 287.67 KB | rows: 8,250 | columns: 23

### 2-3. Column Schema & Unique Values

#### `record_id`  (`object`)
- unique: 8,250 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: extremely-high-cardinality, id-like (name)
- top 20 values:
  - `rec_023722`: 1 (0.012%) 
  - `rec_013420`: 1 (0.012%) 
  - `rec_007836`: 1 (0.012%) 
  - `rec_027925`: 1 (0.012%) 
  - `rec_004386`: 1 (0.012%) 
  - `rec_001014`: 1 (0.012%) 
  - `rec_013375`: 1 (0.012%) 
  - `rec_022687`: 1 (0.012%) 
  - `rec_027769`: 1 (0.012%) 
  - `rec_048963`: 1 (0.012%) 
  - `rec_013885`: 1 (0.012%) 
  - `rec_001991`: 1 (0.012%) 
  - `rec_013724`: 1 (0.012%) 
  - `rec_041338`: 1 (0.012%) 
  - `rec_011658`: 1 (0.012%) 
  - `rec_014321`: 1 (0.012%) 
  - `rec_033284`: 1 (0.012%) 
  - `rec_048657`: 1 (0.012%) 
  - `rec_005618`: 1 (0.012%) 
  - `rec_051416`: 1 (0.012%) 

#### `customer_id`  (`int64`)
- unique: 7,913 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: extremely-high-cardinality, id-like (name)
- min=1,004 max=99,994 mean=50,236.4646 median=50,458 std=28,420.1953
- quantiles: p1=1,907.37 p5=6,243.9 p25=25,337.75 p50=50,458 p75=74,696.75 p95=94,715.2 p99=98,681.51

#### `customer_archetype`  (`object`)
- unique: 3 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: categorical-like (name)
- top 3 values:
  - `reliable`: 5750 (69.697%) 
  - `occasional`: 1637 (19.842%) 
  - `high_risk`: 863 (10.461%) 

#### `customer_ltv`  (`float64`)
- unique: 8,246 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: extremely-high-cardinality
- min=5,003.13 max=99,994.12 mean=49,288.207 median=45,400.255 std=25,959.0708
- quantiles: p1=7,494.9309 p5=12,476.351 p25=26,618.9225 p50=45,400.255 p75=70,927.8625 p95=94,151.3265 p99=98,923.2826

#### `customer_failure_rate`  (`float64`)
- unique: 3 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: target-like (name)
- all values (n=3): 0.04×5750, 0.15×1637, 0.35×863

#### `customer_opted_out`  (`bool`)
- unique: 1 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: CONSTANT
- top 1 values:
  - `False`: 8250 (100.0%) 

#### `subscription_id`  (`object`)
- unique: 7,913 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: extremely-high-cardinality, id-like (name)
- top 20 values:
  - `sub_sim_96904`: 3 (0.036%) 
  - `sub_sim_54909`: 3 (0.036%) 
  - `sub_sim_45076`: 3 (0.036%) 
  - `sub_sim_85638`: 3 (0.036%) 
  - `sub_sim_13043`: 3 (0.036%) 
  - `sub_sim_47150`: 3 (0.036%) 
  - `sub_sim_31716`: 3 (0.036%) 
  - `sub_sim_60656`: 3 (0.036%) 
  - `sub_sim_59934`: 3 (0.036%) 
  - `sub_sim_58171`: 3 (0.036%) 
  - `sub_sim_73916`: 2 (0.024%) 
  - `sub_sim_40550`: 2 (0.024%) 
  - `sub_sim_9613`: 2 (0.024%) 
  - `sub_sim_16369`: 2 (0.024%) 
  - `sub_sim_93314`: 2 (0.024%) 
  - `sub_sim_38644`: 2 (0.024%) 
  - `sub_sim_95597`: 2 (0.024%) 
  - `sub_sim_36902`: 2 (0.024%) 
  - `sub_sim_20623`: 2 (0.024%) 
  - `sub_sim_10223`: 2 (0.024%) 

#### `subscription_paid_count`  (`int64`)
- unique: 9 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=9): 1×921, 2×918, 3×896, 4×857, 5×940, 6×981, 7×910, 8×942, 9×885

#### `subscription_remaining_count`  (`int64`)
- unique: 9 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=9): 2×874, 3×910, 4×942, 5×960, 6×885, 7×929, 8×923, 9×905, 10×922

#### `amount`  (`float64`)
- unique: 6 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- all values (n=6): 999.0×1370, 2499.0×1369, 4999.0×1400, 9999.0×1361, 24999.0×1397, 59999.0×1353

#### `failure_reason`  (`object`)
- unique: 6 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: target-like (name)
- top 6 values:
  - `temporary_bank_failure`: 3265 (39.576%) 
  - `insufficient_funds`: 2469 (29.927%) 
  - `invalid_payment_method`: 1243 (15.067%) 
  - `network_error`: 573 (6.945%) 
  - `card_expired`: 437 (5.297%) 
  - `authentication_failed`: 263 (3.188%) 

#### `attempt_count`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 0 | negative: 0
- flags: CONSTANT
- all values (n=1): 1×8250

#### `hours_since_first_failure`  (`float64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 8,250 | negative: 0
- flags: CONSTANT, target-like (name)
- all values (n=1): 0.0×8250

#### `interventions_count`  (`int64`)
- unique: 1 | missing: 0 (0.0%) | zeros: 8,250 | negative: 0
- flags: CONSTANT
- all values (n=1): 0×8250

#### `is_weekend`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 6,008 | negative: 0
- all values (n=2): 0×6008, 1×2242

#### `action_taken`  (`object`)
- unique: 7 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: target-like (name)
- top 7 values:
  - `RETRY`: 4029 (48.836%) 
  - `PAYMENT_LINK`: 1562 (18.933%) 
  - `REQUEST_ALTERNATE_METHOD`: 962 (11.661%) 
  - `SEND_REMINDER`: 786 (9.527%) 
  - `WAIT`: 394 (4.776%) 
  - `ESCALATE_TO_HUMAN`: 291 (3.527%) 
  - `STOP_RECOVERY`: 226 (2.739%) 

#### `recovered`  (`int64`)
- unique: 2 | missing: 0 (0.0%) | zeros: 5,427 | negative: 0
- flags: target-like (name)
- all values (n=2): 0×5427, 1×2823

#### `recovered_amount`  (`float64`)
- unique: 7 | missing: 0 (0.0%) | zeros: 5,427 | negative: 0
- flags: target-like (name)
- all values (n=7): 0.0×5427, 999.0×488, 2499.0×468, 4999.0×479, 9999.0×434, 24999.0×460, 59999.0×494

#### `recovery_time_hours`  (`float64`)
- unique: 7 | missing: 0 (0.0%) | zeros: 226 | negative: 0
- flags: timestamp-like, target-like (name)
- all values (n=7): 0.0×226, 1.0×4029, 6.0×104, 12.0×786, 24.0×1852, 36.0×962, 48.0×291

#### `action_cost`  (`float64`)
- unique: 6 | missing: 0 (0.0%) | zeros: 620 | negative: 0
- flags: target-like (name)
- all values (n=6): 0.0×620, 5.0×4029, 10.0×786, 15.0×1562, 20.0×962, 150.0×291

#### `friction`  (`float64`)
- unique: 6 | missing: 0 (0.0%) | zeros: 620 | negative: 0
- all values (n=6): 0.0×620, 0.2×4029, 0.8×291, 1.0×1562, 1.2×786, 1.5×962

#### `reward`  (`float64`)
- unique: 37 | missing: 0 (0.0%) | zeros: 620 | negative: 4,807
- min=-230 max=59,974 mean=5,923.1724 median=-25 std=14,868.9211
- quantiles: p1=-230 p5=-170 p25=-75 p50=-25 p75=2,384 p95=59,829 p99=59,974

#### `provenance`  (`object`)
- unique: 1 | missing: 0 (0.0%) | zeros: n/a | negative: n/a
- flags: CONSTANT
- top 1 values:
  - `SYNTHETIC_TRAINING_DATA`: 8250 (100.0%) 

### 4. Data Quality Flags
- **constant columns**: customer_opted_out, attempt_count, hours_since_first_failure, interventions_count, provenance
- **near constant columns**: none
- **extremely high cardinality columns**: record_id, customer_id, customer_ltv, subscription_id
- **likely id columns**: record_id, customer_id, subscription_id
- **likely timestamp columns**: recovery_time_hours
- **likely categorical columns**: record_id, customer_archetype, customer_opted_out, subscription_id, failure_reason, action_taken, provenance
- **likely target outcome columns**: customer_failure_rate, failure_reason, hours_since_first_failure, action_taken, recovered, recovered_amount, recovery_time_hours, action_cost
- **columns with possible post outcome info**: none

### 5. Relationships / Duplicates
- duplicate rows: 0 (0.0%)
- candidate ID columns (unique counts):
  - `record_id`: 8,250 unique
  - `customer_id`: 7,913 unique
  - `subscription_id`: 7,913 unique
- inferred entity relationships:
  - `customer_id` -> 7,913 unique entities

### 6. Target / Outcome Analysis
**`recovered`** (binary)
- 0: 5,427 (65.782%)
- 1: 2,823 (34.218%)
**`recovered_amount`** (numeric)
- min=0 max=59,999 mean=6,003.6578 median=0 std=14,883.1742

### 9. Dataset-Specific Summary
**Potentially useful for:**
- customer/payment context (entity id columns present)
- sequential/temporal information (timestamp-like columns present)
- outcome information (candidate target columns present)
**Potential limitations:**
- 5 constant column(s) present

## 10. Comparison Across Datasets

| Dataset | Rows | Columns | Customer ID | Payment ID | Action | Outcome | Timestamp | Sequential info |
|---|---|---|---|---|---|---|---|---|
| .config/.last_update_check.json | ERROR | ERROR | - | - | - | - | - | - |
| bandit_model_metrics.json | 5 | 5 | no | no | no | no | no | no |
| customer_recovery_and_behavioral_dataset.csv | 20,000 | 45 | yes | no | no | no | yes | yes |
| episodes.parquet | 199,757 | 29 | no | no | yes | yes | no | no |
| episodes_test.parquet | 30,061 | 29 | no | no | yes | yes | no | no |
| episodes_train.parquet | 139,910 | 29 | no | no | yes | yes | no | no |
| episodes_val.parquet | 29,786 | 29 | no | no | yes | yes | no | no |
| historical_records.csv | 1,000 | 23 | yes | no | no | yes | no | no |
| historical_records.parquet | 55,000 | 23 | yes | no | no | yes | no | no |
| live_persona_state.json | 50 | 9 | no | no | no | yes | no | no |
| sample_data/anscombe.json | 44 | 3 | no | no | no | no | no | no |
| sample_data/california_housing_test.csv | 3,000 | 9 | no | no | no | no | no | no |
| sample_data/california_housing_train.csv | 17,000 | 9 | no | no | no | no | no | no |
| sample_data/mnist_test.csv | 9,999 | 785 | no | no | no | no | no | no |
| sample_data/mnist_train_small.csv | 19,999 | 785 | no | no | no | no | no | no |
| scenarios.json | 10 | 1 | no | no | no | no | no | no |
| test.parquet | 8,250 | 23 | yes | no | no | yes | no | no |
| train.parquet | 38,500 | 23 | yes | no | no | yes | no | no |
| val.parquet | 8,250 | 23 | yes | no | no | yes | no | no |

**Columns shared (exact name match) across ALL datasets:**
- none

**Pairwise shared columns:**
- `customer_recovery_and_behavioral_dataset.csv` ∩ `episodes.parquet`: failure_reason
- `customer_recovery_and_behavioral_dataset.csv` ∩ `episodes_test.parquet`: failure_reason
- `customer_recovery_and_behavioral_dataset.csv` ∩ `episodes_train.parquet`: failure_reason
- `customer_recovery_and_behavioral_dataset.csv` ∩ `episodes_val.parquet`: failure_reason
- `customer_recovery_and_behavioral_dataset.csv` ∩ `historical_records.csv`: customer_id, failure_reason
- `customer_recovery_and_behavioral_dataset.csv` ∩ `historical_records.parquet`: customer_id, failure_reason
- `customer_recovery_and_behavioral_dataset.csv` ∩ `test.parquet`: customer_id, failure_reason
- `customer_recovery_and_behavioral_dataset.csv` ∩ `train.parquet`: customer_id, failure_reason
- `customer_recovery_and_behavioral_dataset.csv` ∩ `val.parquet`: customer_id, failure_reason
- `episodes.parquet` ∩ `episodes_test.parquet`: account_tenure_days, action, allowed_actions, amount, attempt_count, behavior_prob, consecutive_failures, customer_archetype, customer_failure_rate, customer_ltv, days_since_last_success, done, episode_id, episode_length, episode_return, failure_reason, historical_ltv, hours_since_first_failure, interventions_count, is_first_ever_failure, is_weekend, lifetime_success_rate, opted_out, provenance, recovered_amount, resolved, reward, subscription_paid_count, timestep
- `episodes.parquet` ∩ `episodes_train.parquet`: account_tenure_days, action, allowed_actions, amount, attempt_count, behavior_prob, consecutive_failures, customer_archetype, customer_failure_rate, customer_ltv, days_since_last_success, done, episode_id, episode_length, episode_return, failure_reason, historical_ltv, hours_since_first_failure, interventions_count, is_first_ever_failure, is_weekend, lifetime_success_rate, opted_out, provenance, recovered_amount, resolved, reward, subscription_paid_count, timestep
- `episodes.parquet` ∩ `episodes_val.parquet`: account_tenure_days, action, allowed_actions, amount, attempt_count, behavior_prob, consecutive_failures, customer_archetype, customer_failure_rate, customer_ltv, days_since_last_success, done, episode_id, episode_length, episode_return, failure_reason, historical_ltv, hours_since_first_failure, interventions_count, is_first_ever_failure, is_weekend, lifetime_success_rate, opted_out, provenance, recovered_amount, resolved, reward, subscription_paid_count, timestep
- `episodes.parquet` ∩ `historical_records.csv`: amount, attempt_count, customer_archetype, customer_failure_rate, customer_ltv, failure_reason, hours_since_first_failure, interventions_count, is_weekend, provenance, recovered_amount, reward, subscription_paid_count
- `episodes.parquet` ∩ `historical_records.parquet`: amount, attempt_count, customer_archetype, customer_failure_rate, customer_ltv, failure_reason, hours_since_first_failure, interventions_count, is_weekend, provenance, recovered_amount, reward, subscription_paid_count
- `episodes.parquet` ∩ `test.parquet`: amount, attempt_count, customer_archetype, customer_failure_rate, customer_ltv, failure_reason, hours_since_first_failure, interventions_count, is_weekend, provenance, recovered_amount, reward, subscription_paid_count
- `episodes.parquet` ∩ `train.parquet`: amount, attempt_count, customer_archetype, customer_failure_rate, customer_ltv, failure_reason, hours_since_first_failure, interventions_count, is_weekend, provenance, recovered_amount, reward, subscription_paid_count
- `episodes.parquet` ∩ `val.parquet`: amount, attempt_count, customer_archetype, customer_failure_rate, customer_ltv, failure_reason, hours_since_first_failure, interventions_count, is_weekend, provenance, recovered_amount, reward, subscription_paid_count
- `episodes_test.parquet` ∩ `episodes_train.parquet`: account_tenure_days, action, allowed_actions, amount, attempt_count, behavior_prob, consecutive_failures, customer_archetype, customer_failure_rate, customer_ltv, days_since_last_success, done, episode_id, episode_length, episode_return, failure_reason, historical_ltv, hours_since_first_failure, interventions_count, is_first_ever_failure, is_weekend, lifetime_success_rate, opted_out, provenance, recovered_amount, resolved, reward, subscription_paid_count, timestep
- `episodes_test.parquet` ∩ `episodes_val.parquet`: account_tenure_days, action, allowed_actions, amount, attempt_count, behavior_prob, consecutive_failures, customer_archetype, customer_failure_rate, customer_ltv, days_since_last_success, done, episode_id, episode_length, episode_return, failure_reason, historical_ltv, hours_since_first_failure, interventions_count, is_first_ever_failure, is_weekend, lifetime_success_rate, opted_out, provenance, recovered_amount, resolved, reward, subscription_paid_count, timestep
- `episodes_test.parquet` ∩ `historical_records.csv`: amount, attempt_count, customer_archetype, customer_failure_rate, customer_ltv, failure_reason, hours_since_first_failure, interventions_count, is_weekend, provenance, recovered_amount, reward, subscription_paid_count
- `episodes_test.parquet` ∩ `historical_records.parquet`: amount, attempt_count, customer_archetype, customer_failure_rate, customer_ltv, failure_reason, hours_since_first_failure, interventions_count, is_weekend, provenance, recovered_amount, reward, subscription_paid_count
- `episodes_test.parquet` ∩ `test.parquet`: amount, attempt_count, customer_archetype, customer_failure_rate, customer_ltv, failure_reason, hours_since_first_failure, interventions_count, is_weekend, provenance, recovered_amount, reward, subscription_paid_count
- `episodes_test.parquet` ∩ `train.parquet`: amount, attempt_count, customer_archetype, customer_failure_rate, customer_ltv, failure_reason, hours_since_first_failure, interventions_count, is_weekend, provenance, recovered_amount, reward, subscription_paid_count
- `episodes_test.parquet` ∩ `val.parquet`: amount, attempt_count, customer_archetype, customer_failure_rate, customer_ltv, failure_reason, hours_since_first_failure, interventions_count, is_weekend, provenance, recovered_amount, reward, subscription_paid_count
- `episodes_train.parquet` ∩ `episodes_val.parquet`: account_tenure_days, action, allowed_actions, amount, attempt_count, behavior_prob, consecutive_failures, customer_archetype, customer_failure_rate, customer_ltv, days_since_last_success, done, episode_id, episode_length, episode_return, failure_reason, historical_ltv, hours_since_first_failure, interventions_count, is_first_ever_failure, is_weekend, lifetime_success_rate, opted_out, provenance, recovered_amount, resolved, reward, subscription_paid_count, timestep
- `episodes_train.parquet` ∩ `historical_records.csv`: amount, attempt_count, customer_archetype, customer_failure_rate, customer_ltv, failure_reason, hours_since_first_failure, interventions_count, is_weekend, provenance, recovered_amount, reward, subscription_paid_count
- `episodes_train.parquet` ∩ `historical_records.parquet`: amount, attempt_count, customer_archetype, customer_failure_rate, customer_ltv, failure_reason, hours_since_first_failure, interventions_count, is_weekend, provenance, recovered_amount, reward, subscription_paid_count
- `episodes_train.parquet` ∩ `test.parquet`: amount, attempt_count, customer_archetype, customer_failure_rate, customer_ltv, failure_reason, hours_since_first_failure, interventions_count, is_weekend, provenance, recovered_amount, reward, subscription_paid_count
- `episodes_train.parquet` ∩ `train.parquet`: amount, attempt_count, customer_archetype, customer_failure_rate, customer_ltv, failure_reason, hours_since_first_failure, interventions_count, is_weekend, provenance, recovered_amount, reward, subscription_paid_count
- `episodes_train.parquet` ∩ `val.parquet`: amount, attempt_count, customer_archetype, customer_failure_rate, customer_ltv, failure_reason, hours_since_first_failure, interventions_count, is_weekend, provenance, recovered_amount, reward, subscription_paid_count
- `episodes_val.parquet` ∩ `historical_records.csv`: amount, attempt_count, customer_archetype, customer_failure_rate, customer_ltv, failure_reason, hours_since_first_failure, interventions_count, is_weekend, provenance, recovered_amount, reward, subscription_paid_count
- `episodes_val.parquet` ∩ `historical_records.parquet`: amount, attempt_count, customer_archetype, customer_failure_rate, customer_ltv, failure_reason, hours_since_first_failure, interventions_count, is_weekend, provenance, recovered_amount, reward, subscription_paid_count
- `episodes_val.parquet` ∩ `test.parquet`: amount, attempt_count, customer_archetype, customer_failure_rate, customer_ltv, failure_reason, hours_since_first_failure, interventions_count, is_weekend, provenance, recovered_amount, reward, subscription_paid_count
- `episodes_val.parquet` ∩ `train.parquet`: amount, attempt_count, customer_archetype, customer_failure_rate, customer_ltv, failure_reason, hours_since_first_failure, interventions_count, is_weekend, provenance, recovered_amount, reward, subscription_paid_count
- `episodes_val.parquet` ∩ `val.parquet`: amount, attempt_count, customer_archetype, customer_failure_rate, customer_ltv, failure_reason, hours_since_first_failure, interventions_count, is_weekend, provenance, recovered_amount, reward, subscription_paid_count
- `historical_records.csv` ∩ `historical_records.parquet`: action_cost, action_taken, amount, attempt_count, customer_archetype, customer_failure_rate, customer_id, customer_ltv, customer_opted_out, failure_reason, friction, hours_since_first_failure, interventions_count, is_weekend, provenance, record_id, recovered, recovered_amount, recovery_time_hours, reward, subscription_id, subscription_paid_count, subscription_remaining_count
- `historical_records.csv` ∩ `test.parquet`: action_cost, action_taken, amount, attempt_count, customer_archetype, customer_failure_rate, customer_id, customer_ltv, customer_opted_out, failure_reason, friction, hours_since_first_failure, interventions_count, is_weekend, provenance, record_id, recovered, recovered_amount, recovery_time_hours, reward, subscription_id, subscription_paid_count, subscription_remaining_count
- `historical_records.csv` ∩ `train.parquet`: action_cost, action_taken, amount, attempt_count, customer_archetype, customer_failure_rate, customer_id, customer_ltv, customer_opted_out, failure_reason, friction, hours_since_first_failure, interventions_count, is_weekend, provenance, record_id, recovered, recovered_amount, recovery_time_hours, reward, subscription_id, subscription_paid_count, subscription_remaining_count
- `historical_records.csv` ∩ `val.parquet`: action_cost, action_taken, amount, attempt_count, customer_archetype, customer_failure_rate, customer_id, customer_ltv, customer_opted_out, failure_reason, friction, hours_since_first_failure, interventions_count, is_weekend, provenance, record_id, recovered, recovered_amount, recovery_time_hours, reward, subscription_id, subscription_paid_count, subscription_remaining_count
- `historical_records.parquet` ∩ `test.parquet`: action_cost, action_taken, amount, attempt_count, customer_archetype, customer_failure_rate, customer_id, customer_ltv, customer_opted_out, failure_reason, friction, hours_since_first_failure, interventions_count, is_weekend, provenance, record_id, recovered, recovered_amount, recovery_time_hours, reward, subscription_id, subscription_paid_count, subscription_remaining_count
- `historical_records.parquet` ∩ `train.parquet`: action_cost, action_taken, amount, attempt_count, customer_archetype, customer_failure_rate, customer_id, customer_ltv, customer_opted_out, failure_reason, friction, hours_since_first_failure, interventions_count, is_weekend, provenance, record_id, recovered, recovered_amount, recovery_time_hours, reward, subscription_id, subscription_paid_count, subscription_remaining_count
- `historical_records.parquet` ∩ `val.parquet`: action_cost, action_taken, amount, attempt_count, customer_archetype, customer_failure_rate, customer_id, customer_ltv, customer_opted_out, failure_reason, friction, hours_since_first_failure, interventions_count, is_weekend, provenance, record_id, recovered, recovered_amount, recovery_time_hours, reward, subscription_id, subscription_paid_count, subscription_remaining_count
- `sample_data/california_housing_test.csv` ∩ `sample_data/california_housing_train.csv`: households, housing_median_age, latitude, longitude, median_house_value, median_income, population, total_bedrooms, total_rooms
- `sample_data/mnist_test.csv` ∩ `sample_data/mnist_train_small.csv`: 0, 0.1, 0.10, 0.100, 0.101, 0.102, 0.103, 0.104, 0.105, 0.106, 0.107, 0.108, 0.109, 0.11, 0.110, 0.111, 0.112, 0.113, 0.114, 0.115, 0.116, 0.117, 0.118, 0.119, 0.12, 0.120, 0.121, 0.122, 0.123, 0.124, 0.125, 0.126, 0.127, 0.128, 0.129, 0.13, 0.130, 0.131, 0.132, 0.133, 0.134, 0.135, 0.136, 0.137, 0.138, 0.139, 0.14, 0.140, 0.141, 0.142, 0.143, 0.144, 0.145, 0.146, 0.147, 0.148, 0.149, 0.15, 0.150, 0.151, 0.152, 0.153, 0.154, 0.155, 0.156, 0.157, 0.158, 0.159, 0.16, 0.160, 0.161, 0.162, 0.163, 0.164, 0.165, 0.166, 0.167, 0.168, 0.169, 0.17, 0.170, 0.171, 0.172, 0.173, 0.174, 0.175, 0.176, 0.177, 0.178, 0.179, 0.18, 0.180, 0.181, 0.182, 0.183, 0.184, 0.185, 0.186, 0.187, 0.188, 0.189, 0.19, 0.190, 0.191, 0.192, 0.193, 0.194, 0.195, 0.196, 0.197, 0.198, 0.199, 0.2, 0.20, 0.200, 0.201, 0.202, 0.203, 0.204, 0.205, 0.206, 0.207, 0.208, 0.209, 0.21, 0.210, 0.211, 0.212, 0.213, 0.214, 0.215, 0.216, 0.217, 0.218, 0.219, 0.22, 0.220, 0.221, 0.222, 0.223, 0.224, 0.225, 0.226, 0.227, 0.228, 0.229, 0.23, 0.230, 0.231, 0.232, 0.233, 0.234, 0.235, 0.236, 0.237, 0.238, 0.239, 0.24, 0.240, 0.241, 0.242, 0.243, 0.244, 0.245, 0.246, 0.247, 0.248, 0.249, 0.25, 0.250, 0.251, 0.252, 0.26, 0.27, 0.28, 0.29, 0.3, 0.30, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.40, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.50, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6, 0.60, 0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.7, 0.70, 0.71, 0.72, 0.73, 0.74, 0.75, 0.76, 0.77, 0.78, 0.79, 0.8, 0.80, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9, 0.90, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 159, 198, 222, 250, 66, 67, 67.1
- `test.parquet` ∩ `train.parquet`: action_cost, action_taken, amount, attempt_count, customer_archetype, customer_failure_rate, customer_id, customer_ltv, customer_opted_out, failure_reason, friction, hours_since_first_failure, interventions_count, is_weekend, provenance, record_id, recovered, recovered_amount, recovery_time_hours, reward, subscription_id, subscription_paid_count, subscription_remaining_count
- `test.parquet` ∩ `val.parquet`: action_cost, action_taken, amount, attempt_count, customer_archetype, customer_failure_rate, customer_id, customer_ltv, customer_opted_out, failure_reason, friction, hours_since_first_failure, interventions_count, is_weekend, provenance, record_id, recovered, recovered_amount, recovery_time_hours, reward, subscription_id, subscription_paid_count, subscription_remaining_count
- `train.parquet` ∩ `val.parquet`: action_cost, action_taken, amount, attempt_count, customer_archetype, customer_failure_rate, customer_id, customer_ltv, customer_opted_out, failure_reason, friction, hours_since_first_failure, interventions_count, is_weekend, provenance, record_id, recovered, recovered_amount, recovery_time_hours, reward, subscription_id, subscription_paid_count, subscription_remaining_count

**Possible similar-meaning / differently-named columns (heuristic, verify manually):**
- `bandit_model_metrics.json.model_type` ~ `customer_recovery_and_behavioral_dataset.csv.model_psychological_diagnosis`
- `customer_recovery_and_behavioral_dataset.csv.ground_truth_recovered_ai_policy` ~ `episodes.parquet.recovered_amount`
- `customer_recovery_and_behavioral_dataset.csv.opted_out_dnd` ~ `episodes.parquet.opted_out`
- `customer_recovery_and_behavioral_dataset.csv.contact_count_24h` ~ `episodes.parquet.interventions_count`
- `customer_recovery_and_behavioral_dataset.csv.contact_count_24h` ~ `episodes.parquet.attempt_count`
- `customer_recovery_and_behavioral_dataset.csv.failure_step` ~ `episodes.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_step` ~ `episodes.parquet.is_first_ever_failure`
- `customer_recovery_and_behavioral_dataset.csv.failure_step` ~ `episodes.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.failure_step` ~ `episodes.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.customer_ltv_inr` ~ `episodes.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_ltv_inr` ~ `episodes.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.customer_ltv_inr` ~ `episodes.parquet.historical_ltv`
- `customer_recovery_and_behavioral_dataset.csv.previous_payment_success_rate` ~ `episodes.parquet.lifetime_success_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_source` ~ `episodes.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_source` ~ `episodes.parquet.is_first_ever_failure`
- `customer_recovery_and_behavioral_dataset.csv.failure_source` ~ `episodes.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.failure_source` ~ `episodes.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `episodes.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `episodes.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `episodes.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `episodes.parquet.episode_id`
- `customer_recovery_and_behavioral_dataset.csv.is_rail_degraded` ~ `episodes.parquet.is_weekend`
- `customer_recovery_and_behavioral_dataset.csv.previous_purchase_count` ~ `episodes.parquet.interventions_count`
- `customer_recovery_and_behavioral_dataset.csv.previous_purchase_count` ~ `episodes.parquet.attempt_count`
- `customer_recovery_and_behavioral_dataset.csv.recommended_recovery_action` ~ `episodes.parquet.action`
- `customer_recovery_and_behavioral_dataset.csv.failure_reason` ~ `episodes.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_reason` ~ `episodes.parquet.is_first_ever_failure`
- `customer_recovery_and_behavioral_dataset.csv.failure_reason` ~ `episodes.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.customer_psychology_archetype` ~ `episodes.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_psychology_archetype` ~ `episodes.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.customer_session_active` ~ `episodes.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_session_active` ~ `episodes.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.amount_inr` ~ `episodes.parquet.amount`
- `customer_recovery_and_behavioral_dataset.csv.amount_inr` ~ `episodes.parquet.recovered_amount`
- `customer_recovery_and_behavioral_dataset.csv.ground_truth_recovered_static` ~ `episodes.parquet.recovered_amount`
- `customer_recovery_and_behavioral_dataset.csv.failure_code` ~ `episodes.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_code` ~ `episodes.parquet.is_first_ever_failure`
- `customer_recovery_and_behavioral_dataset.csv.failure_code` ~ `episodes.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.failure_code` ~ `episodes.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.time_since_failure_minutes` ~ `episodes.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `episodes.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `episodes.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `episodes.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.order_id` ~ `episodes.parquet.episode_id`
- `customer_recovery_and_behavioral_dataset.csv.historical_checkout_abandonment_count` ~ `episodes.parquet.interventions_count`
- `customer_recovery_and_behavioral_dataset.csv.historical_checkout_abandonment_count` ~ `episodes.parquet.historical_ltv`
- `customer_recovery_and_behavioral_dataset.csv.historical_checkout_abandonment_count` ~ `episodes.parquet.attempt_count`
- `customer_recovery_and_behavioral_dataset.csv.case_id` ~ `episodes.parquet.episode_id`
- `customer_recovery_and_behavioral_dataset.csv.is_recoverable` ~ `episodes.parquet.is_first_ever_failure`
- `customer_recovery_and_behavioral_dataset.csv.is_recoverable` ~ `episodes.parquet.is_weekend`
- `customer_recovery_and_behavioral_dataset.csv.ground_truth_recovered_ai_policy` ~ `episodes_test.parquet.recovered_amount`
- `customer_recovery_and_behavioral_dataset.csv.opted_out_dnd` ~ `episodes_test.parquet.opted_out`
- `customer_recovery_and_behavioral_dataset.csv.contact_count_24h` ~ `episodes_test.parquet.interventions_count`
- `customer_recovery_and_behavioral_dataset.csv.contact_count_24h` ~ `episodes_test.parquet.attempt_count`
- `customer_recovery_and_behavioral_dataset.csv.failure_step` ~ `episodes_test.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_step` ~ `episodes_test.parquet.is_first_ever_failure`
- `customer_recovery_and_behavioral_dataset.csv.failure_step` ~ `episodes_test.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.failure_step` ~ `episodes_test.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.customer_ltv_inr` ~ `episodes_test.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_ltv_inr` ~ `episodes_test.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.customer_ltv_inr` ~ `episodes_test.parquet.historical_ltv`
- `customer_recovery_and_behavioral_dataset.csv.previous_payment_success_rate` ~ `episodes_test.parquet.lifetime_success_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_source` ~ `episodes_test.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_source` ~ `episodes_test.parquet.is_first_ever_failure`
- `customer_recovery_and_behavioral_dataset.csv.failure_source` ~ `episodes_test.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.failure_source` ~ `episodes_test.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `episodes_test.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `episodes_test.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `episodes_test.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `episodes_test.parquet.episode_id`
- `customer_recovery_and_behavioral_dataset.csv.is_rail_degraded` ~ `episodes_test.parquet.is_weekend`
- `customer_recovery_and_behavioral_dataset.csv.previous_purchase_count` ~ `episodes_test.parquet.interventions_count`
- `customer_recovery_and_behavioral_dataset.csv.previous_purchase_count` ~ `episodes_test.parquet.attempt_count`
- `customer_recovery_and_behavioral_dataset.csv.recommended_recovery_action` ~ `episodes_test.parquet.action`
- `customer_recovery_and_behavioral_dataset.csv.failure_reason` ~ `episodes_test.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_reason` ~ `episodes_test.parquet.is_first_ever_failure`
- `customer_recovery_and_behavioral_dataset.csv.failure_reason` ~ `episodes_test.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.customer_psychology_archetype` ~ `episodes_test.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_psychology_archetype` ~ `episodes_test.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.customer_session_active` ~ `episodes_test.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_session_active` ~ `episodes_test.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.amount_inr` ~ `episodes_test.parquet.amount`
- `customer_recovery_and_behavioral_dataset.csv.amount_inr` ~ `episodes_test.parquet.recovered_amount`
- `customer_recovery_and_behavioral_dataset.csv.ground_truth_recovered_static` ~ `episodes_test.parquet.recovered_amount`
- `customer_recovery_and_behavioral_dataset.csv.failure_code` ~ `episodes_test.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_code` ~ `episodes_test.parquet.is_first_ever_failure`
- `customer_recovery_and_behavioral_dataset.csv.failure_code` ~ `episodes_test.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.failure_code` ~ `episodes_test.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.time_since_failure_minutes` ~ `episodes_test.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `episodes_test.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `episodes_test.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `episodes_test.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.order_id` ~ `episodes_test.parquet.episode_id`
- `customer_recovery_and_behavioral_dataset.csv.historical_checkout_abandonment_count` ~ `episodes_test.parquet.interventions_count`
- `customer_recovery_and_behavioral_dataset.csv.historical_checkout_abandonment_count` ~ `episodes_test.parquet.historical_ltv`
- `customer_recovery_and_behavioral_dataset.csv.historical_checkout_abandonment_count` ~ `episodes_test.parquet.attempt_count`
- `customer_recovery_and_behavioral_dataset.csv.case_id` ~ `episodes_test.parquet.episode_id`
- `customer_recovery_and_behavioral_dataset.csv.is_recoverable` ~ `episodes_test.parquet.is_first_ever_failure`
- `customer_recovery_and_behavioral_dataset.csv.is_recoverable` ~ `episodes_test.parquet.is_weekend`
- `customer_recovery_and_behavioral_dataset.csv.ground_truth_recovered_ai_policy` ~ `episodes_train.parquet.recovered_amount`
- `customer_recovery_and_behavioral_dataset.csv.opted_out_dnd` ~ `episodes_train.parquet.opted_out`
- `customer_recovery_and_behavioral_dataset.csv.contact_count_24h` ~ `episodes_train.parquet.interventions_count`
- `customer_recovery_and_behavioral_dataset.csv.contact_count_24h` ~ `episodes_train.parquet.attempt_count`
- `customer_recovery_and_behavioral_dataset.csv.failure_step` ~ `episodes_train.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_step` ~ `episodes_train.parquet.is_first_ever_failure`
- `customer_recovery_and_behavioral_dataset.csv.failure_step` ~ `episodes_train.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.failure_step` ~ `episodes_train.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.customer_ltv_inr` ~ `episodes_train.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_ltv_inr` ~ `episodes_train.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.customer_ltv_inr` ~ `episodes_train.parquet.historical_ltv`
- `customer_recovery_and_behavioral_dataset.csv.previous_payment_success_rate` ~ `episodes_train.parquet.lifetime_success_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_source` ~ `episodes_train.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_source` ~ `episodes_train.parquet.is_first_ever_failure`
- `customer_recovery_and_behavioral_dataset.csv.failure_source` ~ `episodes_train.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.failure_source` ~ `episodes_train.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `episodes_train.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `episodes_train.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `episodes_train.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `episodes_train.parquet.episode_id`
- `customer_recovery_and_behavioral_dataset.csv.is_rail_degraded` ~ `episodes_train.parquet.is_weekend`
- `customer_recovery_and_behavioral_dataset.csv.previous_purchase_count` ~ `episodes_train.parquet.interventions_count`
- `customer_recovery_and_behavioral_dataset.csv.previous_purchase_count` ~ `episodes_train.parquet.attempt_count`
- `customer_recovery_and_behavioral_dataset.csv.recommended_recovery_action` ~ `episodes_train.parquet.action`
- `customer_recovery_and_behavioral_dataset.csv.failure_reason` ~ `episodes_train.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_reason` ~ `episodes_train.parquet.is_first_ever_failure`
- `customer_recovery_and_behavioral_dataset.csv.failure_reason` ~ `episodes_train.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.customer_psychology_archetype` ~ `episodes_train.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_psychology_archetype` ~ `episodes_train.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.customer_session_active` ~ `episodes_train.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_session_active` ~ `episodes_train.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.amount_inr` ~ `episodes_train.parquet.amount`
- `customer_recovery_and_behavioral_dataset.csv.amount_inr` ~ `episodes_train.parquet.recovered_amount`
- `customer_recovery_and_behavioral_dataset.csv.ground_truth_recovered_static` ~ `episodes_train.parquet.recovered_amount`
- `customer_recovery_and_behavioral_dataset.csv.failure_code` ~ `episodes_train.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_code` ~ `episodes_train.parquet.is_first_ever_failure`
- `customer_recovery_and_behavioral_dataset.csv.failure_code` ~ `episodes_train.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.failure_code` ~ `episodes_train.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.time_since_failure_minutes` ~ `episodes_train.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `episodes_train.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `episodes_train.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `episodes_train.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.order_id` ~ `episodes_train.parquet.episode_id`
- `customer_recovery_and_behavioral_dataset.csv.historical_checkout_abandonment_count` ~ `episodes_train.parquet.interventions_count`
- `customer_recovery_and_behavioral_dataset.csv.historical_checkout_abandonment_count` ~ `episodes_train.parquet.historical_ltv`
- `customer_recovery_and_behavioral_dataset.csv.historical_checkout_abandonment_count` ~ `episodes_train.parquet.attempt_count`
- `customer_recovery_and_behavioral_dataset.csv.case_id` ~ `episodes_train.parquet.episode_id`
- `customer_recovery_and_behavioral_dataset.csv.is_recoverable` ~ `episodes_train.parquet.is_first_ever_failure`
- `customer_recovery_and_behavioral_dataset.csv.is_recoverable` ~ `episodes_train.parquet.is_weekend`
- `customer_recovery_and_behavioral_dataset.csv.ground_truth_recovered_ai_policy` ~ `episodes_val.parquet.recovered_amount`
- `customer_recovery_and_behavioral_dataset.csv.opted_out_dnd` ~ `episodes_val.parquet.opted_out`
- `customer_recovery_and_behavioral_dataset.csv.contact_count_24h` ~ `episodes_val.parquet.interventions_count`
- `customer_recovery_and_behavioral_dataset.csv.contact_count_24h` ~ `episodes_val.parquet.attempt_count`
- `customer_recovery_and_behavioral_dataset.csv.failure_step` ~ `episodes_val.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_step` ~ `episodes_val.parquet.is_first_ever_failure`
- `customer_recovery_and_behavioral_dataset.csv.failure_step` ~ `episodes_val.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.failure_step` ~ `episodes_val.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.customer_ltv_inr` ~ `episodes_val.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_ltv_inr` ~ `episodes_val.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.customer_ltv_inr` ~ `episodes_val.parquet.historical_ltv`
- `customer_recovery_and_behavioral_dataset.csv.previous_payment_success_rate` ~ `episodes_val.parquet.lifetime_success_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_source` ~ `episodes_val.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_source` ~ `episodes_val.parquet.is_first_ever_failure`
- `customer_recovery_and_behavioral_dataset.csv.failure_source` ~ `episodes_val.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.failure_source` ~ `episodes_val.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `episodes_val.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `episodes_val.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `episodes_val.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `episodes_val.parquet.episode_id`
- `customer_recovery_and_behavioral_dataset.csv.is_rail_degraded` ~ `episodes_val.parquet.is_weekend`
- `customer_recovery_and_behavioral_dataset.csv.previous_purchase_count` ~ `episodes_val.parquet.interventions_count`
- `customer_recovery_and_behavioral_dataset.csv.previous_purchase_count` ~ `episodes_val.parquet.attempt_count`
- `customer_recovery_and_behavioral_dataset.csv.recommended_recovery_action` ~ `episodes_val.parquet.action`
- `customer_recovery_and_behavioral_dataset.csv.failure_reason` ~ `episodes_val.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_reason` ~ `episodes_val.parquet.is_first_ever_failure`
- `customer_recovery_and_behavioral_dataset.csv.failure_reason` ~ `episodes_val.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.customer_psychology_archetype` ~ `episodes_val.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_psychology_archetype` ~ `episodes_val.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.customer_session_active` ~ `episodes_val.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_session_active` ~ `episodes_val.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.amount_inr` ~ `episodes_val.parquet.amount`
- `customer_recovery_and_behavioral_dataset.csv.amount_inr` ~ `episodes_val.parquet.recovered_amount`
- `customer_recovery_and_behavioral_dataset.csv.ground_truth_recovered_static` ~ `episodes_val.parquet.recovered_amount`
- `customer_recovery_and_behavioral_dataset.csv.failure_code` ~ `episodes_val.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_code` ~ `episodes_val.parquet.is_first_ever_failure`
- `customer_recovery_and_behavioral_dataset.csv.failure_code` ~ `episodes_val.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.failure_code` ~ `episodes_val.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.time_since_failure_minutes` ~ `episodes_val.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `episodes_val.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `episodes_val.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `episodes_val.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.order_id` ~ `episodes_val.parquet.episode_id`
- `customer_recovery_and_behavioral_dataset.csv.historical_checkout_abandonment_count` ~ `episodes_val.parquet.interventions_count`
- `customer_recovery_and_behavioral_dataset.csv.historical_checkout_abandonment_count` ~ `episodes_val.parquet.historical_ltv`
- `customer_recovery_and_behavioral_dataset.csv.historical_checkout_abandonment_count` ~ `episodes_val.parquet.attempt_count`
- `customer_recovery_and_behavioral_dataset.csv.case_id` ~ `episodes_val.parquet.episode_id`
- `customer_recovery_and_behavioral_dataset.csv.is_recoverable` ~ `episodes_val.parquet.is_first_ever_failure`
- `customer_recovery_and_behavioral_dataset.csv.is_recoverable` ~ `episodes_val.parquet.is_weekend`
- `customer_recovery_and_behavioral_dataset.csv.ground_truth_recovered_ai_policy` ~ `historical_records.csv.recovered`
- `customer_recovery_and_behavioral_dataset.csv.ground_truth_recovered_ai_policy` ~ `historical_records.csv.recovered_amount`
- `customer_recovery_and_behavioral_dataset.csv.opted_out_dnd` ~ `historical_records.csv.customer_opted_out`
- `customer_recovery_and_behavioral_dataset.csv.contact_count_24h` ~ `historical_records.csv.interventions_count`
- `customer_recovery_and_behavioral_dataset.csv.contact_count_24h` ~ `historical_records.csv.attempt_count`
- `customer_recovery_and_behavioral_dataset.csv.failure_step` ~ `historical_records.csv.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_step` ~ `historical_records.csv.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.failure_step` ~ `historical_records.csv.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.customer_ltv_inr` ~ `historical_records.csv.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_ltv_inr` ~ `historical_records.csv.customer_id`
- `customer_recovery_and_behavioral_dataset.csv.customer_ltv_inr` ~ `historical_records.csv.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.failure_source` ~ `historical_records.csv.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_source` ~ `historical_records.csv.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.failure_source` ~ `historical_records.csv.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `historical_records.csv.record_id`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `historical_records.csv.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `historical_records.csv.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `historical_records.csv.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `historical_records.csv.customer_opted_out`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `historical_records.csv.subscription_id`
- `customer_recovery_and_behavioral_dataset.csv.is_rail_degraded` ~ `historical_records.csv.is_weekend`
- `customer_recovery_and_behavioral_dataset.csv.previous_purchase_count` ~ `historical_records.csv.interventions_count`
- `customer_recovery_and_behavioral_dataset.csv.previous_purchase_count` ~ `historical_records.csv.attempt_count`
- `customer_recovery_and_behavioral_dataset.csv.recommended_recovery_action` ~ `historical_records.csv.action_cost`
- `customer_recovery_and_behavioral_dataset.csv.recommended_recovery_action` ~ `historical_records.csv.action_taken`
- `customer_recovery_and_behavioral_dataset.csv.failure_reason` ~ `historical_records.csv.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_reason` ~ `historical_records.csv.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.customer_psychology_archetype` ~ `historical_records.csv.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_psychology_archetype` ~ `historical_records.csv.customer_id`
- `customer_recovery_and_behavioral_dataset.csv.customer_psychology_archetype` ~ `historical_records.csv.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.customer_session_active` ~ `historical_records.csv.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_session_active` ~ `historical_records.csv.customer_id`
- `customer_recovery_and_behavioral_dataset.csv.customer_session_active` ~ `historical_records.csv.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.amount_inr` ~ `historical_records.csv.amount`
- `customer_recovery_and_behavioral_dataset.csv.amount_inr` ~ `historical_records.csv.recovered_amount`
- `customer_recovery_and_behavioral_dataset.csv.ground_truth_recovered_static` ~ `historical_records.csv.recovered`
- `customer_recovery_and_behavioral_dataset.csv.ground_truth_recovered_static` ~ `historical_records.csv.recovered_amount`
- `customer_recovery_and_behavioral_dataset.csv.failure_code` ~ `historical_records.csv.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_code` ~ `historical_records.csv.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.failure_code` ~ `historical_records.csv.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.time_since_failure_minutes` ~ `historical_records.csv.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `historical_records.csv.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `historical_records.csv.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `historical_records.csv.customer_id`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `historical_records.csv.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `historical_records.csv.customer_opted_out`
- `customer_recovery_and_behavioral_dataset.csv.order_id` ~ `historical_records.csv.record_id`
- `customer_recovery_and_behavioral_dataset.csv.order_id` ~ `historical_records.csv.customer_id`
- `customer_recovery_and_behavioral_dataset.csv.order_id` ~ `historical_records.csv.subscription_id`
- `customer_recovery_and_behavioral_dataset.csv.historical_checkout_abandonment_count` ~ `historical_records.csv.interventions_count`
- `customer_recovery_and_behavioral_dataset.csv.historical_checkout_abandonment_count` ~ `historical_records.csv.attempt_count`
- `customer_recovery_and_behavioral_dataset.csv.case_id` ~ `historical_records.csv.record_id`
- `customer_recovery_and_behavioral_dataset.csv.case_id` ~ `historical_records.csv.customer_id`
- `customer_recovery_and_behavioral_dataset.csv.case_id` ~ `historical_records.csv.subscription_id`
- `customer_recovery_and_behavioral_dataset.csv.is_recoverable` ~ `historical_records.csv.is_weekend`
- `customer_recovery_and_behavioral_dataset.csv.ground_truth_recovered_ai_policy` ~ `historical_records.parquet.recovered`
- `customer_recovery_and_behavioral_dataset.csv.ground_truth_recovered_ai_policy` ~ `historical_records.parquet.recovered_amount`
- `customer_recovery_and_behavioral_dataset.csv.opted_out_dnd` ~ `historical_records.parquet.customer_opted_out`
- `customer_recovery_and_behavioral_dataset.csv.contact_count_24h` ~ `historical_records.parquet.interventions_count`
- `customer_recovery_and_behavioral_dataset.csv.contact_count_24h` ~ `historical_records.parquet.attempt_count`
- `customer_recovery_and_behavioral_dataset.csv.failure_step` ~ `historical_records.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_step` ~ `historical_records.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.failure_step` ~ `historical_records.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.customer_ltv_inr` ~ `historical_records.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_ltv_inr` ~ `historical_records.parquet.customer_id`
- `customer_recovery_and_behavioral_dataset.csv.customer_ltv_inr` ~ `historical_records.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.failure_source` ~ `historical_records.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_source` ~ `historical_records.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.failure_source` ~ `historical_records.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `historical_records.parquet.record_id`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `historical_records.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `historical_records.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `historical_records.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `historical_records.parquet.customer_opted_out`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `historical_records.parquet.subscription_id`
- `customer_recovery_and_behavioral_dataset.csv.is_rail_degraded` ~ `historical_records.parquet.is_weekend`
- `customer_recovery_and_behavioral_dataset.csv.previous_purchase_count` ~ `historical_records.parquet.interventions_count`
- `customer_recovery_and_behavioral_dataset.csv.previous_purchase_count` ~ `historical_records.parquet.attempt_count`
- `customer_recovery_and_behavioral_dataset.csv.recommended_recovery_action` ~ `historical_records.parquet.action_cost`
- `customer_recovery_and_behavioral_dataset.csv.recommended_recovery_action` ~ `historical_records.parquet.action_taken`
- `customer_recovery_and_behavioral_dataset.csv.failure_reason` ~ `historical_records.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_reason` ~ `historical_records.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.customer_psychology_archetype` ~ `historical_records.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_psychology_archetype` ~ `historical_records.parquet.customer_id`
- `customer_recovery_and_behavioral_dataset.csv.customer_psychology_archetype` ~ `historical_records.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.customer_session_active` ~ `historical_records.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_session_active` ~ `historical_records.parquet.customer_id`
- `customer_recovery_and_behavioral_dataset.csv.customer_session_active` ~ `historical_records.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.amount_inr` ~ `historical_records.parquet.amount`
- `customer_recovery_and_behavioral_dataset.csv.amount_inr` ~ `historical_records.parquet.recovered_amount`
- `customer_recovery_and_behavioral_dataset.csv.ground_truth_recovered_static` ~ `historical_records.parquet.recovered`
- `customer_recovery_and_behavioral_dataset.csv.ground_truth_recovered_static` ~ `historical_records.parquet.recovered_amount`
- `customer_recovery_and_behavioral_dataset.csv.failure_code` ~ `historical_records.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_code` ~ `historical_records.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.failure_code` ~ `historical_records.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.time_since_failure_minutes` ~ `historical_records.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `historical_records.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `historical_records.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `historical_records.parquet.customer_id`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `historical_records.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `historical_records.parquet.customer_opted_out`
- `customer_recovery_and_behavioral_dataset.csv.order_id` ~ `historical_records.parquet.record_id`
- `customer_recovery_and_behavioral_dataset.csv.order_id` ~ `historical_records.parquet.customer_id`
- `customer_recovery_and_behavioral_dataset.csv.order_id` ~ `historical_records.parquet.subscription_id`
- `customer_recovery_and_behavioral_dataset.csv.historical_checkout_abandonment_count` ~ `historical_records.parquet.interventions_count`
- `customer_recovery_and_behavioral_dataset.csv.historical_checkout_abandonment_count` ~ `historical_records.parquet.attempt_count`
- `customer_recovery_and_behavioral_dataset.csv.case_id` ~ `historical_records.parquet.record_id`
- `customer_recovery_and_behavioral_dataset.csv.case_id` ~ `historical_records.parquet.customer_id`
- `customer_recovery_and_behavioral_dataset.csv.case_id` ~ `historical_records.parquet.subscription_id`
- `customer_recovery_and_behavioral_dataset.csv.is_recoverable` ~ `historical_records.parquet.is_weekend`
- `customer_recovery_and_behavioral_dataset.csv.ground_truth_recovered_ai_policy` ~ `test.parquet.recovered`
- `customer_recovery_and_behavioral_dataset.csv.ground_truth_recovered_ai_policy` ~ `test.parquet.recovered_amount`
- `customer_recovery_and_behavioral_dataset.csv.opted_out_dnd` ~ `test.parquet.customer_opted_out`
- `customer_recovery_and_behavioral_dataset.csv.contact_count_24h` ~ `test.parquet.interventions_count`
- `customer_recovery_and_behavioral_dataset.csv.contact_count_24h` ~ `test.parquet.attempt_count`
- `customer_recovery_and_behavioral_dataset.csv.failure_step` ~ `test.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_step` ~ `test.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.failure_step` ~ `test.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.customer_ltv_inr` ~ `test.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_ltv_inr` ~ `test.parquet.customer_id`
- `customer_recovery_and_behavioral_dataset.csv.customer_ltv_inr` ~ `test.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.failure_source` ~ `test.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_source` ~ `test.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.failure_source` ~ `test.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `test.parquet.record_id`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `test.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `test.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `test.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `test.parquet.customer_opted_out`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `test.parquet.subscription_id`
- `customer_recovery_and_behavioral_dataset.csv.is_rail_degraded` ~ `test.parquet.is_weekend`
- `customer_recovery_and_behavioral_dataset.csv.previous_purchase_count` ~ `test.parquet.interventions_count`
- `customer_recovery_and_behavioral_dataset.csv.previous_purchase_count` ~ `test.parquet.attempt_count`
- `customer_recovery_and_behavioral_dataset.csv.recommended_recovery_action` ~ `test.parquet.action_cost`
- `customer_recovery_and_behavioral_dataset.csv.recommended_recovery_action` ~ `test.parquet.action_taken`
- `customer_recovery_and_behavioral_dataset.csv.failure_reason` ~ `test.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_reason` ~ `test.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.customer_psychology_archetype` ~ `test.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_psychology_archetype` ~ `test.parquet.customer_id`
- `customer_recovery_and_behavioral_dataset.csv.customer_psychology_archetype` ~ `test.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.customer_session_active` ~ `test.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_session_active` ~ `test.parquet.customer_id`
- `customer_recovery_and_behavioral_dataset.csv.customer_session_active` ~ `test.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.amount_inr` ~ `test.parquet.amount`
- `customer_recovery_and_behavioral_dataset.csv.amount_inr` ~ `test.parquet.recovered_amount`
- `customer_recovery_and_behavioral_dataset.csv.ground_truth_recovered_static` ~ `test.parquet.recovered`
- `customer_recovery_and_behavioral_dataset.csv.ground_truth_recovered_static` ~ `test.parquet.recovered_amount`
- `customer_recovery_and_behavioral_dataset.csv.failure_code` ~ `test.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_code` ~ `test.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.failure_code` ~ `test.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.time_since_failure_minutes` ~ `test.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `test.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `test.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `test.parquet.customer_id`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `test.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `test.parquet.customer_opted_out`
- `customer_recovery_and_behavioral_dataset.csv.order_id` ~ `test.parquet.record_id`
- `customer_recovery_and_behavioral_dataset.csv.order_id` ~ `test.parquet.customer_id`
- `customer_recovery_and_behavioral_dataset.csv.order_id` ~ `test.parquet.subscription_id`
- `customer_recovery_and_behavioral_dataset.csv.historical_checkout_abandonment_count` ~ `test.parquet.interventions_count`
- `customer_recovery_and_behavioral_dataset.csv.historical_checkout_abandonment_count` ~ `test.parquet.attempt_count`
- `customer_recovery_and_behavioral_dataset.csv.case_id` ~ `test.parquet.record_id`
- `customer_recovery_and_behavioral_dataset.csv.case_id` ~ `test.parquet.customer_id`
- `customer_recovery_and_behavioral_dataset.csv.case_id` ~ `test.parquet.subscription_id`
- `customer_recovery_and_behavioral_dataset.csv.is_recoverable` ~ `test.parquet.is_weekend`
- `customer_recovery_and_behavioral_dataset.csv.ground_truth_recovered_ai_policy` ~ `train.parquet.recovered`
- `customer_recovery_and_behavioral_dataset.csv.ground_truth_recovered_ai_policy` ~ `train.parquet.recovered_amount`
- `customer_recovery_and_behavioral_dataset.csv.opted_out_dnd` ~ `train.parquet.customer_opted_out`
- `customer_recovery_and_behavioral_dataset.csv.contact_count_24h` ~ `train.parquet.interventions_count`
- `customer_recovery_and_behavioral_dataset.csv.contact_count_24h` ~ `train.parquet.attempt_count`
- `customer_recovery_and_behavioral_dataset.csv.failure_step` ~ `train.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_step` ~ `train.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.failure_step` ~ `train.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.customer_ltv_inr` ~ `train.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_ltv_inr` ~ `train.parquet.customer_id`
- `customer_recovery_and_behavioral_dataset.csv.customer_ltv_inr` ~ `train.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.failure_source` ~ `train.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_source` ~ `train.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.failure_source` ~ `train.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `train.parquet.record_id`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `train.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `train.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `train.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `train.parquet.customer_opted_out`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `train.parquet.subscription_id`
- `customer_recovery_and_behavioral_dataset.csv.is_rail_degraded` ~ `train.parquet.is_weekend`
- `customer_recovery_and_behavioral_dataset.csv.previous_purchase_count` ~ `train.parquet.interventions_count`
- `customer_recovery_and_behavioral_dataset.csv.previous_purchase_count` ~ `train.parquet.attempt_count`
- `customer_recovery_and_behavioral_dataset.csv.recommended_recovery_action` ~ `train.parquet.action_cost`
- `customer_recovery_and_behavioral_dataset.csv.recommended_recovery_action` ~ `train.parquet.action_taken`
- `customer_recovery_and_behavioral_dataset.csv.failure_reason` ~ `train.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_reason` ~ `train.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.customer_psychology_archetype` ~ `train.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_psychology_archetype` ~ `train.parquet.customer_id`
- `customer_recovery_and_behavioral_dataset.csv.customer_psychology_archetype` ~ `train.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.customer_session_active` ~ `train.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_session_active` ~ `train.parquet.customer_id`
- `customer_recovery_and_behavioral_dataset.csv.customer_session_active` ~ `train.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.amount_inr` ~ `train.parquet.amount`
- `customer_recovery_and_behavioral_dataset.csv.amount_inr` ~ `train.parquet.recovered_amount`
- `customer_recovery_and_behavioral_dataset.csv.ground_truth_recovered_static` ~ `train.parquet.recovered`
- `customer_recovery_and_behavioral_dataset.csv.ground_truth_recovered_static` ~ `train.parquet.recovered_amount`
- `customer_recovery_and_behavioral_dataset.csv.failure_code` ~ `train.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_code` ~ `train.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.failure_code` ~ `train.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.time_since_failure_minutes` ~ `train.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `train.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `train.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `train.parquet.customer_id`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `train.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `train.parquet.customer_opted_out`
- `customer_recovery_and_behavioral_dataset.csv.order_id` ~ `train.parquet.record_id`
- `customer_recovery_and_behavioral_dataset.csv.order_id` ~ `train.parquet.customer_id`
- `customer_recovery_and_behavioral_dataset.csv.order_id` ~ `train.parquet.subscription_id`
- `customer_recovery_and_behavioral_dataset.csv.historical_checkout_abandonment_count` ~ `train.parquet.interventions_count`
- `customer_recovery_and_behavioral_dataset.csv.historical_checkout_abandonment_count` ~ `train.parquet.attempt_count`
- `customer_recovery_and_behavioral_dataset.csv.case_id` ~ `train.parquet.record_id`
- `customer_recovery_and_behavioral_dataset.csv.case_id` ~ `train.parquet.customer_id`
- `customer_recovery_and_behavioral_dataset.csv.case_id` ~ `train.parquet.subscription_id`
- `customer_recovery_and_behavioral_dataset.csv.is_recoverable` ~ `train.parquet.is_weekend`
- `customer_recovery_and_behavioral_dataset.csv.ground_truth_recovered_ai_policy` ~ `val.parquet.recovered`
- `customer_recovery_and_behavioral_dataset.csv.ground_truth_recovered_ai_policy` ~ `val.parquet.recovered_amount`
- `customer_recovery_and_behavioral_dataset.csv.opted_out_dnd` ~ `val.parquet.customer_opted_out`
- `customer_recovery_and_behavioral_dataset.csv.contact_count_24h` ~ `val.parquet.interventions_count`
- `customer_recovery_and_behavioral_dataset.csv.contact_count_24h` ~ `val.parquet.attempt_count`
- `customer_recovery_and_behavioral_dataset.csv.failure_step` ~ `val.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_step` ~ `val.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.failure_step` ~ `val.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.customer_ltv_inr` ~ `val.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_ltv_inr` ~ `val.parquet.customer_id`
- `customer_recovery_and_behavioral_dataset.csv.customer_ltv_inr` ~ `val.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.failure_source` ~ `val.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_source` ~ `val.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.failure_source` ~ `val.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `val.parquet.record_id`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `val.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `val.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `val.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `val.parquet.customer_opted_out`
- `customer_recovery_and_behavioral_dataset.csv.customer_id` ~ `val.parquet.subscription_id`
- `customer_recovery_and_behavioral_dataset.csv.is_rail_degraded` ~ `val.parquet.is_weekend`
- `customer_recovery_and_behavioral_dataset.csv.previous_purchase_count` ~ `val.parquet.interventions_count`
- `customer_recovery_and_behavioral_dataset.csv.previous_purchase_count` ~ `val.parquet.attempt_count`
- `customer_recovery_and_behavioral_dataset.csv.recommended_recovery_action` ~ `val.parquet.action_cost`
- `customer_recovery_and_behavioral_dataset.csv.recommended_recovery_action` ~ `val.parquet.action_taken`
- `customer_recovery_and_behavioral_dataset.csv.failure_reason` ~ `val.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_reason` ~ `val.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.customer_psychology_archetype` ~ `val.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_psychology_archetype` ~ `val.parquet.customer_id`
- `customer_recovery_and_behavioral_dataset.csv.customer_psychology_archetype` ~ `val.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.customer_session_active` ~ `val.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_session_active` ~ `val.parquet.customer_id`
- `customer_recovery_and_behavioral_dataset.csv.customer_session_active` ~ `val.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.amount_inr` ~ `val.parquet.amount`
- `customer_recovery_and_behavioral_dataset.csv.amount_inr` ~ `val.parquet.recovered_amount`
- `customer_recovery_and_behavioral_dataset.csv.ground_truth_recovered_static` ~ `val.parquet.recovered`
- `customer_recovery_and_behavioral_dataset.csv.ground_truth_recovered_static` ~ `val.parquet.recovered_amount`
- `customer_recovery_and_behavioral_dataset.csv.failure_code` ~ `val.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.failure_code` ~ `val.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.failure_code` ~ `val.parquet.hours_since_first_failure`
- `customer_recovery_and_behavioral_dataset.csv.time_since_failure_minutes` ~ `val.parquet.failure_reason`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `val.parquet.customer_ltv`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `val.parquet.customer_failure_rate`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `val.parquet.customer_id`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `val.parquet.customer_archetype`
- `customer_recovery_and_behavioral_dataset.csv.customer_name` ~ `val.parquet.customer_opted_out`
- `customer_recovery_and_behavioral_dataset.csv.order_id` ~ `val.parquet.record_id`
- `customer_recovery_and_behavioral_dataset.csv.order_id` ~ `val.parquet.customer_id`
- `customer_recovery_and_behavioral_dataset.csv.order_id` ~ `val.parquet.subscription_id`
- `customer_recovery_and_behavioral_dataset.csv.historical_checkout_abandonment_count` ~ `val.parquet.interventions_count`
- `customer_recovery_and_behavioral_dataset.csv.historical_checkout_abandonment_count` ~ `val.parquet.attempt_count`
- `customer_recovery_and_behavioral_dataset.csv.case_id` ~ `val.parquet.record_id`
- `customer_recovery_and_behavioral_dataset.csv.case_id` ~ `val.parquet.customer_id`
- `customer_recovery_and_behavioral_dataset.csv.case_id` ~ `val.parquet.subscription_id`
- `customer_recovery_and_behavioral_dataset.csv.is_recoverable` ~ `val.parquet.is_weekend`
- `episodes.parquet.amount` ~ `episodes_test.parquet.recovered_amount`
- `episodes.parquet.customer_ltv` ~ `episodes_test.parquet.customer_failure_rate`
- `episodes.parquet.customer_ltv` ~ `episodes_test.parquet.customer_archetype`
- `episodes.parquet.customer_ltv` ~ `episodes_test.parquet.historical_ltv`
- `episodes.parquet.recovered_amount` ~ `episodes_test.parquet.amount`
- `episodes.parquet.customer_failure_rate` ~ `episodes_test.parquet.customer_ltv`
- `episodes.parquet.customer_failure_rate` ~ `episodes_test.parquet.customer_archetype`
- `episodes.parquet.customer_failure_rate` ~ `episodes_test.parquet.failure_reason`
- `episodes.parquet.is_first_ever_failure` ~ `episodes_test.parquet.failure_reason`
- `episodes.parquet.is_first_ever_failure` ~ `episodes_test.parquet.is_weekend`
- `episodes.parquet.subscription_paid_count` ~ `episodes_test.parquet.interventions_count`
- `episodes.parquet.subscription_paid_count` ~ `episodes_test.parquet.attempt_count`
- `episodes.parquet.customer_archetype` ~ `episodes_test.parquet.customer_ltv`
- `episodes.parquet.customer_archetype` ~ `episodes_test.parquet.customer_failure_rate`
- `episodes.parquet.interventions_count` ~ `episodes_test.parquet.subscription_paid_count`
- `episodes.parquet.interventions_count` ~ `episodes_test.parquet.attempt_count`
- `episodes.parquet.episode_length` ~ `episodes_test.parquet.episode_return`
- `episodes.parquet.episode_length` ~ `episodes_test.parquet.episode_id`
- `episodes.parquet.failure_reason` ~ `episodes_test.parquet.customer_failure_rate`
- `episodes.parquet.failure_reason` ~ `episodes_test.parquet.is_first_ever_failure`
- `episodes.parquet.failure_reason` ~ `episodes_test.parquet.hours_since_first_failure`
- `episodes.parquet.episode_return` ~ `episodes_test.parquet.episode_length`
- `episodes.parquet.episode_return` ~ `episodes_test.parquet.episode_id`
- `episodes.parquet.episode_id` ~ `episodes_test.parquet.episode_length`
- `episodes.parquet.episode_id` ~ `episodes_test.parquet.episode_return`
- `episodes.parquet.is_weekend` ~ `episodes_test.parquet.is_first_ever_failure`
- `episodes.parquet.hours_since_first_failure` ~ `episodes_test.parquet.failure_reason`
- `episodes.parquet.historical_ltv` ~ `episodes_test.parquet.customer_ltv`
- `episodes.parquet.attempt_count` ~ `episodes_test.parquet.subscription_paid_count`
- `episodes.parquet.attempt_count` ~ `episodes_test.parquet.interventions_count`
- `episodes.parquet.amount` ~ `episodes_train.parquet.recovered_amount`
- `episodes.parquet.customer_ltv` ~ `episodes_train.parquet.customer_failure_rate`
- `episodes.parquet.customer_ltv` ~ `episodes_train.parquet.customer_archetype`
- `episodes.parquet.customer_ltv` ~ `episodes_train.parquet.historical_ltv`
- `episodes.parquet.recovered_amount` ~ `episodes_train.parquet.amount`
- `episodes.parquet.customer_failure_rate` ~ `episodes_train.parquet.customer_ltv`
- `episodes.parquet.customer_failure_rate` ~ `episodes_train.parquet.customer_archetype`
- `episodes.parquet.customer_failure_rate` ~ `episodes_train.parquet.failure_reason`
- `episodes.parquet.is_first_ever_failure` ~ `episodes_train.parquet.failure_reason`
- `episodes.parquet.is_first_ever_failure` ~ `episodes_train.parquet.is_weekend`
- `episodes.parquet.subscription_paid_count` ~ `episodes_train.parquet.interventions_count`
- `episodes.parquet.subscription_paid_count` ~ `episodes_train.parquet.attempt_count`
- `episodes.parquet.customer_archetype` ~ `episodes_train.parquet.customer_ltv`
- `episodes.parquet.customer_archetype` ~ `episodes_train.parquet.customer_failure_rate`
- `episodes.parquet.interventions_count` ~ `episodes_train.parquet.subscription_paid_count`
- `episodes.parquet.interventions_count` ~ `episodes_train.parquet.attempt_count`
- `episodes.parquet.episode_length` ~ `episodes_train.parquet.episode_return`
- `episodes.parquet.episode_length` ~ `episodes_train.parquet.episode_id`
- `episodes.parquet.failure_reason` ~ `episodes_train.parquet.customer_failure_rate`
- `episodes.parquet.failure_reason` ~ `episodes_train.parquet.is_first_ever_failure`
- `episodes.parquet.failure_reason` ~ `episodes_train.parquet.hours_since_first_failure`
- `episodes.parquet.episode_return` ~ `episodes_train.parquet.episode_length`
- `episodes.parquet.episode_return` ~ `episodes_train.parquet.episode_id`
- `episodes.parquet.episode_id` ~ `episodes_train.parquet.episode_length`
- `episodes.parquet.episode_id` ~ `episodes_train.parquet.episode_return`
- `episodes.parquet.is_weekend` ~ `episodes_train.parquet.is_first_ever_failure`
- `episodes.parquet.hours_since_first_failure` ~ `episodes_train.parquet.failure_reason`
- `episodes.parquet.historical_ltv` ~ `episodes_train.parquet.customer_ltv`
- `episodes.parquet.attempt_count` ~ `episodes_train.parquet.subscription_paid_count`
- `episodes.parquet.attempt_count` ~ `episodes_train.parquet.interventions_count`
- `episodes.parquet.amount` ~ `episodes_val.parquet.recovered_amount`
- `episodes.parquet.customer_ltv` ~ `episodes_val.parquet.customer_failure_rate`
- `episodes.parquet.customer_ltv` ~ `episodes_val.parquet.customer_archetype`
- `episodes.parquet.customer_ltv` ~ `episodes_val.parquet.historical_ltv`
- `episodes.parquet.recovered_amount` ~ `episodes_val.parquet.amount`
- `episodes.parquet.customer_failure_rate` ~ `episodes_val.parquet.customer_ltv`
- `episodes.parquet.customer_failure_rate` ~ `episodes_val.parquet.customer_archetype`
- `episodes.parquet.customer_failure_rate` ~ `episodes_val.parquet.failure_reason`
- `episodes.parquet.is_first_ever_failure` ~ `episodes_val.parquet.failure_reason`
- `episodes.parquet.is_first_ever_failure` ~ `episodes_val.parquet.is_weekend`
- `episodes.parquet.subscription_paid_count` ~ `episodes_val.parquet.interventions_count`
- `episodes.parquet.subscription_paid_count` ~ `episodes_val.parquet.attempt_count`
- `episodes.parquet.customer_archetype` ~ `episodes_val.parquet.customer_ltv`
- `episodes.parquet.customer_archetype` ~ `episodes_val.parquet.customer_failure_rate`
- `episodes.parquet.interventions_count` ~ `episodes_val.parquet.subscription_paid_count`
- `episodes.parquet.interventions_count` ~ `episodes_val.parquet.attempt_count`
- `episodes.parquet.episode_length` ~ `episodes_val.parquet.episode_return`
- `episodes.parquet.episode_length` ~ `episodes_val.parquet.episode_id`
- `episodes.parquet.failure_reason` ~ `episodes_val.parquet.customer_failure_rate`
- `episodes.parquet.failure_reason` ~ `episodes_val.parquet.is_first_ever_failure`
- `episodes.parquet.failure_reason` ~ `episodes_val.parquet.hours_since_first_failure`
- `episodes.parquet.episode_return` ~ `episodes_val.parquet.episode_length`
- `episodes.parquet.episode_return` ~ `episodes_val.parquet.episode_id`
- `episodes.parquet.episode_id` ~ `episodes_val.parquet.episode_length`
- `episodes.parquet.episode_id` ~ `episodes_val.parquet.episode_return`
- `episodes.parquet.is_weekend` ~ `episodes_val.parquet.is_first_ever_failure`
- `episodes.parquet.hours_since_first_failure` ~ `episodes_val.parquet.failure_reason`
- `episodes.parquet.historical_ltv` ~ `episodes_val.parquet.customer_ltv`
- `episodes.parquet.attempt_count` ~ `episodes_val.parquet.subscription_paid_count`
- `episodes.parquet.attempt_count` ~ `episodes_val.parquet.interventions_count`
- `episodes.parquet.amount` ~ `historical_records.csv.recovered_amount`
- `episodes.parquet.opted_out` ~ `historical_records.csv.customer_opted_out`
- `episodes.parquet.customer_ltv` ~ `historical_records.csv.customer_failure_rate`
- `episodes.parquet.customer_ltv` ~ `historical_records.csv.customer_id`
- `episodes.parquet.customer_ltv` ~ `historical_records.csv.customer_archetype`
- `episodes.parquet.customer_ltv` ~ `historical_records.csv.customer_opted_out`
- `episodes.parquet.recovered_amount` ~ `historical_records.csv.recovered`
- `episodes.parquet.recovered_amount` ~ `historical_records.csv.amount`
- `episodes.parquet.customer_failure_rate` ~ `historical_records.csv.customer_ltv`
- `episodes.parquet.customer_failure_rate` ~ `historical_records.csv.customer_id`
- `episodes.parquet.customer_failure_rate` ~ `historical_records.csv.customer_archetype`
- `episodes.parquet.customer_failure_rate` ~ `historical_records.csv.failure_reason`
- `episodes.parquet.is_first_ever_failure` ~ `historical_records.csv.failure_reason`
- `episodes.parquet.is_first_ever_failure` ~ `historical_records.csv.is_weekend`
- `episodes.parquet.subscription_paid_count` ~ `historical_records.csv.interventions_count`
- `episodes.parquet.subscription_paid_count` ~ `historical_records.csv.subscription_id`
- `episodes.parquet.subscription_paid_count` ~ `historical_records.csv.subscription_remaining_count`
- `episodes.parquet.subscription_paid_count` ~ `historical_records.csv.attempt_count`
- `episodes.parquet.customer_archetype` ~ `historical_records.csv.customer_ltv`
- `episodes.parquet.customer_archetype` ~ `historical_records.csv.customer_failure_rate`
- `episodes.parquet.customer_archetype` ~ `historical_records.csv.customer_id`
- `episodes.parquet.customer_archetype` ~ `historical_records.csv.customer_opted_out`
- `episodes.parquet.interventions_count` ~ `historical_records.csv.subscription_paid_count`
- `episodes.parquet.interventions_count` ~ `historical_records.csv.subscription_remaining_count`
- `episodes.parquet.interventions_count` ~ `historical_records.csv.attempt_count`
- `episodes.parquet.failure_reason` ~ `historical_records.csv.customer_failure_rate`
- `episodes.parquet.failure_reason` ~ `historical_records.csv.hours_since_first_failure`
- `episodes.parquet.action` ~ `historical_records.csv.action_cost`
- `episodes.parquet.action` ~ `historical_records.csv.action_taken`
- `episodes.parquet.episode_id` ~ `historical_records.csv.record_id`
- `episodes.parquet.episode_id` ~ `historical_records.csv.customer_id`
- `episodes.parquet.episode_id` ~ `historical_records.csv.subscription_id`
- `episodes.parquet.hours_since_first_failure` ~ `historical_records.csv.failure_reason`
- `episodes.parquet.historical_ltv` ~ `historical_records.csv.customer_ltv`
- `episodes.parquet.attempt_count` ~ `historical_records.csv.subscription_paid_count`
- `episodes.parquet.attempt_count` ~ `historical_records.csv.interventions_count`
- `episodes.parquet.attempt_count` ~ `historical_records.csv.subscription_remaining_count`
- `episodes.parquet.amount` ~ `historical_records.parquet.recovered_amount`
- `episodes.parquet.opted_out` ~ `historical_records.parquet.customer_opted_out`
- `episodes.parquet.customer_ltv` ~ `historical_records.parquet.customer_failure_rate`
- `episodes.parquet.customer_ltv` ~ `historical_records.parquet.customer_id`
- `episodes.parquet.customer_ltv` ~ `historical_records.parquet.customer_archetype`
- `episodes.parquet.customer_ltv` ~ `historical_records.parquet.customer_opted_out`
- `episodes.parquet.recovered_amount` ~ `historical_records.parquet.recovered`
- `episodes.parquet.recovered_amount` ~ `historical_records.parquet.amount`
- `episodes.parquet.customer_failure_rate` ~ `historical_records.parquet.customer_ltv`
- `episodes.parquet.customer_failure_rate` ~ `historical_records.parquet.customer_id`
- `episodes.parquet.customer_failure_rate` ~ `historical_records.parquet.customer_archetype`
- `episodes.parquet.customer_failure_rate` ~ `historical_records.parquet.failure_reason`
- `episodes.parquet.is_first_ever_failure` ~ `historical_records.parquet.failure_reason`
- `episodes.parquet.is_first_ever_failure` ~ `historical_records.parquet.is_weekend`
- `episodes.parquet.subscription_paid_count` ~ `historical_records.parquet.interventions_count`
- `episodes.parquet.subscription_paid_count` ~ `historical_records.parquet.subscription_id`
- `episodes.parquet.subscription_paid_count` ~ `historical_records.parquet.subscription_remaining_count`
- `episodes.parquet.subscription_paid_count` ~ `historical_records.parquet.attempt_count`
- `episodes.parquet.customer_archetype` ~ `historical_records.parquet.customer_ltv`
- `episodes.parquet.customer_archetype` ~ `historical_records.parquet.customer_failure_rate`
- `episodes.parquet.customer_archetype` ~ `historical_records.parquet.customer_id`
- `episodes.parquet.customer_archetype` ~ `historical_records.parquet.customer_opted_out`
- `episodes.parquet.interventions_count` ~ `historical_records.parquet.subscription_paid_count`
- `episodes.parquet.interventions_count` ~ `historical_records.parquet.subscription_remaining_count`
- `episodes.parquet.interventions_count` ~ `historical_records.parquet.attempt_count`
- `episodes.parquet.failure_reason` ~ `historical_records.parquet.customer_failure_rate`
- `episodes.parquet.failure_reason` ~ `historical_records.parquet.hours_since_first_failure`
- `episodes.parquet.action` ~ `historical_records.parquet.action_cost`
- `episodes.parquet.action` ~ `historical_records.parquet.action_taken`
- `episodes.parquet.episode_id` ~ `historical_records.parquet.record_id`
- `episodes.parquet.episode_id` ~ `historical_records.parquet.customer_id`
- `episodes.parquet.episode_id` ~ `historical_records.parquet.subscription_id`
- `episodes.parquet.hours_since_first_failure` ~ `historical_records.parquet.failure_reason`
- `episodes.parquet.historical_ltv` ~ `historical_records.parquet.customer_ltv`
- `episodes.parquet.attempt_count` ~ `historical_records.parquet.subscription_paid_count`
- `episodes.parquet.attempt_count` ~ `historical_records.parquet.interventions_count`
- `episodes.parquet.attempt_count` ~ `historical_records.parquet.subscription_remaining_count`
- `episodes.parquet.interventions_count` ~ `live_persona_state.json.seen_interventions`
- `episodes.parquet.amount` ~ `test.parquet.recovered_amount`
- `episodes.parquet.opted_out` ~ `test.parquet.customer_opted_out`
- `episodes.parquet.customer_ltv` ~ `test.parquet.customer_failure_rate`
- `episodes.parquet.customer_ltv` ~ `test.parquet.customer_id`
- `episodes.parquet.customer_ltv` ~ `test.parquet.customer_archetype`
- `episodes.parquet.customer_ltv` ~ `test.parquet.customer_opted_out`
- `episodes.parquet.recovered_amount` ~ `test.parquet.recovered`
- `episodes.parquet.recovered_amount` ~ `test.parquet.amount`
- `episodes.parquet.customer_failure_rate` ~ `test.parquet.customer_ltv`
- `episodes.parquet.customer_failure_rate` ~ `test.parquet.customer_id`
- `episodes.parquet.customer_failure_rate` ~ `test.parquet.customer_archetype`
- `episodes.parquet.customer_failure_rate` ~ `test.parquet.failure_reason`
- `episodes.parquet.is_first_ever_failure` ~ `test.parquet.failure_reason`
- `episodes.parquet.is_first_ever_failure` ~ `test.parquet.is_weekend`
- `episodes.parquet.subscription_paid_count` ~ `test.parquet.interventions_count`
- `episodes.parquet.subscription_paid_count` ~ `test.parquet.subscription_id`
- `episodes.parquet.subscription_paid_count` ~ `test.parquet.subscription_remaining_count`
- `episodes.parquet.subscription_paid_count` ~ `test.parquet.attempt_count`
- `episodes.parquet.customer_archetype` ~ `test.parquet.customer_ltv`
- `episodes.parquet.customer_archetype` ~ `test.parquet.customer_failure_rate`
- `episodes.parquet.customer_archetype` ~ `test.parquet.customer_id`
- `episodes.parquet.customer_archetype` ~ `test.parquet.customer_opted_out`
- `episodes.parquet.interventions_count` ~ `test.parquet.subscription_paid_count`
- `episodes.parquet.interventions_count` ~ `test.parquet.subscription_remaining_count`
- `episodes.parquet.interventions_count` ~ `test.parquet.attempt_count`
- `episodes.parquet.failure_reason` ~ `test.parquet.customer_failure_rate`
- `episodes.parquet.failure_reason` ~ `test.parquet.hours_since_first_failure`
- `episodes.parquet.action` ~ `test.parquet.action_cost`
- `episodes.parquet.action` ~ `test.parquet.action_taken`
- `episodes.parquet.episode_id` ~ `test.parquet.record_id`
- `episodes.parquet.episode_id` ~ `test.parquet.customer_id`
- `episodes.parquet.episode_id` ~ `test.parquet.subscription_id`
- `episodes.parquet.hours_since_first_failure` ~ `test.parquet.failure_reason`
- `episodes.parquet.historical_ltv` ~ `test.parquet.customer_ltv`
- `episodes.parquet.attempt_count` ~ `test.parquet.subscription_paid_count`
- `episodes.parquet.attempt_count` ~ `test.parquet.interventions_count`
- `episodes.parquet.attempt_count` ~ `test.parquet.subscription_remaining_count`
- `episodes.parquet.amount` ~ `train.parquet.recovered_amount`
- `episodes.parquet.opted_out` ~ `train.parquet.customer_opted_out`
- `episodes.parquet.customer_ltv` ~ `train.parquet.customer_failure_rate`
- `episodes.parquet.customer_ltv` ~ `train.parquet.customer_id`
- `episodes.parquet.customer_ltv` ~ `train.parquet.customer_archetype`
- `episodes.parquet.customer_ltv` ~ `train.parquet.customer_opted_out`
- `episodes.parquet.recovered_amount` ~ `train.parquet.recovered`
- `episodes.parquet.recovered_amount` ~ `train.parquet.amount`
- `episodes.parquet.customer_failure_rate` ~ `train.parquet.customer_ltv`
- `episodes.parquet.customer_failure_rate` ~ `train.parquet.customer_id`
- `episodes.parquet.customer_failure_rate` ~ `train.parquet.customer_archetype`
- `episodes.parquet.customer_failure_rate` ~ `train.parquet.failure_reason`
- `episodes.parquet.is_first_ever_failure` ~ `train.parquet.failure_reason`
- `episodes.parquet.is_first_ever_failure` ~ `train.parquet.is_weekend`
- `episodes.parquet.subscription_paid_count` ~ `train.parquet.interventions_count`
- `episodes.parquet.subscription_paid_count` ~ `train.parquet.subscription_id`
- `episodes.parquet.subscription_paid_count` ~ `train.parquet.subscription_remaining_count`
- `episodes.parquet.subscription_paid_count` ~ `train.parquet.attempt_count`
- `episodes.parquet.customer_archetype` ~ `train.parquet.customer_ltv`
- `episodes.parquet.customer_archetype` ~ `train.parquet.customer_failure_rate`
- `episodes.parquet.customer_archetype` ~ `train.parquet.customer_id`
- `episodes.parquet.customer_archetype` ~ `train.parquet.customer_opted_out`
- `episodes.parquet.interventions_count` ~ `train.parquet.subscription_paid_count`
- `episodes.parquet.interventions_count` ~ `train.parquet.subscription_remaining_count`
- `episodes.parquet.interventions_count` ~ `train.parquet.attempt_count`
- `episodes.parquet.failure_reason` ~ `train.parquet.customer_failure_rate`
- `episodes.parquet.failure_reason` ~ `train.parquet.hours_since_first_failure`
- `episodes.parquet.action` ~ `train.parquet.action_cost`
- `episodes.parquet.action` ~ `train.parquet.action_taken`
- `episodes.parquet.episode_id` ~ `train.parquet.record_id`
- `episodes.parquet.episode_id` ~ `train.parquet.customer_id`
- `episodes.parquet.episode_id` ~ `train.parquet.subscription_id`
- `episodes.parquet.hours_since_first_failure` ~ `train.parquet.failure_reason`
- `episodes.parquet.historical_ltv` ~ `train.parquet.customer_ltv`
- `episodes.parquet.attempt_count` ~ `train.parquet.subscription_paid_count`
- `episodes.parquet.attempt_count` ~ `train.parquet.interventions_count`
- `episodes.parquet.attempt_count` ~ `train.parquet.subscription_remaining_count`
- `episodes.parquet.amount` ~ `val.parquet.recovered_amount`
- `episodes.parquet.opted_out` ~ `val.parquet.customer_opted_out`
- `episodes.parquet.customer_ltv` ~ `val.parquet.customer_failure_rate`
- `episodes.parquet.customer_ltv` ~ `val.parquet.customer_id`
- `episodes.parquet.customer_ltv` ~ `val.parquet.customer_archetype`
- `episodes.parquet.customer_ltv` ~ `val.parquet.customer_opted_out`
- `episodes.parquet.recovered_amount` ~ `val.parquet.recovered`
- `episodes.parquet.recovered_amount` ~ `val.parquet.amount`
- `episodes.parquet.customer_failure_rate` ~ `val.parquet.customer_ltv`
- `episodes.parquet.customer_failure_rate` ~ `val.parquet.customer_id`
- `episodes.parquet.customer_failure_rate` ~ `val.parquet.customer_archetype`
- `episodes.parquet.customer_failure_rate` ~ `val.parquet.failure_reason`
- `episodes.parquet.is_first_ever_failure` ~ `val.parquet.failure_reason`
- `episodes.parquet.is_first_ever_failure` ~ `val.parquet.is_weekend`
- `episodes.parquet.subscription_paid_count` ~ `val.parquet.interventions_count`
- `episodes.parquet.subscription_paid_count` ~ `val.parquet.subscription_id`
- `episodes.parquet.subscription_paid_count` ~ `val.parquet.subscription_remaining_count`
- `episodes.parquet.subscription_paid_count` ~ `val.parquet.attempt_count`
- `episodes.parquet.customer_archetype` ~ `val.parquet.customer_ltv`
- `episodes.parquet.customer_archetype` ~ `val.parquet.customer_failure_rate`
- `episodes.parquet.customer_archetype` ~ `val.parquet.customer_id`
- `episodes.parquet.customer_archetype` ~ `val.parquet.customer_opted_out`
- `episodes.parquet.interventions_count` ~ `val.parquet.subscription_paid_count`
- `episodes.parquet.interventions_count` ~ `val.parquet.subscription_remaining_count`
- `episodes.parquet.interventions_count` ~ `val.parquet.attempt_count`
- `episodes.parquet.failure_reason` ~ `val.parquet.customer_failure_rate`
- `episodes.parquet.failure_reason` ~ `val.parquet.hours_since_first_failure`
- `episodes.parquet.action` ~ `val.parquet.action_cost`
- `episodes.parquet.action` ~ `val.parquet.action_taken`
- `episodes.parquet.episode_id` ~ `val.parquet.record_id`
- `episodes.parquet.episode_id` ~ `val.parquet.customer_id`
- `episodes.parquet.episode_id` ~ `val.parquet.subscription_id`
- `episodes.parquet.hours_since_first_failure` ~ `val.parquet.failure_reason`
- `episodes.parquet.historical_ltv` ~ `val.parquet.customer_ltv`
- `episodes.parquet.attempt_count` ~ `val.parquet.subscription_paid_count`
- `episodes.parquet.attempt_count` ~ `val.parquet.interventions_count`
- `episodes.parquet.attempt_count` ~ `val.parquet.subscription_remaining_count`
- `episodes_test.parquet.amount` ~ `episodes_train.parquet.recovered_amount`
- `episodes_test.parquet.customer_ltv` ~ `episodes_train.parquet.customer_failure_rate`
- `episodes_test.parquet.customer_ltv` ~ `episodes_train.parquet.customer_archetype`
- `episodes_test.parquet.customer_ltv` ~ `episodes_train.parquet.historical_ltv`
- `episodes_test.parquet.recovered_amount` ~ `episodes_train.parquet.amount`
- `episodes_test.parquet.customer_failure_rate` ~ `episodes_train.parquet.customer_ltv`
- `episodes_test.parquet.customer_failure_rate` ~ `episodes_train.parquet.customer_archetype`
- `episodes_test.parquet.customer_failure_rate` ~ `episodes_train.parquet.failure_reason`
- `episodes_test.parquet.is_first_ever_failure` ~ `episodes_train.parquet.failure_reason`
- `episodes_test.parquet.is_first_ever_failure` ~ `episodes_train.parquet.is_weekend`
- `episodes_test.parquet.subscription_paid_count` ~ `episodes_train.parquet.interventions_count`
- `episodes_test.parquet.subscription_paid_count` ~ `episodes_train.parquet.attempt_count`
- `episodes_test.parquet.customer_archetype` ~ `episodes_train.parquet.customer_ltv`
- `episodes_test.parquet.customer_archetype` ~ `episodes_train.parquet.customer_failure_rate`
- `episodes_test.parquet.interventions_count` ~ `episodes_train.parquet.subscription_paid_count`
- `episodes_test.parquet.interventions_count` ~ `episodes_train.parquet.attempt_count`
- `episodes_test.parquet.episode_length` ~ `episodes_train.parquet.episode_return`
- `episodes_test.parquet.episode_length` ~ `episodes_train.parquet.episode_id`
- `episodes_test.parquet.failure_reason` ~ `episodes_train.parquet.customer_failure_rate`
- `episodes_test.parquet.failure_reason` ~ `episodes_train.parquet.is_first_ever_failure`
- `episodes_test.parquet.failure_reason` ~ `episodes_train.parquet.hours_since_first_failure`
- `episodes_test.parquet.episode_return` ~ `episodes_train.parquet.episode_length`
- `episodes_test.parquet.episode_return` ~ `episodes_train.parquet.episode_id`
- `episodes_test.parquet.episode_id` ~ `episodes_train.parquet.episode_length`
- `episodes_test.parquet.episode_id` ~ `episodes_train.parquet.episode_return`
- `episodes_test.parquet.is_weekend` ~ `episodes_train.parquet.is_first_ever_failure`
- `episodes_test.parquet.hours_since_first_failure` ~ `episodes_train.parquet.failure_reason`
- `episodes_test.parquet.historical_ltv` ~ `episodes_train.parquet.customer_ltv`
- `episodes_test.parquet.attempt_count` ~ `episodes_train.parquet.subscription_paid_count`
- `episodes_test.parquet.attempt_count` ~ `episodes_train.parquet.interventions_count`
- `episodes_test.parquet.amount` ~ `episodes_val.parquet.recovered_amount`
- `episodes_test.parquet.customer_ltv` ~ `episodes_val.parquet.customer_failure_rate`
- `episodes_test.parquet.customer_ltv` ~ `episodes_val.parquet.customer_archetype`
- `episodes_test.parquet.customer_ltv` ~ `episodes_val.parquet.historical_ltv`
- `episodes_test.parquet.recovered_amount` ~ `episodes_val.parquet.amount`
- `episodes_test.parquet.customer_failure_rate` ~ `episodes_val.parquet.customer_ltv`
- `episodes_test.parquet.customer_failure_rate` ~ `episodes_val.parquet.customer_archetype`
- `episodes_test.parquet.customer_failure_rate` ~ `episodes_val.parquet.failure_reason`
- `episodes_test.parquet.is_first_ever_failure` ~ `episodes_val.parquet.failure_reason`
- `episodes_test.parquet.is_first_ever_failure` ~ `episodes_val.parquet.is_weekend`
- `episodes_test.parquet.subscription_paid_count` ~ `episodes_val.parquet.interventions_count`
- `episodes_test.parquet.subscription_paid_count` ~ `episodes_val.parquet.attempt_count`
- `episodes_test.parquet.customer_archetype` ~ `episodes_val.parquet.customer_ltv`
- `episodes_test.parquet.customer_archetype` ~ `episodes_val.parquet.customer_failure_rate`
- `episodes_test.parquet.interventions_count` ~ `episodes_val.parquet.subscription_paid_count`
- `episodes_test.parquet.interventions_count` ~ `episodes_val.parquet.attempt_count`
- `episodes_test.parquet.episode_length` ~ `episodes_val.parquet.episode_return`
- `episodes_test.parquet.episode_length` ~ `episodes_val.parquet.episode_id`
- `episodes_test.parquet.failure_reason` ~ `episodes_val.parquet.customer_failure_rate`
- `episodes_test.parquet.failure_reason` ~ `episodes_val.parquet.is_first_ever_failure`
- `episodes_test.parquet.failure_reason` ~ `episodes_val.parquet.hours_since_first_failure`
- `episodes_test.parquet.episode_return` ~ `episodes_val.parquet.episode_length`
- `episodes_test.parquet.episode_return` ~ `episodes_val.parquet.episode_id`
- `episodes_test.parquet.episode_id` ~ `episodes_val.parquet.episode_length`
- `episodes_test.parquet.episode_id` ~ `episodes_val.parquet.episode_return`
- `episodes_test.parquet.is_weekend` ~ `episodes_val.parquet.is_first_ever_failure`
- `episodes_test.parquet.hours_since_first_failure` ~ `episodes_val.parquet.failure_reason`
- `episodes_test.parquet.historical_ltv` ~ `episodes_val.parquet.customer_ltv`
- `episodes_test.parquet.attempt_count` ~ `episodes_val.parquet.subscription_paid_count`
- `episodes_test.parquet.attempt_count` ~ `episodes_val.parquet.interventions_count`
- `episodes_test.parquet.amount` ~ `historical_records.csv.recovered_amount`
- `episodes_test.parquet.opted_out` ~ `historical_records.csv.customer_opted_out`
- `episodes_test.parquet.customer_ltv` ~ `historical_records.csv.customer_failure_rate`
- `episodes_test.parquet.customer_ltv` ~ `historical_records.csv.customer_id`
- `episodes_test.parquet.customer_ltv` ~ `historical_records.csv.customer_archetype`
- `episodes_test.parquet.customer_ltv` ~ `historical_records.csv.customer_opted_out`
- `episodes_test.parquet.recovered_amount` ~ `historical_records.csv.recovered`
- `episodes_test.parquet.recovered_amount` ~ `historical_records.csv.amount`
- `episodes_test.parquet.customer_failure_rate` ~ `historical_records.csv.customer_ltv`
- `episodes_test.parquet.customer_failure_rate` ~ `historical_records.csv.customer_id`
- `episodes_test.parquet.customer_failure_rate` ~ `historical_records.csv.customer_archetype`
- `episodes_test.parquet.customer_failure_rate` ~ `historical_records.csv.failure_reason`
- `episodes_test.parquet.is_first_ever_failure` ~ `historical_records.csv.failure_reason`
- `episodes_test.parquet.is_first_ever_failure` ~ `historical_records.csv.is_weekend`
- `episodes_test.parquet.subscription_paid_count` ~ `historical_records.csv.interventions_count`
- `episodes_test.parquet.subscription_paid_count` ~ `historical_records.csv.subscription_id`
- `episodes_test.parquet.subscription_paid_count` ~ `historical_records.csv.subscription_remaining_count`
- `episodes_test.parquet.subscription_paid_count` ~ `historical_records.csv.attempt_count`
- `episodes_test.parquet.customer_archetype` ~ `historical_records.csv.customer_ltv`
- `episodes_test.parquet.customer_archetype` ~ `historical_records.csv.customer_failure_rate`
- `episodes_test.parquet.customer_archetype` ~ `historical_records.csv.customer_id`
- `episodes_test.parquet.customer_archetype` ~ `historical_records.csv.customer_opted_out`
- `episodes_test.parquet.interventions_count` ~ `historical_records.csv.subscription_paid_count`
- `episodes_test.parquet.interventions_count` ~ `historical_records.csv.subscription_remaining_count`
- `episodes_test.parquet.interventions_count` ~ `historical_records.csv.attempt_count`
- `episodes_test.parquet.failure_reason` ~ `historical_records.csv.customer_failure_rate`
- `episodes_test.parquet.failure_reason` ~ `historical_records.csv.hours_since_first_failure`
- `episodes_test.parquet.action` ~ `historical_records.csv.action_cost`
- `episodes_test.parquet.action` ~ `historical_records.csv.action_taken`
- `episodes_test.parquet.episode_id` ~ `historical_records.csv.record_id`
- `episodes_test.parquet.episode_id` ~ `historical_records.csv.customer_id`
- `episodes_test.parquet.episode_id` ~ `historical_records.csv.subscription_id`
- `episodes_test.parquet.hours_since_first_failure` ~ `historical_records.csv.failure_reason`
- `episodes_test.parquet.historical_ltv` ~ `historical_records.csv.customer_ltv`
- `episodes_test.parquet.attempt_count` ~ `historical_records.csv.subscription_paid_count`
- `episodes_test.parquet.attempt_count` ~ `historical_records.csv.interventions_count`
- `episodes_test.parquet.attempt_count` ~ `historical_records.csv.subscription_remaining_count`
- `episodes_test.parquet.amount` ~ `historical_records.parquet.recovered_amount`
- `episodes_test.parquet.opted_out` ~ `historical_records.parquet.customer_opted_out`
- `episodes_test.parquet.customer_ltv` ~ `historical_records.parquet.customer_failure_rate`
- `episodes_test.parquet.customer_ltv` ~ `historical_records.parquet.customer_id`
- `episodes_test.parquet.customer_ltv` ~ `historical_records.parquet.customer_archetype`
- `episodes_test.parquet.customer_ltv` ~ `historical_records.parquet.customer_opted_out`
- `episodes_test.parquet.recovered_amount` ~ `historical_records.parquet.recovered`
- `episodes_test.parquet.recovered_amount` ~ `historical_records.parquet.amount`
- `episodes_test.parquet.customer_failure_rate` ~ `historical_records.parquet.customer_ltv`
- `episodes_test.parquet.customer_failure_rate` ~ `historical_records.parquet.customer_id`
- `episodes_test.parquet.customer_failure_rate` ~ `historical_records.parquet.customer_archetype`
- `episodes_test.parquet.customer_failure_rate` ~ `historical_records.parquet.failure_reason`
- `episodes_test.parquet.is_first_ever_failure` ~ `historical_records.parquet.failure_reason`
- `episodes_test.parquet.is_first_ever_failure` ~ `historical_records.parquet.is_weekend`
- `episodes_test.parquet.subscription_paid_count` ~ `historical_records.parquet.interventions_count`
- `episodes_test.parquet.subscription_paid_count` ~ `historical_records.parquet.subscription_id`
- `episodes_test.parquet.subscription_paid_count` ~ `historical_records.parquet.subscription_remaining_count`
- `episodes_test.parquet.subscription_paid_count` ~ `historical_records.parquet.attempt_count`
- `episodes_test.parquet.customer_archetype` ~ `historical_records.parquet.customer_ltv`
- `episodes_test.parquet.customer_archetype` ~ `historical_records.parquet.customer_failure_rate`
- `episodes_test.parquet.customer_archetype` ~ `historical_records.parquet.customer_id`
- `episodes_test.parquet.customer_archetype` ~ `historical_records.parquet.customer_opted_out`
- `episodes_test.parquet.interventions_count` ~ `historical_records.parquet.subscription_paid_count`
- `episodes_test.parquet.interventions_count` ~ `historical_records.parquet.subscription_remaining_count`
- `episodes_test.parquet.interventions_count` ~ `historical_records.parquet.attempt_count`
- `episodes_test.parquet.failure_reason` ~ `historical_records.parquet.customer_failure_rate`
- `episodes_test.parquet.failure_reason` ~ `historical_records.parquet.hours_since_first_failure`
- `episodes_test.parquet.action` ~ `historical_records.parquet.action_cost`
- `episodes_test.parquet.action` ~ `historical_records.parquet.action_taken`
- `episodes_test.parquet.episode_id` ~ `historical_records.parquet.record_id`
- `episodes_test.parquet.episode_id` ~ `historical_records.parquet.customer_id`
- `episodes_test.parquet.episode_id` ~ `historical_records.parquet.subscription_id`
- `episodes_test.parquet.hours_since_first_failure` ~ `historical_records.parquet.failure_reason`
- `episodes_test.parquet.historical_ltv` ~ `historical_records.parquet.customer_ltv`
- `episodes_test.parquet.attempt_count` ~ `historical_records.parquet.subscription_paid_count`
- `episodes_test.parquet.attempt_count` ~ `historical_records.parquet.interventions_count`
- `episodes_test.parquet.attempt_count` ~ `historical_records.parquet.subscription_remaining_count`
- `episodes_test.parquet.interventions_count` ~ `live_persona_state.json.seen_interventions`
- `episodes_test.parquet.amount` ~ `test.parquet.recovered_amount`
- `episodes_test.parquet.opted_out` ~ `test.parquet.customer_opted_out`
- `episodes_test.parquet.customer_ltv` ~ `test.parquet.customer_failure_rate`
- `episodes_test.parquet.customer_ltv` ~ `test.parquet.customer_id`
- `episodes_test.parquet.customer_ltv` ~ `test.parquet.customer_archetype`
- `episodes_test.parquet.customer_ltv` ~ `test.parquet.customer_opted_out`
- `episodes_test.parquet.recovered_amount` ~ `test.parquet.recovered`
- `episodes_test.parquet.recovered_amount` ~ `test.parquet.amount`
- `episodes_test.parquet.customer_failure_rate` ~ `test.parquet.customer_ltv`
- `episodes_test.parquet.customer_failure_rate` ~ `test.parquet.customer_id`
- `episodes_test.parquet.customer_failure_rate` ~ `test.parquet.customer_archetype`
- `episodes_test.parquet.customer_failure_rate` ~ `test.parquet.failure_reason`
- `episodes_test.parquet.is_first_ever_failure` ~ `test.parquet.failure_reason`
- `episodes_test.parquet.is_first_ever_failure` ~ `test.parquet.is_weekend`
- `episodes_test.parquet.subscription_paid_count` ~ `test.parquet.interventions_count`
- `episodes_test.parquet.subscription_paid_count` ~ `test.parquet.subscription_id`
- `episodes_test.parquet.subscription_paid_count` ~ `test.parquet.subscription_remaining_count`
- `episodes_test.parquet.subscription_paid_count` ~ `test.parquet.attempt_count`
- `episodes_test.parquet.customer_archetype` ~ `test.parquet.customer_ltv`
- `episodes_test.parquet.customer_archetype` ~ `test.parquet.customer_failure_rate`
- `episodes_test.parquet.customer_archetype` ~ `test.parquet.customer_id`
- `episodes_test.parquet.customer_archetype` ~ `test.parquet.customer_opted_out`
- `episodes_test.parquet.interventions_count` ~ `test.parquet.subscription_paid_count`
- `episodes_test.parquet.interventions_count` ~ `test.parquet.subscription_remaining_count`
- `episodes_test.parquet.interventions_count` ~ `test.parquet.attempt_count`
- `episodes_test.parquet.failure_reason` ~ `test.parquet.customer_failure_rate`
- `episodes_test.parquet.failure_reason` ~ `test.parquet.hours_since_first_failure`
- `episodes_test.parquet.action` ~ `test.parquet.action_cost`
- `episodes_test.parquet.action` ~ `test.parquet.action_taken`
- `episodes_test.parquet.episode_id` ~ `test.parquet.record_id`
- `episodes_test.parquet.episode_id` ~ `test.parquet.customer_id`
- `episodes_test.parquet.episode_id` ~ `test.parquet.subscription_id`
- `episodes_test.parquet.hours_since_first_failure` ~ `test.parquet.failure_reason`
- `episodes_test.parquet.historical_ltv` ~ `test.parquet.customer_ltv`
- `episodes_test.parquet.attempt_count` ~ `test.parquet.subscription_paid_count`
- `episodes_test.parquet.attempt_count` ~ `test.parquet.interventions_count`
- `episodes_test.parquet.attempt_count` ~ `test.parquet.subscription_remaining_count`
- `episodes_test.parquet.amount` ~ `train.parquet.recovered_amount`
- `episodes_test.parquet.opted_out` ~ `train.parquet.customer_opted_out`
- `episodes_test.parquet.customer_ltv` ~ `train.parquet.customer_failure_rate`
- `episodes_test.parquet.customer_ltv` ~ `train.parquet.customer_id`
- `episodes_test.parquet.customer_ltv` ~ `train.parquet.customer_archetype`
- `episodes_test.parquet.customer_ltv` ~ `train.parquet.customer_opted_out`
- `episodes_test.parquet.recovered_amount` ~ `train.parquet.recovered`
- `episodes_test.parquet.recovered_amount` ~ `train.parquet.amount`
- `episodes_test.parquet.customer_failure_rate` ~ `train.parquet.customer_ltv`
- `episodes_test.parquet.customer_failure_rate` ~ `train.parquet.customer_id`
- `episodes_test.parquet.customer_failure_rate` ~ `train.parquet.customer_archetype`
- `episodes_test.parquet.customer_failure_rate` ~ `train.parquet.failure_reason`
- `episodes_test.parquet.is_first_ever_failure` ~ `train.parquet.failure_reason`
- `episodes_test.parquet.is_first_ever_failure` ~ `train.parquet.is_weekend`
- `episodes_test.parquet.subscription_paid_count` ~ `train.parquet.interventions_count`
- `episodes_test.parquet.subscription_paid_count` ~ `train.parquet.subscription_id`
- `episodes_test.parquet.subscription_paid_count` ~ `train.parquet.subscription_remaining_count`
- `episodes_test.parquet.subscription_paid_count` ~ `train.parquet.attempt_count`
- `episodes_test.parquet.customer_archetype` ~ `train.parquet.customer_ltv`
- `episodes_test.parquet.customer_archetype` ~ `train.parquet.customer_failure_rate`
- `episodes_test.parquet.customer_archetype` ~ `train.parquet.customer_id`
- `episodes_test.parquet.customer_archetype` ~ `train.parquet.customer_opted_out`
- `episodes_test.parquet.interventions_count` ~ `train.parquet.subscription_paid_count`
- `episodes_test.parquet.interventions_count` ~ `train.parquet.subscription_remaining_count`
- `episodes_test.parquet.interventions_count` ~ `train.parquet.attempt_count`
- `episodes_test.parquet.failure_reason` ~ `train.parquet.customer_failure_rate`
- `episodes_test.parquet.failure_reason` ~ `train.parquet.hours_since_first_failure`
- `episodes_test.parquet.action` ~ `train.parquet.action_cost`
- `episodes_test.parquet.action` ~ `train.parquet.action_taken`
- `episodes_test.parquet.episode_id` ~ `train.parquet.record_id`
- `episodes_test.parquet.episode_id` ~ `train.parquet.customer_id`
- `episodes_test.parquet.episode_id` ~ `train.parquet.subscription_id`
- `episodes_test.parquet.hours_since_first_failure` ~ `train.parquet.failure_reason`
- `episodes_test.parquet.historical_ltv` ~ `train.parquet.customer_ltv`
- `episodes_test.parquet.attempt_count` ~ `train.parquet.subscription_paid_count`
- `episodes_test.parquet.attempt_count` ~ `train.parquet.interventions_count`
- `episodes_test.parquet.attempt_count` ~ `train.parquet.subscription_remaining_count`
- `episodes_test.parquet.amount` ~ `val.parquet.recovered_amount`
- `episodes_test.parquet.opted_out` ~ `val.parquet.customer_opted_out`
- `episodes_test.parquet.customer_ltv` ~ `val.parquet.customer_failure_rate`
- `episodes_test.parquet.customer_ltv` ~ `val.parquet.customer_id`
- `episodes_test.parquet.customer_ltv` ~ `val.parquet.customer_archetype`
- `episodes_test.parquet.customer_ltv` ~ `val.parquet.customer_opted_out`
- `episodes_test.parquet.recovered_amount` ~ `val.parquet.recovered`
- `episodes_test.parquet.recovered_amount` ~ `val.parquet.amount`
- `episodes_test.parquet.customer_failure_rate` ~ `val.parquet.customer_ltv`
- `episodes_test.parquet.customer_failure_rate` ~ `val.parquet.customer_id`
- `episodes_test.parquet.customer_failure_rate` ~ `val.parquet.customer_archetype`
- `episodes_test.parquet.customer_failure_rate` ~ `val.parquet.failure_reason`
- `episodes_test.parquet.is_first_ever_failure` ~ `val.parquet.failure_reason`
- `episodes_test.parquet.is_first_ever_failure` ~ `val.parquet.is_weekend`
- `episodes_test.parquet.subscription_paid_count` ~ `val.parquet.interventions_count`
- `episodes_test.parquet.subscription_paid_count` ~ `val.parquet.subscription_id`
- `episodes_test.parquet.subscription_paid_count` ~ `val.parquet.subscription_remaining_count`
- `episodes_test.parquet.subscription_paid_count` ~ `val.parquet.attempt_count`
- `episodes_test.parquet.customer_archetype` ~ `val.parquet.customer_ltv`
- `episodes_test.parquet.customer_archetype` ~ `val.parquet.customer_failure_rate`
- `episodes_test.parquet.customer_archetype` ~ `val.parquet.customer_id`
- `episodes_test.parquet.customer_archetype` ~ `val.parquet.customer_opted_out`
- `episodes_test.parquet.interventions_count` ~ `val.parquet.subscription_paid_count`
- `episodes_test.parquet.interventions_count` ~ `val.parquet.subscription_remaining_count`
- `episodes_test.parquet.interventions_count` ~ `val.parquet.attempt_count`
- `episodes_test.parquet.failure_reason` ~ `val.parquet.customer_failure_rate`
- `episodes_test.parquet.failure_reason` ~ `val.parquet.hours_since_first_failure`
- `episodes_test.parquet.action` ~ `val.parquet.action_cost`
- `episodes_test.parquet.action` ~ `val.parquet.action_taken`
- `episodes_test.parquet.episode_id` ~ `val.parquet.record_id`
- `episodes_test.parquet.episode_id` ~ `val.parquet.customer_id`
- `episodes_test.parquet.episode_id` ~ `val.parquet.subscription_id`
- `episodes_test.parquet.hours_since_first_failure` ~ `val.parquet.failure_reason`
- `episodes_test.parquet.historical_ltv` ~ `val.parquet.customer_ltv`
- `episodes_test.parquet.attempt_count` ~ `val.parquet.subscription_paid_count`
- `episodes_test.parquet.attempt_count` ~ `val.parquet.interventions_count`
- `episodes_test.parquet.attempt_count` ~ `val.parquet.subscription_remaining_count`
- `episodes_train.parquet.amount` ~ `episodes_val.parquet.recovered_amount`
- `episodes_train.parquet.customer_ltv` ~ `episodes_val.parquet.customer_failure_rate`
- `episodes_train.parquet.customer_ltv` ~ `episodes_val.parquet.customer_archetype`
- `episodes_train.parquet.customer_ltv` ~ `episodes_val.parquet.historical_ltv`
- `episodes_train.parquet.recovered_amount` ~ `episodes_val.parquet.amount`
- `episodes_train.parquet.customer_failure_rate` ~ `episodes_val.parquet.customer_ltv`
- `episodes_train.parquet.customer_failure_rate` ~ `episodes_val.parquet.customer_archetype`
- `episodes_train.parquet.customer_failure_rate` ~ `episodes_val.parquet.failure_reason`
- `episodes_train.parquet.is_first_ever_failure` ~ `episodes_val.parquet.failure_reason`
- `episodes_train.parquet.is_first_ever_failure` ~ `episodes_val.parquet.is_weekend`
- `episodes_train.parquet.subscription_paid_count` ~ `episodes_val.parquet.interventions_count`
- `episodes_train.parquet.subscription_paid_count` ~ `episodes_val.parquet.attempt_count`
- `episodes_train.parquet.customer_archetype` ~ `episodes_val.parquet.customer_ltv`
- `episodes_train.parquet.customer_archetype` ~ `episodes_val.parquet.customer_failure_rate`
- `episodes_train.parquet.interventions_count` ~ `episodes_val.parquet.subscription_paid_count`
- `episodes_train.parquet.interventions_count` ~ `episodes_val.parquet.attempt_count`
- `episodes_train.parquet.episode_length` ~ `episodes_val.parquet.episode_return`
- `episodes_train.parquet.episode_length` ~ `episodes_val.parquet.episode_id`
- `episodes_train.parquet.failure_reason` ~ `episodes_val.parquet.customer_failure_rate`
- `episodes_train.parquet.failure_reason` ~ `episodes_val.parquet.is_first_ever_failure`
- `episodes_train.parquet.failure_reason` ~ `episodes_val.parquet.hours_since_first_failure`
- `episodes_train.parquet.episode_return` ~ `episodes_val.parquet.episode_length`
- `episodes_train.parquet.episode_return` ~ `episodes_val.parquet.episode_id`
- `episodes_train.parquet.episode_id` ~ `episodes_val.parquet.episode_length`
- `episodes_train.parquet.episode_id` ~ `episodes_val.parquet.episode_return`
- `episodes_train.parquet.is_weekend` ~ `episodes_val.parquet.is_first_ever_failure`
- `episodes_train.parquet.hours_since_first_failure` ~ `episodes_val.parquet.failure_reason`
- `episodes_train.parquet.historical_ltv` ~ `episodes_val.parquet.customer_ltv`
- `episodes_train.parquet.attempt_count` ~ `episodes_val.parquet.subscription_paid_count`
- `episodes_train.parquet.attempt_count` ~ `episodes_val.parquet.interventions_count`
- `episodes_train.parquet.amount` ~ `historical_records.csv.recovered_amount`
- `episodes_train.parquet.opted_out` ~ `historical_records.csv.customer_opted_out`
- `episodes_train.parquet.customer_ltv` ~ `historical_records.csv.customer_failure_rate`
- `episodes_train.parquet.customer_ltv` ~ `historical_records.csv.customer_id`
- `episodes_train.parquet.customer_ltv` ~ `historical_records.csv.customer_archetype`
- `episodes_train.parquet.customer_ltv` ~ `historical_records.csv.customer_opted_out`
- `episodes_train.parquet.recovered_amount` ~ `historical_records.csv.recovered`
- `episodes_train.parquet.recovered_amount` ~ `historical_records.csv.amount`
- `episodes_train.parquet.customer_failure_rate` ~ `historical_records.csv.customer_ltv`
- `episodes_train.parquet.customer_failure_rate` ~ `historical_records.csv.customer_id`
- `episodes_train.parquet.customer_failure_rate` ~ `historical_records.csv.customer_archetype`
- `episodes_train.parquet.customer_failure_rate` ~ `historical_records.csv.failure_reason`
- `episodes_train.parquet.is_first_ever_failure` ~ `historical_records.csv.failure_reason`
- `episodes_train.parquet.is_first_ever_failure` ~ `historical_records.csv.is_weekend`
- `episodes_train.parquet.subscription_paid_count` ~ `historical_records.csv.interventions_count`
- `episodes_train.parquet.subscription_paid_count` ~ `historical_records.csv.subscription_id`
- `episodes_train.parquet.subscription_paid_count` ~ `historical_records.csv.subscription_remaining_count`
- `episodes_train.parquet.subscription_paid_count` ~ `historical_records.csv.attempt_count`
- `episodes_train.parquet.customer_archetype` ~ `historical_records.csv.customer_ltv`
- `episodes_train.parquet.customer_archetype` ~ `historical_records.csv.customer_failure_rate`
- `episodes_train.parquet.customer_archetype` ~ `historical_records.csv.customer_id`
- `episodes_train.parquet.customer_archetype` ~ `historical_records.csv.customer_opted_out`
- `episodes_train.parquet.interventions_count` ~ `historical_records.csv.subscription_paid_count`
- `episodes_train.parquet.interventions_count` ~ `historical_records.csv.subscription_remaining_count`
- `episodes_train.parquet.interventions_count` ~ `historical_records.csv.attempt_count`
- `episodes_train.parquet.failure_reason` ~ `historical_records.csv.customer_failure_rate`
- `episodes_train.parquet.failure_reason` ~ `historical_records.csv.hours_since_first_failure`
- `episodes_train.parquet.action` ~ `historical_records.csv.action_cost`
- `episodes_train.parquet.action` ~ `historical_records.csv.action_taken`
- `episodes_train.parquet.episode_id` ~ `historical_records.csv.record_id`
- `episodes_train.parquet.episode_id` ~ `historical_records.csv.customer_id`
- `episodes_train.parquet.episode_id` ~ `historical_records.csv.subscription_id`
- `episodes_train.parquet.hours_since_first_failure` ~ `historical_records.csv.failure_reason`
- `episodes_train.parquet.historical_ltv` ~ `historical_records.csv.customer_ltv`
- `episodes_train.parquet.attempt_count` ~ `historical_records.csv.subscription_paid_count`
- `episodes_train.parquet.attempt_count` ~ `historical_records.csv.interventions_count`
- `episodes_train.parquet.attempt_count` ~ `historical_records.csv.subscription_remaining_count`
- `episodes_train.parquet.amount` ~ `historical_records.parquet.recovered_amount`
- `episodes_train.parquet.opted_out` ~ `historical_records.parquet.customer_opted_out`
- `episodes_train.parquet.customer_ltv` ~ `historical_records.parquet.customer_failure_rate`
- `episodes_train.parquet.customer_ltv` ~ `historical_records.parquet.customer_id`
- `episodes_train.parquet.customer_ltv` ~ `historical_records.parquet.customer_archetype`
- `episodes_train.parquet.customer_ltv` ~ `historical_records.parquet.customer_opted_out`
- `episodes_train.parquet.recovered_amount` ~ `historical_records.parquet.recovered`
- `episodes_train.parquet.recovered_amount` ~ `historical_records.parquet.amount`
- `episodes_train.parquet.customer_failure_rate` ~ `historical_records.parquet.customer_ltv`
- `episodes_train.parquet.customer_failure_rate` ~ `historical_records.parquet.customer_id`
- `episodes_train.parquet.customer_failure_rate` ~ `historical_records.parquet.customer_archetype`
- `episodes_train.parquet.customer_failure_rate` ~ `historical_records.parquet.failure_reason`
- `episodes_train.parquet.is_first_ever_failure` ~ `historical_records.parquet.failure_reason`
- `episodes_train.parquet.is_first_ever_failure` ~ `historical_records.parquet.is_weekend`
- `episodes_train.parquet.subscription_paid_count` ~ `historical_records.parquet.interventions_count`
- `episodes_train.parquet.subscription_paid_count` ~ `historical_records.parquet.subscription_id`
- `episodes_train.parquet.subscription_paid_count` ~ `historical_records.parquet.subscription_remaining_count`
- `episodes_train.parquet.subscription_paid_count` ~ `historical_records.parquet.attempt_count`
- `episodes_train.parquet.customer_archetype` ~ `historical_records.parquet.customer_ltv`
- `episodes_train.parquet.customer_archetype` ~ `historical_records.parquet.customer_failure_rate`
- `episodes_train.parquet.customer_archetype` ~ `historical_records.parquet.customer_id`
- `episodes_train.parquet.customer_archetype` ~ `historical_records.parquet.customer_opted_out`
- `episodes_train.parquet.interventions_count` ~ `historical_records.parquet.subscription_paid_count`
- `episodes_train.parquet.interventions_count` ~ `historical_records.parquet.subscription_remaining_count`
- `episodes_train.parquet.interventions_count` ~ `historical_records.parquet.attempt_count`
- `episodes_train.parquet.failure_reason` ~ `historical_records.parquet.customer_failure_rate`
- `episodes_train.parquet.failure_reason` ~ `historical_records.parquet.hours_since_first_failure`
- `episodes_train.parquet.action` ~ `historical_records.parquet.action_cost`
- `episodes_train.parquet.action` ~ `historical_records.parquet.action_taken`
- `episodes_train.parquet.episode_id` ~ `historical_records.parquet.record_id`
- `episodes_train.parquet.episode_id` ~ `historical_records.parquet.customer_id`
- `episodes_train.parquet.episode_id` ~ `historical_records.parquet.subscription_id`
- `episodes_train.parquet.hours_since_first_failure` ~ `historical_records.parquet.failure_reason`
- `episodes_train.parquet.historical_ltv` ~ `historical_records.parquet.customer_ltv`
- `episodes_train.parquet.attempt_count` ~ `historical_records.parquet.subscription_paid_count`
- `episodes_train.parquet.attempt_count` ~ `historical_records.parquet.interventions_count`
- `episodes_train.parquet.attempt_count` ~ `historical_records.parquet.subscription_remaining_count`
- `episodes_train.parquet.interventions_count` ~ `live_persona_state.json.seen_interventions`
- `episodes_train.parquet.amount` ~ `test.parquet.recovered_amount`
- `episodes_train.parquet.opted_out` ~ `test.parquet.customer_opted_out`
- `episodes_train.parquet.customer_ltv` ~ `test.parquet.customer_failure_rate`
- `episodes_train.parquet.customer_ltv` ~ `test.parquet.customer_id`
- `episodes_train.parquet.customer_ltv` ~ `test.parquet.customer_archetype`
- `episodes_train.parquet.customer_ltv` ~ `test.parquet.customer_opted_out`
- `episodes_train.parquet.recovered_amount` ~ `test.parquet.recovered`
- `episodes_train.parquet.recovered_amount` ~ `test.parquet.amount`
- `episodes_train.parquet.customer_failure_rate` ~ `test.parquet.customer_ltv`
- `episodes_train.parquet.customer_failure_rate` ~ `test.parquet.customer_id`
- `episodes_train.parquet.customer_failure_rate` ~ `test.parquet.customer_archetype`
- `episodes_train.parquet.customer_failure_rate` ~ `test.parquet.failure_reason`
- `episodes_train.parquet.is_first_ever_failure` ~ `test.parquet.failure_reason`
- `episodes_train.parquet.is_first_ever_failure` ~ `test.parquet.is_weekend`
- `episodes_train.parquet.subscription_paid_count` ~ `test.parquet.interventions_count`
- `episodes_train.parquet.subscription_paid_count` ~ `test.parquet.subscription_id`
- `episodes_train.parquet.subscription_paid_count` ~ `test.parquet.subscription_remaining_count`
- `episodes_train.parquet.subscription_paid_count` ~ `test.parquet.attempt_count`
- `episodes_train.parquet.customer_archetype` ~ `test.parquet.customer_ltv`
- `episodes_train.parquet.customer_archetype` ~ `test.parquet.customer_failure_rate`
- `episodes_train.parquet.customer_archetype` ~ `test.parquet.customer_id`
- `episodes_train.parquet.customer_archetype` ~ `test.parquet.customer_opted_out`
- `episodes_train.parquet.interventions_count` ~ `test.parquet.subscription_paid_count`
- `episodes_train.parquet.interventions_count` ~ `test.parquet.subscription_remaining_count`
- `episodes_train.parquet.interventions_count` ~ `test.parquet.attempt_count`
- `episodes_train.parquet.failure_reason` ~ `test.parquet.customer_failure_rate`
- `episodes_train.parquet.failure_reason` ~ `test.parquet.hours_since_first_failure`
- `episodes_train.parquet.action` ~ `test.parquet.action_cost`
- `episodes_train.parquet.action` ~ `test.parquet.action_taken`
- `episodes_train.parquet.episode_id` ~ `test.parquet.record_id`
- `episodes_train.parquet.episode_id` ~ `test.parquet.customer_id`
- `episodes_train.parquet.episode_id` ~ `test.parquet.subscription_id`
- `episodes_train.parquet.hours_since_first_failure` ~ `test.parquet.failure_reason`
- `episodes_train.parquet.historical_ltv` ~ `test.parquet.customer_ltv`
- `episodes_train.parquet.attempt_count` ~ `test.parquet.subscription_paid_count`
- `episodes_train.parquet.attempt_count` ~ `test.parquet.interventions_count`
- `episodes_train.parquet.attempt_count` ~ `test.parquet.subscription_remaining_count`
- `episodes_train.parquet.amount` ~ `train.parquet.recovered_amount`
- `episodes_train.parquet.opted_out` ~ `train.parquet.customer_opted_out`
- `episodes_train.parquet.customer_ltv` ~ `train.parquet.customer_failure_rate`
- `episodes_train.parquet.customer_ltv` ~ `train.parquet.customer_id`
- `episodes_train.parquet.customer_ltv` ~ `train.parquet.customer_archetype`
- `episodes_train.parquet.customer_ltv` ~ `train.parquet.customer_opted_out`
- `episodes_train.parquet.recovered_amount` ~ `train.parquet.recovered`
- `episodes_train.parquet.recovered_amount` ~ `train.parquet.amount`
- `episodes_train.parquet.customer_failure_rate` ~ `train.parquet.customer_ltv`
- `episodes_train.parquet.customer_failure_rate` ~ `train.parquet.customer_id`
- `episodes_train.parquet.customer_failure_rate` ~ `train.parquet.customer_archetype`
- `episodes_train.parquet.customer_failure_rate` ~ `train.parquet.failure_reason`
- `episodes_train.parquet.is_first_ever_failure` ~ `train.parquet.failure_reason`
- `episodes_train.parquet.is_first_ever_failure` ~ `train.parquet.is_weekend`
- `episodes_train.parquet.subscription_paid_count` ~ `train.parquet.interventions_count`
- `episodes_train.parquet.subscription_paid_count` ~ `train.parquet.subscription_id`
- `episodes_train.parquet.subscription_paid_count` ~ `train.parquet.subscription_remaining_count`
- `episodes_train.parquet.subscription_paid_count` ~ `train.parquet.attempt_count`
- `episodes_train.parquet.customer_archetype` ~ `train.parquet.customer_ltv`
- `episodes_train.parquet.customer_archetype` ~ `train.parquet.customer_failure_rate`
- `episodes_train.parquet.customer_archetype` ~ `train.parquet.customer_id`
- `episodes_train.parquet.customer_archetype` ~ `train.parquet.customer_opted_out`
- `episodes_train.parquet.interventions_count` ~ `train.parquet.subscription_paid_count`
- `episodes_train.parquet.interventions_count` ~ `train.parquet.subscription_remaining_count`
- `episodes_train.parquet.interventions_count` ~ `train.parquet.attempt_count`
- `episodes_train.parquet.failure_reason` ~ `train.parquet.customer_failure_rate`
- `episodes_train.parquet.failure_reason` ~ `train.parquet.hours_since_first_failure`
- `episodes_train.parquet.action` ~ `train.parquet.action_cost`
- `episodes_train.parquet.action` ~ `train.parquet.action_taken`
- `episodes_train.parquet.episode_id` ~ `train.parquet.record_id`
- `episodes_train.parquet.episode_id` ~ `train.parquet.customer_id`
- `episodes_train.parquet.episode_id` ~ `train.parquet.subscription_id`
- `episodes_train.parquet.hours_since_first_failure` ~ `train.parquet.failure_reason`
- `episodes_train.parquet.historical_ltv` ~ `train.parquet.customer_ltv`
- `episodes_train.parquet.attempt_count` ~ `train.parquet.subscription_paid_count`
- `episodes_train.parquet.attempt_count` ~ `train.parquet.interventions_count`
- `episodes_train.parquet.attempt_count` ~ `train.parquet.subscription_remaining_count`
- `episodes_train.parquet.amount` ~ `val.parquet.recovered_amount`
- `episodes_train.parquet.opted_out` ~ `val.parquet.customer_opted_out`
- `episodes_train.parquet.customer_ltv` ~ `val.parquet.customer_failure_rate`
- `episodes_train.parquet.customer_ltv` ~ `val.parquet.customer_id`
- `episodes_train.parquet.customer_ltv` ~ `val.parquet.customer_archetype`
- `episodes_train.parquet.customer_ltv` ~ `val.parquet.customer_opted_out`
- `episodes_train.parquet.recovered_amount` ~ `val.parquet.recovered`
- `episodes_train.parquet.recovered_amount` ~ `val.parquet.amount`
- `episodes_train.parquet.customer_failure_rate` ~ `val.parquet.customer_ltv`
- `episodes_train.parquet.customer_failure_rate` ~ `val.parquet.customer_id`
- `episodes_train.parquet.customer_failure_rate` ~ `val.parquet.customer_archetype`
- `episodes_train.parquet.customer_failure_rate` ~ `val.parquet.failure_reason`
- `episodes_train.parquet.is_first_ever_failure` ~ `val.parquet.failure_reason`
- `episodes_train.parquet.is_first_ever_failure` ~ `val.parquet.is_weekend`
- `episodes_train.parquet.subscription_paid_count` ~ `val.parquet.interventions_count`
- `episodes_train.parquet.subscription_paid_count` ~ `val.parquet.subscription_id`
- `episodes_train.parquet.subscription_paid_count` ~ `val.parquet.subscription_remaining_count`
- `episodes_train.parquet.subscription_paid_count` ~ `val.parquet.attempt_count`
- `episodes_train.parquet.customer_archetype` ~ `val.parquet.customer_ltv`
- `episodes_train.parquet.customer_archetype` ~ `val.parquet.customer_failure_rate`
- `episodes_train.parquet.customer_archetype` ~ `val.parquet.customer_id`
- `episodes_train.parquet.customer_archetype` ~ `val.parquet.customer_opted_out`
- `episodes_train.parquet.interventions_count` ~ `val.parquet.subscription_paid_count`
- `episodes_train.parquet.interventions_count` ~ `val.parquet.subscription_remaining_count`
- `episodes_train.parquet.interventions_count` ~ `val.parquet.attempt_count`
- `episodes_train.parquet.failure_reason` ~ `val.parquet.customer_failure_rate`
- `episodes_train.parquet.failure_reason` ~ `val.parquet.hours_since_first_failure`
- `episodes_train.parquet.action` ~ `val.parquet.action_cost`
- `episodes_train.parquet.action` ~ `val.parquet.action_taken`
- `episodes_train.parquet.episode_id` ~ `val.parquet.record_id`
- `episodes_train.parquet.episode_id` ~ `val.parquet.customer_id`
- `episodes_train.parquet.episode_id` ~ `val.parquet.subscription_id`
- `episodes_train.parquet.hours_since_first_failure` ~ `val.parquet.failure_reason`
- `episodes_train.parquet.historical_ltv` ~ `val.parquet.customer_ltv`
- `episodes_train.parquet.attempt_count` ~ `val.parquet.subscription_paid_count`
- `episodes_train.parquet.attempt_count` ~ `val.parquet.interventions_count`
- `episodes_train.parquet.attempt_count` ~ `val.parquet.subscription_remaining_count`
- `episodes_val.parquet.amount` ~ `historical_records.csv.recovered_amount`
- `episodes_val.parquet.opted_out` ~ `historical_records.csv.customer_opted_out`
- `episodes_val.parquet.customer_ltv` ~ `historical_records.csv.customer_failure_rate`
- `episodes_val.parquet.customer_ltv` ~ `historical_records.csv.customer_id`
- `episodes_val.parquet.customer_ltv` ~ `historical_records.csv.customer_archetype`
- `episodes_val.parquet.customer_ltv` ~ `historical_records.csv.customer_opted_out`
- `episodes_val.parquet.recovered_amount` ~ `historical_records.csv.recovered`
- `episodes_val.parquet.recovered_amount` ~ `historical_records.csv.amount`
- `episodes_val.parquet.customer_failure_rate` ~ `historical_records.csv.customer_ltv`
- `episodes_val.parquet.customer_failure_rate` ~ `historical_records.csv.customer_id`
- `episodes_val.parquet.customer_failure_rate` ~ `historical_records.csv.customer_archetype`
- `episodes_val.parquet.customer_failure_rate` ~ `historical_records.csv.failure_reason`
- `episodes_val.parquet.is_first_ever_failure` ~ `historical_records.csv.failure_reason`
- `episodes_val.parquet.is_first_ever_failure` ~ `historical_records.csv.is_weekend`
- `episodes_val.parquet.subscription_paid_count` ~ `historical_records.csv.interventions_count`
- `episodes_val.parquet.subscription_paid_count` ~ `historical_records.csv.subscription_id`
- `episodes_val.parquet.subscription_paid_count` ~ `historical_records.csv.subscription_remaining_count`
- `episodes_val.parquet.subscription_paid_count` ~ `historical_records.csv.attempt_count`
- `episodes_val.parquet.customer_archetype` ~ `historical_records.csv.customer_ltv`
- `episodes_val.parquet.customer_archetype` ~ `historical_records.csv.customer_failure_rate`
- `episodes_val.parquet.customer_archetype` ~ `historical_records.csv.customer_id`
- `episodes_val.parquet.customer_archetype` ~ `historical_records.csv.customer_opted_out`
- `episodes_val.parquet.interventions_count` ~ `historical_records.csv.subscription_paid_count`
- `episodes_val.parquet.interventions_count` ~ `historical_records.csv.subscription_remaining_count`
- `episodes_val.parquet.interventions_count` ~ `historical_records.csv.attempt_count`
- `episodes_val.parquet.failure_reason` ~ `historical_records.csv.customer_failure_rate`
- `episodes_val.parquet.failure_reason` ~ `historical_records.csv.hours_since_first_failure`
- `episodes_val.parquet.action` ~ `historical_records.csv.action_cost`
- `episodes_val.parquet.action` ~ `historical_records.csv.action_taken`
- `episodes_val.parquet.episode_id` ~ `historical_records.csv.record_id`
- `episodes_val.parquet.episode_id` ~ `historical_records.csv.customer_id`
- `episodes_val.parquet.episode_id` ~ `historical_records.csv.subscription_id`
- `episodes_val.parquet.hours_since_first_failure` ~ `historical_records.csv.failure_reason`
- `episodes_val.parquet.historical_ltv` ~ `historical_records.csv.customer_ltv`
- `episodes_val.parquet.attempt_count` ~ `historical_records.csv.subscription_paid_count`
- `episodes_val.parquet.attempt_count` ~ `historical_records.csv.interventions_count`
- `episodes_val.parquet.attempt_count` ~ `historical_records.csv.subscription_remaining_count`
- `episodes_val.parquet.amount` ~ `historical_records.parquet.recovered_amount`
- `episodes_val.parquet.opted_out` ~ `historical_records.parquet.customer_opted_out`
- `episodes_val.parquet.customer_ltv` ~ `historical_records.parquet.customer_failure_rate`
- `episodes_val.parquet.customer_ltv` ~ `historical_records.parquet.customer_id`
- `episodes_val.parquet.customer_ltv` ~ `historical_records.parquet.customer_archetype`
- `episodes_val.parquet.customer_ltv` ~ `historical_records.parquet.customer_opted_out`
- `episodes_val.parquet.recovered_amount` ~ `historical_records.parquet.recovered`
- `episodes_val.parquet.recovered_amount` ~ `historical_records.parquet.amount`
- `episodes_val.parquet.customer_failure_rate` ~ `historical_records.parquet.customer_ltv`
- `episodes_val.parquet.customer_failure_rate` ~ `historical_records.parquet.customer_id`
- `episodes_val.parquet.customer_failure_rate` ~ `historical_records.parquet.customer_archetype`
- `episodes_val.parquet.customer_failure_rate` ~ `historical_records.parquet.failure_reason`
- `episodes_val.parquet.is_first_ever_failure` ~ `historical_records.parquet.failure_reason`
- `episodes_val.parquet.is_first_ever_failure` ~ `historical_records.parquet.is_weekend`
- `episodes_val.parquet.subscription_paid_count` ~ `historical_records.parquet.interventions_count`
- `episodes_val.parquet.subscription_paid_count` ~ `historical_records.parquet.subscription_id`
- `episodes_val.parquet.subscription_paid_count` ~ `historical_records.parquet.subscription_remaining_count`
- `episodes_val.parquet.subscription_paid_count` ~ `historical_records.parquet.attempt_count`
- `episodes_val.parquet.customer_archetype` ~ `historical_records.parquet.customer_ltv`
- `episodes_val.parquet.customer_archetype` ~ `historical_records.parquet.customer_failure_rate`
- `episodes_val.parquet.customer_archetype` ~ `historical_records.parquet.customer_id`
- `episodes_val.parquet.customer_archetype` ~ `historical_records.parquet.customer_opted_out`
- `episodes_val.parquet.interventions_count` ~ `historical_records.parquet.subscription_paid_count`
- `episodes_val.parquet.interventions_count` ~ `historical_records.parquet.subscription_remaining_count`
- `episodes_val.parquet.interventions_count` ~ `historical_records.parquet.attempt_count`
- `episodes_val.parquet.failure_reason` ~ `historical_records.parquet.customer_failure_rate`
- `episodes_val.parquet.failure_reason` ~ `historical_records.parquet.hours_since_first_failure`
- `episodes_val.parquet.action` ~ `historical_records.parquet.action_cost`
- `episodes_val.parquet.action` ~ `historical_records.parquet.action_taken`
- `episodes_val.parquet.episode_id` ~ `historical_records.parquet.record_id`
- `episodes_val.parquet.episode_id` ~ `historical_records.parquet.customer_id`
- `episodes_val.parquet.episode_id` ~ `historical_records.parquet.subscription_id`
- `episodes_val.parquet.hours_since_first_failure` ~ `historical_records.parquet.failure_reason`
- `episodes_val.parquet.historical_ltv` ~ `historical_records.parquet.customer_ltv`
- `episodes_val.parquet.attempt_count` ~ `historical_records.parquet.subscription_paid_count`
- `episodes_val.parquet.attempt_count` ~ `historical_records.parquet.interventions_count`
- `episodes_val.parquet.attempt_count` ~ `historical_records.parquet.subscription_remaining_count`
- `episodes_val.parquet.interventions_count` ~ `live_persona_state.json.seen_interventions`
- `episodes_val.parquet.amount` ~ `test.parquet.recovered_amount`
- `episodes_val.parquet.opted_out` ~ `test.parquet.customer_opted_out`
- `episodes_val.parquet.customer_ltv` ~ `test.parquet.customer_failure_rate`
- `episodes_val.parquet.customer_ltv` ~ `test.parquet.customer_id`
- `episodes_val.parquet.customer_ltv` ~ `test.parquet.customer_archetype`
- `episodes_val.parquet.customer_ltv` ~ `test.parquet.customer_opted_out`
- `episodes_val.parquet.recovered_amount` ~ `test.parquet.recovered`
- `episodes_val.parquet.recovered_amount` ~ `test.parquet.amount`
- `episodes_val.parquet.customer_failure_rate` ~ `test.parquet.customer_ltv`
- `episodes_val.parquet.customer_failure_rate` ~ `test.parquet.customer_id`
- `episodes_val.parquet.customer_failure_rate` ~ `test.parquet.customer_archetype`
- `episodes_val.parquet.customer_failure_rate` ~ `test.parquet.failure_reason`
- `episodes_val.parquet.is_first_ever_failure` ~ `test.parquet.failure_reason`
- `episodes_val.parquet.is_first_ever_failure` ~ `test.parquet.is_weekend`
- `episodes_val.parquet.subscription_paid_count` ~ `test.parquet.interventions_count`
- `episodes_val.parquet.subscription_paid_count` ~ `test.parquet.subscription_id`
- `episodes_val.parquet.subscription_paid_count` ~ `test.parquet.subscription_remaining_count`
- `episodes_val.parquet.subscription_paid_count` ~ `test.parquet.attempt_count`
- `episodes_val.parquet.customer_archetype` ~ `test.parquet.customer_ltv`
- `episodes_val.parquet.customer_archetype` ~ `test.parquet.customer_failure_rate`
- `episodes_val.parquet.customer_archetype` ~ `test.parquet.customer_id`
- `episodes_val.parquet.customer_archetype` ~ `test.parquet.customer_opted_out`
- `episodes_val.parquet.interventions_count` ~ `test.parquet.subscription_paid_count`
- `episodes_val.parquet.interventions_count` ~ `test.parquet.subscription_remaining_count`
- `episodes_val.parquet.interventions_count` ~ `test.parquet.attempt_count`
- `episodes_val.parquet.failure_reason` ~ `test.parquet.customer_failure_rate`
- `episodes_val.parquet.failure_reason` ~ `test.parquet.hours_since_first_failure`
- `episodes_val.parquet.action` ~ `test.parquet.action_cost`
- `episodes_val.parquet.action` ~ `test.parquet.action_taken`
- `episodes_val.parquet.episode_id` ~ `test.parquet.record_id`
- `episodes_val.parquet.episode_id` ~ `test.parquet.customer_id`
- `episodes_val.parquet.episode_id` ~ `test.parquet.subscription_id`
- `episodes_val.parquet.hours_since_first_failure` ~ `test.parquet.failure_reason`
- `episodes_val.parquet.historical_ltv` ~ `test.parquet.customer_ltv`
- `episodes_val.parquet.attempt_count` ~ `test.parquet.subscription_paid_count`
- `episodes_val.parquet.attempt_count` ~ `test.parquet.interventions_count`
- `episodes_val.parquet.attempt_count` ~ `test.parquet.subscription_remaining_count`
- `episodes_val.parquet.amount` ~ `train.parquet.recovered_amount`
- `episodes_val.parquet.opted_out` ~ `train.parquet.customer_opted_out`
- `episodes_val.parquet.customer_ltv` ~ `train.parquet.customer_failure_rate`
- `episodes_val.parquet.customer_ltv` ~ `train.parquet.customer_id`
- `episodes_val.parquet.customer_ltv` ~ `train.parquet.customer_archetype`
- `episodes_val.parquet.customer_ltv` ~ `train.parquet.customer_opted_out`
- `episodes_val.parquet.recovered_amount` ~ `train.parquet.recovered`
- `episodes_val.parquet.recovered_amount` ~ `train.parquet.amount`
- `episodes_val.parquet.customer_failure_rate` ~ `train.parquet.customer_ltv`
- `episodes_val.parquet.customer_failure_rate` ~ `train.parquet.customer_id`
- `episodes_val.parquet.customer_failure_rate` ~ `train.parquet.customer_archetype`
- `episodes_val.parquet.customer_failure_rate` ~ `train.parquet.failure_reason`
- `episodes_val.parquet.is_first_ever_failure` ~ `train.parquet.failure_reason`
- `episodes_val.parquet.is_first_ever_failure` ~ `train.parquet.is_weekend`
- `episodes_val.parquet.subscription_paid_count` ~ `train.parquet.interventions_count`
- `episodes_val.parquet.subscription_paid_count` ~ `train.parquet.subscription_id`
- `episodes_val.parquet.subscription_paid_count` ~ `train.parquet.subscription_remaining_count`
- `episodes_val.parquet.subscription_paid_count` ~ `train.parquet.attempt_count`
- `episodes_val.parquet.customer_archetype` ~ `train.parquet.customer_ltv`
- `episodes_val.parquet.customer_archetype` ~ `train.parquet.customer_failure_rate`
- `episodes_val.parquet.customer_archetype` ~ `train.parquet.customer_id`
- `episodes_val.parquet.customer_archetype` ~ `train.parquet.customer_opted_out`
- `episodes_val.parquet.interventions_count` ~ `train.parquet.subscription_paid_count`
- `episodes_val.parquet.interventions_count` ~ `train.parquet.subscription_remaining_count`
- `episodes_val.parquet.interventions_count` ~ `train.parquet.attempt_count`
- `episodes_val.parquet.failure_reason` ~ `train.parquet.customer_failure_rate`
- `episodes_val.parquet.failure_reason` ~ `train.parquet.hours_since_first_failure`
- `episodes_val.parquet.action` ~ `train.parquet.action_cost`
- `episodes_val.parquet.action` ~ `train.parquet.action_taken`
- `episodes_val.parquet.episode_id` ~ `train.parquet.record_id`
- `episodes_val.parquet.episode_id` ~ `train.parquet.customer_id`
- `episodes_val.parquet.episode_id` ~ `train.parquet.subscription_id`
- `episodes_val.parquet.hours_since_first_failure` ~ `train.parquet.failure_reason`
- `episodes_val.parquet.historical_ltv` ~ `train.parquet.customer_ltv`
- `episodes_val.parquet.attempt_count` ~ `train.parquet.subscription_paid_count`
- `episodes_val.parquet.attempt_count` ~ `train.parquet.interventions_count`
- `episodes_val.parquet.attempt_count` ~ `train.parquet.subscription_remaining_count`
- `episodes_val.parquet.amount` ~ `val.parquet.recovered_amount`
- `episodes_val.parquet.opted_out` ~ `val.parquet.customer_opted_out`
- `episodes_val.parquet.customer_ltv` ~ `val.parquet.customer_failure_rate`
- `episodes_val.parquet.customer_ltv` ~ `val.parquet.customer_id`
- `episodes_val.parquet.customer_ltv` ~ `val.parquet.customer_archetype`
- `episodes_val.parquet.customer_ltv` ~ `val.parquet.customer_opted_out`
- `episodes_val.parquet.recovered_amount` ~ `val.parquet.recovered`
- `episodes_val.parquet.recovered_amount` ~ `val.parquet.amount`
- `episodes_val.parquet.customer_failure_rate` ~ `val.parquet.customer_ltv`
- `episodes_val.parquet.customer_failure_rate` ~ `val.parquet.customer_id`
- `episodes_val.parquet.customer_failure_rate` ~ `val.parquet.customer_archetype`
- `episodes_val.parquet.customer_failure_rate` ~ `val.parquet.failure_reason`
- `episodes_val.parquet.is_first_ever_failure` ~ `val.parquet.failure_reason`
- `episodes_val.parquet.is_first_ever_failure` ~ `val.parquet.is_weekend`
- `episodes_val.parquet.subscription_paid_count` ~ `val.parquet.interventions_count`
- `episodes_val.parquet.subscription_paid_count` ~ `val.parquet.subscription_id`
- `episodes_val.parquet.subscription_paid_count` ~ `val.parquet.subscription_remaining_count`
- `episodes_val.parquet.subscription_paid_count` ~ `val.parquet.attempt_count`
- `episodes_val.parquet.customer_archetype` ~ `val.parquet.customer_ltv`
- `episodes_val.parquet.customer_archetype` ~ `val.parquet.customer_failure_rate`
- `episodes_val.parquet.customer_archetype` ~ `val.parquet.customer_id`
- `episodes_val.parquet.customer_archetype` ~ `val.parquet.customer_opted_out`
- `episodes_val.parquet.interventions_count` ~ `val.parquet.subscription_paid_count`
- `episodes_val.parquet.interventions_count` ~ `val.parquet.subscription_remaining_count`
- `episodes_val.parquet.interventions_count` ~ `val.parquet.attempt_count`
- `episodes_val.parquet.failure_reason` ~ `val.parquet.customer_failure_rate`
- `episodes_val.parquet.failure_reason` ~ `val.parquet.hours_since_first_failure`
- `episodes_val.parquet.action` ~ `val.parquet.action_cost`
- `episodes_val.parquet.action` ~ `val.parquet.action_taken`
- `episodes_val.parquet.episode_id` ~ `val.parquet.record_id`
- `episodes_val.parquet.episode_id` ~ `val.parquet.customer_id`
- `episodes_val.parquet.episode_id` ~ `val.parquet.subscription_id`
- `episodes_val.parquet.hours_since_first_failure` ~ `val.parquet.failure_reason`
- `episodes_val.parquet.historical_ltv` ~ `val.parquet.customer_ltv`
- `episodes_val.parquet.attempt_count` ~ `val.parquet.subscription_paid_count`
- `episodes_val.parquet.attempt_count` ~ `val.parquet.interventions_count`
- `episodes_val.parquet.attempt_count` ~ `val.parquet.subscription_remaining_count`
- `historical_records.csv.recovered` ~ `historical_records.parquet.recovered_amount`
- `historical_records.csv.record_id` ~ `historical_records.parquet.customer_id`
- `historical_records.csv.record_id` ~ `historical_records.parquet.subscription_id`
- `historical_records.csv.amount` ~ `historical_records.parquet.recovered_amount`
- `historical_records.csv.customer_ltv` ~ `historical_records.parquet.customer_failure_rate`
- `historical_records.csv.customer_ltv` ~ `historical_records.parquet.customer_id`
- `historical_records.csv.customer_ltv` ~ `historical_records.parquet.customer_archetype`
- `historical_records.csv.customer_ltv` ~ `historical_records.parquet.customer_opted_out`
- `historical_records.csv.recovered_amount` ~ `historical_records.parquet.recovered`
- `historical_records.csv.recovered_amount` ~ `historical_records.parquet.amount`
- `historical_records.csv.customer_failure_rate` ~ `historical_records.parquet.customer_ltv`
- `historical_records.csv.customer_failure_rate` ~ `historical_records.parquet.customer_id`
- `historical_records.csv.customer_failure_rate` ~ `historical_records.parquet.customer_archetype`
- `historical_records.csv.customer_failure_rate` ~ `historical_records.parquet.failure_reason`
- `historical_records.csv.customer_id` ~ `historical_records.parquet.record_id`
- `historical_records.csv.customer_id` ~ `historical_records.parquet.customer_ltv`
- `historical_records.csv.customer_id` ~ `historical_records.parquet.customer_failure_rate`
- `historical_records.csv.customer_id` ~ `historical_records.parquet.customer_archetype`
- `historical_records.csv.customer_id` ~ `historical_records.parquet.customer_opted_out`
- `historical_records.csv.customer_id` ~ `historical_records.parquet.subscription_id`
- `historical_records.csv.subscription_paid_count` ~ `historical_records.parquet.interventions_count`
- `historical_records.csv.subscription_paid_count` ~ `historical_records.parquet.subscription_id`
- `historical_records.csv.subscription_paid_count` ~ `historical_records.parquet.subscription_remaining_count`
- `historical_records.csv.subscription_paid_count` ~ `historical_records.parquet.attempt_count`
- `historical_records.csv.action_cost` ~ `historical_records.parquet.action_taken`
- `historical_records.csv.customer_archetype` ~ `historical_records.parquet.customer_ltv`
- `historical_records.csv.customer_archetype` ~ `historical_records.parquet.customer_failure_rate`
- `historical_records.csv.customer_archetype` ~ `historical_records.parquet.customer_id`
- `historical_records.csv.customer_archetype` ~ `historical_records.parquet.customer_opted_out`
- `historical_records.csv.interventions_count` ~ `historical_records.parquet.subscription_paid_count`
- `historical_records.csv.interventions_count` ~ `historical_records.parquet.subscription_remaining_count`
- `historical_records.csv.interventions_count` ~ `historical_records.parquet.attempt_count`
- `historical_records.csv.customer_opted_out` ~ `historical_records.parquet.customer_ltv`
- `historical_records.csv.customer_opted_out` ~ `historical_records.parquet.customer_id`
- `historical_records.csv.customer_opted_out` ~ `historical_records.parquet.customer_archetype`
- `historical_records.csv.failure_reason` ~ `historical_records.parquet.customer_failure_rate`
- `historical_records.csv.failure_reason` ~ `historical_records.parquet.hours_since_first_failure`
- `historical_records.csv.subscription_id` ~ `historical_records.parquet.record_id`
- `historical_records.csv.subscription_id` ~ `historical_records.parquet.customer_id`
- `historical_records.csv.subscription_id` ~ `historical_records.parquet.subscription_paid_count`
- `historical_records.csv.subscription_id` ~ `historical_records.parquet.subscription_remaining_count`
- `historical_records.csv.hours_since_first_failure` ~ `historical_records.parquet.failure_reason`
- `historical_records.csv.subscription_remaining_count` ~ `historical_records.parquet.subscription_paid_count`
- `historical_records.csv.subscription_remaining_count` ~ `historical_records.parquet.interventions_count`
- `historical_records.csv.subscription_remaining_count` ~ `historical_records.parquet.subscription_id`
- `historical_records.csv.subscription_remaining_count` ~ `historical_records.parquet.attempt_count`
- `historical_records.csv.attempt_count` ~ `historical_records.parquet.subscription_paid_count`
- `historical_records.csv.attempt_count` ~ `historical_records.parquet.interventions_count`
- `historical_records.csv.attempt_count` ~ `historical_records.parquet.subscription_remaining_count`
- `historical_records.csv.action_taken` ~ `historical_records.parquet.action_cost`
- `historical_records.csv.interventions_count` ~ `live_persona_state.json.seen_interventions`
- `historical_records.csv.recovered` ~ `test.parquet.recovered_amount`
- `historical_records.csv.record_id` ~ `test.parquet.customer_id`
- `historical_records.csv.record_id` ~ `test.parquet.subscription_id`
- `historical_records.csv.amount` ~ `test.parquet.recovered_amount`
- `historical_records.csv.customer_ltv` ~ `test.parquet.customer_failure_rate`
- `historical_records.csv.customer_ltv` ~ `test.parquet.customer_id`
- `historical_records.csv.customer_ltv` ~ `test.parquet.customer_archetype`
- `historical_records.csv.customer_ltv` ~ `test.parquet.customer_opted_out`
- `historical_records.csv.recovered_amount` ~ `test.parquet.recovered`
- `historical_records.csv.recovered_amount` ~ `test.parquet.amount`
- `historical_records.csv.customer_failure_rate` ~ `test.parquet.customer_ltv`
- `historical_records.csv.customer_failure_rate` ~ `test.parquet.customer_id`
- `historical_records.csv.customer_failure_rate` ~ `test.parquet.customer_archetype`
- `historical_records.csv.customer_failure_rate` ~ `test.parquet.failure_reason`
- `historical_records.csv.customer_id` ~ `test.parquet.record_id`
- `historical_records.csv.customer_id` ~ `test.parquet.customer_ltv`
- `historical_records.csv.customer_id` ~ `test.parquet.customer_failure_rate`
- `historical_records.csv.customer_id` ~ `test.parquet.customer_archetype`
- `historical_records.csv.customer_id` ~ `test.parquet.customer_opted_out`
- `historical_records.csv.customer_id` ~ `test.parquet.subscription_id`
- `historical_records.csv.subscription_paid_count` ~ `test.parquet.interventions_count`
- `historical_records.csv.subscription_paid_count` ~ `test.parquet.subscription_id`
- `historical_records.csv.subscription_paid_count` ~ `test.parquet.subscription_remaining_count`
- `historical_records.csv.subscription_paid_count` ~ `test.parquet.attempt_count`
- `historical_records.csv.action_cost` ~ `test.parquet.action_taken`
- `historical_records.csv.customer_archetype` ~ `test.parquet.customer_ltv`
- `historical_records.csv.customer_archetype` ~ `test.parquet.customer_failure_rate`
- `historical_records.csv.customer_archetype` ~ `test.parquet.customer_id`
- `historical_records.csv.customer_archetype` ~ `test.parquet.customer_opted_out`
- `historical_records.csv.interventions_count` ~ `test.parquet.subscription_paid_count`
- `historical_records.csv.interventions_count` ~ `test.parquet.subscription_remaining_count`
- `historical_records.csv.interventions_count` ~ `test.parquet.attempt_count`
- `historical_records.csv.customer_opted_out` ~ `test.parquet.customer_ltv`
- `historical_records.csv.customer_opted_out` ~ `test.parquet.customer_id`
- `historical_records.csv.customer_opted_out` ~ `test.parquet.customer_archetype`
- `historical_records.csv.failure_reason` ~ `test.parquet.customer_failure_rate`
- `historical_records.csv.failure_reason` ~ `test.parquet.hours_since_first_failure`
- `historical_records.csv.subscription_id` ~ `test.parquet.record_id`
- `historical_records.csv.subscription_id` ~ `test.parquet.customer_id`
- `historical_records.csv.subscription_id` ~ `test.parquet.subscription_paid_count`
- `historical_records.csv.subscription_id` ~ `test.parquet.subscription_remaining_count`
- `historical_records.csv.hours_since_first_failure` ~ `test.parquet.failure_reason`
- `historical_records.csv.subscription_remaining_count` ~ `test.parquet.subscription_paid_count`
- `historical_records.csv.subscription_remaining_count` ~ `test.parquet.interventions_count`
- `historical_records.csv.subscription_remaining_count` ~ `test.parquet.subscription_id`
- `historical_records.csv.subscription_remaining_count` ~ `test.parquet.attempt_count`
- `historical_records.csv.attempt_count` ~ `test.parquet.subscription_paid_count`
- `historical_records.csv.attempt_count` ~ `test.parquet.interventions_count`
- `historical_records.csv.attempt_count` ~ `test.parquet.subscription_remaining_count`
- `historical_records.csv.action_taken` ~ `test.parquet.action_cost`
- `historical_records.csv.recovered` ~ `train.parquet.recovered_amount`
- `historical_records.csv.record_id` ~ `train.parquet.customer_id`
- `historical_records.csv.record_id` ~ `train.parquet.subscription_id`
- `historical_records.csv.amount` ~ `train.parquet.recovered_amount`
- `historical_records.csv.customer_ltv` ~ `train.parquet.customer_failure_rate`
- `historical_records.csv.customer_ltv` ~ `train.parquet.customer_id`
- `historical_records.csv.customer_ltv` ~ `train.parquet.customer_archetype`
- `historical_records.csv.customer_ltv` ~ `train.parquet.customer_opted_out`
- `historical_records.csv.recovered_amount` ~ `train.parquet.recovered`
- `historical_records.csv.recovered_amount` ~ `train.parquet.amount`
- `historical_records.csv.customer_failure_rate` ~ `train.parquet.customer_ltv`
- `historical_records.csv.customer_failure_rate` ~ `train.parquet.customer_id`
- `historical_records.csv.customer_failure_rate` ~ `train.parquet.customer_archetype`
- `historical_records.csv.customer_failure_rate` ~ `train.parquet.failure_reason`
- `historical_records.csv.customer_id` ~ `train.parquet.record_id`
- `historical_records.csv.customer_id` ~ `train.parquet.customer_ltv`
- `historical_records.csv.customer_id` ~ `train.parquet.customer_failure_rate`
- `historical_records.csv.customer_id` ~ `train.parquet.customer_archetype`
- `historical_records.csv.customer_id` ~ `train.parquet.customer_opted_out`
- `historical_records.csv.customer_id` ~ `train.parquet.subscription_id`
- `historical_records.csv.subscription_paid_count` ~ `train.parquet.interventions_count`
- `historical_records.csv.subscription_paid_count` ~ `train.parquet.subscription_id`
- `historical_records.csv.subscription_paid_count` ~ `train.parquet.subscription_remaining_count`
- `historical_records.csv.subscription_paid_count` ~ `train.parquet.attempt_count`
- `historical_records.csv.action_cost` ~ `train.parquet.action_taken`
- `historical_records.csv.customer_archetype` ~ `train.parquet.customer_ltv`
- `historical_records.csv.customer_archetype` ~ `train.parquet.customer_failure_rate`
- `historical_records.csv.customer_archetype` ~ `train.parquet.customer_id`
- `historical_records.csv.customer_archetype` ~ `train.parquet.customer_opted_out`
- `historical_records.csv.interventions_count` ~ `train.parquet.subscription_paid_count`
- `historical_records.csv.interventions_count` ~ `train.parquet.subscription_remaining_count`
- `historical_records.csv.interventions_count` ~ `train.parquet.attempt_count`
- `historical_records.csv.customer_opted_out` ~ `train.parquet.customer_ltv`
- `historical_records.csv.customer_opted_out` ~ `train.parquet.customer_id`
- `historical_records.csv.customer_opted_out` ~ `train.parquet.customer_archetype`
- `historical_records.csv.failure_reason` ~ `train.parquet.customer_failure_rate`
- `historical_records.csv.failure_reason` ~ `train.parquet.hours_since_first_failure`
- `historical_records.csv.subscription_id` ~ `train.parquet.record_id`
- `historical_records.csv.subscription_id` ~ `train.parquet.customer_id`
- `historical_records.csv.subscription_id` ~ `train.parquet.subscription_paid_count`
- `historical_records.csv.subscription_id` ~ `train.parquet.subscription_remaining_count`
- `historical_records.csv.hours_since_first_failure` ~ `train.parquet.failure_reason`
- `historical_records.csv.subscription_remaining_count` ~ `train.parquet.subscription_paid_count`
- `historical_records.csv.subscription_remaining_count` ~ `train.parquet.interventions_count`
- `historical_records.csv.subscription_remaining_count` ~ `train.parquet.subscription_id`
- `historical_records.csv.subscription_remaining_count` ~ `train.parquet.attempt_count`
- `historical_records.csv.attempt_count` ~ `train.parquet.subscription_paid_count`
- `historical_records.csv.attempt_count` ~ `train.parquet.interventions_count`
- `historical_records.csv.attempt_count` ~ `train.parquet.subscription_remaining_count`
- `historical_records.csv.action_taken` ~ `train.parquet.action_cost`
- `historical_records.csv.recovered` ~ `val.parquet.recovered_amount`
- `historical_records.csv.record_id` ~ `val.parquet.customer_id`
- `historical_records.csv.record_id` ~ `val.parquet.subscription_id`
- `historical_records.csv.amount` ~ `val.parquet.recovered_amount`
- `historical_records.csv.customer_ltv` ~ `val.parquet.customer_failure_rate`
- `historical_records.csv.customer_ltv` ~ `val.parquet.customer_id`
- `historical_records.csv.customer_ltv` ~ `val.parquet.customer_archetype`
- `historical_records.csv.customer_ltv` ~ `val.parquet.customer_opted_out`
- `historical_records.csv.recovered_amount` ~ `val.parquet.recovered`
- `historical_records.csv.recovered_amount` ~ `val.parquet.amount`
- `historical_records.csv.customer_failure_rate` ~ `val.parquet.customer_ltv`
- `historical_records.csv.customer_failure_rate` ~ `val.parquet.customer_id`
- `historical_records.csv.customer_failure_rate` ~ `val.parquet.customer_archetype`
- `historical_records.csv.customer_failure_rate` ~ `val.parquet.failure_reason`
- `historical_records.csv.customer_id` ~ `val.parquet.record_id`
- `historical_records.csv.customer_id` ~ `val.parquet.customer_ltv`
- `historical_records.csv.customer_id` ~ `val.parquet.customer_failure_rate`
- `historical_records.csv.customer_id` ~ `val.parquet.customer_archetype`
- `historical_records.csv.customer_id` ~ `val.parquet.customer_opted_out`
- `historical_records.csv.customer_id` ~ `val.parquet.subscription_id`
- `historical_records.csv.subscription_paid_count` ~ `val.parquet.interventions_count`
- `historical_records.csv.subscription_paid_count` ~ `val.parquet.subscription_id`
- `historical_records.csv.subscription_paid_count` ~ `val.parquet.subscription_remaining_count`
- `historical_records.csv.subscription_paid_count` ~ `val.parquet.attempt_count`
- `historical_records.csv.action_cost` ~ `val.parquet.action_taken`
- `historical_records.csv.customer_archetype` ~ `val.parquet.customer_ltv`
- `historical_records.csv.customer_archetype` ~ `val.parquet.customer_failure_rate`
- `historical_records.csv.customer_archetype` ~ `val.parquet.customer_id`
- `historical_records.csv.customer_archetype` ~ `val.parquet.customer_opted_out`
- `historical_records.csv.interventions_count` ~ `val.parquet.subscription_paid_count`
- `historical_records.csv.interventions_count` ~ `val.parquet.subscription_remaining_count`
- `historical_records.csv.interventions_count` ~ `val.parquet.attempt_count`
- `historical_records.csv.customer_opted_out` ~ `val.parquet.customer_ltv`
- `historical_records.csv.customer_opted_out` ~ `val.parquet.customer_id`
- `historical_records.csv.customer_opted_out` ~ `val.parquet.customer_archetype`
- `historical_records.csv.failure_reason` ~ `val.parquet.customer_failure_rate`
- `historical_records.csv.failure_reason` ~ `val.parquet.hours_since_first_failure`
- `historical_records.csv.subscription_id` ~ `val.parquet.record_id`
- `historical_records.csv.subscription_id` ~ `val.parquet.customer_id`
- `historical_records.csv.subscription_id` ~ `val.parquet.subscription_paid_count`
- `historical_records.csv.subscription_id` ~ `val.parquet.subscription_remaining_count`
- `historical_records.csv.hours_since_first_failure` ~ `val.parquet.failure_reason`
- `historical_records.csv.subscription_remaining_count` ~ `val.parquet.subscription_paid_count`
- `historical_records.csv.subscription_remaining_count` ~ `val.parquet.interventions_count`
- `historical_records.csv.subscription_remaining_count` ~ `val.parquet.subscription_id`
- `historical_records.csv.subscription_remaining_count` ~ `val.parquet.attempt_count`
- `historical_records.csv.attempt_count` ~ `val.parquet.subscription_paid_count`
- `historical_records.csv.attempt_count` ~ `val.parquet.interventions_count`
- `historical_records.csv.attempt_count` ~ `val.parquet.subscription_remaining_count`
- `historical_records.csv.action_taken` ~ `val.parquet.action_cost`
- `historical_records.parquet.interventions_count` ~ `live_persona_state.json.seen_interventions`
- `historical_records.parquet.recovered` ~ `test.parquet.recovered_amount`
- `historical_records.parquet.record_id` ~ `test.parquet.customer_id`
- `historical_records.parquet.record_id` ~ `test.parquet.subscription_id`
- `historical_records.parquet.amount` ~ `test.parquet.recovered_amount`
- `historical_records.parquet.customer_ltv` ~ `test.parquet.customer_failure_rate`
- `historical_records.parquet.customer_ltv` ~ `test.parquet.customer_id`
- `historical_records.parquet.customer_ltv` ~ `test.parquet.customer_archetype`
- `historical_records.parquet.customer_ltv` ~ `test.parquet.customer_opted_out`
- `historical_records.parquet.recovered_amount` ~ `test.parquet.recovered`
- `historical_records.parquet.recovered_amount` ~ `test.parquet.amount`
- `historical_records.parquet.customer_failure_rate` ~ `test.parquet.customer_ltv`
- `historical_records.parquet.customer_failure_rate` ~ `test.parquet.customer_id`
- `historical_records.parquet.customer_failure_rate` ~ `test.parquet.customer_archetype`
- `historical_records.parquet.customer_failure_rate` ~ `test.parquet.failure_reason`
- `historical_records.parquet.customer_id` ~ `test.parquet.record_id`
- `historical_records.parquet.customer_id` ~ `test.parquet.customer_ltv`
- `historical_records.parquet.customer_id` ~ `test.parquet.customer_failure_rate`
- `historical_records.parquet.customer_id` ~ `test.parquet.customer_archetype`
- `historical_records.parquet.customer_id` ~ `test.parquet.customer_opted_out`
- `historical_records.parquet.customer_id` ~ `test.parquet.subscription_id`
- `historical_records.parquet.subscription_paid_count` ~ `test.parquet.interventions_count`
- `historical_records.parquet.subscription_paid_count` ~ `test.parquet.subscription_id`
- `historical_records.parquet.subscription_paid_count` ~ `test.parquet.subscription_remaining_count`
- `historical_records.parquet.subscription_paid_count` ~ `test.parquet.attempt_count`
- `historical_records.parquet.action_cost` ~ `test.parquet.action_taken`
- `historical_records.parquet.customer_archetype` ~ `test.parquet.customer_ltv`
- `historical_records.parquet.customer_archetype` ~ `test.parquet.customer_failure_rate`
- `historical_records.parquet.customer_archetype` ~ `test.parquet.customer_id`
- `historical_records.parquet.customer_archetype` ~ `test.parquet.customer_opted_out`
- `historical_records.parquet.interventions_count` ~ `test.parquet.subscription_paid_count`
- `historical_records.parquet.interventions_count` ~ `test.parquet.subscription_remaining_count`
- `historical_records.parquet.interventions_count` ~ `test.parquet.attempt_count`
- `historical_records.parquet.customer_opted_out` ~ `test.parquet.customer_ltv`
- `historical_records.parquet.customer_opted_out` ~ `test.parquet.customer_id`
- `historical_records.parquet.customer_opted_out` ~ `test.parquet.customer_archetype`
- `historical_records.parquet.failure_reason` ~ `test.parquet.customer_failure_rate`
- `historical_records.parquet.failure_reason` ~ `test.parquet.hours_since_first_failure`
- `historical_records.parquet.subscription_id` ~ `test.parquet.record_id`
- `historical_records.parquet.subscription_id` ~ `test.parquet.customer_id`
- `historical_records.parquet.subscription_id` ~ `test.parquet.subscription_paid_count`
- `historical_records.parquet.subscription_id` ~ `test.parquet.subscription_remaining_count`
- `historical_records.parquet.hours_since_first_failure` ~ `test.parquet.failure_reason`
- `historical_records.parquet.subscription_remaining_count` ~ `test.parquet.subscription_paid_count`
- `historical_records.parquet.subscription_remaining_count` ~ `test.parquet.interventions_count`
- `historical_records.parquet.subscription_remaining_count` ~ `test.parquet.subscription_id`
- `historical_records.parquet.subscription_remaining_count` ~ `test.parquet.attempt_count`
- `historical_records.parquet.attempt_count` ~ `test.parquet.subscription_paid_count`
- `historical_records.parquet.attempt_count` ~ `test.parquet.interventions_count`
- `historical_records.parquet.attempt_count` ~ `test.parquet.subscription_remaining_count`
- `historical_records.parquet.action_taken` ~ `test.parquet.action_cost`
- `historical_records.parquet.recovered` ~ `train.parquet.recovered_amount`
- `historical_records.parquet.record_id` ~ `train.parquet.customer_id`
- `historical_records.parquet.record_id` ~ `train.parquet.subscription_id`
- `historical_records.parquet.amount` ~ `train.parquet.recovered_amount`
- `historical_records.parquet.customer_ltv` ~ `train.parquet.customer_failure_rate`
- `historical_records.parquet.customer_ltv` ~ `train.parquet.customer_id`
- `historical_records.parquet.customer_ltv` ~ `train.parquet.customer_archetype`
- `historical_records.parquet.customer_ltv` ~ `train.parquet.customer_opted_out`
- `historical_records.parquet.recovered_amount` ~ `train.parquet.recovered`
- `historical_records.parquet.recovered_amount` ~ `train.parquet.amount`
- `historical_records.parquet.customer_failure_rate` ~ `train.parquet.customer_ltv`
- `historical_records.parquet.customer_failure_rate` ~ `train.parquet.customer_id`
- `historical_records.parquet.customer_failure_rate` ~ `train.parquet.customer_archetype`
- `historical_records.parquet.customer_failure_rate` ~ `train.parquet.failure_reason`
- `historical_records.parquet.customer_id` ~ `train.parquet.record_id`
- `historical_records.parquet.customer_id` ~ `train.parquet.customer_ltv`
- `historical_records.parquet.customer_id` ~ `train.parquet.customer_failure_rate`
- `historical_records.parquet.customer_id` ~ `train.parquet.customer_archetype`
- `historical_records.parquet.customer_id` ~ `train.parquet.customer_opted_out`
- `historical_records.parquet.customer_id` ~ `train.parquet.subscription_id`
- `historical_records.parquet.subscription_paid_count` ~ `train.parquet.interventions_count`
- `historical_records.parquet.subscription_paid_count` ~ `train.parquet.subscription_id`
- `historical_records.parquet.subscription_paid_count` ~ `train.parquet.subscription_remaining_count`
- `historical_records.parquet.subscription_paid_count` ~ `train.parquet.attempt_count`
- `historical_records.parquet.action_cost` ~ `train.parquet.action_taken`
- `historical_records.parquet.customer_archetype` ~ `train.parquet.customer_ltv`
- `historical_records.parquet.customer_archetype` ~ `train.parquet.customer_failure_rate`
- `historical_records.parquet.customer_archetype` ~ `train.parquet.customer_id`
- `historical_records.parquet.customer_archetype` ~ `train.parquet.customer_opted_out`
- `historical_records.parquet.interventions_count` ~ `train.parquet.subscription_paid_count`
- `historical_records.parquet.interventions_count` ~ `train.parquet.subscription_remaining_count`
- `historical_records.parquet.interventions_count` ~ `train.parquet.attempt_count`
- `historical_records.parquet.customer_opted_out` ~ `train.parquet.customer_ltv`
- `historical_records.parquet.customer_opted_out` ~ `train.parquet.customer_id`
- `historical_records.parquet.customer_opted_out` ~ `train.parquet.customer_archetype`
- `historical_records.parquet.failure_reason` ~ `train.parquet.customer_failure_rate`
- `historical_records.parquet.failure_reason` ~ `train.parquet.hours_since_first_failure`
- `historical_records.parquet.subscription_id` ~ `train.parquet.record_id`
- `historical_records.parquet.subscription_id` ~ `train.parquet.customer_id`
- `historical_records.parquet.subscription_id` ~ `train.parquet.subscription_paid_count`
- `historical_records.parquet.subscription_id` ~ `train.parquet.subscription_remaining_count`
- `historical_records.parquet.hours_since_first_failure` ~ `train.parquet.failure_reason`
- `historical_records.parquet.subscription_remaining_count` ~ `train.parquet.subscription_paid_count`
- `historical_records.parquet.subscription_remaining_count` ~ `train.parquet.interventions_count`
- `historical_records.parquet.subscription_remaining_count` ~ `train.parquet.subscription_id`
- `historical_records.parquet.subscription_remaining_count` ~ `train.parquet.attempt_count`
- `historical_records.parquet.attempt_count` ~ `train.parquet.subscription_paid_count`
- `historical_records.parquet.attempt_count` ~ `train.parquet.interventions_count`
- `historical_records.parquet.attempt_count` ~ `train.parquet.subscription_remaining_count`
- `historical_records.parquet.action_taken` ~ `train.parquet.action_cost`
- `historical_records.parquet.recovered` ~ `val.parquet.recovered_amount`
- `historical_records.parquet.record_id` ~ `val.parquet.customer_id`
- `historical_records.parquet.record_id` ~ `val.parquet.subscription_id`
- `historical_records.parquet.amount` ~ `val.parquet.recovered_amount`
- `historical_records.parquet.customer_ltv` ~ `val.parquet.customer_failure_rate`
- `historical_records.parquet.customer_ltv` ~ `val.parquet.customer_id`
- `historical_records.parquet.customer_ltv` ~ `val.parquet.customer_archetype`
- `historical_records.parquet.customer_ltv` ~ `val.parquet.customer_opted_out`
- `historical_records.parquet.recovered_amount` ~ `val.parquet.recovered`
- `historical_records.parquet.recovered_amount` ~ `val.parquet.amount`
- `historical_records.parquet.customer_failure_rate` ~ `val.parquet.customer_ltv`
- `historical_records.parquet.customer_failure_rate` ~ `val.parquet.customer_id`
- `historical_records.parquet.customer_failure_rate` ~ `val.parquet.customer_archetype`
- `historical_records.parquet.customer_failure_rate` ~ `val.parquet.failure_reason`
- `historical_records.parquet.customer_id` ~ `val.parquet.record_id`
- `historical_records.parquet.customer_id` ~ `val.parquet.customer_ltv`
- `historical_records.parquet.customer_id` ~ `val.parquet.customer_failure_rate`
- `historical_records.parquet.customer_id` ~ `val.parquet.customer_archetype`
- `historical_records.parquet.customer_id` ~ `val.parquet.customer_opted_out`
- `historical_records.parquet.customer_id` ~ `val.parquet.subscription_id`
- `historical_records.parquet.subscription_paid_count` ~ `val.parquet.interventions_count`
- `historical_records.parquet.subscription_paid_count` ~ `val.parquet.subscription_id`
- `historical_records.parquet.subscription_paid_count` ~ `val.parquet.subscription_remaining_count`
- `historical_records.parquet.subscription_paid_count` ~ `val.parquet.attempt_count`
- `historical_records.parquet.action_cost` ~ `val.parquet.action_taken`
- `historical_records.parquet.customer_archetype` ~ `val.parquet.customer_ltv`
- `historical_records.parquet.customer_archetype` ~ `val.parquet.customer_failure_rate`
- `historical_records.parquet.customer_archetype` ~ `val.parquet.customer_id`
- `historical_records.parquet.customer_archetype` ~ `val.parquet.customer_opted_out`
- `historical_records.parquet.interventions_count` ~ `val.parquet.subscription_paid_count`
- `historical_records.parquet.interventions_count` ~ `val.parquet.subscription_remaining_count`
- `historical_records.parquet.interventions_count` ~ `val.parquet.attempt_count`
- `historical_records.parquet.customer_opted_out` ~ `val.parquet.customer_ltv`
- `historical_records.parquet.customer_opted_out` ~ `val.parquet.customer_id`
- `historical_records.parquet.customer_opted_out` ~ `val.parquet.customer_archetype`
- `historical_records.parquet.failure_reason` ~ `val.parquet.customer_failure_rate`
- `historical_records.parquet.failure_reason` ~ `val.parquet.hours_since_first_failure`
- `historical_records.parquet.subscription_id` ~ `val.parquet.record_id`
- `historical_records.parquet.subscription_id` ~ `val.parquet.customer_id`
- `historical_records.parquet.subscription_id` ~ `val.parquet.subscription_paid_count`
- `historical_records.parquet.subscription_id` ~ `val.parquet.subscription_remaining_count`
- `historical_records.parquet.hours_since_first_failure` ~ `val.parquet.failure_reason`
- `historical_records.parquet.subscription_remaining_count` ~ `val.parquet.subscription_paid_count`
- `historical_records.parquet.subscription_remaining_count` ~ `val.parquet.interventions_count`
- `historical_records.parquet.subscription_remaining_count` ~ `val.parquet.subscription_id`
- `historical_records.parquet.subscription_remaining_count` ~ `val.parquet.attempt_count`
- `historical_records.parquet.attempt_count` ~ `val.parquet.subscription_paid_count`
- `historical_records.parquet.attempt_count` ~ `val.parquet.interventions_count`
- `historical_records.parquet.attempt_count` ~ `val.parquet.subscription_remaining_count`
- `historical_records.parquet.action_taken` ~ `val.parquet.action_cost`
- `live_persona_state.json.seen_interventions` ~ `test.parquet.interventions_count`
- `live_persona_state.json.seen_interventions` ~ `train.parquet.interventions_count`
- `live_persona_state.json.seen_interventions` ~ `val.parquet.interventions_count`
- `sample_data/california_housing_test.csv.total_bedrooms` ~ `sample_data/california_housing_train.csv.total_rooms`
- `sample_data/california_housing_test.csv.median_income` ~ `sample_data/california_housing_train.csv.housing_median_age`
- `sample_data/california_housing_test.csv.median_income` ~ `sample_data/california_housing_train.csv.median_house_value`
- `sample_data/california_housing_test.csv.housing_median_age` ~ `sample_data/california_housing_train.csv.median_income`
- `sample_data/california_housing_test.csv.total_rooms` ~ `sample_data/california_housing_train.csv.total_bedrooms`
- `sample_data/california_housing_test.csv.median_house_value` ~ `sample_data/california_housing_train.csv.median_income`
- `test.parquet.recovered` ~ `train.parquet.recovered_amount`
- `test.parquet.record_id` ~ `train.parquet.customer_id`
- `test.parquet.record_id` ~ `train.parquet.subscription_id`
- `test.parquet.amount` ~ `train.parquet.recovered_amount`
- `test.parquet.customer_ltv` ~ `train.parquet.customer_failure_rate`
- `test.parquet.customer_ltv` ~ `train.parquet.customer_id`
- `test.parquet.customer_ltv` ~ `train.parquet.customer_archetype`
- `test.parquet.customer_ltv` ~ `train.parquet.customer_opted_out`
- `test.parquet.recovered_amount` ~ `train.parquet.recovered`
- `test.parquet.recovered_amount` ~ `train.parquet.amount`
- `test.parquet.customer_failure_rate` ~ `train.parquet.customer_ltv`
- `test.parquet.customer_failure_rate` ~ `train.parquet.customer_id`
- `test.parquet.customer_failure_rate` ~ `train.parquet.customer_archetype`
- `test.parquet.customer_failure_rate` ~ `train.parquet.failure_reason`
- `test.parquet.customer_id` ~ `train.parquet.record_id`
- `test.parquet.customer_id` ~ `train.parquet.customer_ltv`
- `test.parquet.customer_id` ~ `train.parquet.customer_failure_rate`
- `test.parquet.customer_id` ~ `train.parquet.customer_archetype`
- `test.parquet.customer_id` ~ `train.parquet.customer_opted_out`
- `test.parquet.customer_id` ~ `train.parquet.subscription_id`
- `test.parquet.subscription_paid_count` ~ `train.parquet.interventions_count`
- `test.parquet.subscription_paid_count` ~ `train.parquet.subscription_id`
- `test.parquet.subscription_paid_count` ~ `train.parquet.subscription_remaining_count`
- `test.parquet.subscription_paid_count` ~ `train.parquet.attempt_count`
- `test.parquet.action_cost` ~ `train.parquet.action_taken`
- `test.parquet.customer_archetype` ~ `train.parquet.customer_ltv`
- `test.parquet.customer_archetype` ~ `train.parquet.customer_failure_rate`
- `test.parquet.customer_archetype` ~ `train.parquet.customer_id`
- `test.parquet.customer_archetype` ~ `train.parquet.customer_opted_out`
- `test.parquet.interventions_count` ~ `train.parquet.subscription_paid_count`
- `test.parquet.interventions_count` ~ `train.parquet.subscription_remaining_count`
- `test.parquet.interventions_count` ~ `train.parquet.attempt_count`
- `test.parquet.customer_opted_out` ~ `train.parquet.customer_ltv`
- `test.parquet.customer_opted_out` ~ `train.parquet.customer_id`
- `test.parquet.customer_opted_out` ~ `train.parquet.customer_archetype`
- `test.parquet.failure_reason` ~ `train.parquet.customer_failure_rate`
- `test.parquet.failure_reason` ~ `train.parquet.hours_since_first_failure`
- `test.parquet.subscription_id` ~ `train.parquet.record_id`
- `test.parquet.subscription_id` ~ `train.parquet.customer_id`
- `test.parquet.subscription_id` ~ `train.parquet.subscription_paid_count`
- `test.parquet.subscription_id` ~ `train.parquet.subscription_remaining_count`
- `test.parquet.hours_since_first_failure` ~ `train.parquet.failure_reason`
- `test.parquet.subscription_remaining_count` ~ `train.parquet.subscription_paid_count`
- `test.parquet.subscription_remaining_count` ~ `train.parquet.interventions_count`
- `test.parquet.subscription_remaining_count` ~ `train.parquet.subscription_id`
- `test.parquet.subscription_remaining_count` ~ `train.parquet.attempt_count`
- `test.parquet.attempt_count` ~ `train.parquet.subscription_paid_count`
- `test.parquet.attempt_count` ~ `train.parquet.interventions_count`
- `test.parquet.attempt_count` ~ `train.parquet.subscription_remaining_count`
- `test.parquet.action_taken` ~ `train.parquet.action_cost`
- `test.parquet.recovered` ~ `val.parquet.recovered_amount`
- `test.parquet.record_id` ~ `val.parquet.customer_id`
- `test.parquet.record_id` ~ `val.parquet.subscription_id`
- `test.parquet.amount` ~ `val.parquet.recovered_amount`
- `test.parquet.customer_ltv` ~ `val.parquet.customer_failure_rate`
- `test.parquet.customer_ltv` ~ `val.parquet.customer_id`
- `test.parquet.customer_ltv` ~ `val.parquet.customer_archetype`
- `test.parquet.customer_ltv` ~ `val.parquet.customer_opted_out`
- `test.parquet.recovered_amount` ~ `val.parquet.recovered`
- `test.parquet.recovered_amount` ~ `val.parquet.amount`
- `test.parquet.customer_failure_rate` ~ `val.parquet.customer_ltv`
- `test.parquet.customer_failure_rate` ~ `val.parquet.customer_id`
- `test.parquet.customer_failure_rate` ~ `val.parquet.customer_archetype`
- `test.parquet.customer_failure_rate` ~ `val.parquet.failure_reason`
- `test.parquet.customer_id` ~ `val.parquet.record_id`
- `test.parquet.customer_id` ~ `val.parquet.customer_ltv`
- `test.parquet.customer_id` ~ `val.parquet.customer_failure_rate`
- `test.parquet.customer_id` ~ `val.parquet.customer_archetype`
- `test.parquet.customer_id` ~ `val.parquet.customer_opted_out`
- `test.parquet.customer_id` ~ `val.parquet.subscription_id`
- `test.parquet.subscription_paid_count` ~ `val.parquet.interventions_count`
- `test.parquet.subscription_paid_count` ~ `val.parquet.subscription_id`
- `test.parquet.subscription_paid_count` ~ `val.parquet.subscription_remaining_count`
- `test.parquet.subscription_paid_count` ~ `val.parquet.attempt_count`
- `test.parquet.action_cost` ~ `val.parquet.action_taken`
- `test.parquet.customer_archetype` ~ `val.parquet.customer_ltv`
- `test.parquet.customer_archetype` ~ `val.parquet.customer_failure_rate`
- `test.parquet.customer_archetype` ~ `val.parquet.customer_id`
- `test.parquet.customer_archetype` ~ `val.parquet.customer_opted_out`
- `test.parquet.interventions_count` ~ `val.parquet.subscription_paid_count`
- `test.parquet.interventions_count` ~ `val.parquet.subscription_remaining_count`
- `test.parquet.interventions_count` ~ `val.parquet.attempt_count`
- `test.parquet.customer_opted_out` ~ `val.parquet.customer_ltv`
- `test.parquet.customer_opted_out` ~ `val.parquet.customer_id`
- `test.parquet.customer_opted_out` ~ `val.parquet.customer_archetype`
- `test.parquet.failure_reason` ~ `val.parquet.customer_failure_rate`
- `test.parquet.failure_reason` ~ `val.parquet.hours_since_first_failure`
- `test.parquet.subscription_id` ~ `val.parquet.record_id`
- `test.parquet.subscription_id` ~ `val.parquet.customer_id`
- `test.parquet.subscription_id` ~ `val.parquet.subscription_paid_count`
- `test.parquet.subscription_id` ~ `val.parquet.subscription_remaining_count`
- `test.parquet.hours_since_first_failure` ~ `val.parquet.failure_reason`
- `test.parquet.subscription_remaining_count` ~ `val.parquet.subscription_paid_count`
- `test.parquet.subscription_remaining_count` ~ `val.parquet.interventions_count`
- `test.parquet.subscription_remaining_count` ~ `val.parquet.subscription_id`
- `test.parquet.subscription_remaining_count` ~ `val.parquet.attempt_count`
- `test.parquet.attempt_count` ~ `val.parquet.subscription_paid_count`
- `test.parquet.attempt_count` ~ `val.parquet.interventions_count`
- `test.parquet.attempt_count` ~ `val.parquet.subscription_remaining_count`
- `test.parquet.action_taken` ~ `val.parquet.action_cost`
- `train.parquet.recovered` ~ `val.parquet.recovered_amount`
- `train.parquet.record_id` ~ `val.parquet.customer_id`
- `train.parquet.record_id` ~ `val.parquet.subscription_id`
- `train.parquet.amount` ~ `val.parquet.recovered_amount`
- `train.parquet.customer_ltv` ~ `val.parquet.customer_failure_rate`
- `train.parquet.customer_ltv` ~ `val.parquet.customer_id`
- `train.parquet.customer_ltv` ~ `val.parquet.customer_archetype`
- `train.parquet.customer_ltv` ~ `val.parquet.customer_opted_out`
- `train.parquet.recovered_amount` ~ `val.parquet.recovered`
- `train.parquet.recovered_amount` ~ `val.parquet.amount`
- `train.parquet.customer_failure_rate` ~ `val.parquet.customer_ltv`
- `train.parquet.customer_failure_rate` ~ `val.parquet.customer_id`
- `train.parquet.customer_failure_rate` ~ `val.parquet.customer_archetype`
- `train.parquet.customer_failure_rate` ~ `val.parquet.failure_reason`
- `train.parquet.customer_id` ~ `val.parquet.record_id`
- `train.parquet.customer_id` ~ `val.parquet.customer_ltv`
- `train.parquet.customer_id` ~ `val.parquet.customer_failure_rate`
- `train.parquet.customer_id` ~ `val.parquet.customer_archetype`
- `train.parquet.customer_id` ~ `val.parquet.customer_opted_out`
- `train.parquet.customer_id` ~ `val.parquet.subscription_id`
- `train.parquet.subscription_paid_count` ~ `val.parquet.interventions_count`
- `train.parquet.subscription_paid_count` ~ `val.parquet.subscription_id`
- `train.parquet.subscription_paid_count` ~ `val.parquet.subscription_remaining_count`
- `train.parquet.subscription_paid_count` ~ `val.parquet.attempt_count`
- `train.parquet.action_cost` ~ `val.parquet.action_taken`
- `train.parquet.customer_archetype` ~ `val.parquet.customer_ltv`
- `train.parquet.customer_archetype` ~ `val.parquet.customer_failure_rate`
- `train.parquet.customer_archetype` ~ `val.parquet.customer_id`
- `train.parquet.customer_archetype` ~ `val.parquet.customer_opted_out`
- `train.parquet.interventions_count` ~ `val.parquet.subscription_paid_count`
- `train.parquet.interventions_count` ~ `val.parquet.subscription_remaining_count`
- `train.parquet.interventions_count` ~ `val.parquet.attempt_count`
- `train.parquet.customer_opted_out` ~ `val.parquet.customer_ltv`
- `train.parquet.customer_opted_out` ~ `val.parquet.customer_id`
- `train.parquet.customer_opted_out` ~ `val.parquet.customer_archetype`
- `train.parquet.failure_reason` ~ `val.parquet.customer_failure_rate`
- `train.parquet.failure_reason` ~ `val.parquet.hours_since_first_failure`
- `train.parquet.subscription_id` ~ `val.parquet.record_id`
- `train.parquet.subscription_id` ~ `val.parquet.customer_id`
- `train.parquet.subscription_id` ~ `val.parquet.subscription_paid_count`
- `train.parquet.subscription_id` ~ `val.parquet.subscription_remaining_count`
- `train.parquet.hours_since_first_failure` ~ `val.parquet.failure_reason`
- `train.parquet.subscription_remaining_count` ~ `val.parquet.subscription_paid_count`
- `train.parquet.subscription_remaining_count` ~ `val.parquet.interventions_count`
- `train.parquet.subscription_remaining_count` ~ `val.parquet.subscription_id`
- `train.parquet.subscription_remaining_count` ~ `val.parquet.attempt_count`
- `train.parquet.attempt_count` ~ `val.parquet.subscription_paid_count`
- `train.parquet.attempt_count` ~ `val.parquet.interventions_count`
- `train.parquet.attempt_count` ~ `val.parquet.subscription_remaining_count`
- `train.parquet.action_taken` ~ `val.parquet.action_cost`

**Note:** This is a schema-inspection report only. Datasets have NOT been merged, modified, or judged for ML-readiness. Review the flagged columns above before deciding which columns to keep/rename/drop when constructing a unified dataset.
