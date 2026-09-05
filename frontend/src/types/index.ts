export interface CandidateAction {
  action_type: string;
  natural_recovery_prob: number;
  action_recovery_prob: number;
  incremental_lift: number;
  payment_amount: number;
  expected_recovery_value: number;
  expected_incremental_revenue: number;
  action_cost: number;
  incentive_cost: number;
  friction_cost: number;
  total_cost: number;
  expected_incremental_contribution: number;
  policy_allowed: boolean;
  policy_block_reason?: string;
  rank: number;
  is_selected: boolean;
}

export interface DecisionRecord {
  id?: string;
  decision: 'ACT' | 'WAIT' | 'DONT_ACT' | 'ESCALATE';
  recommended_action: string;
  recommended_timing: string;
  incremental_lift?: number;
  expected_incremental_revenue?: number;
  expected_incremental_contribution?: number;
  confidence: number;
  policy_status: 'APPROVED' | 'VETOED' | 'SUPPRESSED' | 'ESCALATED';
  policy_reason?: string;
  reason: string;
  candidate_actions: CandidateAction[];
  ml_model_name: string;
  ml_model_version: string;
  natural_recovery_prob: number;
}

export interface Case {
  id: string;
  payment_id: string;
  order_id?: string;
  customer_id: string;
  customer_name?: string;
  customer_email?: string;
  customer_phone?: string;
  amount: number;
  currency: string;
  payment_method?: string;
  failure_code?: string;
  failure_reason?: string;
  issuing_bank?: string;
  attempt_count: number;
  status: string;
  final_decision?: 'ACT' | 'WAIT' | 'DONT_ACT' | 'ESCALATE';
  recommended_action?: string;
  executed_action?: string;
  policy_status?: string;
  natural_recovery_prob?: number;
  best_action_recovery_prob?: number;
  incremental_lift?: number;
  expected_incremental_contribution?: number;
  decision_confidence?: number;
  decision_reason?: string;
  experiment_id?: string;
  experiment_group?: string;
  created_at: string;
  updated_at: string;
}

export interface CaseDetail extends Case {
  contexts?: any[];
  decisions?: DecisionRecord[];
  action_executions?: any[];
  outcomes?: any[];
  policy_evaluations?: any[];
}

export interface TimelineEvent {
  id: string;
  timestamp: string;
  event_type: string;
  actor: string;
  summary: string;
  details?: Record<string, any>;
}

export interface DashboardKPIs {
  revenue_at_risk: number;
  expected_recoverable_revenue: number;
  total_incremental_contribution: number;
  gross_recovery_rate_pct: number;
  average_incremental_lift_pct: number;
  total_intervention_cost: number;
  active_recovery_cases: number;
  cases_suppressed_by_safety: number;
  recovered_cases_count: number;
  total_cases_analyzed: number;
}

export interface ActionPerformance {
  action_type: string;
  count_executed: number;
  success_rate_pct: number;
  total_cost: number;
  net_contribution: number;
}

export interface LiftBucket {
  bucket_label: string;
  case_count: number;
  avg_contribution: number;
}

export interface AnalyticsOverview {
  kpis: DashboardKPIs;
  actions_breakdown: ActionPerformance[];
  lift_distribution: LiftBucket[];
  recent_activity: any[];
}

export interface ScenarioDefinition {
  id?: string;
  scenario_id?: string;
  title: string;
  description: string;
  customer_name: string;
  amount: number;
  payment_method?: string;
  failure_code?: string;
  failure_reason?: string;
  natural_recovery_rate: number;
  expected_decision: string;
  expected_action?: string;
  expected_rationale: string;
}

export interface PolicyBenchmarkMetrics {
  policy_name: string;
  policy_description: string;
  total_cases: number;
  interventions_triggered: number;
  interventions_suppressed_by_safety: number;
  gross_recovered_cases: number;
  gross_recovery_rate_pct: number;
  gross_recovered_revenue: number;
  natural_recovered_revenue: number;
  true_incremental_revenue: number;
  true_incremental_lift_pct: number;
  total_intervention_cost: number;
  net_incremental_contribution: number;
  contribution_per_contacted_inr: number;
  unnecessary_interventions_count: number;
}

export interface MultiPolicyBenchmarkResult {
  simulation_id: string;
  total_cases_simulated: number;
  timestamp: string;
  policies: Record<string, PolicyBenchmarkMetrics>;
  winner_policy: string;
  incremental_value_generated_over_propensity: number;
  unnecessary_contacts_avoided_count: number;
}
