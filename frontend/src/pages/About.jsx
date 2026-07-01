import React from 'react';
import { Target, Eye, Users2, ShieldCheck } from 'lucide-react';

function About() {
  const values = [
    { icon: <Target className="w-5 h-5 text-blue-600 dark:text-cyan-400" />, title: "Precision Tuning", desc: "We turn complex mechanical fluid metrics and lane throughput analytics into simple, responsive web apps." },
    { icon: <Eye className="w-5 h-5 text-indigo-600 dark:text-purple-400" />, title: "Radical Transparency", desc: "We track every single wash cycle and chemical flow drop down to the precise milliliter and timestamp." },
    { icon: <Users2 className="w-5 h-5 text-sky-600 dark:text-teal-400" />, title: "Operational Growth", desc: "We optimize software layers so operators can scale business locations safely while protecting their staff tips." }
  ];

  return (
    <div className="max-w-7xl mx-auto px-6 lg:px-8 py-12 transition-colors duration-300">
      
      {/* Brand Bio Editorial Banner */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center mb-20 max-w-5xl mx-auto">
        <div className="lg:col-span-7 space-y-4 text-center lg:text-left">
          <span className="text-xs font-bold uppercase tracking-wider text-blue-600 dark:text-cyan-400">Our Story</span>
          <h1 className="text-4xl font-black tracking-tight text-slate-900 dark:text-white leading-tight">
            Rewriting the rules of automotive care operations.
          </h1>
          <p className="text-base text-slate-500 dark:text-slate-400 leading-relaxed font-medium">
            Founded in Nairobi, Apex Glow was born from a simple observation: while modern vehicles have evolved at lightning speed, car wash operations remained trapped in paper ledgers, uncalibrated soap valves, and hidden revenue leakage.
          </p>
          <p className="text-base text-slate-500 dark:text-slate-400 leading-relaxed font-medium">
            We built a cloud-based software engine that links directly with physical point-of-sale systems and digital IoT tank gauges. We give forward-thinking wash operators the tech infrastructure to run autonomous, high-yield businesses.
          </p>
        </div>
        
        {/* Statistics Call-Out Card */}
        <div className="lg:col-span-5 relative bg-gradient-to-br from-blue-600 to-indigo-700 dark:from-slate-900 dark:to-slate-950 p-8 rounded-3xl text-white shadow-xl overflow-hidden min-h-[260px] flex flex-col justify-end">
          <div className="absolute top-0 right-0 w-32 h-32 bg-white/5 rounded-full blur-2xl" />
          <ShieldCheck size={40} className="text-blue-200 dark:text-cyan-400 mb-6" />
          <h3 className="text-3xl font-black">1.2M+ Washes</h3>
          <p className="text-xs font-bold text-blue-100 dark:text-slate-400 mt-1 uppercase tracking-wider">Processed and protected via our secure system</p>
        </div>
      </div>

      {/* Corporate Pillars Grid */}
      <div className="border-t border-blue-100/60 dark:border-slate-900 pt-16 max-w-5xl mx-auto">
        <h2 className="text-2xl font-black text-center text-slate-900 dark:text-white mb-12">The Pillars That Drive Our Team</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {values.map((val, idx) => (
            <div key={idx} className="p-6 bg-white dark:bg-slate-900 border border-slate-100 dark:border-slate-800 rounded-2xl shadow-sm space-y-3">
              <div className="p-2.5 bg-slate-50 dark:bg-slate-950 border border-slate-100 dark:border-slate-850 rounded-xl w-fit">{val.icon}</div>
              <h3 className="font-bold text-lg text-slate-900 dark:text-white tracking-tight">{val.title}</h3>
              <p className="text-sm text-slate-500 dark:text-slate-400 font-medium leading-relaxed">{val.desc}</p>
            </div>
          ))}
        </div>
      </div>

    </div>
  );
}

export default About;
