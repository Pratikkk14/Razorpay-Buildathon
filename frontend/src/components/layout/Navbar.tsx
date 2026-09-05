import React from 'react';
import {
  Sparkles,
  ShieldCheck,
  TrendingUp,
  RefreshCw,
  PlusCircle,
  Zap,
} from 'lucide-react';
import { Badge } from '../common/Badge';

interface NavbarProps {
  onRefresh?: () => void;
  onOpenDemo?: () => void;
  onGenerateBatch?: () => void;
  isRefreshing?: boolean;
}

export const Navbar: React.FC<NavbarProps> = ({
  onRefresh,
  onOpenDemo,
  onGenerateBatch,
  isRefreshing = false,
}) => {
  return (
    <header className="sticky top-0 z-40 w-full border-b border-slate-800/80 bg-[#0B0F19]/90 backdrop-blur-xl px-6 py-3.5">
      <div className="flex items-center justify-between gap-4">
        {/* Brand & Thesis Tag */}
        <div className="flex items-center gap-4">
          <div className="flex items-center gap-3">
            <div className="w-9 h-9 rounded-xl bg-gradient-to-tr from-indigo-600 via-indigo-500 to-cyan-400 p-[1.5px] shadow-[0_0_20px_rgba(99,102,241,0.4)]">
              <div className="w-full h-full bg-[#0B0F19] rounded-[10px] flex items-center justify-center">
                <TrendingUp className="w-5 h-5 text-indigo-400" />
              </div>
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h1 className="text-base font-bold tracking-tight text-white flex items-center gap-1.5">
                  Razorpay <span className="bg-gradient-to-r from-indigo-400 to-cyan-400 bg-clip-text text-transparent">Recovery Intelligence</span>
                </h1>
                <Badge variant="indigo" size="sm">
                  Buildathon 2026
                </Badge>
              </div>
              <p className="text-[11px] text-slate-400 font-medium">
                Optimizing for <span className="text-emerald-400 font-semibold">Incremental Contribution</span>, not raw recovery rate
              </p>
            </div>
          </div>
        </div>

        {/* Global Action Bar */}
        <div className="flex items-center gap-3">
          <button
            onClick={onOpenDemo}
            className="flex items-center gap-2 px-3.5 py-1.5 rounded-xl bg-gradient-to-r from-indigo-600 to-cyan-600 hover:from-indigo-500 hover:to-cyan-500 text-white font-semibold text-xs transition-all shadow-[0_0_20px_rgba(99,102,241,0.35)] hover:shadow-[0_0_25px_rgba(99,102,241,0.5)]"
          >
            <Sparkles className="w-3.5 h-3.5 text-yellow-300" />
            <span>Judge Demo Walkthrough</span>
          </button>

          <button
            onClick={onGenerateBatch}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-slate-800/80 hover:bg-slate-700/80 border border-slate-700 text-slate-200 font-medium text-xs transition-all"
            title="Generate synthetic payment failure events"
          >
            <PlusCircle className="w-3.5 h-3.5 text-indigo-400" />
            <span>+25 Synthetic Cases</span>
          </button>

          <button
            onClick={onRefresh}
            disabled={isRefreshing}
            className="p-2 rounded-xl bg-slate-800/80 hover:bg-slate-700 border border-slate-700 text-slate-300 transition-all disabled:opacity-50"
            title="Refresh dashboard data"
          >
            <RefreshCw className={`w-3.5 h-3.5 ${isRefreshing ? 'animate-spin text-indigo-400' : ''}`} />
          </button>

          <div className="flex items-center gap-2 pl-2 border-l border-slate-800">
            <span className="relative flex h-2.5 w-2.5">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
              <span className="relative inline-flex rounded-full h-2.5 w-2.5 bg-emerald-500"></span>
            </span>
            <span className="text-[11px] font-semibold text-slate-300">Live Engine</span>
          </div>
        </div>
      </div>
    </header>
  );
};
