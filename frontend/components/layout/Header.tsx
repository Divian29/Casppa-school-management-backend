"use client";

import { Bell, Search, ChevronDown } from "lucide-react";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";
import { Input } from "@/components/ui/input";

export default function Header() {
  return (
    <header className="flex h-20 items-center justify-between border-b bg-white px-8">
      {/* Left */}
      <div>
        <h2 className="text-2xl font-bold text-gray-900">
          Students
        </h2>

        <p className="text-sm text-gray-500">
          Manage student onboarding and records
        </p>
      </div>

      {/* Right */}
      <div className="flex items-center gap-5">
        <div className="relative w-80">
          <Search
            className="absolute left-3 top-3 text-gray-400"
            size={18}
          />

          <Input
            placeholder="Search..."
            className="pl-10"
          />
        </div>

        <button className="rounded-full border p-2 hover:bg-gray-100">
          <Bell size={20} />
        </button>

        <div className="flex cursor-pointer items-center gap-3">
          <Avatar>
            <AvatarFallback>OI</AvatarFallback>
          </Avatar>

          <div>
            <p className="text-sm font-semibold">
              Olivia
            </p>

            <p className="text-xs text-gray-500">
              Administrator
            </p>
          </div>

          <ChevronDown size={18} />
        </div>
      </div>
    </header>
  );
}