import React, { useEffect, useState } from 'react';
import {
  ArrowLeft,
  CheckCircle2,
  AlertCircle,
  Clock,
  ShieldCheck,
  Zap,
  TrendingUp,
  Cpu,
  DollarSign,
  Play,
  RotateCcw,
  Sparkles,
  ExternalLink,
} from 'lucide-react';
import { api } from '../services/api';
import { CaseDetail as ICaseDetail, TimelineEvent } from '../types';
import { Badge } from '../components/common/Badge';

interface CaseDetailProps {
  caseId: string;
  onBack: () => void;
  onRefreshList: () => void;
}

export const CaseDetail: React.FC<CaseDetailProps> = ({
  caseId,
  onBack,
  onRefreshList,
}) => {
  const [caseData, setCaseData] = useState<ICaseDetail | null>(null);
  const [timeline, setTimeline] = useState<TimelineEvent[]>([]);
  const [loading, setLoading] = useState(true);
  const [executing, setExecuting] = useState(false);
  const [reEvaluating, setReEvaluating] = useState(false);

  const loadData = async () => {
    setLoading(true);
    try {
      const [detail, tl] = await Promise.all([
        api.getCaseDetail(caseId),
        api.getCaseTimeline(caseId),
      ]);
      setCaseData(detail);
      setTimeline(tl.events);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadData();
  }, [caseId]);

  const handleExecute = async () => {
    if (!caseData || !caseData.recommended_action) return;
    setExecuting(true);
    try {
      await api.executeAction(caseId, caseData.recommended_action);
      await loadData();
      onRefreshList();
    } catch (err) {
      console.error('Execution error:', err);
    } finally {
      setExecuting(false);
    }
  };

  const handleReEvaluate = async (hour?: number) => {
    setReEvaluating(true);
    try {
      await api.evaluateDecision(caseId, hour);
      await loadData();
      onRefreshList();
    } catch (err) {
      console.error('Re-evaluation error:', err);
    } finally {
      setReEvaluating(false);
    }
  };

  if (loading || !caseData) {
    return (
      <div className="flex items-center justify-center py-20 text-slate-400">
        <div className="flex flex-col items-center gap-3">
          <RotateCcw className="w-6 h-6 animate-spin text-indigo-400" />
          <span className="text-xs font-semibold">Loading Case Audit Timeline...</span>
        </div>
      </div>
    );
  }

  const latestDecision = caseData.decisions?.[caseData.decisions.length - 1];
  const candidates = latestDecision?.candidate_actions || [];
  const policies = caseData.policy_evaluations || [];
  const executions = caseData.action_executions || [];

  return (
    <div className="space-y-6">
      {/* Top Header & Breadcrumbs */}
      <div className="flex items-center justify-between gap-4">
        <button
          onClick={onBack}
          className="flex items-center gap-2 text-xs font-semibold text-slate-400 hover:text-white transition-colors"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Back to Recovery Queue</span>
        </button>

        <div className="flex items-center gap-3">
          {caseData.final_decision === 'ACT' && caseData.status !== 'ACTION_EXECUTED' && caseData.status !== 'RECOVERED' && (
            <button
              onClick={handleExecute}
              disabled={executing}
              className="px-4 py-2 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-bold text-xs shadow-lg shadow-emerald-600/30 transition-all flex items-center gap-2 disabled:opacity-50"
            >
              <Play className="w-3.5 h-3.5 fill-current" />
              <span>{executing ? 'Executing...' : `Execute Action (${caseData.recommended_action})`}</span>
            </button>
          )}

          <button
            onClick={() => handleReEvaluate()}
            disabled={reEvaluating}
            className="px-3.5 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 font-semibold text-xs transition-all flex items-center gap-1.5 disabled:opacity-50"
          >
            <RotateCcw className={`w-3.5 h-3.5 ${reEvaluating ? 'animate-spin text-indigo-400' : ''}`} />
            <span>Re-Evaluate</span>
          </button>
        </div>
      </div>

      {/* Hero Overview Card */}
      <div className="glass-panel rounded-2xl p-6 space-y-4 border border-indigo-900/40">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-4 border-b border-slate-800/80">
          <div>
            <div className="flex items-center gap-3">
              <h2 className="text-xl font-extrabold text-white tracking-tight">
                {caseData.customer_name || caseData.customer_id}
              </h2>
              <Badge
                variant={
                  caseData.final_decision === 'ACT'
                    ? 'emerald'
                    : caseData.final_decision === 'WAIT'
                    ? 'amber'
                    : caseData.final_decision === 'ESCALATE'
                    ? 'indigo'
                    : 'slate'
                }
                size="md"
              >
                {caseData.final_decision || caseData.status}
              </Badge>
            </div>
            <div className="flex items-center gap-3 text-xs text-slate-400 font-mono mt-1">
              <span>Payment ID: {caseData.payment_id}</span>
              <span>•</span>
              <span>Case ID: {caseData.id.slice(0, 8)}</span>
              <span>•</span>
              <span className="text-slate-300 font-sans font-semibold">
                Amount: ₹{caseData.amount.toLocaleString('en-IN')}
              </span>
            </div>
          </div>

          <div className="flex items-center gap-6 text-right">
            <div>
              <p className="text-[10px] uppercase tracking-wider text-slate-400 font-semibold">Natural Recovery</p>
              <p className="text-lg font-bold text-slate-200">
                {caseData.natural_recovery_prob ? `${Math.round(caseData.natural_recovery_prob * 100)}%` : '--'}
              </p>
            </div>
            <div>
              <p className="text-[10px] uppercase tracking-wider text-slate-400 font-semibold">Incremental Lift</p>
              <p className="text-lg font-bold text-emerald-400">
                {caseData.incremental_lift !== undefined && caseData.incremental_lift !== null
                  ? `+${Math.round(caseData.incremental_lift * 100)}%`
                  : '--'}
              </p>
            </div>
            <div>
              <p className="text-[10px] uppercase tracking-wider text-slate-400 font-semibold">Net Contribution</p>
              <p className="text-lg font-bold text-emerald-400">
                ₹{caseData.expected_incremental_contribution?.toLocaleString('en-IN') || '0.00'}
              </p>
            </div>
          </div>
        </div>

        {/* Decision Reasoning Alert */}
        {latestDecision && (
          <div className="rounded-xl bg-slate-900/90 border border-slate-700/60 p-4 space-y-2">
            <div className="flex items-center gap-2 text-xs font-bold text-indigo-400">
              <Sparkles className="w-4 h-4 text-yellow-400" />
              <span>Decision Explanation & Economic Justification</span>
            </div>
            <p className="text-xs text-slate-200 leading-relaxed">
              {latestDecision.reason}
            </p>
          </div>
        )}
      </div>

      {/* 2-Column Grid: 8-Step Timeline on Left, Economic Matrix on Right */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Left Column: 8-Step Audit Timeline */}
        <div className="lg:col-span-6 space-y-4">
          <div className="glass-panel rounded-2xl p-5 space-y-4">
            <div className="flex items-center justify-between border-b border-slate-800 pb-3">
              <h3 className="text-sm font-bold text-white flex items-center gap-2">
                <Clock className="w-4 h-4 text-indigo-400" />
                <span>8-Step Decision & Audit Trail</span>
              </h3>
              <Badge variant="indigo" size="sm">Immutable Log</Badge>
            </div>

            <div className="space-y-4 relative before:absolute before:left-4 before:top-2 before:bottom-2 before:w-0.5 before:bg-slate-800">
              {/* Step 1: Payment Failed */}
              <div className="relative flex items-start gap-4 pl-1">
                <div className="w-7 h-7 rounded-full bg-rose-950 border border-rose-800 text-rose-400 flex items-center justify-center shrink-0 z-10 text-xs font-bold">
                  1
                </div>
                <div className="bg-slate-900/60 border border-slate-800 rounded-xl p-3 flex-1 text-xs space-y-1">
                  <div className="flex items-center justify-between">
                    <span className="font-bold text-white">Payment Failed Ingested</span>
                    <span className="text-[10px] text-slate-400 font-mono">payment.failed</span>
                  </div>
                  <p className="text-slate-400">
                    Failed payment of <strong className="text-slate-200">₹{caseData.amount.toLocaleString('en-IN')}</strong> via {caseData.payment_method}. Error code: <span className="font-mono text-rose-400">{caseData.failure_code}</span>.
                  </p>
                </div>
              </div>

              {/* Step 2: Context Diagnosis */}
              <div className="relative flex items-start gap-4 pl-1">
                <div className="w-7 h-7 rounded-full bg-slate-800 border border-slate-700 text-slate-300 flex items-center justify-center shrink-0 z-10 text-xs font-bold">
                  2
                </div>
                <div className="bg-slate-900/60 border border-slate-800 rounded-xl p-3 flex-1 text-xs space-y-1">
                  <span className="font-bold text-white">Context Aggregated</span>
                  <p className="text-slate-400">
                    Customer history: {caseData.contexts?.[0]?.tenure_days || 45} days tenure, segment: <strong className="text-indigo-400">{caseData.contexts?.[0]?.segment || 'standard'}</strong>, attempts: {caseData.attempt_count}.
                  </p>
                </div>
              </div>

              {/* Step 3: ML Inference */}
              <div className="relative flex items-start gap-4 pl-1">
                <div className="w-7 h-7 rounded-full bg-indigo-950 border border-indigo-800 text-indigo-400 flex items-center justify-center shrink-0 z-10 text-xs font-bold">
                  3
                </div>
                <div className="bg-slate-900/60 border border-slate-800 rounded-xl p-3 flex-1 text-xs space-y-1">
                  <div className="flex items-center justify-between">
                    <span className="font-bold text-white">ML Model Inference</span>
                    <Badge variant="indigo" size="sm">Confidence: {Math.round((latestDecision?.confidence || 0.85) * 100)}%</Badge>
                  </div>
                  <p className="text-slate-400">
                    Natural Recovery Probability: <strong className="text-white">{Math.round((latestDecision?.natural_recovery_prob || 0) * 100)}%</strong>. Model version: <span className="font-mono text-slate-300">{latestDecision?.ml_model_name} ({latestDecision?.ml_model_version})</span>.
                  </p>
                </div>
              </div>

              {/* Step 4 & 5: Candidate Actions & Economic Allocation */}
              <div className="relative flex items-start gap-4 pl-1">
                <div className="w-7 h-7 rounded-full bg-emerald-950 border border-emerald-800 text-emerald-400 flex items-center justify-center shrink-0 z-10 text-xs font-bold">
                  4
                </div>
                <div className="bg-slate-900/60 border border-slate-800 rounded-xl p-3 flex-1 text-xs space-y-1">
                  <span className="font-bold text-white">Economic Allocation Ranked</span>
                  <p className="text-slate-400">
                    Evaluated 6 candidate actions by Net Incremental Contribution. Selected <strong className="text-emerald-400">{caseData.recommended_action || 'NO_ACTION'}</strong> with expected contribution of ₹{caseData.expected_incremental_contribution?.toFixed(2)}.
                  </p>
                </div>
              </div>

              {/* Step 6: Policy Checks */}
              <div className="relative flex items-start gap-4 pl-1">
                <div className="w-7 h-7 rounded-full bg-amber-950 border border-amber-800 text-amber-400 flex items-center justify-center shrink-0 z-10 text-xs font-bold">
                  5
                </div>
                <div className="bg-slate-900/60 border border-slate-800 rounded-xl p-3 flex-1 text-xs space-y-2">
                  <div className="flex items-center justify-between">
                    <span className="font-bold text-white">Deterministic Policy Guardrails</span>
                    <Badge variant={caseData.policy_status === 'APPROVED' ? 'emerald' : 'rose'} size="sm">
                      {caseData.policy_status || 'APPROVED'}
                    </Badge>
                  </div>
                  <div className="space-y-1 text-[11px]">
                    {policies.map((p, idx) => (
                      <div key={idx} className="flex items-center justify-between text-slate-400">
                        <span>{p.rule_name}</span>
                        <span className={p.passed ? 'text-emerald-400 font-semibold' : 'text-rose-400 font-semibold'}>
                          {p.passed ? '✓ Passed' : `✗ ${p.veto_reason}`}
                        </span>
                      </div>
                    ))}
                  </div>
                </div>
              </div>

              {/* Step 7: Final Decision */}
              <div className="relative flex items-start gap-4 pl-1">
                <div className="w-7 h-7 rounded-full bg-cyan-950 border border-cyan-800 text-cyan-400 flex items-center justify-center shrink-0 z-10 text-xs font-bold">
                  6
                </div>
                <div className="bg-slate-900/60 border border-slate-800 rounded-xl p-3 flex-1 text-xs space-y-1">
                  <div className="flex items-center justify-between">
                    <span className="font-bold text-white">Final Structured Decision</span>
                    <Badge variant="emerald" size="sm">{caseData.final_decision}</Badge>
                  </div>
                  <p className="text-slate-400">
                    Action: <strong className="text-white">{caseData.recommended_action}</strong> | Timing: <span className="font-mono text-indigo-400">{latestDecision?.recommended_timing || 'IMMEDIATE'}</span>.
                  </p>
                </div>
              </div>

              {/* Step 8: Execution & Outcome */}
              <div className="relative flex items-start gap-4 pl-1">
                <div className="w-7 h-7 rounded-full bg-slate-800 border border-slate-700 text-slate-300 flex items-center justify-center shrink-0 z-10 text-xs font-bold">
                  7
                </div>
                <div className="bg-slate-900/60 border border-slate-800 rounded-xl p-3 flex-1 text-xs space-y-1">
                  <div className="flex items-center justify-between">
                    <span className="font-bold text-white">Execution & Outcome</span>
                    <span className="text-[10px] text-slate-400">Status: {caseData.status}</span>
                  </div>
                  {executions.length > 0 ? (
                    <div className="text-slate-300 text-[11px] font-mono">
                      Executed {executions[0].action_type} via {executions[0].gateway} (Cost: ₹{executions[0].cost_incurred})
                    </div>
                  ) : (
                    <p className="text-slate-500 italic">No execution dispatched yet.</p>
                  )}
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Right Column: Candidate Action Comparison Matrix */}
        <div className="lg:col-span-6 space-y-4">
          <div className="glass-panel rounded-2xl p-5 space-y-4">
            <div className="flex items-center justify-between border-b border-slate-800 pb-3">
              <div>
                <h3 className="text-sm font-bold text-white">Candidate Actions Economic Matrix</h3>
                <p className="text-xs text-slate-400">Why the engine chose {caseData.recommended_action} over other candidate actions</p>
              </div>
              <Badge variant="emerald" size="sm">Ranked</Badge>
            </div>

            <div className="space-y-3">
              {candidates.map((cand, idx) => {
                const isWinner = cand.is_selected;
                return (
                  <div
                    key={idx}
                    className={`rounded-xl p-4 border transition-all ${
                      isWinner
                        ? 'bg-emerald-950/30 border-emerald-500/60 shadow-[0_0_20px_rgba(16,185,129,0.15)]'
                        : !cand.policy_allowed
                        ? 'bg-rose-950/20 border-rose-900/40 opacity-70'
                        : 'bg-slate-900/60 border-slate-800 hover:border-slate-700'
                    }`}
                  >
                    <div className="flex items-center justify-between mb-2">
                      <div className="flex items-center gap-2">
                        <span className="font-bold text-white text-xs">{cand.action_type}</span>
                        {isWinner && <Badge variant="emerald" size="sm">Selected Best Action</Badge>}
                        {!cand.policy_allowed && <Badge variant="rose" size="sm">Blocked by Policy</Badge>}
                      </div>
                      <span className="font-mono font-bold text-xs text-emerald-400">
                        Net: ₹{cand.expected_incremental_contribution.toFixed(2)}
                      </span>
                    </div>

                    <div className="grid grid-cols-4 gap-2 text-[11px] pt-2 border-t border-slate-800/60 text-slate-400">
                      <div>
                        <span className="block text-[10px] text-slate-500">Recovery Prob</span>
                        <span className="font-semibold text-slate-200">{Math.round(cand.action_recovery_prob * 100)}%</span>
                      </div>
                      <div>
                        <span className="block text-[10px] text-slate-500">Incremental Lift</span>
                        <span className="font-semibold text-indigo-400">+{Math.round(cand.incremental_lift * 100)}%</span>
                      </div>
                      <div>
                        <span className="block text-[10px] text-slate-500">Gross Rev</span>
                        <span className="font-semibold text-slate-200">₹{cand.expected_incremental_revenue.toFixed(2)}</span>
                      </div>
                      <div>
                        <span className="block text-[10px] text-slate-500">Total Cost</span>
                        <span className="font-semibold text-rose-400">-₹{cand.total_cost.toFixed(2)}</span>
                      </div>
                    </div>

                    {cand.policy_block_reason && (
                      <p className="text-[10px] text-rose-400 font-medium mt-2 pt-1 border-t border-rose-900/40">
                        Veto Reason: {cand.policy_block_reason}
                      </p>
                    )}
                  </div>
                );
              })}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
