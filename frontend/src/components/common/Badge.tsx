import React from 'react';

interface BadgeProps {
  children: React.ReactNode;
  variant?: 'default' | 'emerald' | 'indigo' | 'amber' | 'rose' | 'slate' | 'outline';
  size?: 'sm' | 'md' | 'lg';
  className?: string;
}

export const Badge: React.FC<BadgeProps> = ({
  children,
  variant = 'default',
  size = 'md',
  className = '',
}) => {
  const variantStyles = {
    default: 'bg-slate-800 text-slate-300 border-slate-700',
    emerald: 'bg-emerald-950/70 text-emerald-400 border-emerald-800/60 shadow-[0_0_12px_rgba(16,185,129,0.15)]',
    indigo: 'bg-indigo-950/70 text-indigo-400 border-indigo-800/60 shadow-[0_0_12px_rgba(99,102,241,0.15)]',
    amber: 'bg-amber-950/70 text-amber-400 border-amber-800/60 shadow-[0_0_12px_rgba(245,158,11,0.15)]',
    rose: 'bg-rose-950/70 text-rose-400 border-rose-800/60 shadow-[0_0_12px_rgba(244,63,94,0.15)]',
    slate: 'bg-slate-900 text-slate-400 border-slate-800',
    outline: 'bg-transparent text-slate-300 border-slate-700',
  };

  const sizeStyles = {
    sm: 'text-[10px] px-1.5 py-0.5 font-medium',
    md: 'text-xs px-2.5 py-1 font-semibold',
    lg: 'text-sm px-3 py-1.5 font-semibold',
  };

  return (
    <span
      className={`inline-flex items-center gap-1.5 rounded-full border transition-colors ${variantStyles[variant]} ${sizeStyles[size]} ${className}`}
    >
      {children}
    </span>
  );
};
