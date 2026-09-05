/**
 * REST API Client for Recovery Intelligence & Allocation Engine
 */
import {
  Case,
  CaseDetail,
  DecisionRecord,
  AnalyticsOverview,
  ScenarioDefinition,
  MultiPolicyBenchmarkResult,
  TimelineEvent,
} from '../types';

const API_BASE = '/api';

export const api = {
  // Analytics / Overview
  async getAnalytics(): Promise<AnalyticsOverview> {
    const res = await fetch(`${API_BASE}/analytics/overview`);
    if (!res.ok) throw new Error('Failed to fetch analytics');
    return res.json();
  },

  // Cases
  async getCases(params?: { status?: string; decision?: string; search?: string }): Promise<Case[]> {
    const query = new URLSearchParams();
    if (params?.status) query.append('status', params.status);
    if (params?.decision) query.append('decision', params.decision);
    if (params?.search) query.append('search', params.search);
    const res = await fetch(`${API_BASE}/cases?${query.toString()}`);
    if (!res.ok) throw new Error('Failed to fetch cases');
    return res.json();
  },

  async getCaseDetail(caseId: string): Promise<CaseDetail> {
    const res = await fetch(`${API_BASE}/cases/${caseId}`);
    if (!res.ok) throw new Error(`Failed to fetch case ${caseId}`);
    return res.json();
  },

  async getCaseTimeline(caseId: string): Promise<{ events: TimelineEvent[]; case_id: string }> {
    const res = await fetch(`${API_BASE}/cases/${caseId}/timeline`);
    if (!res.ok) throw new Error(`Failed to fetch timeline for ${caseId}`);
    return res.json();
  },

  // Decisions
  async evaluateDecision(caseId: string, simulatedHour?: number): Promise<DecisionRecord> {
    const query = simulatedHour !== undefined ? `?simulated_hour=${simulatedHour}` : '';
    const res = await fetch(`${API_BASE}/decisions/evaluate/${caseId}${query}`, { method: 'POST' });
    if (!res.ok) throw new Error(`Failed to evaluate decision for ${caseId}`);
    return res.json();
  },

  async explainDecision(caseId: string): Promise<any> {
    const res = await fetch(`${API_BASE}/decisions/explain/${caseId}`);
    if (!res.ok) throw new Error(`Failed to fetch explanation for ${caseId}`);
    return res.json();
  },

  // Actions
  async executeAction(caseId: string, actionType?: string): Promise<any> {
    const res = await fetch(`${API_BASE}/actions/execute`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ case_id: caseId, action_type: actionType }),
    });
    if (!res.ok) throw new Error(`Failed to execute action for ${caseId}`);
    return res.json();
  },

  // Simulator
  async getScenarios(): Promise<ScenarioDefinition[]> {
    const res = await fetch(`${API_BASE}/simulator/scenarios`);
    if (!res.ok) throw new Error('Failed to fetch scenarios');
    return res.json();
  },

  async loadScenario(scenarioId: string): Promise<{ scenario: ScenarioDefinition; case_id: string; decision: DecisionRecord }> {
    const res = await fetch(`${API_BASE}/simulator/scenarios/${scenarioId}/load`, { method: 'POST' });
    if (!res.ok) throw new Error(`Failed to load scenario ${scenarioId}`);
    return res.json();
  },

  async runBenchmark(config: {
    num_cases?: number;
    natural_recovery_multiplier?: number;
    payment_link_effectiveness?: number;
    retry_effectiveness?: number;
    reminder_effectiveness?: number;
    customer_fatigue_penalty?: number;
    avg_payment_amount?: number;
  }): Promise<MultiPolicyBenchmarkResult> {
    const res = await fetch(`${API_BASE}/simulator/benchmark`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(config),
    });
    if (!res.ok) throw new Error('Failed to run benchmark');
    return res.json();
  },

  async generateBatch(numCases: number = 25): Promise<any> {
    const res = await fetch(`${API_BASE}/simulator/generate-batch`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ num_cases: numCases }),
    });
    if (!res.ok) throw new Error('Failed to generate synthetic batch');
    return res.json();
  },

  // Experiments
  async getExperiments(): Promise<any[]> {
    const res = await fetch(`${API_BASE}/experiments`);
    if (!res.ok) throw new Error('Failed to fetch experiments');
    return res.json();
  },

  async getExperimentMetrics(experimentId: string): Promise<any> {
    const res = await fetch(`${API_BASE}/experiments/${experimentId}/metrics`);
    if (!res.ok) throw new Error('Failed to fetch experiment metrics');
    return res.json();
  },

  // Governance
  async getGovernanceRules(): Promise<any[]> {
    const res = await fetch(`${API_BASE}/governance/rules`);
    if (!res.ok) throw new Error('Failed to fetch governance rules');
    return res.json();
  },

  async getVetoLogs(): Promise<any[]> {
    const res = await fetch(`${API_BASE}/governance/veto-logs`);
    if (!res.ok) throw new Error('Failed to fetch veto logs');
    return res.json();
  },

  async getAuditEvents(): Promise<any[]> {
    const res = await fetch(`${API_BASE}/audit/events?limit=100`);
    if (!res.ok) throw new Error('Failed to fetch audit events');
    return res.json();
  },

  // Demo
  async getDemoScenarios(): Promise<any[]> {
    const res = await fetch(`${API_BASE}/demo/scenarios`);
    if (!res.ok) throw new Error('Failed to fetch demo scenarios');
    return res.json();
  },

  async executeDemoScenario(scenarioId: string): Promise<any> {
    const res = await fetch(`${API_BASE}/demo/scenarios/${scenarioId}/execute`, { method: 'POST' });
    if (!res.ok) throw new Error(`Failed to execute demo scenario ${scenarioId}`);
    return res.json();
  },

  async seedAllDemoScenarios(): Promise<any> {
    const res = await fetch(`${API_BASE}/demo/seed-all`, { method: 'POST' });
    if (!res.ok) throw new Error('Failed to seed demo scenarios');
    return res.json();
  },
};
