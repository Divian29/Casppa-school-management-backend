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
  
    house: number;
    house_name: string | null;
  
    parent: number;
    parent_name: string | null;
  
    status: string;
  
    admission_date: string;
  }