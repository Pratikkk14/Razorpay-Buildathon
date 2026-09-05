import React from 'react';
import {
  TrendingUp,
  AlertTriangle,
  ShieldCheck,
  CheckCircle2,
  DollarSign,
  Layers,
  ArrowUpRight,
  Sparkles,
  Zap,
} from 'lucide-react';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  AreaChart,
  Area,
  CartesianGrid,
} from 'recharts';
import { AnalyticsOverview, Case } from '../types';
import { MetricCard } from '../components/common/MetricCard';
import { Badge } from '../components/common/Badge';

interface CommandCenterProps {
  analytics: AnalyticsOverview | null;
  cases: Case[];
  onSelectCase: (caseId: string) => void;
  onNavigateTab: (tab: any) => void;
}

export const CommandCenter: React.FC<CommandCenterProps> = ({
  analytics,
  cases,
  onSelectCase,
  onNavigateTab,
}) => {
  const kpis = analytics?.kpis || {
    revenue_at_risk: 0,
    expected_recoverable_revenue: 0,
    total_incremental_contribution: 0,
    gross_recovery_rate_pct: 0,
    average_incremental_lift_pct: 0,
    total_intervention_cost: 0,
    active_recovery_cases: 0,
    cases_suppressed_by_safety: 0,
    recovered_cases_count: 0,
    total_cases_analyzed: 0,
  };

  const actionData = analytics?.actions_breakdown || [];
  const liftData = analytics?.lift_distribution || [];

  return (
    <div className="space-y-6">
      {/* Top Banner: Core Thesis & Executive Summary */}
      <div className="relative overflow-hidden rounded-2xl bg-gradient-to-r from-indigo-950/90 via-slate-900 to-slate-900 border border-indigo-800/40 p-6 shadow-[0_10px_40px_-15px_rgba(99,102,241,0.2)]">
        <div className="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div className="space-y-2 max-w-2xl">
            <div className="flex items-center gap-2">
              <Badge variant="emerald" size="sm">
                <Sparkles className="w-3 h-3 text-emerald-400" />
                Active Optimization Target: Incremental Contribution
              </Badge>
              <span className="text-xs text-slate-400 font-mono">v1.0-buildathon</span>
            </div>
            <h2 className="text-xl font-extrabold tracking-tight text-white">
              Recovery Intelligence & Allocation Engine
            </h2>
            <p className="text-xs text-slate-300 leading-relaxed">
              Evaluating each payment failure against natural baseline recovery to eliminate wasteful interventions,
              protect customer goodwill, and maximize <strong className="text-emerald-400">Net Incremental Contribution</strong> under strict deterministic safety guardrails.
            </p>
          </div>

          <div className="flex items-center gap-3 shrink-0">
            <button
              onClick={() => onNavigateTab('demo')}
              className="px-4 py-2 rounded-xl bg-gradient-to-r from-indigo-600 to-cyan-600 hover:from-indigo-500 hover:to-cyan-500 text-white font-semibold text-xs shadow-lg shadow-indigo-600/30 transition-all flex items-center gap-2"
            >
              <Zap className="w-3.5 h-3.5 text-yellow-300" />
              <span>Launch 5-Step Demo</span>
            </button>
            <button
              onClick={() => onNavigateTab('experiments')}
              className="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-200 font-semibold text-xs transition-all"
            >
              5-Policy Benchmark
            </button>
          </div>
        </div>
      </div>

      {/* 8 Primary Executive KPIs */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <MetricCard
          title="Revenue at Risk"
          value={`₹${kpis.revenue_at_risk.toLocaleString('en-IN')}`}
          subtitle={`${kpis.total_cases_analyzed} failed payments analyzed`}
          icon={AlertTriangle}
          variant="amber"
          tooltip="Total sum of failed transaction amounts requiring evaluation"
        />

        <MetricCard
          title="Net Incremental Contribution"
          value={`₹${kpis.total_incremental_contribution.toLocaleString('en-IN')}`}
          trend={{
            value: `+${kpis.average_incremental_lift_pct}%`,
            isPositive: true,
            label: 'avg uplift',
          }}
          icon={TrendingUp}
          variant="emerald"
          tooltip="Incremental recovered revenue minus action costs and customer friction"
        />

        <MetricCard
          title="Gross Recovery Rate"
          value={`${kpis.gross_recovery_rate_pct}%`}
          subtitle={`${kpis.recovered_cases_count} payments recovered`}
          icon={CheckCircle2}
          variant="indigo"
          tooltip="Total realized recovery proportion across natural and assisted channels"
        />

        <MetricCard
          title="Safety Guardrail Vetoes"
          value={kpis.cases_suppressed_by_safety}
          subtitle="Customer fatigue & retries saved"
          icon={ShieldCheck}
          variant="rose"
          tooltip="Interventions safely suppressed by deterministic cooldown, DND, or retry limits"
        />
      </div>

      {/* Charts Row */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Action Performance & Net Contribution Chart */}
        <div className="glass-panel rounded-2xl p-5 space-y-4">
          <div className="flex items-center justify-between">
            <div>
              <h3 className="text-sm font-bold text-white">Net Contribution by Intervention Action</h3>
              <p className="text-xs text-slate-400">Total economic value generated after deducting delivery and friction costs</p>
            </div>
            <Badge variant="indigo" size="sm">Financial ROI</Badge>
          </div>

          <div className="h-64 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={actionData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" vertical={false} />
                <XAxis dataKey="action_type" stroke="#64748B" fontSize={11} tickLine={false} />
                <YAxis stroke="#64748B" fontSize={11} tickLine={false} />
                <Tooltip
                  contentStyle={{ backgroundColor: '#111827', borderColor: '#374151', borderRadius: '12px', fontSize: '12px' }}
                  formatter={(value: any) => [`₹${Number(value).toLocaleString('en-IN')}`, 'Net Contribution']}
                />
                <Bar dataKey="net_contribution" fill="#6366F1" radius={[6, 6, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Uplift Distribution Chart */}
        <div className="glass-panel rounded-2xl p-5 space-y-4">
          <div className="flex items-center justify-between">
            <div>
              <h3 className="text-sm font-bold text-white">Incremental Lift Distribution</h3>
              <p className="text-xs text-slate-400">Concentration of cases by incremental recovery uplift percentage</p>
            </div>
            <Badge variant="emerald" size="sm">Lift Buckets</Badge>
          </div>

          <div className="h-64 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={liftData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" vertical={false} />
                <XAxis dataKey="bucket_label" stroke="#64748B" fontSize={11} tickLine={false} />
                <YAxis stroke="#64748B" fontSize={11} tickLine={false} />
                <Tooltip
                  contentStyle={{ backgroundColor: '#111827', borderColor: '#374151', borderRadius: '12px', fontSize: '12px' }}
                  formatter={(value: any, name: any) => [value, name === 'case_count' ? 'Case Count' : 'Avg Contribution']}
                />
                <Bar dataKey="case_count" fill="#10B981" radius={[6, 6, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      {/* Recent Recovery Cases Live Table */}
      <div className="glass-panel rounded-2xl p-5 space-y-4">
        <div className="flex items-center justify-between">
          <div>
            <h3 className="text-sm font-bold text-white">Recent Recovery Intelligence Decisions</h3>
            <p className="text-xs text-slate-400">Real-time decisions generated by the Economic Allocation and Policy Engine</p>
          </div>
          <button
            onClick={() => onNavigateTab('recovery-queue')}
            className="text-xs font-semibold text-indigo-400 hover:text-indigo-300 flex items-center gap-1 transition-colors"
          >
            <span>View Full Queue ({cases.length})</span>
            <ArrowUpRight className="w-3.5 h-3.5" />
          </button>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead>
              <tr className="border-b border-slate-800 text-slate-400 uppercase tracking-wider text-[10px]">
                <th className="pb-3 font-semibold">Customer / Payment</th>
                <th className="pb-3 font-semibold">Amount</th>
                <th className="pb-3 font-semibold">Failure Diagnosis</th>
                <th className="pb-3 font-semibold">Natural Rec.</th>
                <th className="pb-3 font-semibold">Uplift</th>
                <th className="pb-3 font-semibold">Decision</th>
                <th className="pb-3 font-semibold">Expected Net Contribution</th>
                <th className="pb-3 font-semibold text-right">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60 text-slate-200">
              {cases.slice(0, 6).map((c) => {
                const natP = c.natural_recovery_prob ? `${Math.round(c.natural_recovery_prob * 100)}%` : '--';
                const lift = c.incremental_lift !== undefined && c.incremental_lift !== null ? `+${Math.round(c.incremental_lift * 100)}%` : '--';
                const contrib = c.expected_incremental_contribution !== undefined && c.expected_incremental_contribution !== null
                  ? `₹${c.expected_incremental_contribution.toLocaleString('en-IN')}`
                  : '--';

                return (
                  <tr key={c.id} className="hover:bg-slate-800/40 transition-colors group">
                    <td className="py-3.5 pr-3">
                      <div className="font-semibold text-white">{c.customer_name || c.customer_id}</div>
                      <div className="text-[10px] text-slate-400 font-mono">{c.payment_id}</div>
                    </td>

                    <td className="py-3.5 font-semibold text-white">
                      ₹{c.amount.toLocaleString('en-IN')}
                    </td>

                    <td className="py-3.5">
                      <span className="font-mono text-xs text-slate-300">{c.failure_code || 'FAILURE'}</span>
                    </td>

                    <td className="py-3.5 text-slate-300 font-medium">
                      {natP}
                    </td>

                    <td className="py-3.5">
                      <Badge variant={c.incremental_lift && c.incremental_lift > 0.20 ? 'emerald' : 'default'} size="sm">
                        {lift}
                      </Badge>
                    </td>

                    <td className="py-3.5">
                      <Badge
                        variant={
                          c.final_decision === 'ACT'
                            ? 'emerald'
                            : c.final_decision === 'WAIT'
                            ? 'amber'
                            : c.final_decision === 'ESCALATE'
                            ? 'indigo'
                            : 'slate'
                        }
                        size="sm"
                      >
                        {c.final_decision || c.status}
                      </Badge>
                    </td>

                    <td className="py-3.5 font-semibold text-emerald-400">
                      {contrib}
                    </td>

                    <td className="py-3.5 text-right">
                      <button
                        onClick={() => onSelectCase(c.id)}
                        className="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-indigo-600 text-slate-300 hover:text-white font-medium text-xs transition-colors"
                      >
                        Audit
                      </button>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
