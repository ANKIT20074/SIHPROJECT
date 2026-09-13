# DoctorKavach (डॉक्टर कवच) 🛡️
### Smart India Hackathon (SIH) — Healthcare Verification, OPD Management & DPDP-Compliant Consultation

**DoctorKavach** is an integrated healthcare verification and OPD management platform engineered for India to eliminate catastrophic OPD queues in public hospitals, Community Health Centres (CHCs), and Primary Health Centres (PHCs). It couples real-time OPD token orchestration with simulated government verification (**NMC Doctor Registry**, **CEA Hospital Licensing**, **NABL Diagnostic Lab Accreditation**, and **ABHA Health IDs**), strict **DPDP-compliant consent expiration** upon consultation completion, grievance auto-flagging ($\ge 3$ complaints), digital e-prescriptions with daily medicine reminders, and regional diet & recovery audio guides.

> **SIH Hackathon Prototype Notice**: Live NMC, CEA, NABL, and ABHA government APIs require state-level access tokens not available to student teams during development. In accordance with SIH evaluation norms, all government verification registers, lab accreditations, and health identity lookups are simulated with high-fidelity mock data.

---

## 🛠️ Architecture & Tech Stack

- **Frontend**: React 18 with Vite, Tailwind CSS, Recharts for interactive analytics, and Lucide React icons.
- **Backend**: Node.js with Express 4, native `node:sqlite` in WAL (Write-Ahead Logging) mode, JWT authentication with HttpOnly cookies, and bcryptjs password hashing.
- **Database**: SQLite WAL database (`server/data/doctorkavach.sqlite`) pre-seeded with realistic Indian healthcare data.
- **Audio / Voice**: Browser-native Web Speech API (`window.speechSynthesis`) supporting Hindi and English voice read-aloud.

---

## 🚀 1-Click Launch (Everything Ready)

You can launch both the **Node.js Express Backend (port 8000)** and **React Frontend (port 5173)** with a single command:

```bash
# From the SIH DOCTOR KAVCHAT directory:
python run_demo.py
```
*(On Windows, you can also simply double-click `start_doctorkavach.bat`)*

- **Frontend Web App**: `http://localhost:5173`
- **Backend REST API**: `http://127.0.0.1:8000`
- **API Health Check**: `http://127.0.0.1:8000/api/v1/health`

---

## 👥 Seeded Demonstration Accounts (For SIH Judges & Pitch)

The top navigation bar features a **1-Click Role Switcher** dropdown allowing immediate switching between all 5 system roles without typing credentials:

| Role | Email | Password | Key Demonstration Flows |
| :--- | :--- | :--- | :--- |
| **🏛️ Govt Health Officer** | `officer@health.gov.in` | `Admin@2026` | Approve pending CEA/NABL/NMC applications, inspect auto-flagged doctors ($\ge 3$ complaints), review Recharts aggregate analytics |
| **🏥 Hospital Admin** | `admin@safdarjung.in` | `Hospital@2026` | Review hospital CEA license status, onboard new doctors with NMC credentials, inspect hospital OPD roster |
| **🔬 Diagnostic Lab Admin** | `admin@lalpathlabs.in` | `Lab@2026` | View NABL accreditation status, search patient by Health ID (ABHA), issue digital lab reports (Blood, X-Ray, MRI, Scans) |
| **🩺 Doctor (NMC)** | `dr.sharma@doctorkavach.in` | `Doctor@2026` | Call next patient, view consent-unlocked ABHA records, check past prescriptions & lab reports, write digital e-Rx, prescribe diet chart, complete visit (strictly auto-expires consent) |
| **👤 Patient (ABHA)** | `ramesh@gmail.com` | `Patient@2026` | Search verified doctors, book live OPD token, approve/deny DPDP record consent, view permanent prescriptions & lab reports, track daily medicines checklist, submit post-visit rating & grievance |

---

## 🌟 Core System Features

### 1. 5 Distinct Role Dashboards
- **Patient Portal**: Search doctors by specialty, book live OPD tokens, view ABHA medical history, manage DPDP consent requests, review permanent "My Prescriptions" and "My Reports", track "Today's Medicines" reminder checklist, listen to diet recovery audio, and submit post-visit ratings.
- **Doctor Portal**: Live consultation queue, call patient into consultation room, review consent-unlocked medical records, inspect past prescriptions & diagnostic lab reports (preventing drug interactions), write digital prescriptions, prescribe condition-specific diets, and complete visits.
- **Hospital Admin Portal**: View Clinical Establishments Act (CEA) license status, register and onboard verified medical staff into hospital departments.
- **Diagnostic Lab Portal**: View NABL license accreditation, search patient by ABHA Health ID, and upload/issue digital diagnostic reports (Blood Tests, X-Rays, MRI, CT, Ultrasound, ECG).
- **Govt Health Officer Portal**: Regulatory oversight, approve/reject pending hospitals, diagnostic labs, and NMC doctor credentials, inspect flagged doctors ($\ge 3$ complaints), and analyze Recharts visual charts.

### 2. Live OPD Queue Orchestration & Token Tracking
- Generates sequential OPD tokens with estimated wait time algorithm based on patient queue depth (~12 minutes per consultation).
- Live token display with status tracking (`waiting`, `in_consultation`, `completed`).

### 3. DPDP Act Compliant Consent Lifecycle
- Doctor requests access to patient's ABHA records during consultation.
- Patient receives a consent modal and explicitly approves or denies access.
- When doctor clicks **"Complete Consultation"**, consent access is **strictly and automatically expired/revoked** in real-time, preventing unauthorized lingering access to patient data.

### 4. Digital Prescriptions (e-Rx) & Medicine Reminders
- Doctors issue digital prescriptions with medicine name, dosage, timing (e.g. 1-0-1), meal relation (Before/After Food), and duration.
- Patient dashboard automatically aggregates all active prescriptions into an interactive **"Today's Medicines"** daily checklist with dosage, timing badges, and progress bar.
- Permanent record: Patients can review and download their prescriptions anytime.

### 5. Diagnostic Lab Integration & Reports Repository
- Verified diagnostic labs upload official test results directly into the patient's record using their ABHA Health ID.
- Doctors with active consultation consent can inspect past lab reports and imaging (Blood Tests, X-Rays, MRI, Ultrasound) before prescribing treatment.
- Patients have permanent access to their digital reports under "My Diagnostic Reports".

### 6. Grievance Auto-Flagging System
- Patients submit 1–5 star ratings and categorical grievances (*Overcharging*, *Unhygienic Conditions*, *Refused Treatment / Negligence*, *Excessive Wait Time*).
- If a medical practitioner accumulates **$\ge 3$ complaints**, the system automatically tags them as **Flagged for Review** with a prominent red badge on the Government Officer dashboard for mandatory CMO audit.

### 7. Recharts Aggregate Analytics (Zero Patient PII)
- Real-time aggregate indicators powered by Recharts on the Government Officer dashboard:
  - **Verification Pipeline Bar Chart**: Stacked breakdown of verified, pending, and rejected hospitals, labs, and doctors.
  - **Citizen Grievance Categories Donut Chart**: Distribution of complaints by category.
  - **Patient Satisfaction Bar Chart**: 1 to 5 star rating distribution.
  - **Statutory Benchmarks**: Licensing clearance percentages and grievance resolution rate.
  - **Privacy Guarantee**: All charts query aggregated counts with zero patient personal identifiable information exposed.

### 8. Multilingual Diet & Recovery Voice Assistance
- 5 regional disease recovery diets (*Type 2 Diabetes*, *Hypertension*, *Dengue & Viral Fever*, *Acute Gastritis*, *Iron Deficiency Anemia*).
- Built-in **"Read Aloud (सुनें)"** text-to-speech utilizing the browser's native **Web Speech API** (`window.speechSynthesis`) with Hindi and English voice selection.

### 9. Hardened Security Architecture
- **Password Hashing**: Bcrypt with 12 salt rounds (max 72-byte truncation boundary).
- **Session Tokens**: JWT stored in HttpOnly cookies with `SameSite=Lax` preventing client-side script theft (XSS).
- **Zero Account Enumeration**: Uniform response timing on failed logins.
- **Offline-First Resilience**: SQLite with Write-Ahead Logging (`PRAGMA journal_mode=WAL`) ready for rural PHC connectivity interruptions.

---

## 🧪 Automated Verification Test Suite

DoctorKavach includes an automated end-to-end test suite verifying all 10 core Express modules:

```bash
cd server
node test_e2e_express.js
```

**Test Suite Coverage (100% Pass Rate - 10/10 modules passed)**:
1. Health check & database connection
2. Authentication (Login, `/me`, role permissions across all 5 roles)
3. Hospital CEA registration & listing
4. Diagnostic Lab NABL accreditation & search patient by ABHA ID
5. Doctor NMC onboarding & public directory
6. OPD Queue booking, live queue, and token calling
7. DPDP Consent lifecycle (Request -> Approve -> Access verified -> Complete visit -> Strictly Revoked!)
8. Digital Prescriptions (Doctor create -> Patient view -> Medicine reminder generator)
9. Lab Reports issuance & consent-gated Doctor report viewer
10. Reviews, Grievance submission & Auto-Flagging ($\ge 3$ threshold) + Govt Recharts analytics

