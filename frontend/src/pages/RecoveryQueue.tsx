import React, { useState } from 'react';
import {
  Search,
  Filter,
  ArrowUpDown,
  ExternalLink,
  ShieldAlert,
  Play,
  Clock,
  Sparkles,
  ChevronRight,
} from 'lucide-react';
import { Case } from '../types';
import { Badge } from '../components/common/Badge';

interface RecoveryQueueProps {
  cases: Case[];
  onSelectCase: (caseId: string) => void;
  onEvaluateCase: (caseId: string) => void;
}

export const RecoveryQueue: React.FC<RecoveryQueueProps> = ({
  cases,
  onSelectCase,
  onEvaluateCase,
}) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedDecision, setSelectedDecision] = useState<string>('ALL');
  const [selectedStatus, setSelectedStatus] = useState<string>('ALL');

  const filteredCases = cases.filter((c) => {
    const matchesSearch =
      !searchTerm ||
      (c.customer_name && c.customer_name.toLowerCase().includes(searchTerm.toLowerCase())) ||
      c.payment_id.toLowerCase().includes(searchTerm.toLowerCase()) ||
      (c.failure_code && c.failure_code.toLowerCase().includes(searchTerm.toLowerCase()));

    const matchesDecision =
      selectedDecision === 'ALL' || c.final_decision === selectedDecision;

    const matchesStatus =
      selectedStatus === 'ALL' || c.status === selectedStatus;

    return matchesSearch && matchesDecision && matchesStatus;
  });

  return (
    <div className="space-y-6">
      {/* Header & Queue Controls */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold tracking-tight text-white flex items-center gap-2">
            Recovery Cases Queue
            <Badge variant="indigo" size="sm">
              {filteredCases.length} Cases
            </Badge>
          </h2>
          <p className="text-xs text-slate-400">
            Real-time pipeline of failed payments evaluated against natural recovery baselines and deterministic safety policies.
          </p>
        </div>
      </div>

      {/* Filter Toolbar */}
      <div className="glass-panel rounded-2xl p-4 flex flex-col md:flex-row items-center justify-between gap-4">
        <div className="relative w-full md:w-96">
          <Search className="absolute left-3.5 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
          <input
            type="text"
            placeholder="Search by customer, payment ID, or error code..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full bg-slate-900/90 border border-slate-700/80 rounded-xl pl-10 pr-4 py-2 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500 transition-colors"
          />
        </div>

        <div className="flex flex-wrap items-center gap-2.5 w-full md:w-auto">
          {/* Decision Filters */}
          <span className="text-[11px] font-semibold uppercase tracking-wider text-slate-400 mr-1">
            Decision:
          </span>
          {['ALL', 'ACT', 'WAIT', 'DONT_ACT', 'ESCALATE'].map((d) => (
            <button
              key={d}
              onClick={() => setSelectedDecision(d)}
              className={`px-3 py-1.5 rounded-xl text-xs font-semibold transition-all ${
                selectedDecision === d
                  ? 'bg-indigo-600 text-white shadow-[0_0_15px_rgba(99,102,241,0.35)]'
                  : 'bg-slate-800 text-slate-400 hover:text-slate-200 hover:bg-slate-700'
              }`}
            >
              {d}
            </button>
          ))}
        </div>
      </div>

      {/* Cases Table */}
      <div className="glass-panel rounded-2xl overflow-hidden border border-slate-800">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead>
              <tr className="border-b border-slate-800 bg-slate-900/60 text-slate-400 uppercase tracking-wider text-[10px]">
                <th className="py-3.5 px-4 font-semibold">Customer & Payment</th>
                <th className="py-3.5 px-4 font-semibold">Amount</th>
                <th className="py-3.5 px-4 font-semibold">Failure Diagnosis</th>
                <th className="py-3.5 px-4 font-semibold">Natural Rec.</th>
                <th className="py-3.5 px-4 font-semibold">Best Action</th>
                <th className="py-3.5 px-4 font-semibold">Incremental Lift</th>
                <th className="py-3.5 px-4 font-semibold">Expected Net Contribution</th>
                <th className="py-3.5 px-4 font-semibold">Decision / Policy</th>
                <th className="py-3.5 px-4 font-semibold text-right">Audit</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60 text-slate-200">
              {filteredCases.length === 0 ? (
                <tr>
                  <td colSpan={9} className="py-12 text-center text-slate-400">
                    No recovery cases matched your current filter criteria.
                  </td>
                </tr>
              ) : (
                filteredCases.map((c) => {
                  const natP = c.natural_recovery_prob ? `${Math.round(c.natural_recovery_prob * 100)}%` : '--';
                  const lift =
                    c.incremental_lift !== undefined && c.incremental_lift !== null
                      ? `+${Math.round(c.incremental_lift * 100)}%`
                      : '--';
                  const contrib =
                    c.expected_incremental_contribution !== undefined && c.expected_incremental_contribution !== null
                      ? `₹${c.expected_incremental_contribution.toLocaleString('en-IN')}`
                      : '--';

                  return (
                    <tr
                      key={c.id}
                      className="hover:bg-slate-800/50 transition-colors cursor-pointer group"
                      onClick={() => onSelectCase(c.id)}
                    >
                      <td className="py-4 px-4">
                        <div className="font-bold text-white group-hover:text-indigo-400 transition-colors">
                          {c.customer_name || c.customer_id}
                        </div>
                        <div className="text-[10px] text-slate-400 font-mono mt-0.5">{c.payment_id}</div>
                      </td>

                      <td className="py-4 px-4 font-bold text-white">
                        ₹{c.amount.toLocaleString('en-IN')}
                      </td>

                      <td className="py-4 px-4">
                        <div className="font-mono text-xs text-slate-300 font-medium">{c.failure_code || 'FAILURE'}</div>
                        <div className="text-[10px] text-slate-500 truncate max-w-[160px]">{c.failure_reason}</div>
                      </td>

                      <td className="py-4 px-4 font-semibold text-slate-300">
                        {natP}
                      </td>

                      <td className="py-4 px-4 font-semibold text-slate-100">
                        {c.recommended_action ? (
                          <Badge variant="default" size="sm">
                            {c.recommended_action}
                          </Badge>
                        ) : (
                          '--'
                        )}
                      </td>

                      <td className="py-4 px-4">
                        <Badge
                          variant={
                            c.incremental_lift && c.incremental_lift > 0.25
                              ? 'emerald'
                              : c.incremental_lift && c.incremental_lift > 0.05
                              ? 'indigo'
                              : 'slate'
                          }
                          size="sm"
                        >
                          {lift}
                        </Badge>
                      </td>

                      <td className="py-4 px-4 font-bold text-emerald-400">
                        {contrib}
                      </td>

                      <td className="py-4 px-4">
                        <div className="flex flex-col gap-1">
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
                            {c.final_decision || 'ANALYZING'}
                          </Badge>

                          {c.policy_status && c.policy_status !== 'APPROVED' && (
                            <span className="text-[9px] font-bold text-rose-400 uppercase tracking-wider">
                              Policy: {c.policy_status}
                            </span>
                          )}
                        </div>
                      </td>

                      <td className="py-4 px-4 text-right">
                        <button
                          onClick={(e) => {
                            e.stopPropagation();
                            onSelectCase(c.id);
                          }}
                          className="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-indigo-600 text-slate-300 hover:text-white font-semibold text-xs transition-all flex items-center gap-1 ml-auto"
                        >
                          <span>Audit</span>
                          <ChevronRight className="w-3.5 h-3.5" />
                        </button>
                      </td>
                    </tr>
                  );
                })
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
