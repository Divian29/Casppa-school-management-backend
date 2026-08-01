"use client";

import { useEffect, useState } from "react";
import { getStudents } from "@/lib/api";
import { Student } from "@/types/student";
import StudentStatusBadge from "@/components/students/StudentStatusBadge";
import AddStudentModal from "@/components/students/AddStudentModal";

export default function StudentsPage() {
  const tabs = [
    "Students",
    "New Enrollment",
    "Running",
    "Attendance",
    "Suspended",
    "Alumni",
    "Analytics",
  ];

  const [students, setStudents] = useState<Student[]>([]);
  const [search, setSearch] = useState("");
  const [activeTab, setActiveTab] = useState("Students");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  async function fetchStudents() {
    try {
      setLoading(true);
  
      const data = await getStudents();
  
      setStudents(data);
  
    } catch (err) {
  
      console.error(
        "Student fetch error:",
        err
      );
  
      setError(
        "Unable to load students"
      );
  
    } finally {
  
      setLoading(false);
  
    }
  }
  
  
  useEffect(() => {
    fetchStudents();
  }, []);


  const filteredStudents = students.filter((student) => {
    const value = search.toLowerCase();
  
  
    const matchesSearch =
      student.first_name.toLowerCase().includes(value) ||
      student.last_name.toLowerCase().includes(value) ||
      student.admission_number.toLowerCase().includes(value) ||
      (student.parent_name &&
        student.parent_name.toLowerCase().includes(value));
  
  
    const matchesTab =
      activeTab === "Students"
        ? true
        : activeTab === "Running"
        ? student.status === "ACTIVE"
        : activeTab === "Suspended"
        ? student.status === "SUSPENDED"
        : activeTab === "Alumni"
        ? student.status === "ALUMNI"
        : false;
  
  
    return matchesSearch && matchesTab;
  });


  return (
    <div className="space-y-6">

      {/* Header */}
      <div className="rounded-xl bg-white p-6 shadow-sm">
        <h1 className="text-2xl font-bold">
          Students
        </h1>

        <p className="mt-2 text-gray-500">
          Manage student records and admissions
        </p>
      </div>


      {/* Tabs */}
      <div className="rounded-xl bg-white p-4 shadow-sm">
        <div className="flex gap-6 border-b">

          {tabs.map((tab, index) => (
            <button
            key={tab}
            onClick={() => setActiveTab(tab)}
            className={`pb-3 text-sm font-medium ${
              activeTab === tab
                ? "border-b-2 border-blue-600 text-blue-600"
                : "text-gray-500 hover:text-gray-700"
            }`}
          >
            {tab}
          </button>
          ))}

        </div>
      </div>


      {/* Search and Actions */}
      <div className="rounded-xl bg-white p-6 shadow-sm">

        <div className="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">

          <input
            type="text"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="Search students..."
            className="w-full rounded-lg border px-4 py-2 md:w-96"
          />


          <div className="flex gap-3">

            <button className="rounded-lg border px-4 py-2">
              Add Parent
            </button>

            <button className="rounded-lg border px-4 py-2">
              Bulk Upload
            </button>

            <AddStudentModal
              onSuccess={() => {
              window.location.reload();
               }}
            />

          </div>

        </div>

      </div>


      {/* Students Table */}
      <div className="overflow-hidden rounded-xl bg-white shadow-sm">

        <table className="w-full">

          <thead className="border-b bg-gray-50">

            <tr>

              <th className="p-4 text-left">
                Name
              </th>

              <th className="p-4 text-left">
                Admission No
              </th>

              <th className="p-4 text-left">
                Class
              </th>

              <th className="p-4 text-left">
                House
              </th>

              <th className="p-4 text-left">
                Parent
              </th>

              <th className="p-4 text-left">
                Gender
              </th>

              <th className="p-4 text-left">
                Status
              </th>

            </tr>

          </thead>


          <tbody>

            {loading && (
              <tr>
                <td
                  colSpan={7}
                  className="p-4 text-center"
                >
                  Loading students...
                </td>
              </tr>
            )}


            {error && (
              <tr>
                <td
                  colSpan={7}
                  className="p-4 text-center text-red-500"
                >
                  {error}
                </td>
              </tr>
            )}


            {!loading &&
              !error &&
              filteredStudents.map((student) => (
                <tr
                  key={student.id}
                  className="border-b hover:bg-gray-50"
                >

                  <td className="p-4">
                    {student.first_name} {student.last_name}
                  </td>


                  <td className="p-4">
                    {student.admission_number}
                  </td>


                  <td className="p-4">
                    {student.student_class_name}
                  </td>


                  <td className="p-4">
                    {student.house_name || "-"}
                  </td>


                  <td className="p-4">
                    {student.parent_name || "-"}
                  </td>


                  <td className="p-4">
                    {student.gender}
                  </td>


                  <td className="p-4">
                    <StudentStatusBadge status={student.status} />
                  </td>

                </tr>
              ))}


            {!loading &&
              !error &&
              filteredStudents.length === 0 && (
                <tr>
                  <td
                    colSpan={7}
                    className="p-4 text-center text-gray-500"
                  >
                    No students found
                  </td>
                </tr>
              )}

          </tbody>

        </table>

      </div>

    </div>
  );
}