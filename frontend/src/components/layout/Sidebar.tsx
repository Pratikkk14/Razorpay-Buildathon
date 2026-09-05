import React from 'react';
import {
  LayoutDashboard,
  Inbox,
  Sliders,
  FlaskConical,
  Cpu,
  ShieldCheck,
  Sparkles,
  Zap,
} from 'lucide-react';

export type NavigationTab =
  | 'command-center'
  | 'recovery-queue'
  | 'decision-explorer'
  | 'experiments'
  | 'simulator'
  | 'governance'
  | 'demo';

interface SidebarProps {
  activeTab: NavigationTab;
  onTabChange: (tab: NavigationTab) => void;
  casesCount?: number;
  suppressedCount?: number;
}

export const Sidebar: React.FC<SidebarProps> = ({
  activeTab,
  onTabChange,
  casesCount = 0,
  suppressedCount = 0,
}) => {
  const navItems = [
    {
      id: 'command-center' as NavigationTab,
      label: 'Command Center',
      icon: LayoutDashboard,
      badge: null,
    },
    {
      id: 'recovery-queue' as NavigationTab,
      label: 'Recovery Queue',
      icon: Inbox,
      badge: casesCount > 0 ? `${casesCount}` : null,
      badgeVariant: 'indigo',
    },
    {
      id: 'decision-explorer' as NavigationTab,
      label: 'Decision Explorer',
      icon: Sliders,
      badge: 'Interactive',
      badgeVariant: 'emerald',
    },
    {
      id: 'experiments' as NavigationTab,
      label: 'Experiments & Benchmark',
      icon: FlaskConical,
      badge: '5 Policies',
      badgeVariant: 'amber',
    },
    {
      id: 'simulator' as NavigationTab,
      label: 'Recovery Simulator',
      icon: Cpu,
      badge: 'Monte Carlo',
      badgeVariant: 'slate',
    },
    {
      id: 'governance' as NavigationTab,
      label: 'Governance & Safety',
      icon: ShieldCheck,
      badge: suppressedCount > 0 ? `${suppressedCount} Vetoed` : 'Active',
      badgeVariant: suppressedCount > 0 ? 'rose' : 'emerald',
    },
    {
      id: 'demo' as NavigationTab,
      label: 'Buildathon Demo',
      icon: Sparkles,
      badge: '5 Scenarios',
      badgeVariant: 'indigo',
    },
  ];

  return (
    <aside className="w-64 border-r border-slate-800/80 bg-[#0B0F19]/95 flex flex-col justify-between p-4 shrink-0 min-h-[calc(100vh-65px)]">
      <div className="space-y-6">
        <div>
          <p className="px-3 text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-3">
            Operations & Intelligence
          </p>
          <nav className="space-y-1.5">
            {navItems.map((item) => {
              const Icon = item.icon;
              const isActive = activeTab === item.id;
              return (
                <button
                  key={item.id}
                  onClick={() => onTabChange(item.id)}
                  className={`w-full flex items-center justify-between px-3 py-2.5 rounded-xl font-medium text-xs transition-all ${
                    isActive
                      ? 'bg-gradient-to-r from-indigo-600/90 to-indigo-700 text-white shadow-[0_0_20px_rgba(99,102,241,0.25)]'
                      : 'text-slate-400 hover:text-slate-100 hover:bg-slate-800/60'
                  }`}
                >
                  <div className="flex items-center gap-3">
                    <Icon className={`w-4 h-4 ${isActive ? 'text-white' : 'text-slate-400'}`} />
                    <span>{item.label}</span>
                  </div>

                  {item.badge && (
                    <span
                      className={`text-[10px] px-2 py-0.5 rounded-full font-semibold ${
                        isActive
                          ? 'bg-white/20 text-white'
                          : item.badgeVariant === 'emerald'
                          ? 'bg-emerald-950 text-emerald-400 border border-emerald-800/60'
                          : item.badgeVariant === 'amber'
                          ? 'bg-amber-950 text-amber-400 border border-amber-800/60'
                          : item.badgeVariant === 'rose'
                          ? 'bg-rose-950 text-rose-400 border border-rose-800/60'
                          : 'bg-slate-800 text-slate-400'
                      }`}
                    >
                      {item.badge}
                    </span>
                  )}
                </button>
              );
            })}
          </nav>
        </div>
      </div>

      {/* Model Contract & Policy Badge at Bottom */}
      <div className="glass-panel rounded-xl p-3.5 border border-slate-800 text-xs">
        <div className="flex items-center gap-2 mb-1.5">
          <Zap className="w-3.5 h-3.5 text-cyan-400" />
          <span className="font-semibold text-slate-200">ML Model Contract</span>
        </div>
        <p className="text-[11px] text-slate-400 leading-relaxed">
          Active Interface: <span className="text-indigo-400 font-mono">MockMLModelService (v1.0.0)</span>. Ready for Kaggle inference drop-in.
        </p>
      </div>
    </aside>
  );
};
