import React, { useState } from 'react';
import {
  Sliders,
  Sparkles,
  TrendingUp,
  ShieldCheck,
  Zap,
  Info,
  DollarSign,
  Layers,
  ArrowRight,
} from 'lucide-react';
import { Badge } from '../components/common/Badge';

export const DecisionExplorer: React.FC = () => {
  // Sandbox parameters
  const [amount, setAmount] = useState<number>(4999);
  const [naturalProb, setNaturalProb] = useState<number>(0.18);
  const [linkProb, setLinkProb] = useState<number>(0.72);
  const [retryProb, setRetryProb] = useState<number>(0.32);
  const [reminderProb, setReminderProb] = useState<number>(0.48);
  const [alternateProb, setAlternateProb] = useState<number>(0.62);
  const [escalateProb, setEscalateProb] = useState<number>(0.85);

  // Policy toggles
  const [isDND, setIsDND] = useState<boolean>(false);
  const [isCooldown, setIsCooldown] = useState<boolean>(false);
  const [isQuietHours, setIsQuietHours] = useState<boolean>(false);
  const [attempts, setAttempts] = useState<number>(1);

  // Economic costs
  const costs = {
    RETRY: 0.50 + 0.10,
    PAYMENT_LINK: 2.00 + 1.00,
    REMINDER: 0.75 + 0.50,
    ALTERNATE_METHOD: 1.50 + 0.80,
    HUMAN_ESCALATION: 150.00,
    NO_ACTION: 0.00,
  };

  // Policy checks
  const maxRetriesBlocked = attempts >= 2;
  const isHighValue = amount >= 50000;

  const candidateActions = [
    {
      action: 'PAYMENT_LINK',
      prob: linkProb,
      cost: costs.PAYMENT_LINK,
      policyAllowed: !isDND && !isCooldown && !isHighValue,
      blockReason: isDND ? 'DND / Opt-Out' : isCooldown ? 'Contact Cooldown' : isHighValue ? 'High-Value Escalation' : null,
    },
    {
      action: 'ALTERNATE_METHOD',
      prob: alternateProb,
      cost: costs.ALTERNATE_METHOD,
      policyAllowed: !isDND && !isCooldown && !isHighValue,
      blockReason: isDND ? 'DND / Opt-Out' : isCooldown ? 'Contact Cooldown' : isHighValue ? 'High-Value Escalation' : null,
    },
    {
      action: 'REMINDER',
      prob: reminderProb,
      cost: costs.REMINDER,
      policyAllowed: !isDND && !isCooldown && !isHighValue,
      blockReason: isDND ? 'DND / Opt-Out' : isCooldown ? 'Contact Cooldown' : isHighValue ? 'High-Value Escalation' : null,
    },
    {
      action: 'RETRY',
      prob: retryProb,
      cost: costs.RETRY,
      policyAllowed: !maxRetriesBlocked && !isHighValue,
      blockReason: maxRetriesBlocked ? 'Max Retries Exceeded' : isHighValue ? 'High-Value Escalation' : null,
    },
    {
      action: 'HUMAN_ESCALATION',
      prob: escalateProb,
      cost: costs.HUMAN_ESCALATION,
      policyAllowed: true,
      blockReason: null,
    },
    {
      action: 'NO_ACTION',
      prob: naturalProb,
      cost: costs.NO_ACTION,
      policyAllowed: true,
      blockReason: null,
    },
  ];

  // Calculate economics for each action
  const evaluatedActions = candidateActions.map((cand) => {
    const lift = cand.action === 'NO_ACTION' ? 0.0 : Math.max(0, cand.prob - naturalProb);
    const incRev = lift * amount;
    const netContrib = cand.action === 'NO_ACTION' ? 0.0 : incRev - cand.cost;

    return {
      ...cand,
      lift,
      incRev,
      netContrib,
    };
  });

  // Sort by net contribution descending
  evaluatedActions.sort((a, b) => b.netContrib - a.netContrib);

  // Pick winner
  let winner = evaluatedActions.find((a) => a.policyAllowed && a.action !== 'NO_ACTION' && a.netContrib > 0);
  if (!winner) {
    winner = evaluatedActions.find((a) => a.action === 'NO_ACTION');
  }

  // Determine decision verdict
  let decisionVerdict = 'DONT_ACT';
  let decisionReason = '';

  if (isHighValue) {
    decisionVerdict = 'ESCALATE';
    decisionReason = `High-value payment (₹${amount.toLocaleString('en-IN')}) requires white-glove manual assistance.`;
  } else if (winner && winner.action !== 'NO_ACTION') {
    if (isQuietHours && ['PAYMENT_LINK', 'REMINDER', 'ALTERNATE_METHOD'].includes(winner.action)) {
      decisionVerdict = 'WAIT';
      decisionReason = `Recommend ${winner.action} with net contribution ₹${winner.netContrib.toFixed(2)}, but holding until quiet hours end (9 AM).`;
    } else {
      decisionVerdict = 'ACT';
      decisionReason = `Act with ${winner.action}. Net incremental contribution is ₹${winner.netContrib.toFixed(2)} (lift +${Math.round(winner.lift * 100)}%).`;
    }
  } else {
    decisionVerdict = 'DONT_ACT';
    decisionReason = `Natural recovery is ${Math.round(naturalProb * 100)}%. No intervention yields positive incremental contribution after deducting costs.`;
  }

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold tracking-tight text-white flex items-center gap-2">
            Decision Explorer & Sandbox
            <Badge variant="emerald" size="sm">Interactive Matrix</Badge>
          </h2>
          <p className="text-xs text-slate-400">
            Simulate how varying natural recovery rates, payment amounts, and policy guardrails affect the final allocation decision.
          </p>
        </div>

        {/* Preset scenario buttons */}
        <div className="flex items-center gap-2">
          <button
            onClick={() => {
              setAmount(3499);
              setNaturalProb(0.82);
              setLinkProb(0.87);
              setIsCooldown(false);
              setIsDND(false);
            }}
            className="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 border border-slate-700 transition-all"
          >
            Scenario 1 (High Natural 82%)
          </button>
          <button
            onClick={() => {
              setAmount(4999);
              setNaturalProb(0.12);
              setLinkProb(0.71);
              setIsCooldown(false);
              setIsDND(false);
            }}
            className="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 border border-slate-700 transition-all"
          >
            Scenario 2 (High Uplift 59%)
          </button>
        </div>
      </div>

      {/* Decision Summary Output Card */}
      <div className="glass-panel rounded-2xl p-6 border border-indigo-500/40 shadow-[0_0_30px_rgba(99,102,241,0.15)] space-y-4">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-4 border-b border-slate-800">
          <div>
            <span className="text-[10px] uppercase tracking-wider font-bold text-slate-400">Decision Verdict</span>
            <div className="flex items-center gap-3 mt-1">
              <Badge
                variant={
                  decisionVerdict === 'ACT'
                    ? 'emerald'
                    : decisionVerdict === 'WAIT'
                    ? 'amber'
                    : decisionVerdict === 'ESCALATE'
                    ? 'indigo'
                    : 'slate'
                }
                size="lg"
              >
                {decisionVerdict}
              </Badge>
              {winner && winner.action !== 'NO_ACTION' && (
                <span className="text-base font-bold text-white">
                  Recommended Action: <span className="text-indigo-400">{winner.action}</span>
                </span>
              )}
            </div>
          </div>

          <div className="flex items-center gap-6">
            <div>
              <span className="text-[10px] uppercase tracking-wider text-slate-400 font-semibold">Payment Amount</span>
              <p className="text-base font-bold text-white">₹{amount.toLocaleString('en-IN')}</p>
            </div>
            <div>
              <span className="text-[10px] uppercase tracking-wider text-slate-400 font-semibold">Natural Recovery</span>
              <p className="text-base font-bold text-slate-300">{Math.round(naturalProb * 100)}%</p>
            </div>
            <div>
              <span className="text-[10px] uppercase tracking-wider text-slate-400 font-semibold">Best Net Contribution</span>
              <p className="text-base font-bold text-emerald-400">
                ₹{winner?.netContrib ? winner.netContrib.toFixed(2) : '0.00'}
              </p>
            </div>
          </div>
        </div>

        <div className="bg-slate-900/80 rounded-xl p-3 text-xs text-slate-200 border border-slate-800">
          <p>
            <strong className="text-indigo-400">Engine Rationale: </strong>
            {decisionReason}
          </p>
        </div>
      </div>

      {/* Interactive Controls & Comparison Matrix Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Controls Column */}
        <div className="lg:col-span-5 glass-panel rounded-2xl p-5 space-y-5">
          <h3 className="text-sm font-bold text-white flex items-center gap-2 border-b border-slate-800 pb-3">
            <Sliders className="w-4 h-4 text-indigo-400" />
            <span>Interactive Parameters</span>
          </h3>

          {/* Amount Slider */}
          <div className="space-y-2">
            <div className="flex items-center justify-between text-xs">
              <span className="text-slate-300 font-semibold">Payment Amount</span>
              <span className="font-mono font-bold text-white">₹{amount.toLocaleString('en-IN')}</span>
            </div>
            <input
              type="range"
              min={500}
              max={100000}
              step={500}
              value={amount}
              onChange={(e) => setAmount(Number(e.target.value))}
              className="w-full accent-indigo-500 bg-slate-800 rounded-lg cursor-pointer"
            />
            {amount >= 50000 && (
              <p className="text-[11px] text-amber-400 font-medium">⚠️ Amount ≥ ₹50,000 triggers High-Value Escalation rule</p>
            )}
          </div>

          {/* Natural Recovery Slider */}
          <div className="space-y-2">
            <div className="flex items-center justify-between text-xs">
              <span className="text-slate-300 font-semibold">Natural Recovery P(recovery | no action)</span>
              <span className="font-mono font-bold text-slate-200">{Math.round(naturalProb * 100)}%</span>
            </div>
            <input
              type="range"
              min={0.01}
              max={0.99}
              step={0.01}
              value={naturalProb}
              onChange={(e) => setNaturalProb(Number(e.target.value))}
              className="w-full accent-cyan-500 bg-slate-800 rounded-lg cursor-pointer"
            />
          </div>

          {/* Payment Link Prob Slider */}
          <div className="space-y-2">
            <div className="flex items-center justify-between text-xs">
              <span className="text-slate-300 font-semibold">Payment Link P(recovery | link)</span>
              <span className="font-mono font-bold text-indigo-400">{Math.round(linkProb * 100)}%</span>
            </div>
            <input
              type="range"
              min={0.01}
              max={0.99}
              step={0.01}
              value={linkProb}
              onChange={(e) => setLinkProb(Number(e.target.value))}
              className="w-full accent-indigo-500 bg-slate-800 rounded-lg cursor-pointer"
            />
          </div>

          {/* Policy Guardrail Toggles */}
          <div className="pt-4 border-t border-slate-800 space-y-3">
            <span className="text-xs font-bold text-slate-300 uppercase tracking-wider block">Policy Guardrail Overrides</span>
            
            <label className="flex items-center justify-between p-2.5 rounded-xl bg-slate-900/60 border border-slate-800 cursor-pointer hover:border-slate-700">
              <span className="text-xs text-slate-300">Customer DND / Opt-Out</span>
              <input
                type="checkbox"
                checked={isDND}
                onChange={(e) => setIsDND(e.target.checked)}
                className="w-4 h-4 accent-indigo-600 rounded"
              />
            </label>

            <label className="flex items-center justify-between p-2.5 rounded-xl bg-slate-900/60 border border-slate-800 cursor-pointer hover:border-slate-700">
              <span className="text-xs text-slate-300">Recent Contact Cooldown Active</span>
              <input
                type="checkbox"
                checked={isCooldown}
                onChange={(e) => setIsCooldown(e.target.checked)}
                className="w-4 h-4 accent-indigo-600 rounded"
              />
            </label>

            <label className="flex items-center justify-between p-2.5 rounded-xl bg-slate-900/60 border border-slate-800 cursor-pointer hover:border-slate-700">
              <span className="text-xs text-slate-300">Quiet Hours Window Active (Nighttime)</span>
              <input
                type="checkbox"
                checked={isQuietHours}
                onChange={(e) => setIsQuietHours(e.target.checked)}
                className="w-4 h-4 accent-indigo-600 rounded"
              />
            </label>
          </div>
        </div>

        {/* Ranked Candidate Actions Comparison Matrix */}
        <div className="lg:col-span-7 glass-panel rounded-2xl p-5 space-y-4">
          <div className="flex items-center justify-between border-b border-slate-800 pb-3">
            <div>
              <h3 className="text-sm font-bold text-white">Full Candidate Actions Economic Matrix</h3>
              <p className="text-xs text-slate-400">Comparing Natural vs Action vs Lift vs Cost vs Net Contribution</p>
            </div>
            <Badge variant="indigo" size="sm">Deterministic Ranking</Badge>
          </div>

          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs">
              <thead>
                <tr className="border-b border-slate-800 text-slate-400 uppercase tracking-wider text-[10px]">
                  <th className="pb-3 font-semibold">Action</th>
                  <th className="pb-3 font-semibold">Action P(rec)</th>
                  <th className="pb-3 font-semibold">Uplift</th>
                  <th className="pb-3 font-semibold">Gross Inc Rev</th>
                  <th className="pb-3 font-semibold">Cost</th>
                  <th className="pb-3 font-semibold">Net Contribution</th>
                  <th className="pb-3 font-semibold text-right">Policy</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-800/60">
                {evaluatedActions.map((cand, idx) => {
                  const isSelected = winner?.action === cand.action;
                  return (
                    <tr
                      key={idx}
                      className={`transition-colors ${
                        isSelected
                          ? 'bg-emerald-950/40 text-white font-semibold'
                          : !cand.policyAllowed
                          ? 'text-slate-500 opacity-60 bg-rose-950/10'
                          : 'text-slate-300 hover:bg-slate-800/30'
                      }`}
                    >
                      <td className="py-3.5 pr-2">
                        <div className="flex items-center gap-1.5">
                          <span>{cand.action}</span>
                          {isSelected && <Badge variant="emerald" size="sm">Selected</Badge>}
                        </div>
                      </td>

                      <td className="py-3.5">{Math.round(cand.prob * 100)}%</td>

                      <td className="py-3.5 text-indigo-400">
                        {cand.action === 'NO_ACTION' ? '--' : `+${Math.round(cand.lift * 100)}%`}
                      </td>

                      <td className="py-3.5">
                        {cand.action === 'NO_ACTION' ? '₹0.00' : `₹${cand.incRev.toFixed(2)}`}
                      </td>

                      <td className="py-3.5 text-rose-400">
                        {cand.cost > 0 ? `-₹${cand.cost.toFixed(2)}` : '₹0.00'}
                      </td>

                      <td className="py-3.5 font-bold text-emerald-400">
                        {cand.action === 'NO_ACTION' ? '₹0.00' : `₹${cand.netContrib.toFixed(2)}`}
                      </td>

                      <td className="py-3.5 text-right">
                        {cand.policyAllowed ? (
                          <span className="text-emerald-400 font-semibold text-[11px]">✓ Allowed</span>
                        ) : (
                          <span className="text-rose-400 font-semibold text-[10px]" title={cand.blockReason || ''}>
                            ✗ {cand.blockReason}
                          </span>
                        )}
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
};
