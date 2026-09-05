import React from 'react';
import { LucideIcon } from 'lucide-react';

interface MetricCardProps {
  title: string;
  value: string | number;
  subtitle?: string;
  icon?: LucideIcon;
  trend?: {
    value: string;
    isPositive?: boolean;
    label?: string;
  };
  variant?: 'indigo' | 'emerald' | 'amber' | 'rose' | 'slate';
  tooltip?: string;
}

export const MetricCard: React.FC<MetricCardProps> = ({
  title,
  value,
  subtitle,
  icon: Icon,
  trend,
  variant = 'indigo',
  tooltip,
}) => {
  const borderStyles = {
    indigo: 'hover:border-indigo-500/40 hover:shadow-[0_0_25px_-5px_rgba(99,102,241,0.25)]',
    emerald: 'hover:border-emerald-500/40 hover:shadow-[0_0_25px_-5px_rgba(16,185,129,0.25)]',
    amber: 'hover:border-amber-500/40 hover:shadow-[0_0_25px_-5px_rgba(245,158,11,0.25)]',
    rose: 'hover:border-rose-500/40 hover:shadow-[0_0_25px_-5px_rgba(244,63,94,0.25)]',
    slate: 'hover:border-slate-600',
  };

  const iconBgStyles = {
    indigo: 'bg-indigo-950/80 text-indigo-400 border border-indigo-800/50',
    emerald: 'bg-emerald-950/80 text-emerald-400 border border-emerald-800/50',
    amber: 'bg-amber-950/80 text-amber-400 border border-amber-800/50',
    rose: 'bg-rose-950/80 text-rose-400 border border-rose-800/50',
    slate: 'bg-slate-800 text-slate-400 border border-slate-700',
  };

  return (
    <div
      className={`glass-panel rounded-2xl p-5 transition-all duration-300 relative group overflow-hidden ${borderStyles[variant]}`}
      title={tooltip}
    >
      <div className="flex items-center justify-between gap-4">
        <div>
          <p className="text-xs font-medium uppercase tracking-wider text-slate-400">
            {title}
          </p>
          <div className="mt-1.5 flex items-baseline gap-2">
            <span className="text-2xl font-bold tracking-tight text-white">
              {value}
            </span>
          </div>
        </div>

        {Icon && (
          <div className={`p-3 rounded-xl ${iconBgStyles[variant]}`}>
            <Icon className="w-5 h-5" />
          </div>
        )}
      </div>

      {(subtitle || trend) && (
        <div className="mt-3 pt-3 border-t border-slate-800/60 flex items-center justify-between text-xs">
          {subtitle && <span className="text-slate-400 font-medium">{subtitle}</span>}
          {trend && (
            <span
              className={`font-semibold flex items-center gap-1 ${
                trend.isPositive ? 'text-emerald-400' : 'text-rose-400'
              }`}
            >
              {trend.value}
              {trend.label && <span className="text-slate-500 font-normal">{trend.label}</span>}
            </span>
          )}
        </div>
      )}

      {/* Decorative gradient glow on card edge */}
      <div className="absolute top-0 left-0 right-0 h-[2px] bg-gradient-to-r from-transparent via-indigo-500/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity" />
    </div>
  );
};
