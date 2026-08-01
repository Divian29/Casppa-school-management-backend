export interface Student {
    id: number;
  
    school: number;
    school_name: string;
  
    admission_number: string;
  
    first_name: string;
    last_name: string;
  
    date_of_birth: string;
  
    gender: string;
  
    photo: string | null;
  
    student_class: number;
    student_class_name: string;
  
    house: number | null;
    house_name: string | null;
  
    parent: number | null;
    parent_name: string | null;
  
    status: string;
  
    admission_date: string;
  }
  
  
  export interface School {
    id: number;
    name: string;
  }
  
  
  export interface SchoolClass {
    id: number;
    name: string;
    level: string;
  }
  
  
  export interface House {
    id: number;
    name: string;
    color: string;
  }
  
  
  export interface Parent {
    id: number;
    first_name: string;
    last_name: string;
    email: string;
  }