import {
    School,
    SchoolClass,
    House,
    Parent,
    Student,
  } from "@/types/student";
  
  
  const API_URL =
    process.env.NEXT_PUBLIC_API_URL ||
    "http://127.0.0.1:8000";
  
  
  
  async function request(url: string, options?: RequestInit) {
    const response = await fetch(
      `${API_URL}${url}`,
      {
        ...options,
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
  
  
    if (!response.ok) {
      throw new Error("API request failed");
    }
  
  
    return response.json();
  }
  
  
  
  export function getStudents(): Promise<Student[]> {
    return request("/api/students/");
  }
  
  
  
  export function getSchools(): Promise<School[]> {
    return request("/api/schools/");
  }
  
  
  
  export function getClasses(): Promise<SchoolClass[]> {
    return request("/api/classes/");
  }
  
  
  
  export function getHouses(): Promise<House[]> {
    return request("/api/houses/");
  }
  
  
  
  export function getParents(): Promise<Parent[]> {
    return request("/api/parents/");
  }
  
  
  
  export function createStudent(data: any) {
    return request(
      "/api/students/",
      {
        method: "POST",
        body: JSON.stringify(data),
      }
    );
  }