[CS5704] Software Engineering

Dr. Chris Brown
Virginia Tech
4/28/2026

Announcements

‹#›

HW6 due Friday (5/1) before midnight
SE Reflection
PM2.3 due Friday (5/1) before midnight
Ut Prosim credits due Wed (5/6) before midnight
Upcoming Classes
Today (4/28): Workshop / Exam Review
4/30: Guest Lecture [Andy Bond, Red Hat]
5/5: Class Retrospective / Project Workday
5/9 [1:05pm]: Project 2 Demos and Final Exam
5/9 [11:59pm]: Project 2 Report and Retrospective (individual)
Please contact me if you have questions/concerns about your grade.

Advanced Topics + Exam Review

Final Project/Exam Details and Review
AI4SE vs SE4AI
Workshop

Final Project Presentation

Logistics
Saturday, 5/9 at 1:05
Presentation slides due on Canvas before class
Order will be decided randomly before class
Please arrive to class on time!
All team members expected to contribute to presentation
Please stick to the time limit ⏰
Please be prepared to transition between groups.

‹#›

Final Presentation Rubric



‹#›

Project 2 Final Report

‹#›

‹#›

Final Exam

Logistics
Saturday, 5/9
1:05pm-3:05pm
PAT 215
Details
Approximately 1 hour (following presentations)
15 Questions (scenario-based: mix of MCQ, short answer, and reflections—1-2 sentences!)
All course content except Guest Lectures and today
Online Exam
Open notes, books, or other resources

Exam Review

Quizizz

AI for Software Engineering

Applications of artificial intelligence/LLMs for SE tasks

‹#›

SE4AI

The application of SE principles in the design, development, and deployment of AI-based systems.

‹#›

SE4AI treats AI models (e.g., trained ML models, deep networks, etc.) as components within larger software systems and focuses on how to make those overall systems reliable, maintainable, safe, and trustworthy in real-world contexts. Rather than centering on model training itself, SE4AI emphasizes requirements, architecture, testing, deployment, monitoring, and continuous improvement for AI-enabled systems.

What are AI-based Software Systems?

AI-based software systems are systems that include one or more AI component (and other components)
Systems that integrate AI capabilities
Statistical Learning
Machine Learning
Deep Learning
AI Component
Embedded AI code
Using AI library to implement AI (i.e., API)

‹#›

[Shihab]

Software 2.0

“The term Software 2.0 was coined by Andrej Karpathy, a computer scientist and former senior director of AI at Tesla, to describe machine learning (ML) models that assist in solving a variety of problems without the traditional human input…Software 2.0 is based on deep learning, where the developer will merely gather data to feed ML systems.” [Softtek]

‹#›

Challenges

SE4AI is increasingly important as AI is integrated into critical software systems:
Customer service chatbots
Autonomous driving
Resume parsing
Crime prediction
Cancer detection
etc.

‹#›

AI-Based System Characteristics

Characteristics of AI-enabled systems cause traditional SE methods to fail:
Data-dependent behavior
Probabilistic/Non-deterministic nature
Model drift [performance degrades as data changes]
New non-functional requirements [fairness, interpretability, robustness, etc.]
New system architectures [model, data pipelines, inference servers, monitoring, etc.]

‹#›

[RI]

How LLMs are Trained



‹#›

[Morgan]

How LLMs are Post-Trained?



‹#›

[Gupta]

Goals for Today’s Workshop

Interact and run with LLMs locally
Customizing your own language model

‹#›

Background: Ollama Drama

https://github.com/omaciel/ollama-drama
🧰 Prerequisites
Python 3.10+
Ollama (with at least one model pulled locally, like qwen3:0.6b)
Git
A GitHub account
Why Ollama and Why Local?
• Local serving of LLMs made easy
• Works on macOS, Windows (WSL), Linux
• Benefits: Privacy, Speed, No API limits

‹#›

Workshop

https://github.com/CS5704-VT/
Why Ollama and Why Local?
• Local serving of LLMs made easy
• Works on macOS, Windows (WSL), Linux
• Benefits: Privacy, Speed, No API limits

‹#›





‹#›

References

Christian Kaestner and Eunsek Kang. “Software Engineering for AI-Enabled Systems (SE4AI)”. Carnegie Mellon, Fall 2020.
“What’s the difference Between AI and Regular Computing?” Royal Institution, 2023.
“Software 2.0: An Emerging Era of Automatic Code Generation”. Softtek Blog, 2023.
Andrej Karpathy. “Software 2.0”. Medium, 2017.
Emad Shihab, Diego Elias Costa. “SOEN 691: Engineering AI-Based Software Systems”. Concordia University, 2022
Suhaib Mujahid. “Deploying ML in Production”. Mozilla, 2022
Abby Morgan. “Pretraining: Breaking Down the Modern LLM Training Pipeline”. Comet, 2025
Og Maciel. “Ollama Drama Workshop”.

‹#›

