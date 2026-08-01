"use client";

import { useEffect, useState } from "react";
import { getStudents } from "@/lib/api";
import { Student } from "@/types/student";

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
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function fetchStudents() {
      try {
        const data = await getStudents();
        setStudents(data);
      } catch (err) {
        console.error("Student fetch error:", err);
        setError("Unable to load students");
      } finally {
        setLoading(false);
      }
    }

    fetchStudents();
  }, []);

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
              className={`pb-3 text-sm font-medium ${
                index === 0
                  ? "border-b-2 border-blue-600 text-blue-600"
                  : "text-gray-500 hover:text-gray-700"
              }`}
            >
              {tab}
            </button>
          ))}

        </div>
      </div>


      {/* Actions */}
      <div className="rounded-xl bg-white p-6 shadow-sm">

        <div className="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">

          <input
            type="text"
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

            <button className="rounded-lg bg-blue-600 px-4 py-2 text-white">
              Add Student
            </button>

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
              students.map((student) => (
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
                    {student.status}
                  </td>

                </tr>
              ))}


            {!loading && !error && students.length === 0 && (
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