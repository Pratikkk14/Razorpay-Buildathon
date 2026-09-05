import React, { useEffect, useState } from 'react';
import {
  Sparkles,
  Play,
  CheckCircle2,
  AlertTriangle,
  ShieldAlert,
  TrendingUp,
  RotateCcw,
  ArrowRight,
  ExternalLink,
  Zap,
} from 'lucide-react';
import { api } from '../services/api';
import { ScenarioDefinition, DecisionRecord } from '../types';
import { Badge } from '../components/common/Badge';

interface DemoShowcaseProps {
  onSelectCase: (caseId: string) => void;
  onRefreshList: () => void;
}

export const DemoShowcase: React.FC<DemoShowcaseProps> = ({
  onSelectCase,
  onRefreshList,
}) => {
  const [scenarios, setScenarios] = useState<ScenarioDefinition[]>([]);
  const [currentStep, setCurrentStep] = useState<number>(0);
  const [executing, setExecuting] = useState(false);
  const [demoResults, setDemoResults] = useState<Record<string, { case_id: string; decision: DecisionRecord }>>({});

  useEffect(() => {
    loadDemoScenarios();
  }, []);

  const loadDemoScenarios = async () => {
    try {
      const list = await api.getDemoScenarios();
      setScenarios(list);
    } catch (err) {
      console.error(err);
    }
  };

  const currentScenario = scenarios[currentStep];

  const handleRunCurrentStep = async () => {
    if (!currentScenario) return;
    const sId = currentScenario.scenario_id || currentScenario.id || '';
    setExecuting(true);
    try {
      const res = await api.executeDemoScenario(sId);
      setDemoResults((prev) => ({
        ...prev,
        [sId]: { case_id: res.case_id, decision: res.decision },
      }));
      onRefreshList();
    } catch (err) {
      console.error(err);
    } finally {
      setExecuting(false);
    }
  };

  const currentResult = currentScenario
    ? demoResults[currentScenario.scenario_id || currentScenario.id || '']
    : null;

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="relative overflow-hidden rounded-2xl bg-gradient-to-r from-indigo-950 via-slate-900 to-cyan-950 border border-indigo-700/50 p-6 shadow-[0_10px_40px_-15px_rgba(99,102,241,0.3)]">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div className="space-y-2 max-w-2xl">
            <div className="flex items-center gap-2">
              <Badge variant="emerald" size="sm">
                <Sparkles className="w-3.5 h-3.5 text-yellow-300" />
                Buildathon 2026 Judge Walkthrough
              </Badge>
              <span className="text-xs text-slate-400 font-mono">5-Minute Interactive Demo</span>
            </div>
            <h2 className="text-xl font-extrabold tracking-tight text-white">
              Core Thesis Demonstration Experience
            </h2>
            <p className="text-xs text-slate-300 leading-relaxed">
              Step through the 5 canonical scenarios demonstrating why <strong className="text-emerald-400">Incremental Contribution</strong> outperforms raw recovery rates, how multi-action economics rank interventions, and how deterministic guardrails veto AI recommendations.
            </p>
          </div>

          <div className="flex items-center gap-2">
            <button
              onClick={async () => {
                setExecuting(true);
                try {
                  await api.seedAllDemoScenarios();
                  await loadDemoScenarios();
                  onRefreshList();
                } finally {
                  setExecuting(false);
                }
              }}
              disabled={executing}
              className="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-semibold transition-all"
            >
              Seed All 5 Scenarios
            </button>
          </div>
        </div>
      </div>

      {/* 5-Step Stepper Navigation */}
      <div className="grid grid-cols-1 sm:grid-cols-5 gap-3">
        {scenarios.map((scen, idx) => {
          const isActive = currentStep === idx;
          const sId = scen.scenario_id || scen.id || '';
          const isDone = Boolean(demoResults[sId]);

          return (
            <button
              key={sId || idx}
              onClick={() => setCurrentStep(idx)}
              className={`p-3.5 rounded-2xl border text-left transition-all ${
                isActive
                  ? 'bg-gradient-to-b from-indigo-950/90 to-slate-900 border-indigo-500 shadow-[0_0_20px_rgba(99,102,241,0.25)]'
                  : 'glass-panel border-slate-800 hover:border-slate-700'
              }`}
            >
              <div className="flex items-center justify-between mb-1.5">
                <span className={`text-[10px] font-bold uppercase tracking-wider ${isActive ? 'text-indigo-400' : 'text-slate-500'}`}>
                  Step {idx + 1}
                </span>
                {isDone ? (
                  <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />
                ) : (
                  <span className="w-2 h-2 rounded-full bg-slate-700" />
                )}
              </div>
              <div className="text-xs font-bold text-white line-clamp-1">
                {scen.title.split(':')[1]?.trim() || scen.title}
              </div>
            </button>
          );
        })}
      </div>

      {/* Active Scenario Spotlight Box */}
      {currentScenario && (
        <div className="glass-panel rounded-2xl p-6 border border-slate-800 space-y-6">
          <div className="flex flex-col md:flex-row md:items-start justify-between gap-4 pb-4 border-b border-slate-800">
            <div className="space-y-2 max-w-2xl">
              <div className="flex items-center gap-2">
                <Badge variant="indigo" size="sm">Step {currentStep + 1} of 5</Badge>
                <Badge
                  variant={
                    currentScenario.expected_decision === 'ACT'
                      ? 'emerald'
                      : currentScenario.expected_decision === 'WAIT'
                      ? 'amber'
                      : currentScenario.expected_decision === 'ESCALATE'
                      ? 'indigo'
                      : 'slate'
                  }
                  size="sm"
                >
                  Expected: {currentScenario.expected_decision}
                </Badge>
              </div>
              <h3 className="text-lg font-bold text-white">{currentScenario.title}</h3>
              <p className="text-xs text-slate-300 leading-relaxed">
                {currentScenario.description}
              </p>
            </div>

            <div className="flex flex-col items-end gap-2 shrink-0">
              <button
                onClick={handleRunCurrentStep}
                disabled={executing}
                className="px-5 py-2.5 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-bold text-xs shadow-lg shadow-emerald-600/30 transition-all flex items-center gap-2 disabled:opacity-50"
              >
                <Play className={`w-4 h-4 fill-current ${executing ? 'animate-spin' : ''}`} />
                <span>{executing ? 'Executing Inference...' : 'Execute Scenario Live'}</span>
              </button>

              {currentResult && (
                <button
                  onClick={() => onSelectCase(currentResult.case_id)}
                  className="text-xs font-semibold text-indigo-400 hover:text-indigo-300 flex items-center gap-1 transition-colors pt-1"
                >
                  <span>Open Full Audit Timeline</span>
                  <ExternalLink className="w-3 h-3" />
                </button>
              )}
            </div>
          </div>

          {/* Scenario Details & Live Result Box */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Left: Input Parameters */}
            <div className="bg-slate-900/70 border border-slate-800 rounded-xl p-4 space-y-3">
              <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wider">Payment & Failure Attributes</h4>
              <div className="grid grid-cols-2 gap-3 text-xs">
                <div>
                  <span className="text-slate-500 text-[10px] block">Customer</span>
                  <span className="font-semibold text-white">{currentScenario.customer_name}</span>
                </div>
                <div>
                  <span className="text-slate-500 text-[10px] block">Payment Amount</span>
                  <span className="font-semibold text-white">₹{currentScenario.amount.toLocaleString('en-IN')}</span>
                </div>
                <div>
                  <span className="text-slate-500 text-[10px] block">Natural Recovery Rate</span>
                  <span className="font-semibold text-cyan-400">{Math.round(currentScenario.natural_recovery_rate * 100)}%</span>
                </div>
                <div>
                  <span className="text-slate-500 text-[10px] block">Target Rationale</span>
                  <span className="font-semibold text-slate-300 text-[11px]">{currentScenario.expected_rationale}</span>
                </div>
              </div>
            </div>

            {/* Right: Live Engine Result */}
            <div className="bg-slate-900/70 border border-slate-800 rounded-xl p-4 space-y-3">
              <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wider flex items-center justify-between">
                <span>Engine Evaluation Output</span>
                {currentResult && <Badge variant="emerald" size="sm">✓ Verified</Badge>}
              </h4>

              {currentResult ? (
                <div className="space-y-3">
                  <div className="flex items-center justify-between">
                    <div>
                      <span className="text-[10px] text-slate-500 block">Decision Verdict</span>
                      <Badge
                        variant={
                          currentResult.decision.decision === 'ACT'
                            ? 'emerald'
                            : currentResult.decision.decision === 'WAIT'
                            ? 'amber'
                            : currentResult.decision.decision === 'ESCALATE'
                            ? 'indigo'
                            : 'slate'
                        }
                        size="md"
                      >
                        {currentResult.decision.decision}
                      </Badge>
                    </div>

                    <div className="text-right">
                      <span className="text-[10px] text-slate-500 block">Recommended Action</span>
                      <span className="font-bold text-xs text-white">
                        {currentResult.decision.recommended_action || 'NO_ACTION'}
                      </span>
                    </div>

                    <div className="text-right">
                      <span className="text-[10px] text-slate-500 block">Net Contribution</span>
                      <span className="font-bold text-xs text-emerald-400">
                        ₹{currentResult.decision.expected_incremental_contribution?.toFixed(2) || '0.00'}
                      </span>
                    </div>
                  </div>

                  <p className="text-xs text-slate-200 bg-slate-950/60 p-2.5 rounded-lg border border-slate-800 leading-relaxed">
                    <strong className="text-indigo-400">Reason: </strong>
                    {currentResult.decision.reason}
                  </p>
                </div>
              ) : (
                <div className="py-6 text-center text-slate-500 text-xs">
                  Click <strong>"Execute Scenario Live"</strong> above to observe the decision engine formulation.
                </div>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
