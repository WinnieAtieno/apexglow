import React from 'react';

function TrustMarquee() {
  // Mock image/logo data array for scalability
  const partnerLogos = [
    { name: 'AERO-WASH', label: 'Aero Wash' },
    { name: 'SPARKLE_X', label: 'Sparkle X' },
    { name: 'TUNNEL_PRO', label: 'Tunnel Pro' },
    { name: 'GLOW_DETAILING', label: 'Glow Detailing' },
  ];

  return (
    <section className="relative z-10 w-full border-y border-slate-200/60 dark:border-slate-800/60 bg-gradient-to-b from-slate-50/50 to-white/50 dark:from-slate-950/20 dark:to-slate-900/10 backdrop-blur-md py-10 transition-colors duration-300">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
              
        <div className="relative w-full overflow-hidden [mask-image:linear-gradient(to_right,transparent,white_20%,white_80%,transparent)]">
          
       
          <div className="flex w-max gap-16 animate-marquee py-2">
            
           
            {partnerLogos.concat(partnerLogos).map((logo, index) => (
              <div 
                key={`${logo.name}-${index}`} 
                className="flex items-center gap-3 grayscale opacity-60 hover:grayscale-0 hover:opacity-100 transition-all duration-300 group cursor-pointer"
              >
              
                <div className="h-9 w-9 rounded-xl bg-gradient-to-br from-slate-100 to-slate-200/60 dark:from-slate-800 dark:to-slate-900/60 flex items-center justify-center border border-slate-200 dark:border-slate-800 shadow-sm group-hover:scale-105 group-hover:border-blue-500/30 dark:group-hover:border-blue-400/30 transition-transform">
                  <span className="text-xs font-black tracking-tighter text-slate-700 dark:text-slate-300">
                    {logo.name.charAt(0)}
                  </span>
                </div>
                
                <span className="text-sm font-bold tracking-wider text-slate-600 dark:text-slate-400 group-hover:text-slate-900 dark:group-hover:text-white transition-colors">
                  {logo.label}
                </span>
              </div>
            ))}

          </div>
        </div>

      </div>
    </section>
  );
}

export default TrustMarquee;
