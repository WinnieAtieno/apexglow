import React, { useState } from 'react';
import { MapPin, Clock, ArrowRight, Briefcase, Sparkles, Building } from 'lucide-react';

function Careers() {
  const [activeDepartment, setActiveDepartment] = useState('All');

  const departments = ['All', 'Engineering', 'Sales & Growth', 'Operations'];

  const openings = [
    { 
      title: "Senior Full-Stack Engineer", 
      dept: "Engineering", 
      location: "Nairobi, Kenya (Hybrid)", 
      type: "Full-Time",
      description: "Scale our real-time synchronization engine processing hardware POS logs and M-Pesa business ledger endpoints."
    },
    { 
      title: "IoT Systems Specialist", 
      dept: "Engineering", 
      location: "Nairobi, Kenya (On-Site)", 
      type: "Full-Time", 
      description: "Deploy and optimize ultrasonic fluid level sensors and digital flow hardware integrated with client chemical systems."
    },
    { 
      title: "B2B SaaS Account Executive", 
      dept: "Sales & Growth", 
      location: "Remote (East Africa)", 
      type: "Full-Time",
      description: "Drive multi-site platform adoption among regional conveyor tunnel networks, auto detailing franchises, and commercial fleets."
    },
    { 
      title: "Technical Support Engineer", 
      dept: "Operations", 
      location: "Nairobi, Kenya (Shift)", 
      type: "Full-Time",
      description: "Provide tier-1 hardware diagnostic support and configuration assistance to car wash owner-operators on the ground."
    }
  ];

  
  const filteredOpenings = activeDepartment === 'All' 
    ? openings 
    : openings.filter(job => job.dept === activeDepartment);

  return (
    <div className="max-w-7xl mx-auto px-6 lg:px-8 py-12 transition-colors duration-300">
      
      {/* 1. EDITORIAL HEADER */}
      <div className="text-center max-w-3xl mx-auto mb-16 space-y-4">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-50 dark:bg-slate-900 border border-blue-100 dark:border-slate-800 text-xs font-bold text-blue-700 dark:text-cyan-400 transition-colors">
          <Sparkles className="w-3.5 h-3.5" />
          <span>We're Hiring</span>
        </div>
        <h1 className="text-4xl font-black tracking-tight text-slate-900 dark:text-white transition-colors">
          Build the Future of Wash Tech
        </h1>
        <p className="text-base sm:text-lg text-slate-500 dark:text-slate-400 font-medium transition-colors">
          Join a high-intensity team transforming brick-and-mortar automotive workflows into smart, autonomous cloud-tracked enterprises across East Africa.
        </p>
      </div>

      {/* 2. LIVE DEPARTMENT FILTER TABS */}
      <div className="flex flex-wrap justify-center items-center gap-2 mb-12 max-w-xl mx-auto">
        {departments.map((dept) => (
          <button
            key={dept}
            onClick={() => setActiveDepartment(dept)}
            className={`px-4 py-2 rounded-xl text-xs font-bold transition-all border ${
              activeDepartment === dept
                ? "bg-blue-600 border-blue-600 dark:bg-cyan-400 dark:border-cyan-400 text-white dark:text-slate-950 shadow-md"
                : "bg-white dark:bg-slate-900 border-slate-200 dark:border-slate-800 text-slate-600 dark:text-slate-400 hover:border-slate-300 dark:hover:border-slate-700"
            }`}
          >
            {dept}
          </button>
        ))}
      </div>

      
      <div className="max-w-4xl mx-auto space-y-4">
        <div className="flex items-center justify-between border-b border-slate-200/60 dark:border-slate-900 pb-4 mb-6">
          <h2 className="text-xl font-bold text-slate-900 dark:text-white tracking-tight flex items-center gap-2">
            <Briefcase size={18} className="text-blue-600 dark:text-cyan-400" />
            Openings ({filteredOpenings.length})
          </h2>
          <span className="text-xs font-bold text-slate-400 uppercase tracking-wider">Nairobi Hub</span>
        </div>

        {filteredOpenings.length === 0 ? (
          <div className="text-center py-12 bg-white dark:bg-slate-900 border border-slate-200/60 dark:border-slate-800 rounded-3xl p-8 shadow-sm">
            <Building className="mx-auto text-slate-300 dark:text-slate-700 mb-3" size={32} />
            <p className="text-sm font-semibold text-slate-400">No active postings right now for this track.</p>
          </div>
        ) : (
          filteredOpenings.map((job, index) => (
            <div 
              key={index}
              className="group flex flex-col md:flex-row md:items-center justify-between gap-6 p-6 bg-white dark:bg-slate-900 border border-slate-200/60 dark:border-slate-800 rounded-2xl shadow-sm hover:border-blue-200 dark:hover:border-slate-700 hover:shadow-md dark:shadow-none transition-all duration-300"
            >
              {/* Job Summary Description Left info block */}
              <div className="space-y-2 max-w-xl">
                <span className="inline-block text-[10px] font-black uppercase tracking-wider text-blue-600 dark:text-cyan-400">
                  {job.dept}
                </span>
                <h3 className="text-lg font-bold text-slate-900 dark:text-white group-hover:text-blue-600 dark:group-hover:text-cyan-300 transition-colors tracking-tight">
                  {job.title}
                </h3>
                <p className="text-xs sm:text-sm text-slate-500 dark:text-slate-400 leading-relaxed font-medium transition-colors">
                  {job.description}
                </p>
                <div className="flex flex-wrap gap-x-4 gap-y-1 text-xs font-bold text-slate-400 pt-1">
                  <span className="flex items-center gap-1"><MapPin size={14} className="text-slate-300 dark:text-slate-600" /> {job.location}</span>
                  <span className="flex items-center gap-1"><Clock size={14} className="text-slate-300 dark:text-slate-600" /> {job.type}</span>
                </div>
              </div>
              
              
              <button className="inline-flex items-center justify-center gap-1.5 self-start md:self-center bg-slate-50 hover:bg-blue-50 dark:bg-slate-950 dark:hover:bg-slate-850 text-slate-800 dark:text-slate-200 group-hover:text-blue-600 dark:group-hover:text-cyan-400 border border-slate-200 dark:border-slate-800 font-bold px-4 py-3 rounded-xl text-sm transition-all shadow-sm shrink-0">
                Apply for Role 
                <ArrowRight size={14} className="transition-transform group-hover:translate-x-0.5" />
              </button>
            </div>
          ))
        )}
      </div>

    </div>
  );
}

export default Careers;
