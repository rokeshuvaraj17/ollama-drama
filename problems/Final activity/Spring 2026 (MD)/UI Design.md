[CS5704] Software Engineering

Dr. Chris Brown
Virginia Tech
2/17/2026

‹#›

Announcements

HW2 due Friday (2/20) at 11:59pm
Requirements and Design activities
PM1.2 due next Wednesday (2/25) at 11:59pm
Project 1 Design milestone
Next Class
Guest Lecture: Matt McHugh
No office hours this afternoon 🚫

‹#›

UI/UX
Design

User Interfaces
Design Heuristics
UI Design Processes

Learning Outcomes

By the end of the course, students should be able to:
Implement a software system following the software life cycle phases
Develop software engineering skills working on a team project
Identify processes related to phases of the software lifecycle
Explain the differences between software engineering processes
Discuss research questions and studies related to software engineering
Communicate (via demo and writing) details about a developed software application

‹#›

Warm-Up

Which software application do you find has the most user-friendly interface, and why? Which applications do you find the least user-friendly?

‹#›

Design

Goal: decide the structure of the software and the hardware configurations that support it.
The how of the project
How individual classes and software components work together in the software system.
User interfaces, structural elements, and data
Software Artifacts: design documents, class diagrams (i.e. UML)

‹#›

Review: High-Level Design

Goal: Design the overall shape and structure of the program to reduce risks and meet requirements.
Common program structures:
Pipe and Filter
Event-based
Layered
Client-Server
Data-Centric
Model-View-Controller (MVC)
Microservices

‹#›

Review: Low-Level Design

Goal: To decompose subsystems into modules
Object-Oriented Design Principles
Modularity, Cohesion and Coupling, Information Hiding, Abstraction and Refinement, S.O.L.I.D.
Design Patterns
Working solutions to identify classes and instances, their roles and collaborations, and responsibilities i a particular context.
Creational, Structural, and Behavioral Pattern Families.

‹#›

Review: Database Design

A digital database with a collection of tables.
Each table contains rows and columns, with a unique key for each row
Each entity described in a database has its own table
Each row represents an instance of the entity
Each column represents an attribute
Entity-Relationship (ER) Diagrams model database designs

‹#›

User Interfaces

The way users interact with the system
Medium between human and computer
A very important part of software design
All software has a user interface!
User experience (UX): software should provide meaningful and relevant experiences to users beyond the look and feel (UI)
Affordances: Property of an object that defines its possible uses
products should make clear how they should be used

‹#›

Why Focus on UIs?

Software engineering is about meeting user needs.
Requirements engineering
But if you build the wrong software…

‹#›

Developers & Users

Why Focus on UIs? (cont.)



‹#›

Design

Interface

Usability

Usability: How well users can use a system’s functionality
Dimensions of usability
Learnability: is it easy to learn?
Efficiency: once learned, is it fast to use?
Visibility: is the state of the system visible?
Errors: are errors few and recoverable?
Satisfaction: is it enjoyable to use?

‹#›

UI Design

UI design is not just about “graphic design” or aesthetics.

‹#›

“Design is about leveraging principles about humans (psychology) to build interactions people can use”[Coblenz]

UI Design (cont.)

How do you build software that people can actually use?
UI/UX research methods
Apply principles of HCI
Iterative and user-centered design processes
Hire a UI/UX designer

‹#›

‹#›















[https://www.nngroup.com/articles/ux-research-cheat-sheet/]

Ten Usability Heuristics

Visibility of system status
Match between system and the real world
User control and freedom
Consistency and standards
Error prevention
Recognition rather than recall
Flexibility and efficiency of use
Aesthetic and minimalist design
Help users recognize, diagnose, and recover from errors
Help and documentation [Nielsen]

‹#›

1. Visibility of System Status

The design should always keep users informed about what is going on, through appropriate feedback within a reasonable amount of time.

‹#›

2. Match Between System and Real World

The design should speak the users' language. Use words, phrases, and concepts familiar to the user, rather than internal jargon. Follow real-world conventions, making information appear in a natural and logical order.

‹#›

Commonly used for save functionality, however floppy disks have been obsolete since 2001! 💾

3. User Control and Freedom

Users often perform actions by mistake. They need a clearly marked "emergency exit" to leave the unwanted action without having to go through an extended process.

‹#›

4. Consistency and Standards

Users should not have to wonder whether different words, situations, or actions mean the same thing. Follow platform and industry conventions.

‹#›

5. Error Prevention

Good error messages are important, but the best designs carefully prevent problems from occurring in the first place. Either eliminate error-prone conditions, or check for them and present users with a confirmation option before they commit to the action.

‹#›

“Upgrades cannot be refunded…”

6. Recognition Rather than Recall

Minimize the user's memory load by making elements, actions, and options visible. The user should not have to remember information from one part of the interface to another. Information required to use the design (e.g. field labels or menu items) should be visible or easily retrievable when needed.

‹#›

7. Flexibility and Efficiency of Use

Shortcuts — hidden from novice users — may speed up the interaction for the expert user so that the design can cater to both inexperienced and experienced users. Allow users to tailor frequent actions.

‹#›

Make text bold:
Ctrl-B



8. Aesthetic and Minimalist Design

Interfaces should not contain information that is irrelevant or rarely needed. Every extra unit of information in an interface competes with the relevant units of information and diminishes their relative visibility.

‹#›

9. Help Users Recognize, Diagnose, and Recover from Errors

Error messages should be expressed in plain language (no error codes), precisely indicate the problem, and constructively suggest a solution.

‹#›

10. Help and Documentation

It’s best if the system doesn’t need any additional explanation. However, it may be necessary to provide documentation to help users understand how to complete their tasks.
Proactive (i.e., tutorials, documentation) and reactive (i.e., FAQ, troubleshooting) help

‹#›

🚫

Iterative UI Design

Designing usable software is an iterative process.
Often will not get it right the first time

‹#›

1. Understand your users
2. Create a prototype
3. Evaluate/get feedback
4. Go to step 1

Plan-Driven Usability

Waterfall processes are bad for usability engineering and user interface design!
UI design is risky
Often will not get it right the first time
Users are often not involved until acceptance testing
No feedback until the end
UI flaws often cause changes in requirements
Throw away carefully-written and tested code, or deploy with a bad UI

‹#›

Iterative Design of UIs

Iterative Design the Wrong Way:
Every iteration corresponds to a release
Feedback (complaints) feed into the next version design for the next iteration.
Evaluation of prototypes
Learn from past mistakes
Using (paying) users to evaluate usability
They won’t like it
They won’t buy version 2

‹#›

Iterative Design of UIs

Build room for several iterations in UI design processes.
Making early iterations as cheap as possible
Early prototypes can detect usability issues
Parallel Design is feasible: build and test multiple prototypes
Later iterations use richer implementation after UI risk is mitigated
More iterations generally means better UI
Mature iterations deployed to users

‹#›



User-Centered Design

Early focus on users and tasks
User analysis: who are the users
Task analysis: what do they need to do
Involve users as evaluators, consultants, and even designers
Constant evaluation
Users involved in every iteration 

‹#›

Universal Design

A school of thought that seeks to design for all users, as much as possible
As opposed to designing for the typical user.
Should not involve “dumbing down” interfaces, but make design better for everyone.
Guidelines for Universal/Accesible Design
Section 508 rules: https://www.section508.gov/
World Wide Web Content (WC3) Accessibility Initiative: https://www.w3.org/TR/WAI-WEBCONTENT/

‹#›

UI Design Processes

 DISCOVER
Bodystorming
Cognitive walkthrough
Contextual inquiry
Design studio
Dot voting
Heuristic analysis
KJ method
Metrics definition
Stakeholder and user interviews

 DECIDE
Affinity diagramming
Comparative analysis
Content audit
Design principles
Journey mapping
Mental modeling
Personas\*
Site mapping
Storyboarding\*
Style tiles
Task flow analysis\*
User scenarios

 MAKE
Design pattern library
Prototyping\*
Wireframing\*

 VALIDATE
Card sorting
Multivariate testing
Usability testing
Visual preference testing

‹#›

Decide: Personas

A persona is arch-user type which represents a segment of a user population, and allows role-play during task planning and UX design.

‹#›

Decide: Storyboarding

A storyboard illustrates the timeline of user performing a task as a sequence of frames.

‹#›

Useful tools:
Storyboarder
Plot
FrameForge
Miro
Canva
StoryboardThat
...

Decide: Task Flow Analysis

A flow map describes the wayfinding activity of a user and transitions between UI states.

‹#›

Make: Prototyping

Prototype involves clients, design quickly and iteratively before implementation.





‹#›

Useful tools:
Figma
Miro
App Builder
Adobe XD
Balsamic
Usability Hub
...

Make: Prototyping (cont.)

In the past, companies adopted a process known as “paper prototyping”.

‹#›

Make: Wireframes

A wireframe is a view schematic that captures all layout and content decisions of that view.
How will you allocate space for particular content?
Where will content live?
What actions can you do?

‹#›

The User Interface is Important

UIs strongly affect the perception of software
Usable software sells better
Unusable software is abandoned
Costly to get the user interface wrong
Users’ time is not cheap
Design it correctly now, or pay for it later

‹#›

But User Interface Design is Hard…

‹#›

Many different types of users…
Different expectations…
Different experiences…
Different goals…
Different abilities…
“Good” design is relative
Evolving technology/interaction norms
Increased digital literacy
Perception can be superficial
The user is always right
…but the user is not always right either
You are not the user!

Usability is only one attribute

Software designers have a lot of other factors to worry about:

‹#›

– Usability
– Functionality
– Cost
– Performance

– Size
– Reliability
– Security
– Accessibility…

Many design decisions in software involve tradeoffs between different attributes.

Class Activity

Work with your project group to:
Brief standup meeting
Use paper prototyping to brainstorm ideas for how at least one interface/feature of your proposed system will look (I forgot to bring the paper, so can skip this step).
[If AI] Use an AI tool to generate a UI design (prototype, wireframe, or storyboard). Provide the prompt(s) provided and which AI tool.
[If !AI] Use an online tool to generate a digital design (prototype, wireframe, or storyboard) of the feature.
Swap with another group/classmate to get feedback on the prototype design (in particular based on the ten usability heuristics).
Demo for entire class? (if time)
Submit the following on Canvas:
Digital UI design(s)
Standup meeting
Summary of feedback
Due: before the end of class today (submit whatever you complete)

‹#›

Next Time…

Guest Lecture on Thursday
Matt McHugh

‹#›

References

RS Pressman. “Software engineering: a practitioner's approach”.
Cast Software “What is Software Architecture?”. 
K.D. Cooper, L. Torczon, “Engineering a Compiler”.Theo Mandel. “Golden Rules of User Interface Design”. 

Na Meng and Barbara Ryder
Chris Parnin
Sarah Heckman

‹#›

