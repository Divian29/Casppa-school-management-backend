"use client";

import { useState } from "react";
import StudentForm from "./StudentForm";


interface Props {
  onSuccess: () => void;
}


export default function AddStudentModal({
  onSuccess,
}: Props) {

  const [open, setOpen] = useState(false);


  function handleSuccess() {
    setOpen(false);
    onSuccess();
  }


  return (
    <>
      <button
        onClick={() => setOpen(true)}
        className="rounded-lg bg-blue-600 px-4 py-2 text-white"
      >
        Add Student
      </button>



      {open && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50">


          <div className="max-h-[90vh] w-full max-w-lg overflow-y-auto rounded-xl bg-white p-6">


            <div className="mb-5 flex items-center justify-between">

              <h2 className="text-xl font-bold">
                Add Student
              </h2>


              <button
                onClick={() => setOpen(false)}
                className="text-gray-500 hover:text-gray-800"
              >
                ✕
              </button>

            </div>



            <StudentForm
              onSuccess={handleSuccess}
            />


          </div>


        </div>
      )}

    </>
  );
}