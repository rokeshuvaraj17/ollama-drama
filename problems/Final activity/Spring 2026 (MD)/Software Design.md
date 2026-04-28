[CS5704] Software Engineering

Dr. Chris Brown
Virginia Tech
2/10/2026

‹#›

Software Architecture and Design

Design Overview
UML Diagrams
Low-Level Design
High-Level Design

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

HW1 due tomorrow before midnight
SE Processes
PM1.1 due Friday (2/13) before midnight
Requirements
Schedule Change 🚨
2/12: UI Design and UX Guest Lecture: David Bates
2/17: Workshop UI Design and UX
2/19: Guest Lecture: Matt McHugh
…
4/30: Discussion Guest Lecture: Andy Bond

‹#›



Warm-Up: Stand-up Meeting

Since the last stand-up meeting, discuss:
What you did.
What you need to do next.
What is blocking you.
- Standing is optional

‹#›

Design

Goal: decide the structure of the software and the hardware configurations that support it.
The how of the project
How individual classes and software components work together in the software system.
User interfaces, structural elements, and data
Software Artifacts: design documents, UML (i.e. class diagrams), prototypes, etc.

‹#›

Design (cont.)

Encompasses the set of concepts, principles, and practices that lead to the development of high-quality systems.

‹#›

How Do Developers Design Software?

Code
Design-while-coding 😥
Iterative and evolutionary design
Diagrams and modeling
UML
Class diagrams
Sequence diagrams
Reuse or modify existing design models
High-level: Architectural patterns
Low-level: Design patterns

‹#›

Diagrams

Drawing and diagramming are essential tasks in software development…

‹#›

Types of Diagrams

Software Design
Class Diagrams\*
Sequence Diagrams
Use Case Diagrams
…
Interface Design (next week)
Wireframes
Flow Maps/Navigation Maps
Storyboards
… and many more!

‹#›

UML

Unified Modeling Language (UML) is a standard for modeling object-oriented software.
Currently on version 2.0
Typically depicted with two types of diagrams
Structural (i.e. class diagrams)
Behavioral (i.e. use case and sequence diagrams)

‹#›



Review: Use Case Diagram

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



Review: Sequence Diagram

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

Class Diagram

A visual representation of main objects and their relations for a system.
– Domain objects or conceptual classes
– Relationship between conceptual classes
– Attributes of conceptual classes
Elements
Classes containing: Attributes, Operations
Various relationships: Association, Aggregation, Composition, Generalization

‹#›

Role of Class Diagrams

Build upon use case diagrams
More emphasis on relationship
Basis for design and implementation
Starting to move toward system design and implementation
The most important and classic model in OO analysis

‹#›

Class Diagram Example



Class name: abstract concept

Attributes: properties relevant to the use case

Operation (Method signatures): behaviors of the class

Generalization: “is-a” relationship. A sub-class inherits all attributes and operations of its super class.

Aggregation: “has-a” relationship. The container and elements can exist independently from each other

‹#›

Building a Class Diagram

• Step 1: Identify conceptual classes
• Step 2: Decide attributes
• Step 3: Identify associations between classes
Note: Step 1 and 2 may occur together, iteratively

‹#›

Class Diagram Example



‹#›



How is UML Really Used?

“UML has been described by some as ‘the lingua franca of software engineering’. Evidence from industry does not necessarily support such endorsements. How exactly is UML being used in industry – if it is? This paper presents a corpus of interviews with 50 professional software engineers in 50 companies and identifies 5 patterns of UML use.” [Petre]

Of those that reported using it…

‹#›

TODO: How do you design coding projects?

Design Practices

High-level: Architecture design
Define major components and their relationship
Low-level: Detailed design
Decide classes, interfaces, and implementation algorithms for each component

‹#›

Low-Level Design

Goal: To decompose subsystems into modules
Two approaches:
Procedural:
System is decomposed into functional modules which accept input data and transform it to output data
achieves mostly procedural abstractions
2. Object-oriented
System is decomposed into a set of communicating objects (achieves procedural + data abstractions)
SOLID design principles

‹#›

S.O.L.I.D. Principles of OOD

• S – Single-responsibility principle
• O – Open-closed principle
• L – Liskov substitution principle
• I – Interface segregation principle
• D – Dependency Inversion Principle

‹#›

Example

Creating software for a Pizza Store 🍕

‹#›

Discuss: What is wrong with this design?

Example

Problems…
– Client (PizzaStore) invokes different pizza constructors among other responsibilities
– New pizza types may be added
• Clam, Veggie, etc.
– New order types may be added
• In Store, Delivery, etc.
– Original pizza types may be removed
• Greek, etc.
– Different styles of pizza
• Chicago, NY, Stuffed crust, etc.
– …

‹#›

Design Patterns (i.e. Low-Level Design)

Design patterns are descriptions of communicating objects and classes that are customized to solve a general design problem in a particular context.The design pattern identifies the participating classes and instances, their roles and collaborations, and the distribution of responsibilities.

‹#›

Design Patterns (cont.)

Why design patterns?
Appy working solutions to approaches
Based on the implementations of many systems
Capture and pass on the knowledge of experienced designers
Useful for inexperienced
Communicating about design

Gang of Four

Design Pattern Families

Creational Concerned with the process of object creation
Increases flexibility and reuse of code
StructuralDeal with the composition of classes or objects
Organizing different classes and modules to form larger structures or add new functionality
BehavioralCharacterize the ways in which classes or objects interact and distribute responsibility
Algorithms and assignment of responsibilities between objects

‹#›

Creation Patterns
Abstract Factory: Creates an instance of several families of classes
Builder: Separates object construction from its representation
Factory Method: Creates an instance of several derived classes
Object Pool: Avoid expensive acquisition and release of resources by recycling objects that are no longer in use
Prototype: A fully initialized instance to be copied or cloned
Singleton A class of which only a single instance can exist

Structural Patterns
Adapter: Match interfaces of different classes
Bridge: Separates an object’s interface from its implementation
Composite: A tree structure of simple and composite objects
Decorator: Add responsibilities to objects dynamically
Facade: A single class that represents an entire subsystem
Flyweight: A fine-grained instance used for efficient sharing
Private Class Data: Restricts accessor/mutator access
Proxy: An object representing another object

Behavioral Patterns
Chain of responsibility: A way of passing a request between a chain of objects
Command: Encapsulate a command request as an object
Interpreter: A way to include language elements in a program
Iterator: Sequentially access the elements of a collection
Mediator: Defines simplified communication between classes
Memento: Capture and restore an object's internal state
Null Object: Designed to act as a default value of an object
Observer: A way of notifying change to a number of classes
State: Alter an object's behavior when its state changes
Strategy: Encapsulates an algorithm inside a class
Template method: Defer the exact steps of an algorithm to a subclass
Visitor: Defines a new operation to a class without change

‹#›

Example Solution: Pizza Factory

Encapsulate object creation

‹#›

Discuss: What is wrong with this design?
Increased maintenance effort
Pizza class violates Single Responsibility Principle
The cut and box methods do not depend on Pizza type
…

Architectural (High-Level) Design

Design overall shape & structure of system
the components
their externally visible properties
their relationships
Goal: choose architecture to reduce risks in software construction and meet requirements.

‹#›

Common Architecture Patterns

Pipe & Filter Architecture
Event-based Architecture
Layered Architecture
Microservices

‹#›

Pipe and Filter

A pipeline contains a chain of data processing elements
–The output of each element is the input of the next element

‹#›

Event-Based Architecture

Promotes the production, detection, consumption of, and reaction to events
Event-driven programming

‹#›

Layered/Tiered Architecture

Multiple layers are defined to allocate responsibilities of a software product
The communication between layers is hierarchical.

‹#›

Layered/Tiered (cont.)

Variants: 2-layer architecture

Data-centric Architecture
Data accessed frequently
Notifications to subscribers

Client-Server Architecture
Multiple hardwares
Partition tasks or workloads between providers and consumer

Ex) most web-based applications, version control system, etc.

‹#›

Layered/Tiered (cont.)

Variants: 3-layer architecture
Model-View-Controller
UI to interact with users
Store and retrieve information as needed

‹#›

Microservices

The microservices pattern involves creating multiple applications—or microservices—that work interdependently. Although each microservice can be developed and deployed independently, its functionality is interwoven with other microservices.

‹#›

‹#›

Uber

Netflix

Amazon

How to Do Architecture Design?

When decomposing a system into subsystems, take into consideration:
how subsystems share data
– data-centric or data-distributed
how control flows between subsystems
– as scheduled or event-driven
how they interact with each other
– via data or via method calls

‹#›

Architecture Design Process





‹#›



Database Design

Modern software is collecting and processing increasing amounts of data (data-centric).
What is a database?
A system that stores data, and lets you create, read, update, and delete the data
Ex) files, spreadsheets, XML, relational, noSQL,...
Why use databases?
Every non-trivial application uses databases to keep program states and to store manipulate, and retrieve data
Databases plays a critical role in applications
– Corrupted data => execution failure
– Poor data organization => poor performance
A poorly designed database allows developers and users to put in arbitrary data (i.e. “none” as a phone number) or access data without authorization!

‹#›

Relational Databases

A digital database with a collection of tables.
Each table contains rows and columns, with a unique key for each row
Each entity type described in a database has its own table
E.g., “Employee”, “Item”, “Order”
Each row represents an instance of the entity
E.g., “John Jenny”, “Soap”
Each column represents an attribute
E.g., “phone number”, “price”

‹#›

Relational Databases (cont.)

Primary Key/Unique Key: to uniquely specify a tuple in a table
Foreign Key: an attribute in a relational table that matches the primary key column of another table. It can be used to cross-reference tables.

‹#›

Entities and Attributes

An entity is similar to a semantic object
It includes attributes that describe the object

‹#›

Entity-Relationship Models

Entity-relationship (ER) diagrams are similar to semantic object modelings (i.e., class diagrams)
They use different notations
Focus is more on relations and less on class structure

‹#›

Relationships

An ER diagram indicates a relationship between entities with a diamond
Sometimes arrows are added to indicate direction of relationship

‹#›

Cardinality

Numbers used to describe relationship quantitatively.

‹#›

Inheritance

A triangle named “IsA” represents the inheritance relationship.

‹#›



Reflexive Associations

An object refers to an object of the same class.

‹#›

A brief digression on web app design

What is a web app?
A program that uses a web browser to perform specific functions.
“There are essentially two basic approaches to [web] design: the artistic ideal of expressing yourself and the engineering ideal of solving a problem for a customer” [Nielsen]
Aesthetics, layout, graphic design, content, navigation,...

[Pressman]

‹#›

…mobile app design

What is a mobile app?
A program that uses a mobile device to perform specific functions.
Still concerned with aesthetics, layout, graphic design, content, navigation,...
And multiple hardware and software platforms!
Smartphones, tablets, wearable devices, etc.
Android, iOS, Blackberry, Windows, etc.
App stores have different rules
More complex interactions
Power and space/storage management
Security and privacy

‹#›

LLMs in Software Design

Software Architecture
LLMs are primarily used for four main tasks:
Reference architectures
Classification and Detection
Extraction and Generation
Assistants
“We found that most of them [articles on LLMs for software architecture] propose automated approaches that use LLMs end-to-end, suggesting that LLMs are capable of addressing complete architectural tasks.” [Schmid]

‹#›

LLMs in Software Design (cont.)

Low-Level Design
LLMs are less reliable for low-level design tasks.

‹#›

[Pan]

LLMs in Software Design (cont.)

LLMs are terrible at generating UML diagrams

‹#›

[Conardy]

LLMs in Software Design (cont.)

But design task performance improves when generating textual output.

Review: Requirements Engineering

The process of defining, understanding, documenting, and maintaining requirements.
Subset of software engineering
Introduced for the waterfall model (first phase)
“The a set of activities concerned with identifying and communicating the purpose of a software-intensive system, and the contexts in which it will be used. Hence, RE acts as the bridge between the real-world needs of users, customers, and other constituencies affected by a software system, and the capabilities and opportunities afforded by software-intensive technologies.” [Easterbrook]

‹#›

Requirements Engineering

‹#›

Requirements elicitation

Requirements analysis

Requirements specification

Requirements Prioritization

⭐

Requirements Prioritization

Why is prioritization important?
Need to select what to design/implement
Customers (usually) ask for way too much
Balance time-to-market with amount of functionality
Decide which features go into the next release
For each requirement/feature, ask:
How important is this to the customer?
How much will it cost to implement?
How risky will it be to attempt to build it?

‹#›

Requirements in Practice

How do modern companies analyze, specify, and prioritize requirements?
Remember:
Developers report not using UML
In Agile, modeling is viewed as inaccurate and typically thrown away.
Only tested code demonstrates the requirements and design!

‹#›

Review: Meetings

Sprint Planning
Meeting to review backlog and determine tasks to be completed in the upcoming sprint
Entire team (Scrum master, manager, developers, etc.)
Project Estimation
Triage
Review of bugs and defects
Analyze reproducibility
Prioritize fixes
NOT coming up with a solution

‹#›

Business/Requirements Analysts

What do requirements analysts do?
Provide a starting point
Some notion that there is a “problem” that needs solving
e.g. dissatisfaction with the current state of affairs
e.g. a new business opportunity
e.g. a potential saving of cost, time, resource usage, etc.
A Requirements Analyst is an agent of change
The requirements analyst must:
identify the “problem”/”opportunity”
Which problem needs to be solved? (identify problem Boundaries)
Where is the problem? (understand the Context/Problem Domain)
Whose problem is it? (identify Stakeholders)
Why does it need solving? (identify the stakeholders’ Goals)
How might a software system help? (collect some Scenarios)
When does it need solving? (identify Development Constraints)
What might prevent us solving it? (identify Feasibility and Risk)
and become an “expert” in the problem domain

‹#›

Gantt Chart (aka Roadmap)

Provide a visual representation of requirements along with scheduled timelines to help visualize the start and end dates of tasks.
Ex) GitHub projects

‹#›

Gap Analysis

Evaluate the gaps in a product performance
Usually after a working product is available
Used by business analysts to present current state and target state of product

‹#›

Community Feedback

Insights from users on most-desired features.
Ex) GitHub Issues and Discussions

Class Activity

Hold a Sprint Planning/Triage Meeting (No AI usage!):
Based on the initial ideas for Project 1:
Create a list of general requirements/functionality for your system (can be formal use cases, user stories, or informal list of ideas—ideally from requirements elicitation results!).
Use the MoSCoW method (see below) to rank the initial lists
For the highest prioritized task(s), come up with a plan to design the code for this feature (i.e., class diagram). Also discuss what high-level architecture patterns you might use.
Submit ranked list and design discussion summary on Canvas (w/ names and PIDs).
Due: before the end of class today (submit what you complete, graded for attendance!)

‹#›

Next Class…

‹#›

Guest Lecture
Announcements
HW1 due Wednesday (2/11) before midnight
SE Processes
PM1.1 due Friday (2/13) before midnight
Requirements

References

RS Pressman. “Software engineering: a practitioner's approach”.
Anand Butani. “5 essential patterns of software architecture”. Red Hat, 2020. 
Cast Software “What is Software Architecture?”. 
K.D. Cooper, L. Torczon, “Engineering a Compiler”.Theo Mandel. “Golden Rules of User Interface Design”. 

Simon Foucher. “Introduction to Software Engineering: Unit 9 – Architectural Design Approaches”. McGill, ECSE-321.
https://refactoring.guru/design-patterns
Ian Sommerville. “Software Engineering”.
Emil Vassev, Joey Paquet. “Java Design Patterns”. 2006-2012. Concordia University
Ashish raap Singh. “S.O.L.I.D. Principles Explained with Code.” AlgoMaster Blog, 2024. https://blog.algomaster.io/p/solid-principles-explained-with-code
Guy Kawasaki. “The Only 10 Slides You Need in a Pitch”. 2020 https://guykawasaki.com/the-only-10-slides-you-need-in-your-pitch/
Noah Parsons. “The 11 Slides You Need to Have in Your Pitch Deck for 2025”. LivePlan, 2025. https://www.liveplan.com/blog/funding/slides-you-need
Yoonsuck Choe. “SOLID Principles for Object-Oriented Design”. CSCE 315, Texas A&M. 2020.
Robert MArtin. “Principles of OOD”. http://butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod

‹#›

References (cont.)

Aaron Conrardy. “From Image to UML: First Results of Image Based Class Diagram Generation Using LLMs”. Modeling Languages. https://modeling-languages.com/image-to-uml-with-llm/
Larissa Schmid, Tobias Hey, Martin Armbruster, Sophie Corallo, Dominik Fuchß, Jan Keim, Haoyu Liu, Anne Koziolek. “Software Architecture Meets LLMs: A Systematic Literature Review”. Arxiv:2505.16697, 2025.
Zhenyu Pan, Xuefeng Song, Yunkun Wang, Rongyu Cao, Binhua Li, Yongbin Li, Han Liu. “Do Code LLMs Understand Design Patterns”. Arxiv:2501.04835, 2025.
Jasmin Jahic, Ashkan Sami. “State of Practice: LLMs in Software Engineering and Software Architecture”. International Conference on Software Architecture Companion (ICSA-C), 2024.
Na Meng and Barbara Ryder
Chris Parnin
Sarah Heckman

