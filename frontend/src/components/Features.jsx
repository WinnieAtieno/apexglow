import React from 'react';
import { Calendar, Users, Droplets, LineChart } from 'lucide-react';

function Features() {
  const featuresList = [
    {
      icon: <Calendar className="w-6 h-6 text-blue-600 dark:text-cyan-400" />,
      title: "Smart Lane Scheduling",
      description:
        "Reduce wait times and maximize vehicle capacity with intelligent booking and lane allocation."
    },
    {
      icon: <Users className="w-6 h-6 text-indigo-600 dark:text-purple-400" />,
      title: "Staff & Commission Tracking",
      description:
        "Automatically calculate commissions, monitor performance, and eliminate spreadsheet headaches."
    },
    {
      icon: <Droplets className="w-6 h-6 text-sky-600 dark:text-teal-400" />,
      title: "Live Chemical Analytics",
      description:
        "Track soaps, waxes, and coatings in real time with automated low-stock alerts."
    },
    {
      icon: <LineChart className="w-6 h-6 text-blue-700 dark:text-indigo-400" />,
      title: "Revenue & Multi-Location Reports",
      description:
        "Track revenue, memberships, and performance across every branch from one dashboard."
    }
  ];

  const painPoints = [
    {
      emoji: "💸",
      title: "Revenue Blind Spots",
      description:
        "Stop guessing how your business is performing. See revenue, bookings, and activity in real time."
    },
    {
      emoji: "🧴",
      title: "Inventory Shortages",
      description:
        "Prevent costly stock-outs and chemical waste with automated inventory monitoring."
    },
    {
      emoji: "👥",
      title: "Manual Staff Management",
      description:
        "Track staff performance and commissions automatically instead of relying on spreadsheets."
    }
  ];

  return (
    <>
      {/* Problems Section */}
      <section className="relative z-10 max-w-7xl mx-auto px-6 lg:px-8 py-8">
        <div className="text-center max-w-3xl mx-auto">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-50 dark:bg-slate-900 border border-blue-100 dark:border-slate-800 text-xs font-bold text-blue-700 dark:text-cyan-400">
            The Problems We Solve
          </div>

          <h2 className="mt-6 text-3xl sm:text-4xl md:text-5xl font-black tracking-tight text-slate-900 dark:text-white">
            Running a carwash shouldn't feel chaotic
          </h2>

          <p className="mt-5 text-base sm:text-lg text-slate-600 dark:text-slate-400 font-medium leading-relaxed">
            Most owners lose revenue visibility, waste chemicals, and spend hours
            managing staff manually. ApexGlow brings everything into one modern,
            real-time operating system.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-14">
          {painPoints.map((item, index) => (
            <div
              key={index}
              className="group rounded-2xl bg-white dark:bg-slate-900/40 border border-slate-200/60 dark:border-slate-800/80 p-6 shadow-sm hover:shadow-md transition-all duration-300 hover:-translate-y-1"
            >
              <div className="text-3xl mb-5">{item.emoji}</div>

              <h3 className="text-xl font-bold text-slate-900 dark:text-white mb-3">
                {item.title}
              </h3>

              <p className="text-sm leading-relaxed text-slate-500 dark:text-slate-400 font-medium">
                {item.description}
              </p>
            </div>
          ))}
        </div>
      </section>

      {/* Features Section */}
      <section className="relative z-10 max-w-7xl mx-auto px-6 lg:px-8 py-20 border-t border-blue-100/60 dark:border-slate-900 transition-colors duration-300">
        <div className="text-center max-w-3xl mx-auto mb-16">
          <h2 className="text-3xl sm:text-4xl font-black tracking-tight text-slate-900 dark:text-white">
            Built to increase profit, not paperwork
          </h2>

          <p className="mt-4 text-base sm:text-lg text-slate-500 dark:text-slate-400 font-medium">
            Every feature is designed to help carwash owners save time,
            reduce waste, and grow revenue.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {featuresList.map((item, index) => (
            <div
              key={index}
              className="group relative p-6 rounded-2xl bg-white dark:bg-slate-900/40 border border-slate-200/60 dark:border-slate-800/80 hover:border-blue-200 dark:hover:border-slate-700 transition-all duration-300 hover:-translate-y-1 shadow-sm hover:shadow-md dark:shadow-none"
            >
              <div className="w-10 h-10 rounded-xl bg-blue-50 dark:bg-slate-950 flex items-center justify-center border border-blue-100/40 dark:border-slate-800">
                {item.icon}
              </div>

              <div className="mt-6">
                <h3 className="text-lg font-bold text-slate-900 dark:text-white tracking-tight group-hover:text-blue-600 dark:group-hover:text-cyan-300 transition-colors">
                  {item.title}
                </h3>

                <p className="mt-2 text-sm text-slate-500 dark:text-slate-400 leading-relaxed font-medium">
                  {item.description}
                </p>
              </div>
            </div>
          ))}
        </div>
      </section>
    </>
  );
}

export default Features;