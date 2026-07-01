import React from 'react';
import { ShieldCheck, Key, Lock, Radio, Server, Fingerprint } from 'lucide-react';

function SecurityProfile() {
  const protocols = [
    { icon: <Lock />, name: "AES-256 Cloud Encryption", desc: "All system databases, transaction logs, and operational telemetry variables are encrypted at rest and in flight." },
    { icon: <Key />, name: "Isolated Multi-Tenant Silos", desc: "Your car wash data is separated at the database architecture layer, ensuring completely private, leakage-free containment." },
    { icon: <Radio />, name: "Secure IoT Hardware Tunnels", desc: "Data streaming from physical chemical volume gauges and lane point-of-sale hardware runs inside end-to-end encrypted networks." },
    { icon: <Fingerprint />, name: "Granular Staff Access Logs", desc: "Track exactly which manager or detailer adjusted inventory counts, voided tickets, or claimed commission pools." }
  ];

  return (
    <div className="max-w-7xl mx-auto px-6 lg:px-8 py-12 transition-colors duration-300">
      
      {/* Core Profile Heading */}
      <div className="text-center max-w-3xl mx-auto mb-16 space-y-4">
        <div className="p-3 bg-blue-50 text-blue-600 dark:bg-slate-900 dark:text-cyan-400 rounded-2xl w-fit mx-auto border border-blue-100 dark:border-slate-800">
          <ShieldCheck size={28} />
        </div>
        <h1 className="text-4xl font-black tracking-tight text-slate-900 dark:text-white transition-colors">
          Trust & Security Profile
        </h1>
        <p className="text-lg text-slate-500 dark:text-slate-400 font-medium transition-colors">
          Enterprise-grade operational defenses built to safeguard point-of-sale data, telemetry arrays, and financial transactions.
        </p>
      </div>

      {/* Protocol Architecture Matrix */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl mx-auto">
        {protocols.map((proto, index) => (
          <div 
            key={index} 
            className="p-6 bg-white dark:bg-slate-900 border border-slate-100 dark:border-slate-800 rounded-3xl shadow-sm space-y-4"
          >
            <div className="p-3 bg-slate-50 dark:bg-slate-950 text-blue-600 dark:text-cyan-400 rounded-2xl w-fit border border-slate-150 dark:border-slate-850">
              {proto.icon}
            </div>
            <div className="space-y-1">
              <h3 className="text-lg font-bold text-slate-900 dark:text-white tracking-tight">{proto.name}</h3>
              <p className="text-sm text-slate-500 dark:text-slate-400 font-medium leading-relaxed">{proto.desc}</p>
            </div>
          </div>
        ))}
      </div>

    </div>
  );
}

export default SecurityProfile;
