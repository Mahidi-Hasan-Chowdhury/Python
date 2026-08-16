// ==============================================================================
// TYPESCRIPT FOUNDATIONS — LESSON 1: TYPES & ANNOTATIONS
// ==============================================================================

// 1. Primitive Types (number, string, boolean)
let userName: string = "Mahidi";
let userAge: number = 22;
let isDeveloper: boolean = true;

console.log(`User: ${userName}, Age: ${userAge}, Developer: ${isDeveloper}`);

// 2. Arrays & Tuples
let skills: string[] = ["JavaScript", "Python", "TypeScript"];
let personInfo: [string, number] = ["Mahidi", 22]; // Tuple (fixed length & types)

console.log("Skills:", skills);

// 3. Functions with Type Annotations
function addNumbers(a: number, b: number): number {
    return a + b;
}

console.log("Sum:", addNumbers(10, 20));

// 4. Interfaces (Defining object shapes - essential for Next.js & APIs)
interface User {
    id: number;
    name: string;
    role: string;
    isActive?: boolean; // Optional property marked with ?
}

const adminUser: User = {
    id: 1,
    name: "Mahidi",
    role: "Full Stack AI Engineer"
};

console.log("Admin User:", adminUser);
