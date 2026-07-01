import React from 'react';
import { NavLink } from 'react-router-dom';
import { ArrowUpRight } from 'lucide-react';
import { FaFacebook, FaTwitter, FaInstagram, FaLinkedin } from 'react-icons/fa';

function Footer() {
  const currentYear = new Date().getFullYear();

  const footerSections = [
    {
      title: "Product",
      links: [
        { label: "Features", path: "/#features" },
        { label: "Packages", path: "/packages" },
        { label: "How It Works", path: "/how" },
        { label: "Services", path: "/services" }
      ]
    },
    {
      title: "Company",
      links: [
        { label: "About Us", path: "/about" },
        { label: "Contact", path: "/contact" },
        { label: "Careers", path: "/careers" },
        { label: "Press Kit", path: "/press" }
      ]
    },
    {
      title: "Legal",
      links: [
        { label: "Privacy Policy", path: "/privacy" },
        { label: "Terms of Service", path: "/terms" },
        { label: "SLA Agreement", path: "/sla" },
        { label: "Security Profile", path: "/security" }
      ]
    }
  ];

  return (
    <footer className="w-full border-t border-blue-100/60 dark:border-slate-900 bg-white/50 dark:bg-slate-950/50 backdrop-blur-sm pt-16 pb-8 transition-colors duration-300">
      <div className="max-w-7xl mx-auto px-6 lg:px-8">

        {/* Top Section */}
        <div className="grid grid-cols-1 md:grid-cols-12 gap-10 md:gap-8 pb-12 border-b border-slate-200/60 dark:border-slate-900">

          {/* Brand */}
          <div className="md:col-span-4 space-y-4">
            <NavLink to="/" className="text-2xl font-black tracking-tight text-slate-900 dark:text-white">
              Apex<span className="text-blue-600 dark:text-cyan-400">Glow</span>
            </NavLink>

            <p className="text-sm text-slate-500 dark:text-slate-400 max-w-sm font-medium leading-relaxed">
              The high-performance cloud operating system engineered to automate bookings, maximize chemical efficiency, and scale commercial car washes across Africa.
            </p>

            {/* Social Icons */}
            <div className="flex items-center gap-4 text-slate-400 dark:text-slate-500">
              <a href="#" className="hover:text-blue-600 dark:hover:text-cyan-400 transition-colors">
                <FaFacebook size={18} />
              </a>
              <a href="#" className="hover:text-blue-600 dark:hover:text-cyan-400 transition-colors">
                <FaTwitter size={18} />
              </a>
              <a href="#" className="hover:text-blue-600 dark:hover:text-cyan-400 transition-colors">
                <FaInstagram size={18} />
              </a>
              <a href="#" className="hover:text-blue-600 dark:hover:text-cyan-400 transition-colors">
                <FaLinkedin size={18} />
              </a>
            </div>
          </div>

          {/* Links Grid */}
          <div className="md:col-span-8 grid grid-cols-2 sm:grid-cols-3 gap-8">
            {footerSections.map((section, index) => (
              <div key={index} className="space-y-4">
                <h4 className="text-xs font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500">
                  {section.title}
                </h4>

                <ul className="space-y-2.5">
                  {section.links.map((link, i) => (
                    <li key={i}>
                      <NavLink
                        to={link.path}
                        className="inline-flex items-center gap-0.5 text-sm font-medium text-slate-500 dark:text-slate-400 hover:text-blue-600 dark:hover:text-cyan-400 transition-colors group"
                      >
                        <span>{link.label}</span>

                        {link.path.startsWith('http') && (
                          <ArrowUpRight
                            size={12}
                            className="opacity-0 group-hover:opacity-100 transition-opacity"
                          />
                        )}
                      </NavLink>
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>

        </div>

        {/* Bottom Section */}
        <div className="flex flex-col sm:flex-row items-center justify-between gap-4 pt-8 text-xs font-semibold text-slate-400 dark:text-slate-500">
          <p>© {currentYear} Apex Glow Ltd. All rights reserved.</p>
          <div className="flex items-center gap-6">
            <span>Built proudly in Nairobi, Kenya</span>
          </div>
        </div>

      </div>
    </footer>
  );
}

export default Footer;