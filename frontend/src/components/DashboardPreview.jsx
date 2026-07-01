import React, { useState, useEffect } from "react";
import Chart from "react-apexcharts";

function DashboardPreview() {
  const [revenue, setRevenue] = useState(48500);
  const [activeWashes, setActiveWashes] = useState(32);
  const [chartData, setChartData] = useState([45, 52, 49, 62, 58, 75, 68, 82, 79, 94]);

  const [staff, setStaff] = useState([
    { id: 1, name: "Otieno J.", role: "Lead Detailer", bay: "Bay 01", status: "Occupied", commission: 3600 },
    { id: 2, name: "Mwangi K.", role: "Bay Operator", bay: "Bay 02", status: "Occupied", commission: 2400 },
    { id: 3, name: "Achieng M.", role: "Detailer", bay: "Manual 03", status: "Standby", commission: 1800 },
    { id: 4, name: "Wanjiku N.", role: "Supervisor", bay: "All Zones", status: "Active", commission: 4500 }
  ]);

  const [logs, setLogs] = useState([
    { id: 1, text: "Job #2213 executed successfully (Bay 01)", value: "KES 1,200", type: "success" },
    { id: 2, text: "M-Pesa C2B Sync Ref: T6G9029X1", value: "Settled", type: "mpesa" },
    { id: 3, text: "Commission payout processed", value: "+KES 180", type: "staff" }
  ]);

  // REALISTIC BUSINESS SIMULATION LOOP
  useEffect(() => {
    const interval = setInterval(() => {

      const ticketTiers = [600, 1200, 2500];
      const randomTicket = ticketTiers[Math.floor(Math.random() * ticketTiers.length)];
      const staffIndex = Math.floor(Math.random() * 3);
      const commission = Math.round(randomTicket * 0.15);

      setRevenue(prev => prev + randomTicket);

      setStaff(prev =>
        prev.map((emp, index) => {
          if (index === staffIndex) {
            return {
              ...emp,
              commission: emp.commission + commission,
              status: "Occupied"
            };
          }
          return emp;
        })
      );

      setChartData(prev => {
        const updated = [...prev.slice(1)];
        const last = prev[prev.length - 1];
        const next = Math.max(30, Math.min(140, last + (Math.random() * 20 - 10)));
        updated.push(Math.round(next));
        return updated;
      });

      const mockRef = `T${Math.floor(Math.random() * 999999)}X`;

      setLogs([
        {
          id: Date.now(),
          text: `Job completed (Bay ${staffIndex + 1})`,
          value: `KES ${randomTicket}`,
          type: "success"
        },
        {
          id: Date.now() + 1,
          text: `M-Pesa Sync Ref: ${mockRef}`,
          value: "Settled",
          type: "mpesa"
        },
        {
          id: Date.now() + 2,
          text: `Commission payout processed`,
          value: `+KES ${commission}`,
          type: "staff"
        }
      ]);

      setActiveWashes(prev => prev + (Math.random() > 0.4 ? 1 : 0));

    }, 5000);

    return () => clearInterval(interval);
  }, []);

  const chartOptions = {
    chart: {
      type: "area",
      sparkline: { enabled: true }
    },
    stroke: { curve: "smooth", width: 2 },
    colors: ["#2563eb"],
    fill: { opacity: 0.2 },
    tooltip: { enabled: true }
  };

  const chartSeries = [{ name: "Revenue", data: chartData }];

  return (
    <div className="relative w-full max-w-5xl mx-auto p-4 space-y-4">

      {/* HEADER */}
      <div className="p-4 rounded-xl border bg-white dark:bg-slate-950">
        <p className="text-xs font-bold uppercase text-slate-400">
          WashPro Enterprise Dashboard
        </p>

        <div className="grid grid-cols-3 gap-3 mt-4">
          <div className="p-3 rounded-lg bg-slate-50 dark:bg-slate-900">
            <p className="text-xs text-slate-400">Revenue</p>
            <p className="font-bold">KES {revenue.toLocaleString()}</p>
          </div>

          <div className="p-3 rounded-lg bg-slate-50 dark:bg-slate-900">
            <p className="text-xs text-slate-400">Active Washes</p>
            <p className="font-bold">{activeWashes}</p>
          </div>

          <div className="p-3 rounded-lg bg-slate-50 dark:bg-slate-900">
            <p className="text-xs text-slate-400">Efficiency</p>
            <p className="font-bold">88%</p>
          </div>
        </div>
      </div>

      {/* CHART */}
      <div className="p-4 rounded-xl border bg-white dark:bg-slate-950">
        <Chart options={chartOptions} series={chartSeries} type="area" height={160} />
      </div>

      {/* LOGS */}
      <div className="p-4 rounded-xl border bg-white dark:bg-slate-950 space-y-2">
        <p className="text-xs font-bold text-slate-400 uppercase">
          Live Activity Feed
        </p>

        {logs.map(log => (
          <div key={log.id} className="flex justify-between text-xs border-b pb-1 last:border-0">
            <span>{log.text}</span>
            <span className="font-bold">{log.value}</span>
          </div>
        ))}
      </div>

    </div>
  );
}

export default DashboardPreview;