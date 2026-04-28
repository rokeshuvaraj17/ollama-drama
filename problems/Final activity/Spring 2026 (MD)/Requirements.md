[CS5704] Software Engineering

Dr. Chris Brown
Virginia Tech
2/5/2026

‹#›

Requirements
Engineering

Requirements Engineering
Requirements Elicitation
Requirements Analysis
Requirements Specification

Learning Outcomes

By the end of the course, students should be able to:
Implement a software system following the software life cycle phases
Develop software engineering skills working on a team project
Identify processes related to phases of the software lifecycle
Explain the differences between software engineering processes
Discuss research questions and studies related to software engineering
Communicate (via demo and writing) details about a developed software application

‹#›

Announcements

HW1 due Wednesday (2/11) before midnight
SE Processes
PM1.1 due Friday (2/13) before midnight
Requirements
Ut Prosim Points
Five due this semester
Schedule Change 🚨
2/10: Software Architecture and Design
2/12: UI Design and UX Guest Lecture: David Bates
2/17: Workshop UI Design and UX
2/19: Guest Lecture: Matt McHugh

‹#›

Project Questions

I am still wondering about what is an acceptable size of a project? If something could be done in 3 hours, would that be acceptable as a course project as long as the steps are taken? [Technically yes, but milestones will take longer than 3 hours]
How complex should the system be? [The proposed idea
How relevant should the real world problem be? [Relevant to interests/skills]
How do we determine mastery within software engineering aspects? [Project milestones—specifically requirements and design for Project 1]
How to structure work per teammate? [Team decision, ideally work would be divided evenly and adhere to team contract]
If I find a group I want to join after submitting this assignment, would it be possible to join them? [Maybe, if you join a team ASAP]
For PM 1.2, how separated should our discussions be between High-level design and Low-level Design? I ask because I believe they greatly impact each other. [Will discuss high/low level design patterns in class, but they should impact each other]
Do those initial ideas have to get one pass? [Preliminary ideas were a pass, but no]
What will happen if none of the ideas are available? [Please contact the instructor]
Is the GitHub repo only for submitting the project? [Repo for hosting code, Canvas for submissions—repository guidelines updated]

Requirements

Goal: Understand customer requirements for the software system
The what of the project
Very difficult to “get right” the first time and evolve over the course of development
Remember the Top 3 reasons for project failure:
(2) Incomplete and (3) Changing Requirements
Software Artifacts: requirements documents, use cases, user stories,...

‹#›

What are requirements?

Definition: Capabilities and conditions to which the system — and more broadly, the project — must conform. [Larman]
Focusing on the WHAT not the HOW
Should always come first in the SDLC

‹#›

Why should we care?

It is much cheaper and easier to modify software and fix bugs earlier in the SDLC.

‹#›

Requirements Are Difficult

“The hardest single part of building a software system is deciding precisely what to build. No other part of the conceptual work is so difficult as establishing the detailed technical requirements, including all the interfaces to people, to machines, and to other software systems. No other part of the work so cripples the resulting system if done wrong. No other part is more difficult to rectify later.” - Fred Brooks

‹#›

‹#›

Requirements are Difficult (cont.)



Requirements Engineering

The process of defining, understanding, documenting, and maintaining requirements.
Subset of software engineering
Introduced for the waterfall model (first phase)
“The a set of activities concerned with identifying and communicating the purpose of a software-intensive system, and the contexts in which it will be used. Hence, RE acts as the bridge between the real-world needs of users, customers, and other constituencies affected by a software system, and the capabilities and opportunities afforded by software-intensive technologies.” [Easterbrook]

‹#›

Types of Requirements

• Functional: expresses a function that an application must perform (primary focus of this lecture)
• Nonfunctional: does not involve functionality, but should be specific, quantifiable, and testable
Examples:
Usability: human factors, help documentation, etc.
– “HokieSPA must meet WCAG 2.1 AA accessibility standards, ensuring compatibility with screen readers.”
Reliability: failure frequency and recoverability
– “In case of system crash, HokieSPA should recover to an operational state within 5 minutes.”
Performance: response times, throughput, availability, resource usage, etc.
– “Page load time for any core task (i.e., registration) should not exceed 2 seconds on campus Wi-Fi.”
Supportability: adaptability, maintainability, internationalization, configurability
– “The system should detect and log 100% of critical errors for review by IT staff.”
Implementation/Constraints: resource limitations, languages, tools, hardware
– “HokieSPA must be written in .NET on a Linux server.”
…

‹#›

Requirements Engineering (cont.)

‹#›

Requirements elicitation

Requirements analysis

Requirements specification

Plan-Driven 

Agile Development

Requirements Prioritization





Requirements Elicitation

The process of identifying business needs, scope, assumptions, and risks of a project based on data from key stakeholders.
This is the main way requirements are identified.
Increases the likelihood users get what they want, and reduces the risk of project failure.
Usually an iterative process.

‹#›

Requirements Elicitation Steps

Gathering requirements
Identifying key stakeholders
Eliciting requirements from key stakeholders
Documenting and confirming requirements
Confirming the findings

‹#›

Requirements Elicitation Steps

Gathering requirements
Identifying key stakeholders
Eliciting requirements from key stakeholders
Documenting requirements
Confirming the findings

‹#›

Questions to ask

Questions to ask internally:
What is the project objective?
What problem are you trying to solve?
What is the success criteria?
Who is the target audience?
What stakeholders will be impacted by the system?
Stakeholder: Anyone who supports, benefits from, or is affected by a software project that has direct or indirect influence on its requirements. (i.e., users, clients, managers, software engineers, marketing, system administrators, testers, etc.)
What is the approval process for requirements?
…

‹#›

Requirements Elicitation Steps

Gathering requirements
Identifying key stakeholders
Eliciting requirements from key stakeholders
Documenting requirements
Confirming the findings

‹#›

Elicitation Techniques

Discovering the requirements of a system.
aka Requirements gathering

‹#›

Elicitation Techniques (Surveys)

Surveys/Questionnaires are widely prevalent.
Useful for collecting multiple types of data:
Closed-ended question example:
How satisfied are you with the current system? [1 = very dissatisfied, 5 = very satisfied]
👍 👎
😊 😐 😡 😥
True or False
Yes/No
Open-ended question example:
What are the top three features you would like to see in the new system and why?
What are the main challenges with existing approaches?
Demographic
etc.

‹#›

Surveys (cont.)

Advantages
Good during the early stages of requirements elicitation
Can incorporate multiple types of questions and data (i.e., open-ended or closed-ended questions)
More efficient way to collect information from a larger group
Disadvantages
Questions must be well-formulated to avoid redundancy and irrelevance, misunderstandings
Limited depth of knowledge acquired

‹#›

Elicitation Techniques (Interviews)

Most traditional and commonly used method
Broad questions to gain insights into user needs:
“Can you give me an example?”
“Why is that important to you?”
“How would you prefer it to work?”
Advantages
Rich collection of information
Good for uncovering opinions, feelings, goals, as well as facts
Can be structured or unstructured
Disadvantages
Large amount of qualitative data can be hard to analyze
Hard to compare different respondents
Interviewing is a difficult skill to master

‹#›

Elicitation Techniques (Group)

Interviews can be done in individual or group settings (e.g., Brainstorming, Focus Groups, etc.)
Advantages
More natural interaction between people than formal interview
Can gauge reaction to stimulus materials (e.g. mock-ups, storyboards, etc)
Disadvantages
May create unnatural groups (uncomfortable for participants)
Danger of Groupthink
May only provide superficial responses to technical questions
Requires a highly trained facilitator

‹#›

Elicitation Techniques (Task-Based)

Using a prototype to gather detailed insights into how users interact with a potential system.
This can be done with low-fidelity (e.g., sketches or wireframes) or high-fidelity (interactive) prototypes.
Advantages
Task analysis can contextualize requirements
Visual aids
What you see is what you get (WYSIWYG) approach
Disadvantages
WYSIWYG approach
Depends on prototype quality
Closer, but still lacks real-world insights

‹#›

Structuring Tasks

Define the task to be analyzed.
Key tasks the users will perform with the system
Break tasks into subtasks.
Ex) For an e-commerce platform. Purchasing an item = search for item, add to card, review cart, checkout,...
Create and present the prototype
Ensure the prototype simulates the task(s) to be performed
Observe users walkthrough and interaction
Monitor behavior and use think-aloud/ask questions to observe thought process
Collect feedback

‹#›

Elicitation Techniques (Ethnography) 🔎

The best way to get requirements is to observe the current state of the problem you are trying to solve in a natural setting.
Advantages
Contextualized
Reveals details that other methods cannot
Disadvantages
Extremely time consuming!
Resulting “rich picture” is hard to analyze
Cannot say much about the results of proposed change

‹#›

Requirements Elicitation Steps

Gathering requirements
Identifying key stakeholders
Eliciting requirements from key stakeholders
Documenting requirements
Confirming the findings

‹#›

What to do with results?

Questions to ask yourself:
Functional Requirements
What are the key functions or features the system should provide?
What are the "must-have" vs. "nice-to-have" features?
Are there specific deadlines or timeframes for delivery?
…
Non-functional Requirements
What is technologically feasible to build?
What performance standards are expected (e.g., response time)?
Are there any security requirements?
What data needs to be captured, stored, and processed?
Does the system need to integrate with any other systems or tools?
What support or maintenance will be required post-launch?
…
Requirements Analysis and Specification!

‹#›

Class Activity

With your project group, you have n minutes complete the following:
Create an initial mechanism for requirements elicitation for your initial project idea (i.e., interview questions, survey, tasks, etc.). Include at least 5 questions.
When you finish, swap with another group to get feedback on your questions for eliciting requirements for your system. Feedback could include but is not limited to: What could be improved? What questions are missing? Wording,...
Submit the following on Canvas [this will be graded for attendance]:
The method you selected for requirements elicitation and why
The name/members of the team you swapped with.
A summary of the feedback on your preliminary devised questions.
[If you used AI] The AI tool, prompt, and a review of the generated questions.
Due: before the end of class today (submit whatever you complete)
Note: You will need to do requirements elicitation for Project Milestone 1.1!
Note’s Note: No, this does not count towards the required responses for PM1.1! 

‹#›

Requirements Analysis

Requirements analysis is a crucial process in software engineering that involves understanding, documenting, and managing the needs and expectations of stakeholders for a system or project. This phase serves as the foundation for designing and building software that meets the desired goals and functionality. The primary goal is to ensure that the development team clearly understands what the system should do and how it should perform.
Prevents misunderstandings: Ensures developers and stakeholders are on the same page.
Reduces risks: Properly defined requirements reduce the risk of project failure or rework.
Improves project planning: Clear requirements help in more accurate estimation of time, cost, and resources.
Enhances customer satisfaction: Building software that meets the user's needs leads to higher satisfaction and success rates.

‹#›

Running Lecture Example

Standup Bot: A software bot to automatically schedule standup meetings between teammates. 🤖
Scrum master: Professional to ensure scrum processes for development team

‹#›

Use Case

Definition: a written description of using the system to fulfill stakeholder goals.
Use case modeling is the traditionally the most widely used approach for requirements analysis.
Useful for providing input into many subsequent software engineering activities and artifacts.
Different levels of formality
Brief: one-paragraph ror the main success scenario
Casual: multiple paragraphs that cover several scenarios
Fully dressed: all steps and variations (see following slides)

‹#›

Use Case (cont.)

A use case is a collection of related success and failure scenarios that describe the actor using a system to support a goal.
Actor: something with a behavior
Person, computer system, organization
Primary, supporting, offstage (interest in behavior)
Scenario (use case instance): a specific sequence of actions and interactions between actors and the system.

‹#›

Writing a Use Case

Preconditions: What must always be true
Often the postconditions of another use case
Should always be something noteworthy
“The system has power” is not interesting
“Scrum master is identified and authenticated” ✅
Postconditions: State what must be true after the completion of the use case—including success or alternative scenarios
Ex) Meeting is requested by authorized user, Date is correctly calculated, Bot has access to developer schedules, Scrum Meeting recorded, Calendar invitation is generated and sent to team,...

‹#›

Basic Flow

An interaction between actors
A validation (usually by the system)
A state change by the system
Extensions or branches should be deferred to an alternate section.
Often comprise the majority of text
Indicate all the other scenarios or branches, both success and failure

‹#›

Example: Stand-Up Bot

Use Case: Create a meeting
1 Preconditions
User must have google calendar api tokens in system.
…
2 Main Flow
User will request meeting and provide list of attendees [S1]. Bot will provide possible meeting times and user confirms [S2]. Bot creates meeting and posts link [S3].
3 Subflows
[S1] User provides /meeting command with @username,@username list.
[S2] Bot will return list of meeting times. User will confirm time.
[S3] Bot will create meeting and post link to google calendar event.
4 Alternative Flows
[E1] No team members are available.
…

‹#›

Use Case Diagrams

A visual representation of interactions between actors and the system

‹#›

Actor

Interactions

<>

System



System Behavior

Create use case diagram

<>

<>

Use Case Diagrams (cont.)

Interactions

<>

<>

Association: relation between an actor and a use case

Includes dependency: a base use case
includes a sub use case as component

Extends dependency: a use case extends
the behavior of a base use case.

‹#›



Example: Stand-Up Bot

‹#›

Scrum master



Find Meeting Times

Requests meeting

Receives availability list

Confirms time



Creates calendar event, sends invite, generates zoom link, etc.

Software
Engineer



Example: Stand-Up Bot (cont.)

‹#›

Scrum master



Search for Meeting Times

Requests meeting

Receives availability list

Confirms time



Create Meeting

Software
Engineer





Generate Zoom link



Create calendar invite

<>

<>

<>



Check
availability

If time is available for all

Sequence Diagram

A notation to illustrate, for a given use case, the events that external actors generate, their order, and inter-system events
Allows for more advanced computational interaction (i.e., conditional statements, loops, etc.)

‹#›

Object

Actor



Activation box: represents time needed to for object to complete a task

[condition]

Return message

message/data

Diagrams: Use Case vs. Sequence

Sequence diagrams can:
Present the behavior of the code
Describes how—and in what order—a group of actors or objects work together.

‹#›

Revisit Stand-Up Bot Use Case

Use Case: Create a meeting
1 Preconditions
User must have google calendar api tokens in system.
2 Main Flow
User will request meeting and provide list of attendees [S1]. Bot will provide possible meeting times and user confirms [S2]. Bot creates meeting and posts link [S3].
3 Subflows
[S1] User provides /meeting command with @username,@username list.
[S2] Bot will return list of meeting times. User will confirm time.
[S3] Bot will create meeting and post link to google calendar event.
4 Alternative Flows
[E1] No team members are available.
…

‹#›



Example: Stand-Up Bot

‹#›

Scrum master

requestMeeting

Bot



Google API

checkAvailability

response





[if true]

[else]

createZoomLink

sendCalendarInvite

sendMessage

‹#›

Requirements Specification

How we communicate Requirements to others

Purpose
Communication
explains the application domain and the system to be developed
Contractual
May be legally binding!
Expresses agreement and a commitment
Baseline for evaluating the software
supports testing, V&V
“enough information to verify whether delivered system meets requirements”
Baseline for change control

Audience
Customers & Users
interested in system requirements…
...but not detailed software requirements
Systems (Requirements) Analysts
Write other specifications that inter-
relate
Developers, Programmers
Have to implement the requirements
Testers
Have to check that the requirements have been met
Project Managers
Have to measure and control the project

Analysis vs. Specification

• Analysis: process of understanding the problem and the requirements for a solution
• Specification: process of describing what a system will do
Analysis leads to Specification – they are not the same!

‹#›

Software Requirements Specification (SRS)



‹#›

‹#›











SRS Approaches

SRS will differ based on your project, team, etc.
Consider two different projects:
Project A) Tiny project, few programmers, few months of work
programmer talks to customer, then writes up a 2-page memo, user stories
Project B) Large project, 50+ programmers, multiple years of work
team of analysts model the requirements, then document them in a 500-page SRS document

‹#›

IEEE Standard



‹#›

IEEE Standard: Section 3

3.1 External Interface Requirements
3.1.1 User Interfaces
3.1.2 Hardware Interfaces
3.1.3 Software Interfaces
3.1.4 Communication Interfaces
3.2 Functional Requirements
(this section organized by mode, user class, feature, etc…)
For example:
3.2.1 Mode 1
3.2.1.1 Functional Requirement 1.1
...
3.2.2 Mode 2
3.2.1.1 Functional Requirement 1.1
...
...
3.2.2 Mode n
...

‹#›

3.3 Performance Requirements
Remember to state this in measurable
terms!
3.4 Design Constraints
3.4.1 Standards compliance
3.4.2 Hardware limitations
etc.
3.5 Software System
Attributes
3.5.1 Reliability
3.5.2 Availability
3.5.3 Security
3.5.4 Maintainability
3.5.5 Portability
3.6 Other Requirements

[Adapted from IEEE-STD-830-1993. See also, Blum 1992, p160]

Real-World Example

FBI Virtual Case File (VCF) Project
In 2000, the FBI began working on the Virtual Case File (VCF) system as part of a larger Trilogy Project to modernize their IT infrastructure. This project was contracted by Science Applications International Corp (SAIC) and intended to replace paper-based processes for managing investigations and intelligence. However, by 2005, the project was abandoned after consuming over $170 million.
What went wrong?

‹#›

[Centre for Public Impact]

Real-World Example

FBI Virtual Case File (VCF) Project
What went wrong? Poorly defined and specified requirements!
The developers/FBI lacked a clear understanding of processes and complex needs, which resulted in a system that was neither functional nor usable.
Ambiguity: Vague requirements, such as…
“Help FBI agents efficiently share data about cases in progress, especially terrorist investigations”
“Enable agents anywhere in the US quickly to search various documents and allow them to connect possible leads from different sources”
“Provide a case management system, an evidence management system, and a records management system to eliminate the need for FBI employees to scan hard-copy documents into computer files.”
Over-specification: “stop building a web front end to the FBI's existing systems and instead begin development of a new application to replace the old ACS”
Wishful thinking: “In January 2002, the FBI requested an additional $70 million from Congress to accelerate the Trilogy project, but received $78 million. SAIC agreed to deliver the VCF system in December 2003 rather than June 2004.”
But, “Trilogy's scope grew by about 80 percent [from the] initiation of the project.”
And many more…

‹#›

[Centre for Public Impact]

Iterative SRS

Agile methods →little/no documentation!
User Stories
Stakeholder-based scenarios with explicit acceptance criteria
“Writing good user stories is essential in software projects, as they convey the needs and perspectives of users and guide the development team in implementing the expected functionalities” [Zhang]
User story is determined to be finished when it meets acceptance criteria.

‹#›

Writing a User Story

Written from the point of view of a stakeholder
User personas to describe interactions

“As a [persona type/stakeholder], I want to [action] so that [benefit].”

‹#›

Running Example

Standup Bot: A software bot to automatically schedule standup meetings between teammates.
Scrum master: Professional to ensure scrum processes for development team



‹#›

Example User Story: Stand-Up Bot

As a Scrum Master, I want to find availability with a list of usernames so that I can schedule team daily stand-ups.
Acceptance criteria:
Given Scrum Master has admin permissions
When Scrum Master types team member usernames
And 
Then System finds list of available times between users

‹#›

User stories vs. Use cases

“A user story is to a use case as a gazelle is to a gazebo” [Cockburn]
They sound similar, but are very different.
Use case: Description of ways a user may want to interact with the system (business).
Includes goal, actors, preconditions, steps, alternatives, and postconditions
User story: Who, what, and why of a goal or outcome that the user wants to achieve (user).
Meant to be as simple as possible

‹#›

Requirements Engineering and AI

There is considerable optimism/concern over LLMs for code generation and SE processes, but what about requirements engineering?

‹#›

AI for Generating Elicitation ?s

AI is increasingly used for generating requirements elicitation questions.
LLMREI: Automating Requirements Elicitation Interviews with LLMs
Alexander Korn, Samuel Gorsch, Andreas Vogelsang

‹#›

Captured 70% of intended requirements.

AI for Analyzing Elicitation Results

LLMs are great at annotating data ✅

‹#›

Transcription
Summarization
Analysis
etc.

AI for Eliciting Requirements

LLMs can provide insights on requirements for systems…

‹#›

[Atai]

Centaur: a model to “predict and simulate human behaviour in any experiment expressible in natural language” [Bowers]
Requirements Simulator

[White]

AI for Eliciting Requirements (cont.)

But not at the same level as humans ⚠️

‹#›

Large Language Models Do Not Simulate Human Psychology Schröder, Morgenroth, Kuhl, et al.

Can ChatGPT emulate humans in software engineering surveys? Steinmacher, Penney, et al.

“Our findings reveal that ChatGPT can successfully replicate the outcomes of some studies, but in others, the results were not significantly better than a random baseline.”

AI and Requirements Artifacts

LLMs are mostly good at generating and refining requirements artifacts.
LLM-Based Agents for Automating the Enhancement of User Story Quality: An Early Report Zheying Zhang, Maruf Rayhan , Tomas Herda, Manuel Goisauf, and Pekka Abrahamsson
Using LLMs in Software Requirements Specifications: An Empirical Evaluation
Madhava Krishna, Bhagesh Gaur, Arsh Verma, Pankaj Jalote

‹#›

“The experiment demonstrates that LLMs may facilitate a significant reduction in development time for entry-level software engineers. Hence, we conclude that the LLMs can be gainfully used by software engineers to increase productivity by saving time and effort in generating, validating and rectifying software requirements.”

AI and Requirements Artifacts

However, concerns remain.
Hallucinations
“Additionally, most LLMs are also prone to hallucinations in their responses.” [Krisha, SRS]
Length
Developers expressed “concerns over the increased length and complexity of [artifacts] generated by the GPT-4 model” [Zhang, user stories]
Practicality

‹#›

[Yamani]

Next Class…

‹#›

Software Architecture and Design
Announcements
HW1 due Wednesday (2/11) before midnight
SE Processes
PM1.1 due Friday (2/13) before midnight
Requirements

References

Mohammadmehdi Ataei, Hyunmin Cheong, Daniele Grandi, Ye Wang, Nigel Morris, and Alexander Tessier. "Elicitron: A large language model agent-based simulation framework for design requirements elicitation." Journal of Computing and Information Science in Engineering. Feb 2025.
Toufique Ahmed, Premkumar Devanbu, Christoph Treude, and Michael Pradel. 2024. Can LLMs replace manual annotation of software engineering artifacts? arXiv preprint arXiv:2408.05534 (2024)
Jeffrey S Bowers, Guillermo Puebla, Sushrut Thorat, Konstantinos Tsetsos, and Casimir Johannes Hendrikus Ludwig. Centaur: A model without a theory, July 2025. URL https://osf.io/v9w37\_v3.
Korn, Alexander, Samuel Gorsch, and Andreas Vogelsang. "LLMREI: Automating Requirements Elicitation Interviews with LLMs." arXiv preprint arXiv:2507.02564 (2025).
Sarah Schröder, Thekla Morgenroth, Ulrike Kuhl, Valerie Vaquet, and Benjamin Paaßen. “Large Language Models Do Not Simulate Human Psychology”. arXiv preprint arXiv:2508.06950 (2025).
Igor Steinmacher, Jacob Mcauley Penney, Katia Romero Felizardo, Alessandro F. Garcia, and Marco A. Gerosa. "Can ChatGPT emulate humans in software engineering surveys?." In Proceedings of the 18th ACM/IEEE International Symposium on Empirical Software Engineering and Measurement, pp. 414-419. 2024.
Madhava Krishna, Bhagesh Gaur, Arsh Verma, Pankaj Jalote. “Using LLMs in Software Requirements
Specifications: An Empirical Evaluation”. International Requirements Engineering Conference, 2024.
Asma Yamani, Malak Baslyman, and Moataz Ahmed. "Leveraging LLMs for User Stories in AI Systems: UStAI Dataset." In Proceedings of the 21st International Conference on Predictive Models and Data Analytics in Software Engineering, pp. 21-30. 2025.
Aaron Conrardy. “From Image to UML: First Results of Image Based Class Diagram Generation Using LLMs”. Modeling Languages. https://modeling-languages.com/image-to-uml-with-llm/
Priya Pedamkar. “Types of UML Diagrams”. https://www.educba.com/types-of-uml-diagrams/
Zheying Zhang, Maruf Rayhan, Tomas Herda, Manuel Goisauf, and Pekka Abrahamsson. “LLM-Based Agents for Automating the Enhancement of User Story Quality: An Early Report”. In International Conference on Agile Software Development, 2024.
Steve Easterbrook (University of Toronto)
Sarah Heckman (NC State)
Na Meng and Barbara Ryder (VT)

‹#›

