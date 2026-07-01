import React from 'react';
import { ShieldCheck, Lock, Eye, Database, HelpCircle } from 'lucide-react';

function PrivacyPolicy() {
  const safetyPoints = [
    {
      icon: <Lock className="w-5 h-5 text-blue-600 dark:text-cyan-400" />,
      title: "Data Encryption",
      desc: "All operational telemetry, financial variables, and point-of-sale logs are encrypted at rest and in transit using AES-256 protocols."
    },
    {
      icon: <Database className="w-5 h-5 text-indigo-600 dark:text-purple-400" />,
      title: "Isolated Tenant Storage",
      desc: "Your carwash transaction counts, staff commission profiles, and chemical volume metrics are housed inside secure, separated multi-tenant silos."
    },
    {
      icon: <Eye className="w-5 h-5 text-sky-600 dark:text-teal-400" />,
      title: "Zero Third-Party Sharing",
      desc: "We do not sell, rent, or lease your wash counts, customer volumes, or business revenue statistics to any external marketing entities."
    }
  ];

  return (
    <div className="max-w-4xl mx-auto px-6 py-12 transition-colors duration-300">
      
      {/* Editorial Header */}
      <div className="flex items-center gap-3 border-b border-slate-200 dark:border-slate-800 pb-6 mb-10">
        <div className="p-3 bg-blue-50 text-blue-600 dark:bg-slate-900 dark:text-cyan-400 rounded-2xl border border-blue-100 dark:border-slate-800">
          <ShieldCheck size={24} />
        </div>
        <div>
          <h1 className="text-3xl font-black text-slate-900 dark:text-white tracking-tight">Privacy Policy</h1>
          <p className="text-xs font-bold text-slate-400 dark:text-slate-500 mt-1 uppercase tracking-wider">Last Updated: June 2026</p>
        </div>
      </div>

      {/* Safety Icons Summary Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
        {safetyPoints.map((point, idx) => (
          <div key={idx} className="p-5 bg-white dark:bg-slate-900 border border-slate-150 dark:border-slate-800/80 rounded-2xl shadow-sm space-y-2">
            <div className="p-2 bg-slate-50 dark:bg-slate-950 w-fit rounded-xl border border-slate-100 dark:border-slate-850">{point.icon}</div>
            <h3 className="font-bold text-sm text-slate-900 dark:text-white tracking-tight">{point.title}</h3>
            <p className="text-xs text-slate-500 dark:text-slate-400 leading-relaxed font-medium">{point.desc}</p>
          </div>
        ))}
      </div>

      {/* Structured Legal Copy Blocks */}
      <div className="space-y-8 text-sm sm:text-base text-slate-600 dark:text-slate-400 font-medium leading-relaxed">
        
        <section className="space-y-3">
          <h2 className="text-lg font-bold text-slate-900 dark:text-white tracking-tight flex items-center gap-2">
            1. Information We Collect
          </h2>
          <p>
            Apex Glow collects operational tracking metrics submitted explicitly by your authorized company personnel or transmitted securely from your physical facility terminal setups. This includes point-of-sale logs, automated water-to-soap flow levels from digital tank gauges, active lane availability, and staff commission configuration parameters.
          </p>
        </section>

        <section className="space-y-3">
          <h2 className="text-lg font-bold text-slate-900 dark:text-white tracking-tight flex items-center gap-2">
            2. How Your Station Telemetry is Utilized
          </h2>
          <p>
            The dashboard analytics data collected is used exclusively to generate real-time performance visualization graphs, trigger automated low-stock SMS notifications to your inventory managers, calculate accurate staff tip metrics, and enforce platform network safety controls.
          </p>
        </section>

        <section className="space-y-3">
          <h2 className="text-lg font-bold text-slate-900 dark:text-white tracking-tight flex items-center gap-2">
            3. Data Retention & Hardware Access Tunnels
          </h2>
          <p>
            We retain platform log fields for the duration of your service subscription to enable historical reporting charts. All hardware data pipelines mapping from your bay terminals run inside end-to-end encrypted tunnels to block external traffic injection or information harvesting.
          </p>
        </section>

        <section className="space-y-3">
          <h2 className="text-lg font-bold text-slate-900 dark:text-white tracking-tight flex items-center gap-2">
            4. Contact Security Operations
          </h2>
          <p>
            If you have structural concerns regarding isolated system data storage tiers, multi-site node profiles, or want to trigger account records deletion paths, reach out directly via <span className="text-blue-600 dark:text-cyan-400 font-bold">privacy@apexglow.com</span>.
          </p>
        </section>

      </div>
    </div>
  );
}

export default PrivacyPolicy;
