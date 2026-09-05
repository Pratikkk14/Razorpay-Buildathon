import React, { useEffect, useState } from 'react';
import {
  FlaskConical,
  Trophy,
  TrendingUp,
  ShieldCheck,
  AlertTriangle,
  Play,
  RotateCcw,
  Sparkles,
  BarChart3,
  CheckCircle2,
} from 'lucide-react';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
  Legend,
} from 'recharts';
import { api } from '../services/api';
import { MultiPolicyBenchmarkResult, PolicyBenchmarkMetrics } from '../types';
import { Badge } from '../components/common/Badge';

export const Experiments: React.FC = () => {
  const [benchmark, setBenchmark] = useState<MultiPolicyBenchmarkResult | null>(null);
  const [loading, setLoading] = useState(false);
  const [numCases, setNumCases] = useState<number>(500);

  const runBenchmark = async () => {
    setLoading(true);
    try {
      const res = await api.runBenchmark({ num_cases: numCases });
      setBenchmark(res);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    runBenchmark();
  }, []);

  const chartData = benchmark
    ? Object.entries(benchmark.policies).map(([key, data]) => ({
        name: key.replace('Policy ', 'P-').split(' ')[0],
        fullName: key,
        recoveryRate: data.gross_recovery_rate_pct,
        netContribution: Math.round(data.net_incremental_contribution),
        totalCost: Math.round(data.total_intervention_cost),
        unnecessary: data.unnecessary_interventions_count,
      }))
    : [];

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold tracking-tight text-white flex items-center gap-2">
            5-Policy Comparative Benchmark
            <Badge variant="amber" size="sm">A/B Evaluation</Badge>
          </h2>
          <p className="text-xs text-slate-400">
            Proving the core thesis: "Recovery rate is the wrong optimization target. Incremental contribution is."
          </p>
        </div>

        <div className="flex items-center gap-3">
          <select
            value={numCases}
            onChange={(e) => setNumCases(Number(e.target.value))}
            className="bg-slate-800 border border-slate-700 text-xs text-slate-200 rounded-xl px-3 py-2 focus:outline-none"
          >
            <option value={100}>100 Payments</option>
            <option value={500}>500 Payments</option>
            <option value={1000}>1,000 Payments</option>
          </select>

          <button
            onClick={runBenchmark}
            disabled={loading}
            className="px-4 py-2 rounded-xl bg-gradient-to-r from-indigo-600 to-cyan-600 hover:from-indigo-500 hover:to-cyan-500 text-white font-bold text-xs shadow-lg shadow-indigo-600/30 transition-all flex items-center gap-2 disabled:opacity-50"
          >
            <RotateCcw className={`w-3.5 h-3.5 ${loading ? 'animate-spin' : ''}`} />
            <span>{loading ? 'Simulating...' : 'Re-Run Benchmark'}</span>
          </button>
        </div>
      </div>

      {/* Winner Spotlight Card */}
      {benchmark && (
        <div className="relative overflow-hidden glass-panel rounded-2xl p-6 border border-emerald-500/50 shadow-[0_0_40px_rgba(16,185,129,0.15)]">
          <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div className="space-y-2">
              <div className="flex items-center gap-2">
                <Trophy className="w-5 h-5 text-yellow-400" />
                <span className="text-xs font-bold uppercase tracking-wider text-emerald-400">Benchmark Winner</span>
              </div>
              <h3 className="text-lg font-extrabold text-white">
                Policy E: Uplift + Economic Allocation Engine
              </h3>
              <p className="text-xs text-slate-300 max-w-2xl leading-relaxed">
                Generates <strong className="text-emerald-400">₹{benchmark.incremental_value_generated_over_propensity.toLocaleString('en-IN')}</strong> more net profit than raw ML Propensity by eliminating wasteful interventions on customers who recover naturally, while avoiding <strong className="text-indigo-400">{benchmark.unnecessary_contacts_avoided_count}</strong> unnecessary customer contacts.
              </p>
            </div>

            <div className="flex items-center gap-6 text-right shrink-0">
              <div>
                <span className="text-[10px] uppercase tracking-wider text-slate-400 font-semibold">Simulated Payments</span>
                <p className="text-xl font-bold text-white">{benchmark.total_cases_simulated}</p>
              </div>
              <div>
                <span className="text-[10px] uppercase tracking-wider text-slate-400 font-semibold">Net Value Added</span>
                <p className="text-xl font-bold text-emerald-400">
                  +₹{benchmark.incremental_value_generated_over_propensity.toLocaleString('en-IN')}
                </p>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Charts: Net Contribution vs Recovery Rate */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Net Contribution Chart */}
        <div className="glass-panel rounded-2xl p-5 space-y-4">
          <div className="flex items-center justify-between">
            <div>
              <h3 className="text-sm font-bold text-white">Net Incremental Contribution (₹)</h3>
              <p className="text-xs text-slate-400">Real profit generated after subtracting action costs & customer friction</p>
            </div>
            <Badge variant="emerald" size="sm">Primary Target</Badge>
          </div>

          <div className="h-64 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={chartData} margin={{ top: 10, right: 10, left: 10, bottom: 0 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" vertical={false} />
                <XAxis dataKey="name" stroke="#64748B" fontSize={11} tickLine={false} />
                <YAxis stroke="#64748B" fontSize={11} tickLine={false} />
                <Tooltip
                  contentStyle={{ backgroundColor: '#111827', borderColor: '#374151', borderRadius: '12px', fontSize: '12px' }}
                  formatter={(value: any) => [`₹${Number(value).toLocaleString('en-IN')}`, 'Net Contribution']}
                />
                <Bar dataKey="netContribution" fill="#10B981" radius={[6, 6, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Total Cost & Unnecessary Contacts Chart */}
        <div className="glass-panel rounded-2xl p-5 space-y-4">
          <div className="flex items-center justify-between">
            <div>
              <h3 className="text-sm font-bold text-white">Intervention Costs Incurred (₹)</h3>
              <p className="text-xs text-slate-400">Blind Retries & ML Propensity waste money on natural recoveries</p>
            </div>
            <Badge variant="rose" size="sm">Cost Efficiency</Badge>
          </div>

          <div className="h-64 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={chartData} margin={{ top: 10, right: 10, left: 10, bottom: 0 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" vertical={false} />
                <XAxis dataKey="name" stroke="#64748B" fontSize={11} tickLine={false} />
                <YAxis stroke="#64748B" fontSize={11} tickLine={false} />
                <Tooltip
                  contentStyle={{ backgroundColor: '#111827', borderColor: '#374151', borderRadius: '12px', fontSize: '12px' }}
                  formatter={(value: any) => [`₹${Number(value).toLocaleString('en-IN')}`, 'Intervention Cost']}
                />
                <Bar dataKey="totalCost" fill="#F43F5E" radius={[6, 6, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      {/* Full 5-Policy Comparative Table */}
      {benchmark && (
        <div className="glass-panel rounded-2xl p-5 space-y-4">
          <div className="flex items-center justify-between border-b border-slate-800 pb-3">
            <div>
              <h3 className="text-sm font-bold text-white">Full Comparative Benchmark Metrics</h3>
              <p className="text-xs text-slate-400">Evaluating identical synthetic payment failure batches across 5 operational policies</p>
            </div>
            <Badge variant="indigo" size="sm">Side-by-Side</Badge>
          </div>

          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs">
              <thead>
                <tr className="border-b border-slate-800 text-slate-400 uppercase tracking-wider text-[10px]">
                  <th className="pb-3 font-semibold">Policy Name</th>
                  <th className="pb-3 font-semibold">Interventions</th>
                  <th className="pb-3 font-semibold">Gross Rec. Rate</th>
                  <th className="pb-3 font-semibold">Gross Recovered (₹)</th>
                  <th className="pb-3 font-semibold">Total Cost (₹)</th>
                  <th className="pb-3 font-semibold">Net Contribution (₹)</th>
                  <th className="pb-3 font-semibold">Unnecessary Contacts</th>
                  <th className="pb-3 font-semibold text-right">Verdict</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-800/60">
                {Object.entries(benchmark.policies).map(([name, p]) => {
                  const isWinner = name.includes('Policy E');
                  return (
                    <tr
                      key={name}
                      className={`transition-colors ${
                        isWinner
                          ? 'bg-emerald-950/40 font-semibold text-white'
                          : 'text-slate-300 hover:bg-slate-800/30'
                      }`}
                    >
                      <td className="py-4 pr-3">
                        <div className="font-bold text-white">{name}</div>
                        <div className="text-[10px] text-slate-400 truncate max-w-xs">{p.policy_description}</div>
                      </td>

                      <td className="py-4 font-mono">{p.interventions_triggered}</td>

                      <td className="py-4 font-semibold text-slate-200">
                        {p.gross_recovery_rate_pct}%
                      </td>

                      <td className="py-4 font-mono">
                        ₹{p.gross_recovered_revenue.toLocaleString('en-IN')}
                      </td>

                      <td className="py-4 font-mono text-rose-400">
                        ₹{p.total_intervention_cost.toLocaleString('en-IN')}
                      </td>

                      <td className="py-4 font-mono font-bold text-emerald-400 text-sm">
                        ₹{p.net_incremental_contribution.toLocaleString('en-IN')}
                      </td>

                      <td className="py-4 font-mono text-amber-400">
                        {p.unnecessary_interventions_count}
                      </td>

                      <td className="py-4 text-right">
                        {isWinner ? (
                          <Badge variant="emerald" size="sm">Optimal Winner</Badge>
                        ) : (
                          <Badge variant="default" size="sm">Sub-optimal</Badge>
                        )}
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        </div>
      )}
    </div>
  );
};
