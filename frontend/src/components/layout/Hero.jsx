import React from 'react'
import car from '../../assets/car.avif'

function Hero() {
  return (
    <>
    

<section class="relative bg-slate-950 text-white min-h-[85vh] flex items-center overflow-hidden">
  
 
  <div class="absolute inset-0 z-0">
    <div class="absolute inset-0 bg-gradient-to-r from-slate-950 via-slate-950/85 to-transparent z-10"></div>
    <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-transparent to-transparent z-10"></div>
   
    <img src={car}
         alt="Premium Car Wash Nairobi" 
         class="w-full h-full object-cover object-center opacity-40"/>
  </div>


  <div class="relative z-20 max-w-7xl mx-auto px-4 py-16 md:px-8 w-full">
    <div class="max-w-2xl">
      
    
      <div class="inline-flex items-center space-x-2 bg-amber-500/10 border border-amber-500/30 rounded-full px-3 py-1.5 text-xs text-amber-400 font-semibold mb-6 uppercase tracking-wider mt-5">
        <span class="flex h-2 w-2 rounded-full bg-amber-500 animate-ping"></span>
        <span>No Waiting Time Right Now • Drive Straight In</span>
      </div>


      <h1 class="text-3xl md:text-5xl font-black tracking-tight leading-tight mb-4 uppercase">
        Give Your Ride The <br/>
        <span class="text-transparent bg-clip-text bg-gradient-to-r from-amber-400 to-amber-600">Showroom Glow</span>
      </h1>

    
      <p class="text-slate-300 text-base md:text-lg mb-8 max-w-xl leading-relaxed">
        Nairobi’s premium drive in car wash and detailing hub. Wash away the city dust while you stream, work, or relax in our premium air conditioned lounge with high-speed Wi-Fi.
      </p>

     
      <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-4">
        
        <a href="https://google.com" target="_blank" class="bg-amber-500 hover:bg-amber-600 text-slate-950 font-extrabold text-center px-8 py-4 rounded-xl transition-all transform active:scale-98 shadow-xl shadow-amber-500/20 tracking-wide flex items-center justify-center space-x-2">
          <span>📍</span>
          <span>TAP FOR GOOGLE MAPS DIRECTIONS</span>
        </a>
        
       
        <a href="#services" class="bg-slate-900 hover:bg-slate-800 text-white border border-slate-700 text-center px-6 py-4 rounded-xl transition-colors font-bold tracking-wide flex items-center justify-center space-x-2">
          <span>💰</span>
          <span>VIEW PRICE MENU</span>
        </a>
      </div>

      {/* <!-- Micro-Trust Badges --> */}
      <div class="grid grid-cols-3 gap-4 mt-12 pt-8 border-t border-slate-800 text-xs text-slate-400 font-medium">
        <div class="flex items-center space-x-2">
          <span class="text-xl">⏱️</span>
          <span>15-Min Express Wash</span>
        </div>
        <div class="flex items-center space-x-2">
          <span class="text-xl">☕</span>
          <span>Free Lounge Cafe</span>
        </div>
        <div class="flex items-center space-x-2">
          <span class="text-xl">💳</span>
          <span>Lipa na M-PESA</span>
        </div>
      </div>

    </div>
  </div>
</section>

    </>
  )
}

export default Hero