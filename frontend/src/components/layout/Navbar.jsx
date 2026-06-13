import React, { useState } from "react";
import { NavLink, Link } from "react-router-dom";

function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  const navLinkClass = ({ isActive }) =>
    `relative font-medium transition-all duration-300 pb-1 ${
      isActive
        ? "text-amber-400 after:absolute after:left-0 after:-bottom-1 after:h-0.5 after:w-full after:bg-amber-400"
        : "text-slate-300 hover:text-amber-400"
    }`;

  const links = [
    { path: "/", label: "Home" },
    { path: "/about", label: "About" },
 
  ];

  return (
    <nav className="fixed top-0 left-0 w-full z-50 bg-slate-950 backdrop-blur-lg border-b border-slate-800">
      <div className="max-w-7xl mx-auto px-4 md:px-8">
        <div className="flex items-center justify-between h-20">
          {/* Logo */}
          <NavLink to="/" className="flex items-center gap-3">
            <div className="h-10 w-10 rounded-xl bg-gradient-to-br from-amber-400 to-amber-600 flex items-center justify-center font-black text-slate-950">
              A
            </div>

            <div>
              <h1 className="font-black text-lg text-white">
                ApexGlow
              </h1>
              <p className="text-xs text-slate-400 -mt-1">
                Premium Wash
              </p>
            </div>
          </NavLink>

          {/* Desktop Navigation */}
          <div className="hidden md:flex items-center gap-8">
            {links.map((link) => (
              <NavLink
                key={link.path}
                to={link.path}
                className={navLinkClass}
              >
                {link.label}
              </NavLink>
            ))}
          </div>

          {/* Desktop CTA */}
          <div className="hidden md:flex items-center gap-4">
            <Link
              to="tel:+254700000000"
              className="text-slate-300 hover:text-white transition font-medium"
            >
              📞 Call Now
            </Link>

            <Link
              to="directions"
              target="_blank"
              rel="noreferrer"
              className="bg-amber-500 hover:bg-amber-600 text-slate-950 font-bold px-5 py-3 rounded-xl transition-all shadow-lg shadow-amber-500/20"
            >
              📍 Get Directions
            </Link>
          </div>

          {/* Mobile Menu Toggle */}
          <button
            onClick={() => setIsOpen(!isOpen)}
            className="md:hidden text-white text-2xl"
          >
            {isOpen ? "✕" : "☰"}
          </button>
        </div>

        {/* Mobile Navigation */}
        <div
          className={`md:hidden overflow-hidden transition-all duration-300 ${
            isOpen ? "max-h-96 py-6 border-t border-slate-800" : "max-h-0"
          }`}
        >
          <div className="flex flex-col gap-5">
            {links.map((link) => (
              <NavLink
                key={link.path}
                to={link.path}
                className={navLinkClass}
                onClick={() => setIsOpen(false)}
              >
                {link.label}
              </NavLink>
            ))}

            <div className="pt-4 border-t border-slate-800">
              <a
                href="tel:+254700000000"
                className="block text-slate-300 mb-4"
              >
                📞 Call Now
              </a>

              <a
                href="https://google.com"
                target="_blank"
                rel="noreferrer"
                className="block text-center bg-amber-500 hover:bg-amber-600 text-slate-950 font-bold py-3 rounded-xl transition"
              >
                📍 Get Directions
              </a>
            </div>
          </div>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;