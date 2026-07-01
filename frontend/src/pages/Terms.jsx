import React from 'react';
import { FileText, Scale, ShieldAlert, BadgeCheck } from 'lucide-react';

function Terms() {
  const highlights = [
    {
      icon: <Scale className="w-5 h-5 text-blue-600 dark:text-cyan-400" />,
      title: "Fair Use Telemetry",
      desc: "Platform sub-accounts are restricted to active operators, managers, and lane detailers assigned to your specific wash locations."
    },
    {
      icon: <BadgeCheck className="w-5 h-5 text-indigo-600 dark:text-purple-400" />,
      title: "Subscription Cycles",
      desc: "SaaS tiers run on automated pay-as-you-go monthly cycles. You maintain full freedom to cancel or adjust limits at any time."
    },
    {
      icon: <ShieldAlert className="w-5 h-5 text-sky-600 dark:text-teal-400" />,
      title: "Hardware Integration",
      desc: "Operators are responsible for ensuring physical facility flow sensors and POS setups comply with local safe electrical regulations."
    }
  ];

  return (
    <div className="max-w-4xl mx-auto px-6 py-12 transition-colors duration-300">
      
      {/* Editorial Header */}
      <div className="flex items-center gap-3 border-b border-slate-200 dark:border-slate-800 pb-6 mb-10">
        <div className="p-3 bg-blue-50 text-blue-600 dark:bg-slate-900 dark:text-cyan-400 rounded-2xl border border-blue-100 dark:border-slate-800">
          <FileText size={24} />
        </div>
        <div>
          <h1 className="text-3xl font-black text-slate-900 dark:text-white tracking-tight">Terms of Service</h1>
          <p className="text-xs font-bold text-slate-400 dark:text-slate-500 mt-1 uppercase tracking-wider">Last Updated: June 2026</p>
        </div>
      </div>

      {/* Highlights Rule Cards Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
        {highlights.map((point, idx) => (
          <div key={idx} className="p-5 bg-white dark:bg-slate-900 border border-slate-150 dark:border-slate-800/80 rounded-2xl shadow-sm space-y-2">
            <div className="p-2 bg-slate-50 dark:bg-slate-950 w-fit rounded-xl border border-slate-100 dark:border-slate-850">{point.icon}</div>
            <h3 className="font-bold text-sm text-slate-900 dark:text-white tracking-tight">{point.title}</h3>
            <p className="text-xs text-slate-500 dark:text-slate-400 leading-relaxed font-medium">{point.desc}</p>
          </div>
        ))}
      </div>

      {/* Structured Legal Content Blocks */}
      <div className="space-y-8 text-sm sm:text-base text-slate-600 dark:text-slate-400 font-medium leading-relaxed">
        
        <section className="space-y-3">
          <h2 className="text-lg font-bold text-slate-900 dark:text-white tracking-tight">
            1. Agreement and Operational Terms
          </h2>
          <p>
            By establishing an active business profile or deploying our proprietary system hardware sync modules at your carwash facility, you explicitly agree to comply with these terms. This agreement establishes a binding software-as-a-service operational framework between your washing business entity and Apex Glow.
          </p>
        </section>

        <section className="space-y-3">
          <h2 className="text-lg font-bold text-slate-900 dark:text-white tracking-tight">
            2. Account Safeguards and Staff Controls
          </h2>
          <p>
            You are exclusively responsible for safeguarding portal login permissions distributed to your facility managers, lane attendants, and office bookkeeping personnel. Apex Glow is not liable for data adjustments, ticket voiding errors, or commission profile manipulation stemming from compromised or shared access vectors.
          </p>
        </section>

        <section className="space-y-3">
          <h2 className="text-lg font-bold text-slate-900 dark:text-white tracking-tight">
            3. Automated Billing and Overages
          </h2>
          <p>
            Subscription profiles are evaluated monthly matching your chosen package caps (such as lane count limits, staff profiles, or reporting depth). If transaction logs exceed your chosen plan limits over a running cycle, the system will apply overage parameters or prompt an automatic system tier adjustment update.
          </p>
        </section>

        <section className="space-y-3">
          <h2 className="text-lg font-bold text-slate-900 dark:text-white tracking-tight">
            4. Limitation of Liability & Local Sensors
          </h2>
          <p>
            Apex Glow maps digital metrics streaming via local hardware arrays but is not liable for data reporting delays due to third-party network grid drops, localized power system blackout outages, or faulty physical valve sensor installations.
          </p>
        </section>

      </div>
    </div>
  );
}

export default Terms;
