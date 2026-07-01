import React, { useState } from 'react';
import { TrendingUp, DollarSign, Clock } from 'lucide-react';

function RoiCalculator() {
  const [carsPerDay, setCarsPerDay] = useState(60);
  const [avgWashPrice, setAvgWashPrice] = useState(1200);

  // Business formula logic: recovering roughly 15% revenue leakage
  const monthlyRevenue = carsPerDay * avgWashPrice * 30;
  const projectedSavings = Math.round(monthlyRevenue * 0.15);

  return (
    <section className="relative z-10 max-w-7xl mx-auto px-6 lg:px-8 py-16 border-t border-blue-100/60 dark:border-slate-900 transition-colors">
      <div className="text-center max-w-3xl mx-auto mb-12 space-y-3">
        <h2 className="text-3xl sm:text-4xl font-black tracking-tight">Calculate Your Savings</h2>
        <p className="text-base sm:text-lg text-slate-500 dark:text-slate-400 font-medium">
          See how much revenue Apex Glow can help you recover by automating operations and inventory control.
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 max-w-5xl mx-auto items-center">
        
        {/* Sliders Input */}
        <div className="lg:col-span-7 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl p-6 sm:p-8 space-y-6 shadow-sm">
          <div>
            <div className="flex justify-between items-center mb-2">
              <label className="text-sm font-bold text-slate-700 dark:text-slate-300">Average Cars Washed Per Day</label>
              <span className="text-lg font-black text-blue-600 dark:text-cyan-400">{carsPerDay}</span>
            </div>
            <input 
              type="range" min="10" max="250" value={carsPerDay} 
              onChange={(e) => setCarsPerDay(Number(e.target.value))}
              className="w-full accent-blue-600 dark:accent-cyan-400 bg-slate-100 dark:bg-slate-950 h-2 rounded-lg cursor-pointer"
            />
          </div>

          <div>
            <div className="flex justify-between items-center mb-2">
              <label className="text-sm font-bold text-slate-700 dark:text-slate-300">Average Ticket Value (KES)</label>
              <span className="text-lg font-black text-blue-600 dark:text-cyan-400">KES {avgWashPrice.toLocaleString()}</span>
            </div>
            <input 
              type="range" min="200" max="5000" step="50" value={avgWashPrice} 
              onChange={(e) => setAvgWashPrice(Number(e.target.value))}
              className="w-full accent-blue-600 dark:accent-cyan-400 bg-slate-100 dark:bg-slate-950 h-2 rounded-lg cursor-pointer"
            />
          </div>
        </div>

        {/* Dynamic Metrics Results Card */}
        <div className="lg:col-span-5 bg-blue-600 dark:bg-slate-900 border border-transparent dark:border-slate-800 rounded-3xl p-6 sm:p-8 text-white space-y-6 shadow-xl relative overflow-hidden">
          <div className="absolute -right-6 -bottom-6 w-32 h-32 bg-white/5 rounded-full pointer-events-none" />
          
          <div>
            <p className="text-xs uppercase font-bold text-blue-100 dark:text-slate-400 tracking-wider">Projected Revenue Restored</p>
            <h4 className="text-3xl sm:text-4xl font-black text-white dark:text-cyan-400 mt-1">
              KES {projectedSavings.toLocaleString()}
              <span className="text-sm font-medium text-blue-100 dark:text-slate-400"> / mo</span>
            </h4>
          </div>

          <ul className="space-y-3 border-t border-white/10 dark:border-slate-800 pt-4 text-sm font-medium text-blue-50 dark:text-slate-300">
            <li className="flex items-center gap-2">
              <TrendingUp size={16} className="text-blue-200 dark:text-emerald-400 shrink-0" />
              <span>~15% tracking error leakage captured</span>
            </li>
            <li className="flex items-center gap-2">
              <DollarSign size={16} className="text-blue-200 dark:text-emerald-400 shrink-0" />
              <span>Prevents chemical compound or wax overhead waste</span>
            </li>
            <li className="flex items-center gap-2">
              <Clock size={16} className="text-blue-200 dark:text-emerald-400 shrink-0" />
              <span>Saves ~24 management administration hours monthly</span>
            </li>
          </ul>
        </div>

      </div>
    </section>
  );
}

export default RoiCalculator;
