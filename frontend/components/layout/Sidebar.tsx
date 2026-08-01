"use client";

import Link from "next/link";
import {
  LayoutDashboard,
  GraduationCap,
  Users,
  UserSquare2,
  CalendarCheck,
  CreditCard,
  FileBarChart,
  Settings,
} from "lucide-react";

const menuItems = [
  {
    name: "Dashboard",
    href: "/dashboard",
    icon: LayoutDashboard,
  },
  {
    name: "Students",
    href: "/dashboard/students",
    icon: GraduationCap,
  },
  {
    name: "Parents",
    href: "#",
    icon: Users,
  },
  {
    name: "Teachers",
    href: "#",
    icon: UserSquare2,
  },
  {
    name: "Attendance",
    href: "#",
    icon: CalendarCheck,
  },
  {
    name: "Finance",
    href: "#",
    icon: CreditCard,
  },
  {
    name: "Reports",
    href: "#",
    icon: FileBarChart,
  },
  {
    name: "Settings",
    href: "#",
    icon: Settings,
  },
];

export default function Sidebar() {
  return (
    <aside className="w-64 min-h-screen border-r bg-white">
      <div className="p-6">
        <h1 className="text-2xl font-bold">
          Casppa
        </h1>
      </div>

      <nav className="space-y-2 px-4">
        {menuItems.map((item) => {
          const Icon = item.icon;

          return (
            <Link
              key={item.name}
              href={item.href}
              className={`flex items-center gap-3 rounded-lg px-4 py-3 transition
              ${
                item.name === "Students"
                  ? "bg-blue-600 text-white"
                  : "hover:bg-gray-100"
              }`}
            >
              <Icon size={20} />

              <span>{item.name}</span>
            </Link>
          );
        })}
      </nav>
    </aside>
  );
}