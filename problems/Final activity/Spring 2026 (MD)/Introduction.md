[CS5704] Software Engineering

Dr. Chris Brown
Virginia Tech
1/20/2026

‹#›

Introduction

What is software and its engineering?
Course Overview
Responsibilities
Software Development Lifecycle

What is software?

Software is a set of instructions, data, or programs used to operate a computer and execute specific tasks. In simpler terms, software tells a computer how to function. [1]

‹#›

Software encompasses:
– Executable programs
– Data associated with these programs
– Documents: user requirements, design documents, user/programmer guides, etc.
[Pressman]

Hardware vs. Software

Hardware
Manufactured
Built using components
Relatively simple
Difficult or impossible to modify
Hiring more people = more work done
…

Software
Developed
Custom built?
Complex
Routinely modified and updated
More people != more productivity
…

‹#›

Hardware “wears out” over time

‹#›

So does software!

‹#›

Why is software important?

Software is eating the world! [Andreessen, 2011]

“More and more major businesses and industries are being run on software and delivered as online services…”

‹#›

Example

“The only thing you can do with an F-22 that does not require software is take a picture of it.” – Air Force Lt. General

‹#›

[Ferguson, 2021]

Example



‹#›

What is software engineering?

A discipline that encompasses:
the process of software development;
methods for software analysis, design, construction, testing, and maintenance; and
tools that support the processes and the methods.

‹#›

[Pressman]

What is SE? (cont.)

The majority of software engineering is not writing code.
The dominant activities are comprehension and maintenance.

‹#›

“Understanding code is by far the activity at which professional developers spend most of their time.” – Peter Hallam, Microsoft [2006]

[Fry, 2014]

What is SE? (cont.)

“... a new subdiscipline, software engineering, has arisen. The development of a large piece of software is perceived as an engineering task, to be approached with the same care as the construction of a skyscraper, for example, and with the same attention to cost, reliability, and maintainability of the final product... Even with such an engineering discipline in place, the software-development process is expensive and time-consuming.”
[Encyclopaedia Britannica]

‹#›

Why study Software Engineering?

‹#›



What is wrong with this picture?

‹#›



‹#›



‹#›

The European Space Agency's Ariane 5 Flight 501 was destroyed 40 seconds after takeoff (June 4, 1996). The US $1 billion prototype rocket self-destructed due to a bugin the on-board guidance software.
(The bug? Bad conversion of double to short, leading to an overflow.)

‹#›

In simple terms, what happened?
The outage that started July 19 was caused by a malformed update that was sent to a piece of security software called “CrowdStrike Falcon”...
The update that was sent to CrowdStrike software on Friday was malformed, which caused the software to crash every time it started and tried to parse the update. Now, usually, when an application like Google Chrome or Microsoft Word crashes, only that one application crashes. However, a lot of security software – including CrowdStrike Falcon – is special in this regard. Because CrowdStrike needs to detect malicious activity on the whole computer, it runs as part of the Windows operating system instead of on top of it. Unfortunately, this also meant that when it crashed, it caused the Windows OS to also crash.
[Kubota, 2024]

“While we’re getting better at software development as a field, we are still a long way from being able to guarantee that complex systems won’t have bugs like this. Infrastructure providers need to be thinking about how they’re architecting [i.e., designing] their systems to be resilient against system failures and how they’re going to recover when a system does fail, because this undoubtedly won’t be the last time we see a bug like this.”

2025 AWS Outage



2025 AWS Outage (cont.)

https://aws.amazon.com/message/101925/

‹#›





What is this class?

CS5704: Software Engineering (Graduate SE course)
Study of the principles and tools applicable to the methodical construction and controlled evolution of complex software systems. All phases of the life cycle are presented; particular attention focuses on the design, testing, and maintenance phases. Introduction to software project management. Attention to measurement models of the software process and product which allow quantitative assessment of cost, reliability, and complexity of software systems.

‹#›

Course Goals

Intellectual development
– Knowledge of processes, methods, and tools to assist software development
– Understand current techniques and problems in software engineering

‹#›

2. Practical development
– Improve development, communication, and writing skills
– Practice various software engineering skills and processes

Course Overview

Teaching Staff
Course Materials
Learning Outcomes
Class Activities

‹#›

About Me

Ph.D. 2015-2021

M.S. 2015-2017

B.S. 2009-2013

Intern 2017, 2018

Intern 2016

Python Developer 2013-2015

‹#›

Education:

Industry:

Contact: dcbrown@vt.edu
Office: 4105 Gilbert
Office Hours: Tu/Th 2:00pm-3:00pm, or by appointment

Research

My research seeks to find ways to improve the behavior, productivity, and decision-making of software engineers.

‹#›

Course Materials

Course materials are primarily on GitHub [https://github.com/CS5704-VT/Course]
Schedule, class activities and assignments, etc.
Mattermost is the primary mode of communication [https://meet.cs.vt.edu/cs-5704]
Class updates, contact students/teaching staff, project coordination, etc.
Canvas will be the course management system [https://canvas.vt.edu/courses/224123]
Class updates, assignments, slides, etc.

‹#›

Course Materials (cont.)

No textbook is required, but FYI the lecture and course content will primarily draw from the following resources:
Software Engineering: A Practitioner's Approach [Pressman]
Building Software Together [Wilson]
Evidence-Based Software Engineering [Jones]
Software Engineering [Somerville]

‹#›

Learning Outcomes

By the end of the course, students should be able to:
Implement a software system following the software life cycle phases
Develop software engineering skills working on a team project
Identify processes related to phases of the software lifecycle
Explain the differences between software engineering processes
Discuss research questions and studies related to software engineering
Communicate (via demo and writing) details about a developed software application

‹#›

Learning Approach: Class Activities

How to achieve the learning outcomes: 📖

‹#›

[Instructor and Guest] lectures
Workshop-style learning experiences
Research Discussions

Generally, the course will be structured to include a lecture and activity for each class.

Lectures

‹#›

Why?
To convey software engineering-related information to students

Workshops

Interactive tutorials, labs, mini-projects, and discussions on SE-related topics.
Some individual and some in small groups
In-class and in-person!
Mostly graded based on completion/for attendance (more on attendance policy later)
Why?
To practice and discuss applicable and real-world SE skills and concepts

‹#›

Research Discussions

Discussions on SE research topics
Each student will present two research papers to the class
Class will be expected to provide a reflection based on the research topic.
Why?
To improve critical thinking and communication skills about SE concepts

‹#›

Learning Evaluation: Course Work

How you will be evaluated on the learning outcomes: 🖉

‹#›

Homework
Exam
Projects

Homework

Mix of lecture review, application, and personal reflection questions.
Always due Fridays at 11:59pm on the assigned deadline
see Course Schedule/Canvas
No late assignments will be accepted!
📣 HW0 due 11:59pm on Friday 1/30!

‹#›

Exam

The exam will cover all course materials (lectures, workshops, and homework) except for guest lectures and the research discussions.
Details
Exam Review: 4/30
Final Exam: 5/9, 1:05 - 3:05pm
📣 Yes, there will be a final exam!

‹#›

Projects

There will be two class projects this semester! Project grades will primarily determined by meeting deliverable deadlines and your mastery of SE concepts discussed in class.
Project 1: February 3 – March 6 (Details on next few slides)
Project 2: March 16 – May 9 (Details released later this semester)

Project 1 Guidelines

For Project 1, you have ~five weeks to build whatever you want. For this assignment, students:
Must implement a software system;
Must use a (public) GitHub repository;
Must complete assigned requirements and design activities (Project Deliverables will be added to the Course Schedule);
Must complete a demo presentation of the implemented system;
May work in a group (choose your own team, or work individually);
May use Generative AI tools to support implementation (adhering to the class AI policy, more details later).

Project 1 Milestones

There will be three major milestones for Project 1:

‹#›

PM1.0: Project Introduction (due 2/3)
PM1.1: Requirements (due 2/13)
PM1.2: Design (due 2/25)
PM1.3: Pitch (due 3/3\*; final report on 3/6)
\* assignment due before class (9:30am) on deadline date!

Ut Prosim

The Virginia Tech motto is Ut Prosim which means “That I May Serve”. To embody this in our course, a portion of your grade will be determined by completing five service activities to the department, university, or VT community.
Ex.) participating in a research study, attending a department seminar, volunteer project, etc.
Submit form for each activity. Opportunities will be shared on Mattermost
Due: 5/6 (last day of classes) at 11:59pm

‹#›

Grading

‹#›

Class Policies: AI Policy

Students are permitted to use generative AI tools (e.g., ChatGPT, GitHub Copilot) for certain assignments and the course project. AI usage is not enforced, please contact the instructor if you prefer not to use AI or LLMs to receive a substitute assignment. You may use AI under these conditions:
Transparency: If you use Generative AI to create any aspect of a deliverable (code, documentation, sprint reports, wordsmithing, etc.), you must clearly identify it at the location where it appears (via a citation, code comment, or other identifier). You must also state which tool was used and include the prompt. Alternatively, you can submit a log (i.e., screenshot) of AI prompts and generated output.
Accountability for Code: You are fully responsible for understanding, testing, and maintaining any AI-generated code. Submitting code without understanding it will be treated as incomplete work.
Class Deliverables: Class deliverables must be completed by you and your team (if applicable), and not copied from AI unless otherwise specified.
Documentation in Your Own Words: All documentation (i.e., reports, discussion summaries, progress reports, meeting notes, etc.) must be written by you and/or your team. AI may be used for brainstorming, but final submissions must reflect your own understanding.
Learning Over Shortcuts: The purpose of this course is to help you learn software engineering practices (planning, collaboration, iteration, reflection). AI may assist, but it cannot replace your learning experience.
Team Collaboration: AI is not a substitute for teamwork. Every team member must actively contribute to discussions, coding, testing, and reviews.
Critical Thinking: Use AI as a starting point, but evaluate its output critically. Consider alternatives, justify design choices, and explain why you accepted or rejected AI-generated suggestions.
Please note: Violating this policy will be treated as an honor code violation.

‹#›

Class Policies: Academic Integrity

Please adhere to university academic integrity and honesty policies.
All violations will be reported to student conduct as an honor code violation and students will receive a -50% on the assignment.
-100% on the exam!
Assignments will describe individual or collaborative work, AI usage or not, etc.
Ask the instructor for clarification, any questions, or concerns before submitting an assignment.

‹#›

Other Class Policies

Late submissions are not accepted.
Be respectful of teaching staff and students.
Let me know if you need accommodations.
Attendance is strongly encouraged!.
But…do not come to class if you are sick! 😷
There will be several opportunities to provide course feedback throughout the semester.

‹#›

‹#›

CS5704: Software Engineering
Adapted from slides by Dr. Brittany Johnson (GMU)

Responsibilities

Fostering an inclusive, safe space

A classroom consists of instructors and students. We all play a role in creating a safe learning space.
Everyone should feel comfortable and supported by:
instructors (and TAs)
fellow classmates
There is ZERO TOLERANCE for:
- sexism, racism, etc.
- bullying
- inappropriate comments

‹#›

Responsibilities of the Professor

Prepare useful and interesting knowledge for you
Prepare materials before class
Come to class on time, prepared to teach
Offer challenging but reasonable homework and tests
Grade fairly without bias
Return graded work promptly with helpful comments
Goals:
- Support discussion and knowledge sharing of important concepts
- Make the class fun and engaging for everyone

‹#›

Responsibilities of the Student

Come to class on time
If you miss or opt-out of class, learn material on your own
Pay attention to all instructions
Turn in assignments on time
Ask for help when you’re confused
If you disagree with me, disagree politely
Contribute to group discussions and assignments
Goals:
- Actively participate in your academic growth
- Engage with course materials and project

‹#›

Questions?

‹#›

Software Development Lifecycle

SDLC Overview
SDLC Myths
Software Crisis
Great Software Engineers

Learning Outcomes

By the end of the course, students should be able to:
Understand software engineering processes, methods, and tools used in the software development life cycle (SDLC)
Use techniques and processes to create and analyze requirements for an application
Use techniques and processes to design a software system
Identify processes, methods, and tools related to phases of the SDLC
Explain the differences between software engineering processes
Discuss research questions and current topics related to software engineering
Create and communicate about the requirements and design of a software application

‹#›

Warm-Up

Discuss: What is your experience with software engineering (i.e. class project, full-time, or internship setting)?

‹#›

Requirements
Design
Implementation
Testing
Deployment/Maintenance
As defined in this class. Specific terms to describe phases will vary based on company, team, process, etc., but basic ideas will apply.

Software Development Life Cycle

‹#›



Requirements

Goal: Understand customer requirements for the software system
The what of the project
Very difficult to “get right” the first time and evolve over the course of development
The top reasons for project failure include:
(a) Incomplete and (b) Changing Requirements
Software Artifacts: requirements documents, use cases, user stories,...

‹#›

Design

Goal: decide the software structure and enable programmers to implement requirements by designating projected parts of the implementation
The how of the project
design: a representation or model of the software to be built
How individual classes and software components work together (Programs can have 1000s+ of classes/methods)
Software Artifacts: design documents, class diagrams,...

‹#›

Implementation

Goal: translating design into a concrete system (i.e. code)
• Can use any language, but some languages are better suited to certain types of programs than others
• Software Artifacts: source code, documentation, configuration files, media, executables, bug database, source code repository, issue trackers…

‹#›

Testing

Goal: Execute software with intent of finding errors
• While you can’t test until there is code to run, you can start planning testing when you’re analyzing the requirements
• Includes Unit (Ut) and System (St) tests to verify code and functionality
• Software Artifacts: test code, bug database, test database, test inputs and outputs, documentation,...

‹#›

Deployment/Maintenance

Goal: release, upgrade, and fix the software
deployment: delivery of software to users
When software is completed, it must be deployed to customers for usage.
• Just because you deliver your software doesn’t mean you’re done with it: Software must be maintained such that user problems are addressed after operation (next version, debugging, increased testing, refactoring, updates to requirements, etc.)
• Software Artifacts: All!

‹#›

The First Law

“No matter where you are in the system life cycle, the system will change, and the desire to change it will persist throughout the life cycle.”
[Bersoff, 1980]

‹#›

What is SE?

A discipline that encompasses:
the process of software development
methods for software analysis, design, construction, testing, and maintenance
tools that support the process and the methods
[Pressman]

‹#›

Processes, Methods, and Tools

• Various tasks required to build and maintain software
– e.g. design, testing, etc.
• SE process: the organization and management of these tasks
– various process models
• SE methods: ways to perform the tasks
• SE tools: assist in perform the tasks
– UML tools, IDEs, issue tracking tools

‹#›

SE Myths

“If we get behind schedule, we can just add more people and catch up”
• Fact: Adding more people to a late project will make it later
– The people working now must spend time educating the newcomers

‹#›

SE Myths (cont.)

“A general statement of objectives is enough to start programming”
• Fact: An ambiguous statement of objectives leads to project failures
– Unambiguous requirements need effective and continuous communication between customer and developer

‹#›

SE Myths (cont.)

“Changes in requirements are easy to deal with because software is flexible”
• Fact: Changes are harder and more expensive over a project 📈

‹#›

SE Myths (cont.)

“Once we get the program running, we are done”
• Fact: 60-80% effort comes after the software is delivered for the first time
– Bug fixes, feature enhancements, software
reengineering, migration

‹#›

SE Myths (cont.)

“Until I get the program running, I cannot assess quality”
• Fact: Software assessment methods can be applied before code is written and are very effective.

‹#›

SE Myths (cont.)

“The only deliverable work product is the running program”
• Fact: Need the entire configuration
– Documentation of system requirements, design, programming, and usage

‹#›

SE Myths (cont.)

Practitioners
• “I need to be an exceptional coder to be in software engineering.
• Fact: There are a variety of roles and skills needed to successfully develop and maintain software applications.
– Managers, QA/testers, scrum masters, UI/UX designers, business analysts, IT, customer support, data analysts, database administrators (DBA), architects, security specialists, deployment engineers,...

‹#›

Software Crisis

“The major cause of the software crisis is that the machines have become several orders of magnitude more powerful! To put it quite bluntly: as long as there were no machines, programming was no problem at all; when we had a few weak computers, programming became a mild problem, and now we have gigantic computers, programming has become an equally gigantic problem.” [Dijkstra]

‹#›

Software Crisis

• Projects running over-budget
• Projects running over-time
• Software was very inefficient
• Software was of low quality
• Software often did not meet requirements
• Projects were unmanageable and code is difficult to maintain
• Software was never delivered

‹#›

Current SE Problems

Software is too expensive and takes too long to build
Frequently over budget and over time!
Low software quality
3.6 billion users, $1.7 trillion caused by bugs [Tricentis, 2017]
Software is more complex to support and maintain
More users = more difficult to scale applications
Failing to meet requirements
Lack of diversity in software development teams
Inadequate testing and security
Ethical decisions in software engineering
What else??? [Discuss w/ someone nearby]

‹#›

Software Engineering?

‹#›

“ ‘It’s Engineering... but not as we know it’… Software Engineering - solution to the software crisis, or part of the problem? ”

[Bryant]

Software Engineers

A person who applies a systematic engineering approach to the design, development, testing, and maintenance of computer software.

‹#›

What Makes a Great Software Engineer?

Authors: Paul Luo Li, Amy J. Ko, and Jiamin Zhu
International Conference on Software Engineering (ICSE) 2015

‹#›

Good software engineers are essential for developing high-quality software…
Companies want to hire them
Universities want to train them
Students/Novices want to be them
But difficult to evaluate!
Technical skills, and beyond

Great Software Engineer (cont.)

Interviewed 59 software engineers at Microsoft.
Questions were mostly reflective
- (i.e. “Think back to someone you’ve worked with that you that was a great software engineer. What were some attributes that made the person ‘great’ in your mind?”)
Analyzed responses to derive 53 attributes of great software engineers.

‹#›

Great Software Engineer Results



‹#›

Discuss: What stands out to you? What do you agree/disagree with? What is missing?

Next Class

Software Engineering Processes
Announcements
HW0 due 1/30 before midnight
Syllabus questions, Introduction, Class setup and configuration checks

‹#›

References

Crouching Dragon, Hidden Software: Software in DOD Weapon Systems (Ferguson, IEEE Software, 2001)
Yu Huang, “Course Introduction”, “Software Engineering: Research Overview, Papers, Proposals and Presentations”, CS 8395: Advanced Topics in Software Engineering. Vanderbilt University, Fall 2023.
Bogdan Vasilescu, “Introduction”, 17-803: Empirical Methods. Carnegie Mellon University, Fall 2022.
Marc Andreessen, “Software is eating the world”. Wall Street Journal, 2011.
Taylor Kubota, “A computer scientist’s take on the CrowdStrike crash”, 2024. 
Peter Hallam, “What do programmers really do anyway”. Microsoft Developer Network, 2006.
Zachary P. Fry, et al., “Leveraging Light-Weight Analyses to Aid Software Maintenance”. 2014.
Brittany Johnson, George Mason University.

‹#›

