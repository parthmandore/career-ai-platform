# 🚀 Career AI Platform

A full-stack AI-powered career guidance platform that analyzes user resumes, identifies skill gaps, generates personalized career recommendations, and creates learning roadmaps using a Multi-Agent LLM Architecture built with LangGraph and Google Gemini.

The platform combines React, Django REST Framework, PostgreSQL, JWT Authentication, Docker, and LangGraph to deliver an end-to-end career intelligence system.

---

# 🎯 Problem Statement

Most students and early professionals struggle to answer:

* What skills am I missing?
* Which career paths fit my profile?
* What should I learn next?
* How do I become industry-ready?

Career AI Platform solves this by using multiple AI agents that collaborate to analyze resumes and generate actionable career insights.

---

# 🏗 System Architecture

```text
                    User
                      │
                      ▼
              React Frontend
                      │
                      ▼
              Django REST API
                      │
                      ▼
               PostgreSQL DB
                      │
                      ▼
              Resume Upload API
                      │
                      ▼
        PDF Resume Extraction Layer
         (PyPDF2 + pdfplumber)
                      │
                      ▼
           LangGraph Orchestrator
                      │
      ┌───────────────┼───────────────┐
      │               │               │
      ▼               ▼               ▼

Resume Analyzer   Career Advisor   Roadmap Generator
     Agent            Agent             Agent

      └───────────────┼───────────────┘
                      │
                      ▼
               Google Gemini
                      │
                      ▼
            Career Recommendations
```

---

# 🤖 Multi-Agent Workflow

The platform uses LangGraph to orchestrate specialized AI agents that collaborate through structured state passing.

## 1. Resume Analyzer Agent

Responsibilities:

* Extract technical skills
* Extract soft skills
* Identify strengths
* Generate profile summary

Input:

```text
Resume Text
```

Output:

```text
Skills
Strengths
Profile Summary
```

---

## 2. Career Advisor Agent

Responsibilities:

* Analyze extracted skills
* Recommend suitable career paths
* Suggest industry-aligned roles
* Generate career guidance

Examples:

* Data Analyst
* Data Engineer
* Machine Learning Engineer
* Backend Developer

---

## 3. Roadmap Generator Agent

Responsibilities:

* Create personalized learning plans
* Prioritize missing skills
* Generate monthly milestones
* Recommend learning progression

Output:

```text
3-Month Roadmap
6-Month Roadmap
Career Growth Plan
```

---

# 📄 Resume Processing Pipeline

The platform supports PDF resume ingestion using:

* PyPDF2
* pdfplumber

Workflow:

```text
PDF Upload
     │
     ▼
Text Extraction
     │
     ▼
Resume Structuring
     │
     ▼
Skill Identification
     │
     ▼
Agent Workflow
```

---

# 🔐 Authentication & Security

Features:

* User Registration
* User Login
* JWT Authentication
* Protected API Endpoints
* User-Specific Resume Access
* Token-Based Authorization

Implemented using:

* Django REST Framework
* Simple JWT

---

# 🛠 Technology Stack

## Frontend

* React.js
* React Router
* Axios

## Backend

* Django
* Django REST Framework
* PostgreSQL

## AI Layer

* LangGraph
* Google Gemini
* Multi-Agent Architecture

## Authentication

* JWT Authentication
* Simple JWT

## Resume Processing

* PyPDF2
* pdfplumber

## DevOps

* Docker
* Docker Compose

---

# 📂 Project Structure

```text
career-ai-platform/

├── frontend/
│
├── backend/
│
├── ai/
│   ├── graph.py
│   ├── state.py
│   ├── gemini_service.py
│   ├── resume_parser.py
│   │
│   └── nodes/
│       ├── resume_analyzer.py
│       ├── career_advisor.py
│       └── roadmap_generator.py
│
├── docker-compose.yml
│
└── README.md
```

---

# 🔄 End-to-End Workflow

1. User registers/login
2. User uploads resume
3. Resume stored in PostgreSQL
4. Resume text extracted
5. LangGraph workflow triggered
6. Resume Analyzer Agent extracts skills
7. Career Advisor Agent suggests career paths
8. Roadmap Generator Agent creates learning roadmap
9. Results returned to dashboard

---

# 🚀 Future Enhancements

* ATS Resume Scoring
* Job Matching Engine
* AI Mock Interviewer
* DSA Progress Tracking
* LinkedIn Profile Analysis
* Agent Memory
* Multi-LLM Support
* Retrieval-Augmented Generation (RAG)
* Personalized Learning Resource Recommender

---

# 📚 Key Learning Outcomes

This project demonstrates:

* Full-Stack Application Development
* REST API Design
* JWT Authentication
* PostgreSQL Integration
* Docker-Based Deployment
* Multi-Agent AI Systems
* LangGraph Workflow Design
* LLM Integration with Gemini
* PDF Data Extraction Pipelines

---

# 👨‍💻 Author

Parth Mandore

B.Tech Computer Science

Interests:
AI Engineering • Data Engineering • Cloud Computing • Full Stack Development
