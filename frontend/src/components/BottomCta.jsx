import React from 'react';
import { ArrowRight } from 'lucide-react';

function BottomCta() {
  return (
    <section className="max-w-7xl mx-auto px-6 lg:px-8 py-12 md:py-16">
      <div className="relative rounded-3xl overflow-hidden bg-gradient-to-r from-blue-600 to-blue-800 dark:from-slate-900 dark:to-slate-950 border border-transparent dark:border-slate-800 text-white p-8 sm:p-12 text-center space-y-6 shadow-2xl">
        <div className="absolute top-0 right-0 w-64 h-64 bg-white/5 dark:bg-cyan-500/5 rounded-full blur-3xl pointer-events-none" />
        <h2 className="text-3xl sm:text-4xl font-black max-w-2xl mx-auto leading-tight">Ready to completely automate your wash operations?</h2>
        <p className="text-blue-100 dark:text-slate-400 max-w-lg mx-auto text-sm sm:text-base font-medium">Join the forward-thinking operators running smart, leak-proof tunnels and bay businesses with Apex Glow.</p>
        <div className="pt-2">
          <button className="w-full sm:w-auto inline-flex items-center justify-center gap-2 bg-white dark:bg-gradient-to-r dark:from-cyan-500 dark:to-teal-500 text-blue-700 dark:text-slate-950 font-black px-8 py-4 rounded-xl shadow-lg transition-transform hover:-translate-y-0.5">
            Start Your 14-Day Free Trial <ArrowRight size={16} />
          </button>
        </div>
        <p className="text-xs text-blue-200/80 dark:text-slate-500 font-semibold">Setup takes 10 minutes • Cancel anytime • No contract required</p>
      </div>
    </section>
  );
}

export default BottomCta;
