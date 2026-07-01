import React from 'react';
import { Layers, Server, ShieldAlert } from 'lucide-react';

function HowItWorks() {
  const steps = [
    { icon: <Server size={24} className="text-blue-600 dark:text-cyan-400" />, num: "01", title: "Connect Hardware", desc: "Plug our secure hub into your existing conveyor tunnel controllers or bay payment terminals. Setup takes under 15 minutes." },
    { icon: <Layers size={24} className="text-indigo-600 dark:text-purple-400" />, num: "02", title: "Configure Your Team", desc: "Add managers and detailers. Assign custom commission splits or tip pools based on specific operational tiers." },
    { icon: <ShieldAlert size={24} className="text-sky-600 dark:text-teal-400" />, num: "03", title: "Monitor the Glow", desc: "Open your tablet or phone. Watch live car counts, track chemical flow rates, and manage busy lanes seamlessly." }
  ];

  return (
    <div className="max-w-7xl mx-auto px-6 lg:px-8 py-12 transition-colors duration-300">
      <div className="text-center max-w-3xl mx-auto mb-16 space-y-4">
        <h1 className="text-4xl font-black text-slate-900 dark:text-white">Setup in 3 Simple Steps</h1>
        <p className="text-lg text-slate-500 dark:text-slate-400">Apex Glow fits effortlessly right into your current real-world car wash framework.</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-12 relative">
        {steps.map((step, index) => (
          <div key={index} className="relative group p-6 rounded-3xl bg-white dark:bg-slate-900 border border-slate-100 dark:border-slate-800 shadow-sm space-y-4">
            <div className="flex justify-between items-center">
              <div className="p-3 rounded-2xl bg-slate-50 dark:bg-slate-950 border border-slate-100 dark:border-slate-800">
                {step.icon}
              </div>
              <span className="text-3xl font-black text-slate-200 dark:text-slate-800 group-hover:text-blue-600 dark:group-hover:text-cyan-400 transition-colors">{step.num}</span>
            </div>
            <h3 className="text-xl font-bold text-slate-900 dark:text-white">{step.title}</h3>
            <p className="text-sm text-slate-500 dark:text-slate-400 leading-relaxed font-medium">{step.desc}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default HowItWorks;
