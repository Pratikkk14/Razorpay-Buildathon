import React, { useEffect, useState } from 'react';
import {
  ShieldCheck,
  ShieldAlert,
  Lock,
  Clock,
  UserX,
  RotateCcw,
  Ban,
  Scale,
  Sparkles,
  Layers,
  CheckCircle2,
} from 'lucide-react';
import { api } from '../services/api';
import { Badge } from '../components/common/Badge';

export const GovernanceSafety: React.FC = () => {
  const [rules, setRules] = useState<any[]>([]);
  const [vetoLogs, setVetoLogs] = useState<any[]>([]);
  const [auditEvents, setAuditEvents] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    setLoading(true);
    try {
      const [r, v, a] = await Promise.all([
        api.getGovernanceRules(),
        api.getVetoLogs(),
        api.getAuditEvents(),
      ]);
      setRules(r);
      setVetoLogs(v);
      setAuditEvents(a);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-6">
      {/* Header & Policy Boundary Banner */}
      <div className="relative overflow-hidden rounded-2xl bg-gradient-to-r from-slate-900 via-slate-900 to-indigo-950/60 border border-slate-800 p-6 space-y-3">
        <div className="flex items-center gap-2">
          <Badge variant="emerald" size="sm">
            <ShieldCheck className="w-3.5 h-3.5 text-emerald-400" />
            Deterministic Trust Boundary Active
          </Badge>
          <span className="text-xs text-slate-400 font-mono">Zero AI Direct Execution Authority</span>
        </div>
        <h2 className="text-xl font-bold tracking-tight text-white">
          Governance, Safety & Deterministic Guardrails
        </h2>
        <p className="text-xs text-slate-300 max-w-3xl leading-relaxed">
          The ML inference model generates probabilistic uplift recommendations; <strong className="text-white">only deterministic policy rules hold execution authority</strong>. Any recommendation violating idempotency, frequency caps, quiet hours, or customer consent is instantly vetoed or modified.
        </p>
      </div>

      {/* Grid of 7 Deterministic Policy Rules */}
      <div className="space-y-3">
        <div className="flex items-center justify-between">
          <h3 className="text-sm font-bold text-white flex items-center gap-2">
            <Lock className="w-4 h-4 text-indigo-400" />
            <span>Deterministic Policy Guardrail Catalog</span>
          </h3>
          <Badge variant="indigo" size="sm">{rules.length} Active Rules</Badge>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {rules.map((rule) => (
            <div
              key={rule.rule_key}
              className="glass-panel rounded-xl p-4 border border-slate-800 hover:border-slate-700 transition-all space-y-2.5"
            >
              <div className="flex items-start justify-between gap-2">
                <span className="font-bold text-xs text-white">{rule.rule_name}</span>
                <span className="text-[10px] px-2 py-0.5 rounded-full bg-emerald-950 border border-emerald-800 text-emerald-400 font-semibold">
                  Enforced
                </span>
              </div>
              <p className="text-[11px] text-slate-400 leading-relaxed">
                {rule.description}
              </p>
              <div className="pt-2 border-t border-slate-800/80 text-[10px] text-indigo-300 font-mono">
                Threshold: {rule.threshold}
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Two Column Section: Safety Veto Logs & Audit Trail */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Veto Logs */}
        <div className="lg:col-span-6 glass-panel rounded-2xl p-5 space-y-4">
          <div className="flex items-center justify-between border-b border-slate-800 pb-3">
            <div>
              <h3 className="text-sm font-bold text-white flex items-center gap-2">
                <ShieldAlert className="w-4 h-4 text-rose-400" />
                <span>Policy Veto & Suppression Logs</span>
              </h3>
              <p className="text-xs text-slate-400">Interventions blocked or rerouted by guardrails</p>
            </div>
            <Badge variant="rose" size="sm">{vetoLogs.length} Vetoes</Badge>
          </div>

          <div className="space-y-3 max-h-[380px] overflow-y-auto pr-1">
            {vetoLogs.length === 0 ? (
              <p className="text-xs text-slate-500 py-8 text-center">No safety vetoes logged yet.</p>
            ) : (
              vetoLogs.map((v) => (
                <div
                  key={v.id}
                  className="rounded-xl p-3 bg-slate-900/80 border border-rose-950/60 space-y-1.5 text-xs"
                >
                  <div className="flex items-center justify-between">
                    <span className="font-bold text-rose-400 text-[11px]">{v.rule_name}</span>
                    <span className="text-[10px] text-slate-500 font-mono">{v.timestamp.slice(0, 19)}</span>
                  </div>
                  <p className="text-slate-200 text-[11px]">
                    {v.veto_reason}
                  </p>
                  <div className="text-[10px] text-slate-400 font-mono pt-1 border-t border-slate-800/60">
                    Case ID: {v.case_id?.slice(0, 8)} | Target Action: {v.action_targeted || 'Outreach'}
                  </div>
                </div>
              ))
            )}
          </div>
        </div>

        {/* Append-Only Audit Trail */}
        <div className="lg:col-span-6 glass-panel rounded-2xl p-5 space-y-4">
          <div className="flex items-center justify-between border-b border-slate-800 pb-3">
            <div>
              <h3 className="text-sm font-bold text-white flex items-center gap-2">
                <Layers className="w-4 h-4 text-cyan-400" />
                <span>Immutable System Audit Trail</span>
              </h3>
              <p className="text-xs text-slate-400">Chronological traceability for regulatory review</p>
            </div>
            <Badge variant="indigo" size="sm">{auditEvents.length} Events</Badge>
          </div>

          <div className="space-y-2.5 max-h-[380px] overflow-y-auto pr-1">
            {auditEvents.slice(0, 15).map((e) => (
              <div
                key={e.id}
                className="p-2.5 rounded-xl bg-slate-900/60 border border-slate-800 text-xs flex items-start justify-between gap-3"
              >
                <div className="space-y-0.5">
                  <div className="flex items-center gap-2">
                    <Badge variant="slate" size="sm">{e.event_type}</Badge>
                    <span className="text-[10px] text-slate-500 font-mono">{e.actor}</span>
                  </div>
                  <p className="text-slate-300 text-[11px]">{e.summary}</p>
                </div>
                <span className="text-[10px] text-slate-500 font-mono shrink-0">
                  {e.timestamp.slice(11, 19)}
                </span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};
