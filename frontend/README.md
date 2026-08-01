This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.

# Casppa Frontend

Frontend application for the Casppa School Management System.

## Built With

- Next.js 15
- React
- TypeScript
- Tailwind CSS
- Shadcn UI

## Features

Completed:
- Dashboard layout
- Student management page
- Student listing from Django REST API

Coming soon:
- Student enrollment
- Bulk upload
- Parent management
- Attendance
- Analytics

## Setup

Clone repository:

```bash
git clone <repo-url>
cd frontend


Install dependencies:

npm install

Create .env.local

NEXT_PUBLIC_API_URL=http://127.0.0.1:8000

Run development server:

npm run dev

Application runs on:

http://localhost:3000
Backend

This frontend connects to the Casppa Django REST API backend.


---

After creating it:

```bash
git add frontend/README.md
git commit -m "Add frontend documentation"
git push origin main
