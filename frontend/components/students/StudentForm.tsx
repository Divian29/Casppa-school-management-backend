"use client";

import { useEffect, useState } from "react";

import {
  getSchools,
  getClasses,
  getHouses,
  getParents,
  createStudent,
} from "@/lib/api";

import {
  School,
  SchoolClass,
  House,
  Parent,
} from "@/types/student";


interface Props {
  onSuccess: () => void;
}


export default function StudentForm({ onSuccess }: Props) {

  const [schools, setSchools] = useState<School[]>([]);
  const [classes, setClasses] = useState<SchoolClass[]>([]);
  const [houses, setHouses] = useState<House[]>([]);
  const [parents, setParents] = useState<Parent[]>([]);


  const [form, setForm] = useState({
    school: "",
    admission_number: "",
    first_name: "",
    last_name: "",
    date_of_birth: "",
    gender: "",
    student_class: "",
    house: "",
    parent: "",
  });


  useEffect(() => {

    async function loadData() {

      const [
        schoolData,
        classData,
        houseData,
        parentData,
      ] = await Promise.all([
        getSchools(),
        getClasses(),
        getHouses(),
        getParents(),
      ]);


      setSchools(schoolData);
      setClasses(classData);
      setHouses(houseData);
      setParents(parentData);
    }


    loadData();

  }, []);



  function handleChange(
    e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>
  ) {

    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });

  }



  async function handleSubmit(
    e: React.FormEvent
  ) {

    e.preventDefault();


    await createStudent({
      ...form,
      school: Number(form.school),
      student_class: Number(form.student_class),
      house: Number(form.house),
      parent: Number(form.parent),
    });


    onSuccess();

  }



  return (

    <form
      onSubmit={handleSubmit}
      className="space-y-4"
    >


      <input
        name="first_name"
        placeholder="First name"
        className="w-full rounded border p-2"
        onChange={handleChange}
      />


      <input
        name="last_name"
        placeholder="Last name"
        className="w-full rounded border p-2"
        onChange={handleChange}
      />


      <input
        name="admission_number"
        placeholder="Admission number"
        className="w-full rounded border p-2"
        onChange={handleChange}
      />


      <input
        type="date"
        name="date_of_birth"
        className="w-full rounded border p-2"
        onChange={handleChange}
      />



      <select
        name="gender"
        className="w-full rounded border p-2"
        onChange={handleChange}
      >

        <option value="">
          Select Gender
        </option>

        <option value="MALE">
          Male
        </option>

        <option value="FEMALE">
          Female
        </option>

      </select>



      <select
        name="school"
        className="w-full rounded border p-2"
        onChange={handleChange}
      >

        <option value="">
          Select School
        </option>


        {schools.map((school)=>(
          <option
            key={school.id}
            value={school.id}
          >
            {school.name}
          </option>
        ))}

      </select>




      <select
        name="student_class"
        className="w-full rounded border p-2"
        onChange={handleChange}
      >

        <option value="">
          Select Class
        </option>


        {classes.map((item)=>(
          <option
            key={item.id}
            value={item.id}
          >
            {item.name}
          </option>
        ))}

      </select>




      <select
        name="house"
        className="w-full rounded border p-2"
        onChange={handleChange}
      >

        <option value="">
          Select House
        </option>


        {houses.map((house)=>(
          <option
            key={house.id}
            value={house.id}
          >
            {house.name}
          </option>
        ))}

      </select>




      <select
        name="parent"
        className="w-full rounded border p-2"
        onChange={handleChange}
      >

        <option value="">
          Select Parent
        </option>


        {parents.map((parent)=>(
          <option
            key={parent.id}
            value={parent.id}
          >
            {parent.first_name} {parent.last_name}
          </option>
        ))}

      </select>



      <button
        type="submit"
        className="rounded bg-blue-600 px-4 py-2 text-white"
      >
        Save Student
      </button>


    </form>

  );

}