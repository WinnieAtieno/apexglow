import React, { useState } from 'react';
import { ChevronDown, HelpCircle } from 'lucide-react';

function FaqAccordion() {
  const [openIndex, setOpenIndex] = useState(null);

  const faqs = [
    { q: "Does Apex Glow work with my existing POS terminals?", a: "Yes. Apex Glow integrates with standard local hardware terminals, M-Pesa business tills, and conveyor tunnel controllers via our secure integration hub." },
    { q: "How does the live chemical tracking work?", a: "We sync up with standard digital flow sensors placed on your soap, wax, and ceramic tanks to read flow volumes and trigger automatic warning texts when inventory drops below 22%." },
    { q: "Can I manage multiple car wash locations with one account?", a: "Absolutely. Our Multi-Site portal allows franchise owners to toggle between different regional branches, compare daily throughput counts, and view unified revenue reports." },
    { q: "Is there a long-term contract requirement?", a: "No. Apex Glow is a monthly pay-as-you-go SaaS product. You can scale your tier up, down, or cancel your subscription at any point with no penalties." }
  ];

  return (
    <section className="relative z-10 max-w-4xl mx-auto px-6 py-16 border-t border-blue-100/60 dark:border-slate-900 transition-colors">
      <div className="text-center mb-12 space-y-2">
        <h2 className="text-3xl font-black tracking-tight">Got Questions?</h2>
        <p className="text-sm font-medium text-slate-500 dark:text-slate-400">Everything you need to know about setting up Apex Glow at your station.</p>
      </div>

      <div className="space-y-4">
        {faqs.map((faq, index) => (
          <div 
            key={index} 
            className="rounded-2xl border border-slate-200/60 dark:border-slate-800 bg-white dark:bg-slate-900 overflow-hidden transition-all shadow-sm"
          >
            <button 
              onClick={() => setOpenIndex(openIndex === index ? null : index)}
              className="w-full flex items-center justify-between p-5 text-left font-bold text-slate-900 dark:text-white focus:outline-none"
            >
              <span className="flex items-center gap-3 text-sm sm:text-base">
                <HelpCircle size={18} className="text-blue-600 dark:text-cyan-400" />
                {faq.q}
              </span>
              <ChevronDown size={18} className={`text-slate-400 transition-transform duration-200 ${openIndex === index ? "rotate-180 text-blue-600 dark:text-cyan-400" : ""}`} />
            </button>
            <div className={`transition-all duration-300 ease-in-out overflow-hidden ${openIndex === index ? "max-h-40 border-t border-slate-100 dark:border-slate-800/50" : "max-h-0"}`}>
              <p className="p-5 text-sm text-slate-500 dark:text-slate-400 leading-relaxed font-medium bg-slate-50/50 dark:bg-slate-950/40">
                {faq.a}
              </p>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}

export default FaqAccordion;
