# 🤖 Financial LLM Multi-Agent System

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Groq](https://img.shields.io/badge/Groq-LLama_3.3_70B-purple?style=flat-square&logo=groq&logoColor=white)](https://groq.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Made with ❤️](https://img.shields.io/badge/Made%20with-%F0%9F%A4%96%20and%20🧠-ff69b4?style=flat-square)]()

---

## 🧩 Project overview

This short project implements a collaborative **multi-agent system** built with the **[Phi Framework](https://github.com/phi-agent/phi)** and powered by the **LLM** Groq’s Llama-3.3-70B model.

The system combines two simple but specialized agents:
- **Finance Agent** 🧮 → retrieves and analyzes real-time financial data from **Yahoo Finance**.
- **Web Agent** 🌐 → searches the web for the latest company news using **DuckDuckGo**.

Both agents collaborate to generate a single, unified report summarizing:
- Market sentiment  
- Analyst recommendations 
- Stock financial reports and information 
- Recent financial headlines  

---

## 🧠 How It Works

```mermaid
graph TD;
    A[User Prompt] --> B[Finance Multi Agent];
    A --> C[Web Agent];
    B --> D[Coordinator Agent];
    C --> D[Coordinator Agent];
    D --> E[Final Report];

contact: jose.saurith@est.uexternado.edu.co
