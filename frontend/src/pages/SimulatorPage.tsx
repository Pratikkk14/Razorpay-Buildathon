import React, { useEffect, useState } from 'react';
import {
  Cpu,
  Play,
  RotateCcw,
  Sliders,
  Sparkles,
  Layers,
  TrendingUp,
  CheckCircle2,
  AlertCircle,
} from 'lucide-react';
import { api } from '../services/api';
import { ScenarioDefinition, MultiPolicyBenchmarkResult } from '../types';
import { Badge } from '../components/common/Badge';

interface SimulatorPageProps {
  onSelectCase: (caseId: string) => void;
  onRefreshList: () => void;
}

export const SimulatorPage: React.FC<SimulatorPageProps> = ({
  onSelectCase,
  onRefreshList,
}) => {
  const [scenarios, setScenarios] = useState<ScenarioDefinition[]>([]);
  const [loadingScenarios, setLoadingScenarios] = useState(false);
  const [runningScenario, setRunningScenario] = useState<string | null>(null);

  // Config sliders
  const [numCases, setNumCases] = useState<number>(200);
  const [naturalMultiplier, setNaturalMultiplier] = useState<number>(1.0);
  const [linkEffectiveness, setLinkEffectiveness] = useState<number>(1.0);
  const [retryEffectiveness, setRetryEffectiveness] = useState<number>(1.0);
  const [fatiguePenalty, setFatiguePenalty] = useState<number>(0.15);

  const [simResult, setSimResult] = useState<MultiPolicyBenchmarkResult | null>(null);
  const [isSimulating, setIsSimulating] = useState(false);
  const [batchGenerating, setBatchGenerating] = useState(false);
  const [batchMsg, setBatchMsg] = useState<string | null>(null);

  useEffect(() => {
    loadScenarios();
  }, []);

  const loadScenarios = async () => {
    setLoadingScenarios(true);
    try {
      const res = await api.getScenarios();
      setScenarios(res);
    } catch (err) {
      console.error(err);
    } finally {
      setLoadingScenarios(false);
    }
  };

  const handleRunScenario = async (scenarioId: string) => {
    setRunningScenario(scenarioId);
    try {
      const res = await api.loadScenario(scenarioId);
      onRefreshList();
      onSelectCase(res.case_id);
    } catch (err) {
      console.error(err);
    } finally {
      setRunningScenario(null);
    }
  };

  const handleRunSimulation = async () => {
    setIsSimulating(true);
    try {
      const res = await api.runBenchmark({
        num_cases: numCases,
        natural_recovery_multiplier: naturalMultiplier,
        payment_link_effectiveness: linkEffectiveness,
        retry_effectiveness: retryEffectiveness,
        customer_fatigue_penalty: fatiguePenalty,
      });
      setSimResult(res);
    } catch (err) {
      console.error(err);
    } finally {
      setIsSimulating(false);
    }
  };

  const handleGenerateBatch = async () => {
    setBatchGenerating(true);
    setBatchMsg(null);
    try {
      const res = await api.generateBatch(numCases > 50 ? 50 : numCases);
      setBatchMsg(res.message);
      onRefreshList();
    } catch (err) {
      console.error(err);
    } finally {
      setBatchGenerating(false);
    }
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold tracking-tight text-white flex items-center gap-2">
            Recovery Simulator & Monte Carlo Engine
            <Badge variant="indigo" size="sm">Sandbox</Badge>
          </h2>
          <p className="text-xs text-slate-400">
            Generate synthetic failure distributions, tweak channel effectiveness, and observe real-time allocation decisions.
          </p>
        </div>
      </div>

      {/* Grid: Environment Config on Left, Canonical Scenarios on Right */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Left: Environment Sliders & Runner */}
        <div className="lg:col-span-6 glass-panel rounded-2xl p-5 space-y-5">
          <div className="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 className="text-sm font-bold text-white flex items-center gap-2">
              <Sliders className="w-4 h-4 text-indigo-400" />
              <span>Environment Configuration</span>
            </h3>
            <Badge variant="indigo" size="sm">Domain Randomization</Badge>
          </div>

          <div className="space-y-4">
            <div className="space-y-1.5">
              <div className="flex items-center justify-between text-xs">
                <span className="text-slate-300 font-semibold">Number of Synthetic Payments</span>
                <span className="font-mono font-bold text-white">{numCases} Cases</span>
              </div>
              <input
                type="range"
                min={50}
                max={1000}
                step={50}
                value={numCases}
                onChange={(e) => setNumCases(Number(e.target.value))}
                className="w-full accent-indigo-500 bg-slate-800 rounded-lg cursor-pointer"
              />
            </div>

            <div className="space-y-1.5">
              <div className="flex items-center justify-between text-xs">
                <span className="text-slate-300 font-semibold">Natural Recovery Multiplier</span>
                <span className="font-mono font-bold text-cyan-400">{naturalMultiplier}x</span>
              </div>
              <input
                type="range"
                min={0.2}
                max={2.5}
                step={0.1}
                value={naturalMultiplier}
                onChange={(e) => setNaturalMultiplier(Number(e.target.value))}
                className="w-full accent-cyan-500 bg-slate-800 rounded-lg cursor-pointer"
              />
            </div>

            <div className="space-y-1.5">
              <div className="flex items-center justify-between text-xs">
                <span className="text-slate-300 font-semibold">Payment Link Effectiveness</span>
                <span className="font-mono font-bold text-emerald-400">{linkEffectiveness}x</span>
              </div>
              <input
                type="range"
                min={0.2}
                max={2.5}
                step={0.1}
                value={linkEffectiveness}
                onChange={(e) => setLinkEffectiveness(Number(e.target.value))}
                className="w-full accent-emerald-500 bg-slate-800 rounded-lg cursor-pointer"
              />
            </div>

            <div className="space-y-1.5">
              <div className="flex items-center justify-between text-xs">
                <span className="text-slate-300 font-semibold">Retry Channel Effectiveness</span>
                <span className="font-mono font-bold text-amber-400">{retryEffectiveness}x</span>
              </div>
              <input
                type="range"
                min={0.2}
                max={2.5}
                step={0.1}
                value={retryEffectiveness}
                onChange={(e) => setRetryEffectiveness(Number(e.target.value))}
                className="w-full accent-amber-500 bg-slate-800 rounded-lg cursor-pointer"
              />
            </div>

            <div className="space-y-1.5">
              <div className="flex items-center justify-between text-xs">
                <span className="text-slate-300 font-semibold">Customer Fatigue Penalty</span>
                <span className="font-mono font-bold text-rose-400">-{Math.round(fatiguePenalty * 100)}%</span>
              </div>
              <input
                type="range"
                min={0.0}
                max={0.5}
                step={0.05}
                value={fatiguePenalty}
                onChange={(e) => setFatiguePenalty(Number(e.target.value))}
                className="w-full accent-rose-500 bg-slate-800 rounded-lg cursor-pointer"
              />
            </div>
          </div>

          <div className="pt-4 border-t border-slate-800 flex items-center gap-3">
            <button
              onClick={handleRunSimulation}
              disabled={isSimulating}
              className="flex-1 py-2.5 rounded-xl bg-gradient-to-r from-indigo-600 to-cyan-600 hover:from-indigo-500 hover:to-cyan-500 text-white font-bold text-xs shadow-lg shadow-indigo-600/30 transition-all flex items-center justify-center gap-2 disabled:opacity-50"
            >
              <Cpu className={`w-4 h-4 ${isSimulating ? 'animate-spin' : ''}`} />
              <span>{isSimulating ? 'Simulating...' : 'Run Monte Carlo Simulation'}</span>
            </button>

            <button
              onClick={handleGenerateBatch}
              disabled={batchGenerating}
              className="py-2.5 px-4 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-200 font-semibold text-xs transition-all disabled:opacity-50"
            >
              {batchGenerating ? 'Ingesting...' : 'Ingest to Database'}
            </button>
          </div>

          {batchMsg && (
            <p className="text-xs text-emerald-400 font-medium bg-emerald-950/40 border border-emerald-800 p-2.5 rounded-xl">
              ✓ {batchMsg}
            </p>
          )}
        </div>

        {/* Right: Canonical Scenarios Catalog */}
        <div className="lg:col-span-6 glass-panel rounded-2xl p-5 space-y-4">
          <div className="flex items-center justify-between border-b border-slate-800 pb-3">
            <div>
              <h3 className="text-sm font-bold text-white">Canonical Test Scenarios</h3>
              <p className="text-xs text-slate-400">Pre-configured edge cases designed to test safety rules and allocation</p>
            </div>
            <Badge variant="emerald" size="sm">{scenarios.length} Scenarios</Badge>
          </div>

          <div className="space-y-3 max-h-[460px] overflow-y-auto pr-1">
            {scenarios.map((scen) => {
              const sId = scen.scenario_id || scen.id || '';
              const isRunning = runningScenario === sId;

              return (
                <div
                  key={sId}
                  className="bg-slate-900/60 border border-slate-800 hover:border-slate-700 rounded-xl p-3.5 space-y-2 transition-colors group"
                >
                  <div className="flex items-center justify-between">
                    <span className="font-bold text-white text-xs group-hover:text-indigo-400 transition-colors">
                      {scen.title}
                    </span>
                    <Badge
                      variant={
                        scen.expected_decision === 'ACT'
                          ? 'emerald'
                          : scen.expected_decision === 'WAIT'
                          ? 'amber'
                          : scen.expected_decision === 'ESCALATE'
                          ? 'indigo'
                          : 'slate'
                      }
                      size="sm"
                    >
                      Target: {scen.expected_decision}
                    </Badge>
                  </div>

                  <p className="text-[11px] text-slate-400 leading-relaxed">
                    {scen.description}
                  </p>

                  <div className="flex items-center justify-between pt-2 border-t border-slate-800/60 text-[10px] text-slate-400">
                    <div>
                      <span>Amount: <strong className="text-slate-200">₹{scen.amount.toLocaleString('en-IN')}</strong></span>
                      <span className="mx-2">•</span>
                      <span>Natural: <strong className="text-cyan-400">{Math.round(scen.natural_recovery_rate * 100)}%</strong></span>
                    </div>

                    <button
                      onClick={() => handleRunScenario(sId)}
                      disabled={isRunning}
                      className="px-3 py-1 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-[11px] transition-all flex items-center gap-1 shadow-sm disabled:opacity-50"
                    >
                      <Play className="w-3 h-3 fill-current" />
                      <span>{isRunning ? 'Running...' : 'Execute & Audit'}</span>
                    </button>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    </div>
  );
};
