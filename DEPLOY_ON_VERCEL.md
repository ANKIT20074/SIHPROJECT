# 🚀 DoctorKavach — Vercel Deployment Guide (वर्सेल पर लाइव करने की गाइड)

DoctorKavach is now **100% pre-configured for Vercel deployment** as a unified full-stack application (React Vite Frontend + Node.js Express Serverless API + SQLite WAL Database).

---

## ⚡ Method 1: Deploy Directly from Terminal (सबसे तेज़ तरीका - 2 मिनट में)

Open PowerShell or Command Prompt in this folder (`SIH DOCTOR KAVCHAT`) and run:

```bash
npx vercel
```

### Prompt Responses during `npx vercel`:
1. **Set up and deploy?** $\rightarrow$ Type `y` and press Enter.
2. **Which scope?** $\rightarrow$ Select your personal account (or team).
3. **Link to existing project?** $\rightarrow$ Type `n` (No).
4. **What's your project's name?** $\rightarrow$ Press Enter (defaults to `doctorkavach`).
5. **In which directory is your code located?** $\rightarrow$ Press Enter (`./`).
6. **Want to modify these settings?** $\rightarrow$ Type `n` (No, `vercel.json` will automatically configure everything!).

Once it finishes, run:
```bash
npx vercel --prod
```
Your website will be live with a production URL like:
👉 **`https://doctorkavach.vercel.app`**

---

## 🌐 Method 2: Deploy via GitHub (गिटहब के जरिए)

If you have pushed this repository to GitHub:

1. Go to **[vercel.com](https://vercel.com)** and log in with GitHub.
2. Click **"Add New..."** $\rightarrow$ **"Project"**.
3. Select your GitHub repository and click **"Import"**.
4. In the Project Configuration:
   - **Framework Preset**: `Vite` (automatically detected)
   - **Root Directory**: `./` (leave default)
   - **Build Command**: `npm --prefix frontend install && npm --prefix frontend run build` (auto-configured by `vercel.json`)
   - **Output Directory**: `frontend/dist` (auto-configured by `vercel.json`)
5. Click **"Deploy"**.

Within 60 seconds, your site will be live!

---

## ⚙️ How Full-Stack Works on Vercel:

| Component | How It Works on Vercel |
| :--- | :--- |
| **Frontend (React + Tailwind)** | Built into static assets at `frontend/dist` and served worldwide on Vercel's Edge CDN. |
| **Backend (Express Node.js)** | Hosted as a serverless function via `api/index.js` running on Node.js 22. |
| **API Routing (`/api/*`)** | All API requests (`/api/v1/auth`, `/api/v1/doctors`, `/api/v1/opd`) are routed to `api/index.js` automatically without CORS restrictions. |
| **Database (SQLite)** | Runs in `/tmp` on serverless functions with the full initial SIH seed dataset preloaded. |
| **File / License Viewer** | Dynamically generates verified statutory HTML certificates and documents in-memory. |

---

## 🔑 Demo Login Accounts to Test on Vercel:

| Role | Email | Password | Features to Demonstrate |
| :--- | :--- | :--- | :--- |
| **Patient** | `ramesh@gmail.com` | `Patient@2026` | Disease search (e.g. `heart`, `knee`), 1-click token booking, photo grievance upload, diet recovery charts. |
| **Doctor** | `dr.suresh@doctorkavach.in` | `Doctor@2026` | Live OPD queue management, digital prescriptions, patient visit completion. |
| **Hospital Admin** | `admin@safdarjung.in` | `Hospital@2026` | CEA license verification, hospital bed/doctor roster, QR token counter. |
| **Govt Health Officer** | `officer@health.gov.in` | `Admin@2026` | Chief Medical Officer desk, photo evidence inspection, doctor verification, city analytics. |
| **Diagnostic Lab** | `admin@lalpathlabs.in` | `Lab@2026` | NABL accreditation, lab report upload (Blood, X-Ray, MRI). |
