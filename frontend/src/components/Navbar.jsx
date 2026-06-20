import React, { useState } from "react";
import { NavLink } from "react-router-dom";
import { Phone } from "lucide-react";

const NAV_LINKS = [
  { path: "/", label: "Home" },
  { path: "/packages", label: "Packages" },
  { path: "/how", label: "How It Works" },
  { path: "/services", label: "Services" },
  { path: "/contact", label: "Contact" },
  { path: "/login", label: "Login" },
];

function Navbar() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => setIsMenuOpen((prev) => !prev);
  const closeMenu = () => setIsMenuOpen(false);

  const getNavLinkClass = ({ isActive }) =>
    `relative py-2 text-sm font-medium transition-colors duration-200 after:absolute after:bottom-0 after:left-0 after:h-[2px] after:w-full after:scale-x-0 after:bg-blue-600 after:transition-transform after:duration-200 hover:text-blue-600 ${
      isActive ? "text-blue-600 after:scale-x-100" : "text-gray-600"
    }`;

  const getMobileLinkClass = ({ isActive }) =>
    `block rounded-lg px-4 py-3 text-sm font-medium transition-colors ${
      isActive
        ? "bg-blue-50 text-blue-600"
        : "text-gray-700 hover:bg-gray-50 hover:text-blue-600"
    }`;

  return (
    <nav className="fixed top-0 left-0 z-50 w-full border-b border-slate-100 bg-white/90 backdrop-blur-md">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-4">
        {/* Logo */}
        <NavLink
          to="/"
          onClick={closeMenu}
          className="rounded text-2xl font-black tracking-tight text-slate-900 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-600"
        >
          Apex<span className="text-sky-500">Glow</span>
        </NavLink>

        {/* Desktop Navigation */}
        <ul className="hidden items-center gap-8 md:flex">
          {NAV_LINKS.map((link) => (
            <li key={link.path}>
              <NavLink to={link.path} className={getNavLinkClass}>
                {link.label}
              </NavLink>
            </li>
          ))}
        </ul>

        {/* Desktop CTA */}
        <div className="hidden items-center gap-6 md:flex">
          <a
            href="tel:+254700000000"
            className="flex items-center gap-2 text-sm font-medium text-gray-600 transition-colors hover:text-blue-600 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-600 rounded"
          >
            <Phone size={16} className="text-sky-500" />
            <span>+254 700 000 000</span>
          </a>

          <button className="rounded-xl bg-blue-600 px-5 py-2.5 text-sm font-semibold text-white shadow-lg shadow-blue-500/20 transition-all duration-200 hover:-translate-y-0.5 hover:bg-blue-500 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-600">
            Book a Wash
          </button>
        </div>

        {/* Mobile Menu Button */}
        <button
          onClick={toggleMenu}
          className="flex h-10 w-10 items-center justify-center rounded-lg border border-gray-200 transition-colors hover:bg-gray-50 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-600 md:hidden"
          aria-expanded={isMenuOpen}
          aria-label={isMenuOpen ? "Close menu" : "Open menu"}
        >
          <svg
            className="h-5 w-5 text-gray-700"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            {isMenuOpen ? (
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M6 18L18 6M6 6l12 12"
              />
            ) : (
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M4 6h16M4 12h16M4 18h16"
              />
            )}
          </svg>
        </button>
      </div>

      {/* Mobile Navigation */}
      <div
        className={`grid transition-all duration-300 ease-in-out md:hidden ${
          isMenuOpen
            ? "grid-rows-[1fr] border-t border-slate-100 opacity-100"
            : "pointer-events-none grid-rows-[0fr] opacity-0"
        }`}
      >
        <div className="overflow-hidden bg-white">
          <ul className="flex flex-col gap-1 p-4">
            {NAV_LINKS.map((link) => (
              <li key={link.path}>
                <NavLink
                  to={link.path}
                  onClick={closeMenu}
                  className={getMobileLinkClass}
                >
                  {link.label}
                </NavLink>
              </li>
            ))}
          </ul>

          <div className="flex flex-col gap-4 px-4 pb-6">
            <a
              href="tel:+254700000000"
              className="flex items-center justify-center gap-2 py-2 text-sm font-medium text-gray-600"
            >
              <Phone size={18} className="text-sky-500" />
              <span>+254 700 000 000</span>
            </a>

            <button className="w-full rounded-xl bg-blue-600 py-3 font-semibold text-white shadow-lg shadow-blue-500/20 transition-all hover:bg-blue-500 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-600">
              Book a Wash
            </button>
          </div>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;