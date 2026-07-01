import React from 'react';
import { NavLink } from 'react-router-dom';
import { Home, Compass, RotateCcw, Droplets } from 'lucide-react';

function NotFound() {
  return (
    <div className="min-h-[75vh] flex flex-col items-center justify-center text-center px-6 relative overflow-hidden pb-4">
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full max-w-md h-[350px] pointer-events-none opacity-30 dark:opacity-10 bg-gradient-to-tr from-blue-500 via-sky-400 to-indigo-600 blur-[120px] z-0" />
        <div className="relative z-10 space-y-6 max-w-md">  

    
        <div className="relative w-24 h-24 mx-auto flex items-center justify-center bg-white dark:bg-slate-900 border border-slate-200/80 dark:border-slate-800 rounded-3xl shadow-xl">
          <Compass size={40} className="text-blue-600 dark:text-cyan-400 animate-spin [animation-duration:10s]" />
          <Droplets size={20} className="text-sky-400 absolute top-4 right-4 animate-bounce" />
        </div>

        {/* Huge Error Tag */}
        <div className="space-y-2">
          <span className="text-xs font-black uppercase tracking-widest text-blue-600 dark:text-cyan-400 bg-blue-50 dark:bg-slate-900 px-3 py-1 rounded-full border border-blue-100 dark:border-slate-800">
            Error 404
          </span>
          <h1 className="text-3xl sm:text-4xl font-black tracking-tight text-slate-900 dark:text-white mt-4">
            This Lane is Blocked
          </h1>
          <p className="text-sm font-medium text-slate-500 dark:text-slate-400 max-w-sm mx-auto leading-relaxed">
            The page path you are trying to access has drifted off-grid or doesn't exist. Let's redirect you back to active operations.
          </p>
        </div>

        {/* Navigation Control Buttons */}
        <div className="flex flex-col sm:flex-row items-center justify-center gap-3 pt-4">
          <NavLink 
            to="/"
            className="w-full sm:w-auto inline-flex items-center justify-center gap-2 bg-blue-600 dark:bg-gradient-to-r dark:from-cyan-500 dark:to-teal-500 text-white dark:text-slate-950 font-black px-6 py-3.5 rounded-xl text-sm shadow-md transition-all duration-200 hover:-translate-y-0.5"
          >
            <Home size={16} />
            Return to Dashboard Home
          </NavLink>
          
          <button 
            onClick={() => window.history.back()}
            className="w-full sm:w-auto inline-flex items-center justify-center gap-2 bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-800 font-bold px-6 py-3.5 rounded-xl text-sm transition-all shadow-sm"
          >
            <RotateCcw size={16} />
            Go Back
          </button>
        </div>

      </div>
    </div>
  );
}

export default NotFound;
