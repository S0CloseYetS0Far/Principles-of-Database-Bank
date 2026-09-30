# Question bank for CS370 practice site.
# prov: key | graded | marked | slides | worked
Q = []
def M(ch, q, opts, ans, src, prov, exp="", img=None, ctx=None):
    Q.append(dict(t="mcq", ch=ch, q=q, o=opts, a=ans, s=src, p=prov, e=exp, img=img, ctx=ctx))
def TF(ch, q, ans, src, prov, exp="", img=None, ctx=None):
    Q.append(dict(t="mcq", ch=ch, q=q, o=["True", "False"], a=0 if ans else 1, s=src, p=prov, e=exp, img=img, ctx=ctx))
def R(ch, q, answer, src, prov, exp="", img=None, ctx=None):
    Q.append(dict(t="reveal", ch=ch, q=q, ans=answer, s=src, p=prov, e=exp, img=img, ctx=ctx))

# ---------------------------------------------------------------- Chapter 1
M(1, "The major disadvantages of file-based systems (FBS) are:",
  ["Data redundancy & inconsistency", "Fixed queries", "Incompatible file format", "All of the above"], 3,
  ["M23S"], "key", "Chapter 1 lists all three as limitations of the file-based approach.")
M(1, "Which of the following is considered as a limitation of the File-Based System?",
  ["File structure is defined in application", "Wasted space and potentially different values", "Unnecessary and uncontrolled redundancy", "All the above"], 3,
  ["F23_1", "M25_2"], "slides", "Every option is an FBS limitation from Chapter 1.")
M(1, "____ is a collection of application programs that perform tasks where each program defines and manages its own data.",
  ["FBS", "DBMS", "DDL", "DML"], 0, ["Q25_2", "M23_1"], "slides",
  "In a file-based system each program defines and manages its own files. The 2021 midterm matching question (graded correct) uses the same definition.")
M(1, "“It is independent of incompatible file formats” is one of the major advantages of:",
  ["FBS", "DBMS", "DDL", "DML"], 1, ["Q25_2"], "slides", "Incompatible file formats are an FBS problem that a DBMS removes.")
M(1, "This may cause some data to be read and some data to be written into the database:",
  ["Database Sharing", "Database Query", "Database Maintained", "Database Transaction"], 3,
  ["M24_2", "Q25_2"], "key", "A transaction reads and/or writes data in the database.")
M(1, "Responsible for authorizing access to the database, coordinating and monitoring its use, and acquiring software and hardware resources:",
  ["Database administrators", "Database analysts", "Database designers", "Database programmers"], 0,
  ["M24_2", "M23_1"], "key", "Chapter 1, 'Actors on the scene': the DBA authorizes access, coordinates and monitors use.")
M(1, "The database administrators are responsible for:",
  ["Determining the requirements of end users", "Acquiring software and hardware resources as needed", "Designing and implementing the software packages that facilitate database design", "Using the data for queries"], 1,
  ["M24_1"], "slides", "Requirements = system analyst; tool packages = tool developers; queries = end users.")
M(1, "The user who is responsible for defining the content, the structure, the constraints, and functions or transactions against the database is:",
  ["Database administrators", "Software engineers", "Database designers", "End-users"], 2, ["M23S"], "key",
  "Database designers define content, structure, constraints and transactions, and must communicate with end users.")
M(1, "Which one of these is NOT considered an actor on the scene?",
  ["Database administrators", "Database designers", "Tool developer"], 2, ["M23_1"], "graded",
  "Tool developers are 'workers behind the scene' (Chapter 1, slide 27).")
M(1, "The person responsible for authorizing access to the database is part of:",
  ["Actors on the scene", "Operators and maintenance personnel", "Actors behind the scenes", "End users"], 0,
  ["Q24_1"], "marked", "The DBA is listed under 'Database Users – Actors on the scene'.")
M(1, "Which type of database user interacts with the system via pre-defined functions (canned transactions) and is typically unaware of the actual database structure?",
  ["Naive user", "Sophisticated user", "Database Administrator", "System Analyst"], 0, ["Q24_S"], "marked",
  "Naive/parametric end users use canned transactions, e.g. bank tellers and reservation clerks.")
M(1, "Which of the following is a database naïve user?",
  ["Retail store cashier", "Hotel receptionist", "Bank clerk", "All the above"], 3, ["M24_1"], "slides",
  "All three repeat the same canned transactions all shift long.")
TF(1, "The System Analyst determines the requirements of end users and develops system specifications.", True,
   ["Q25_1"], "slides", "Chapter 1, slide 25: 'System Analyst: determine the requirements of end users & develop system specifications.'")
M(1, "The DBMS software together with the data itself. Sometimes, the applications are also included:",
  ["Database Application", "DBMS", "Database system (DBS)", "DBA"], 2, ["Q24_S"], "marked")
M(1, "Database system consists of:",
  ["DBMS", "Database", "Database applications", "All the above"], 3, ["M24_1", "Q25_3"], "slides",
  "A database system is the DBMS plus the data, and sometimes the applications too.")
M(1, "Stored by the DBMS in the form of a database catalog or dictionary:",
  ["Database Application", "DBMS", "Database", "Meta-data"], 3, ["Q24_S", "Q25_2"], "marked")
M(1, "Stores the description of a particular database (e.g. data structures, types, and constraints):",
  ["A DBMS catalog", "Backup", "Domain"], 0, ["M23_1"], "graded")
M(1, "What is the DBMS catalog used for?",
  ["Update", "Store the actual data", "Query", "Store metadata"], 3, ["Q24_1"], "marked")
M(1, "Information that defines and describes data is called:",
  ["Sequence", "Meta data", "Sub data", "None of these"], 1, ["Q25_1"], "slides")
TF(1, "Data about data is called meta-data.", True, ["Q25_1"], "slides")
M(1, "The Meta-data tells ____ to the DBMS:",
  ["What tables are in the database", "What these tables contain", "What attributes are owned by each table", "All of the above"], 3,
  ["F23_1"], "marked")
M(1, "A database is:",
  ["A software package", "A collection of related data", "A programming language", "A system to query and update"], 1,
  ["Q24_1"], "marked", "Chapter 1, slide 3: 'Database (DB) is a collection of related data.'")
TF(1, "Data and information are the same thing.", False, ["Q25_1"], "slides",
   "Information is data processed so that it becomes meaningful (Chapter 1, slide 3).")
TF(1, "Databases may be more expensive to maintain than files because of backup and recovery needs.", True, ["M24_2"], "key")
M(1, "Which of the following is NOT a characteristic of the database approach?",
  ["Insulation between programs and data", "Support of multiple views of the data", "Self-describing nature of a database system", "Data dependence"], 3,
  ["Q24_1"], "marked", "The database approach gives data independence, not dependence.")
M(1, "Which of the following is considered an advantage of DBMSs?",
  ["Data integrity", "Controlling data redundancy", "All the above"], 2, ["M23_1"], "graded")
M(1, "One of the major advantages of DBMS is:",
  ["Incompatible file format", "Data dependence", "Data redundancy", "Data independence"], 3, ["M24_1", "Q25_3"], "slides")
M(1, "An advantage of the database management approach is:",
  ["Data is dependent on programs", "Data redundancy increases", "Data is integrated and can be accessed by multiple programs", "None of the above"], 2,
  ["F23_1"], "slides")
M(1, "Which of the following is an advantage of using the DBMS approach?",
  ["Increased data redundancy", "Improved data consistency", "Increased data storage cost", "Limited access to data"], 1, ["F25_2"], "slides")
M(1, "Which of the following applications requires concurrency control?",
  ["Calculator application", "Personal notes application", "Multiplayer online game", "Alarm clock application"], 2, ["M24_1"], "slides",
  "Concurrency control is needed when many users update shared data at the same time (Chapter 1, slide 19).")
M(1, "Which scenario below does NOT need the use of a DBMS?",
  ["A cloud-based project management tool used by remote workers that requires real-time collaboration and data synchronization",
   "A personal budgeting application that tracks income and expenses for an individual user without the need for sharing financial data",
   "An online booking system for a small local restaurant that manages table reservations and customer details",
   "An e-commerce platform handling thousands of customer transactions daily"], 1, ["M24_1"], "worked",
  "Single user, no sharing, no concurrency: a simple file is enough.")
M(1, "A software package/system to facilitate the creation and maintenance of a computerized database:",
  ["DB", "DBMS", "Database Application", "File-Based Systems (FBS)"], 1, ["M25_2", "M23_1"], "slides")
TF(1, "A DBMS does not allow multiple users to access the database at the same time.", False, ["Q24_S"], "marked",
   "Sharing and concurrent multi-user access is a core DBMS feature.")
R(1, "List four advantages of using a DBMS.",
  "Any four of: controlling redundancy; restricting unauthorized access; providing backup and recovery; enforcing integrity constraints; providing multiple user interfaces; representing complex relationships among data; concurrency control / data sharing; data independence; availability of up-to-date information.",
  ["Q26_2"], "slides", "Chapter 1, 'Advantages of using the database approach' slides.")

# ---------------------------------------------------------------- Chapter 2
M(2, "Hiding details of data storage that are not needed by most database users by using a data model is called:",
  ["Data Model", "Data Abstraction", "Database"], 1, ["M23_1"], "graded", "Chapter 2, slide 3.")
M(2, "At the conceptual level of a data model:",
  ["The description is about how to store data", "The description is about how to process data", "The description is about how people perceive data", "None of the options"], 2,
  ["M24_2"], "key", "Conceptual (high-level) models give concepts close to how users perceive data.")
TF(2, "The internal data model provides concepts that describe details of how data is stored in the computer.", True, ["Q25_2"], "slides",
   "Physical (low-level, internal) data models, Chapter 2 slide 4.")
M(2, "The actual data stored in a database at a particular moment in time. This includes the collection of all the data.",
  ["Database Instance", "Database Schema", "Schema Construct"], 0, ["M23_1"], "graded")
M(2, "A database state is:",
  ["The current set of data in the database at a specific moment", "The hardware", "The software", "The structure and schema"], 0, ["Q24_1"], "marked")
M(2, "Which of the following is a state of a database?",
  ["Empty state", "Current state", "Initial database state", "All of the above"], 3, ["M23S"], "key")
M(2, "The database state when it is initially loaded into the system is called:",
  ["Empty state", "Initial database state", "Valid state", "Current state"], 1, ["M24_1"], "slides")
TF(2, "The database schema changes frequently.", False, ["Q25_2"], "slides", "The schema rarely changes; the state (instance) changes often.")
TF(2, "An instance is the description of the database that rarely changes.", False, ["Q24_S"], "marked",
   "That describes the schema. An instance/state is the data at a given moment and changes all the time.")
M(2, "Schema level that describes the structure and constraints for the whole database for a community of users:",
  ["Internal schema", "Conceptual schema", "External schemas"], 1, ["M23_1"], "graded")
M(2, "What does a conceptual schema describe?",
  ["Physical storage structures", "User views", "The structure and constraints for the entire database", "Indexes and tables"], 2, ["Q24_S"], "marked")
M(2, "The description of the actual DBMS storage structure and access paths is the:",
  ["Conceptual schema", "Internal schema", "External schemas", "All of the above"], 1, ["M23S"], "key")
TF(2, "The three levels of the three-schema architecture are internal, conceptual and external.", True, ["Q24_S"], "marked")
M(2, "Which one is NOT one of the three schemas?",
  ["External", "Conceptual", "User", "Internal"], 2, ["Q25_1"], "slides")
M(2, "The ____ architecture is used to explain data independence.",
  ["One-schema", "Two-schema", "Three-schema", "All of these"], 2, ["Q25_1"], "slides")
M(2, "The ability to modify a schema definition in one level without affecting a schema definition in the next higher level:",
  ["Mappings", "Data Independence", "Data Model"], 1, ["M23_1", "Q24_1"], "graded")
M(2, "The ability to change the conceptual schema without having to change the application programs is called:",
  ["Data consistency independence", "Logical data independence", "Data redundancy independence", "Physical data independence"], 1,
  ["M24_1"], "slides", "Chapter 2, slide 15.")
M(2, "With logical data independence, the conceptual schema can be changed without changing the ____ schema.",
  ["Internal", "External", "Both", "None"], 1, ["Q25_1"], "slides")
M(2, "The DBMS language used by the database administrator to specify the schema of the database:",
  ["DDL", "DML", "DBA", "None of the above"], 0, ["M23S"], "key")
M(2, "A language that manipulates the structure of a database is called:",
  ["FBS", "DBMS", "DDL", "DML"], 2, ["M24_2"], "key")
M(2, "The purpose of DDL (Data Definition Language) is to:",
  ["Retrieve and manipulate data", "Back up the database", "Describe constraints on data", "Define the database schema"], 3, ["Q24_1"], "marked")
TF(2, "DDL is used to specify database retrievals and updates.", False, ["Q24_S"], "marked", "Retrievals and updates are DML.")
M(2, "Used to specify database retrieval and updates:",
  ["Recursive relationship", "File-Based Systems (FBS)", "Data Manipulation Language (DML)", "Database Management System (DBMS)"], 2,
  ["M23_1"], "graded")
TF(2, "When using a high-level language, the user specifies what data is required without specifying how to get those data.", True, ["Q24_S"], "marked")
R(2, "What are the categories of data models?",
  "Conceptual (high-level, semantic) models, close to how users perceive data (e.g. ER).<br>Physical (low-level, internal) models, describing how data is stored.<br>Implementation (representational, record-based) models, in between the two (e.g. relational).",
  ["Q26_2"], "slides", "Chapter 2, slide 4.")

# ---------------------------------------------------------------- Chapter 3
TF(3, "ER and EER models are used to describe the structure of the database at the conceptual level.", True, ["M23_1"], "graded")
TF(3, "ER and EER models are the implementation of the database at the internal level.", False, ["M24_2"], "key")
M(3, "A student can attend five classes, each with a different professor. Each professor has 30 students. The relationship of students to professors is a ____ relationship.",
  ["One-to-one", "Many-to-one", "One-to-many", "Many-to-many"], 3, ["M24_2"], "key")
M(3, "If an attribute consists of different parts, it is displayed in ER as:",
  ["Multi-valued attribute", "Composite attribute", "Derived attribute", "Complex attribute"], 1, ["M24_2"], "key")
M(3, "Select the attribute type which is made up of more than one single attribute, each with a single value.",
  ["Multi-value attribute", "Derived attribute", "Complex attribute", "Composite attribute"], 3, ["M25_3", "Q25_2"], "slides")
M(3, "In the diagram, 'Parts' is drawn as a double oval with components Season, Episode and Title. What type of attribute is 'Parts'?",
  ["Multivalued", "Complex", "Composite", "All"], 1, ["Q24_1"], "slides",
  "The quiz screenshot shows 'Composite' selected, but the Chapter 3 slides (slides 16–18) define a composite attribute that is also multivalued (double oval with parts) as a complex attribute.",
  img="tvshow")
M(3, "Select from the following the multi-valued attribute.",
  ["Date_of_birth", "Name", "Phone_number", "All of the mentioned"], 2, ["Q25_2"], "slides")
M(3, "An attribute computed as TOTAL PRICE = UNIT PRICE × QUANTITY is:",
  ["A primary key", "All the above", "A weak attribute", "A derived attribute"], 3, ["Q24_1"], "marked",
  "Chapter 3, slide 14: Total_cost is derived from quantity*unit_price.")
M(3, "Which of the following is true about derived attributes?",
  ["Have to be in the same entity", "Derived from the value of a related attribute", "Can be a primary key", "All of the above"], 1, ["M23S"], "key")
M(3, "Which of the following is true about a primary key?",
  ["Can be null", "Must be unique for each entity", "Must be more than one character", "All of the above"], 1, ["M23S"], "key")
M(3, "Among several candidate keys, choosing a primary key is based on:",
  ["The data type of the CK", "The uniqueness of the CK", "The name of the CK", "All of the above"], 1, ["M23S"], "key",
  "This is the official key. Every candidate key is unique by definition, so read it as: pick the key that best guarantees uniqueness.")
M(3, "The entity type that does not have a primary key:",
  ["Composite entity type", "Strong entity type", "Weak entity type", "Partial entity type"], 2, ["M23S"], "key")
M(3, "Select the true statement about a weak entity set in an ER diagram.",
  ["It has a primary key", "It can exist dependently", "It must participate in an identifying relationship type with an owner", "None of the options"], 2,
  ["M24_2"], "key")
M(3, "Which of the following is true about a weak entity in an ER model?",
  ["It can exist independently without a related strong entity", "It does not have its own primary key", "It has a strong relationship with itself", "It can never have a relationship with a strong entity"], 1,
  ["M25_2"], "slides", "Chapter 3, slide 28.")
M(3, "Which is a set of entities of the same type that share the same properties/attributes?",
  ["Relation set", "Attribute set", "Entity set", "Entity model"], 2, ["Q25_2"], "slides")
TF(3, "The set of entities of the same entity type share the same attributes and the same values for these attributes.", False, ["M23_1"], "graded",
   "They share the same attributes, but each entity has its own values.")
M(3, "If you were collecting and storing data about your podcast collection, an album would be considered as:",
  ["Relation", "Entity instance", "Relationship instance", "Complex attribute"], 1, ["M25_3"], "slides")
M(3, "The number of entities to which another entity can be related through a relationship set is called:",
  ["Cardinality ratio", "Entity instances", "DB schema", "Multivalued attributes"], 0, ["M25_3"], "slides")
TF(3, "If entity type X has a partial participation constraint in a relationship, the set of entities of X may or may not participate in that relationship.", True, ["M23_1"], "graded")
TF(3, "If entity type X has a total participation constraint in a relationship, the set of entities of X may or may not participate in that relationship.", False, ["M24_2"], "key",
   "Total participation means every entity of X must participate.")
M(3, "An entity on the '1' side has a double (total) line to the relationship, and the other entity is on the 'M' side with a single line. What is the equivalent (min,max) notation (left entity, right entity)?",
  ["(1,M) (0,1)", "(0,M) (1,1)", "(1,1) (0,M)"], 0, ["Q21"], "graded",
  "The student chose (1,1)(0,M) and it was marked wrong. In min-max notation the left entity must participate (min 1) and can relate to M others: (1,M). The right entity relates to at most one and need not participate: (0,1).")
M(3, "The participation of the same entity type more than once in a relationship, in different roles, is a:",
  ["Recursive relationship", "File-Based System", "Data Manipulation Language", "Database Management System"], 0, ["M23_1"], "graded")

co = "company"
for i, (s, a) in enumerate([
    ("Two employees can have the same SSN.", False),
    ("Two departments can have the same number_of_employees.", True),
    ("Each employee can have two supervisors.", False),
    ("Each employee must have a dependent.", False),
    ("An employee can be employed by two departments.", False),
    ("An employee can work on multiple projects.", True),
    ("An employee can manage multiple departments.", False),
    ("Department locations is a complex attribute.", False),
    ("The dependent name is a local attribute.", False),
    ("The employee’s salary can be a candidate key.", False)]):
    TF(3, "COMPANY diagram: " + s, a, ["M23S"], "key", img=co)
for s, a, e in [
    ("For any team, it is possible to consist of 4 students.", True, "MemberOf is N:N, so a team can have any number of members."),
    ("All students should be members of a team.", True, "The double line on the student side of MemberOf means total participation."),
    ("All students should lead at least 1 team.", False, "The student side of LeaderOf is a single line (partial)."),
    ("'Lab team' is a role name.", True, ""),
    ("A student is a weak entity.", False, "Student is drawn as a single rectangle.")]:
    TF(3, "Student/Team diagram: " + s, a, ["M24_2"], "key", e, img="student_team")
for s, a in [
    ("An order can be placed by many customers.", False),
    ("A customer can place only one order.", False),
    ("A product is included in one order only.", False),
    ("Two orders can have the same “order date” value.", True),
    ("A customer can have multiple payment methods.", True)]:
    TF(3, "Customer/Order/Product diagram: " + s, a, ["M23_1"], "graded", img="order_product")
for s, a, e in [
    ("A Customer may place multiple Orders.", True, "Customer 1 : M Order through Places."),
    ("Every Order must be managed by at least one Employee.", True, "Double line from Order to 'managed by' = total participation."),
    ("Product is the owner entity of OrderItems.", False, "The identifying relationship (double diamond) is Contains, so the owner is Order."),
    ("The (min, max) on the Product side of the BelongsTo relationship is (0,1).", False, "A product can belong to many order items and need not have any: (0,N)."),
    ("Each order must be placed by exactly one customer.", True, "Places is 1:M (one customer per order), and the double line on the Order side means every order must be placed.")]:
    TF(3, "Product/Order/Employee diagram: " + s, a, ["F24_1", "Q25_3"], "worked", e, img="customer_order_employee")
for s, a, e in [
    ("Any Coach may train as many Athletes as he or she wishes.", False, "Train is 1:1."),
    ("Each Coach will train at most one Athlete.", True, "Train is 1:1."),
    ("Each coach can train only one athlete.", True, "Train is 1:1."),
    ("All Athletes should be trained at the Gym.", False, "Single line on the Athlete side = partial participation."),
    ("An athlete can only train at one gym.", False, "Trained At is N:M."),
    ("The “Champion” entity is associated with only one medal.", True, "Medal is a single-valued attribute."),
    ("The “Win” relationship connects an athlete to a champion.", True, ""),
    ("A gym can have multiple devices recorded.", False, "Device is a single oval (single-valued), not a double oval."),
    ("A coach has attributes SSN and Job_ID.", True, ""),
    ("An athlete can have multiple champions associated with them through the “Win” relationship.", True, "Win is 1:M."),
    ("Each “Champion” entity must have a “Year” attribute.", True, "Year is the partial key (dashed underline) of the weak entity Champion.")]:
    TF(3, "Athlete diagram: " + s, a, ["M25_2", "F23_1"], "worked", e, img="athlete")

# ---------------------------------------------------------------- Chapter 4
M(4, "Generalization in the Enhanced ER model is the process of:",
  ["Defining an entity type that contains the common features of a set of entity types", "Defining a set of superclasses of an entity type", "Defining a set of subclasses of an entity type", "None of the options"], 0,
  ["M24_2"], "key")
TF(4, "A generalization may be total or partial.", True, ["M25_3"], "slides")
TF(4, "A partial specialization means that all entity instances in the superclass must exist in just one of the specialization subclasses.", False, ["M25_3"], "slides",
   "Partial means an instance may belong to no subclass. 'Just one' is the disjoint constraint.")
M(4, "In the EER model, what is a disjoint constraint?",
  ["It specifies that an entity can be a member of at most one of the subclasses of the specialization", "It specifies that an entity can belong to multiple subclasses", "It specifies that attributes are shared between entities", "It specifies that a relationship occurs between unrelated entities"], 0,
  ["F25_2"], "slides", "Chapter 4, slide 21.")
M(4, "There are persons other than employees, volunteers and donors who are of interest, so a person need not belong to any of these groups. At a given time a person may belong to two or more of these groups. What type of specialization is this?",
  ["Disjoint, total", "Disjoint, partial", "Overlapping, total", "Overlapping, partial"], 3, ["M23_1"], "graded",
  "May belong to several groups = overlapping (o). Need not belong to any = partial (single line).")
R(4, "Person(SSN, name, address, Telephone) is specialized into Employee(H_date), Volunteers, Donor. Employee is specialized (disjoint) into Faculty(rank) and Staff(position). List all the attributes of the Faculty entity type.",
  "rank, H_date, SSN, name, address, Telephone. A subclass inherits every attribute of its superclasses.",
  ["M23_1"], "graded")
for s, a, e in [
    ("A person can either be a student or an employee, but not both.", False, "The 'o' means overlapping, so a person can be both."),
    ("Every person in the system must be either a student or an employee.", False, "Single line from Person to the circle = partial specialization."),
    ("A student can only major in one subject area.", True, "Majors In is N:1 (student N, subject area 1)."),
    ("An employee can hold multiple positions.", False, "Position is a single-valued attribute."),
    ("Some students may not have a major.", False, "Double line on the Student side = total participation."),
    ("A subject area cannot exist without students.", False, "Single line on the SubjectArea side = partial participation.")]:
    TF(4, "Person/Student/SubjectArea diagram: " + s, a, ["M24_1", "M25_3", "F25_2"], "worked", e, img="person_subject")
TF(3, "Person/Student/SubjectArea diagram: Position is considered as a composed attribute.", False, ["F25_2"], "worked",
   "Position is a simple oval with no sub-attributes.", img="person_subject")
TF(4, "Product/Order/Employee diagram: The Customer and Employee entities could be generalized into a superclass Person.", True,
   ["F24_1"], "worked", "They share common attributes such as Name and Email.", img="customer_order_employee")
TF(4, "Athlete diagram: It is possible to generalize the Coach and Athlete entities into a superclass.", True,
   ["F23_1"], "worked", "Both have SSN, so a superclass such as Person could hold it.", img="athlete")
for s, a, e in [
    ("A single photo can belong to more than one type (e.g., both Landscape and Abstract).", False, "The circle has a 'd', so the subclasses are disjoint."),
    ("A photo can exist without being linked to any photographer.", True, "PHOTO participates in TAKES with (0,1)."),
    ("An Abstract photo includes multiple models.", False, "MODELS connects to PORTRAIT, not ABSTRACT."),
    ("Attributes like Film, Speed, and Resolution belong to all types of PHOTO, regardless of subtype.", True, "They are superclass attributes, inherited by every subclass."),
    ("Each transaction must be made by exactly one customer.", True, "TRANSACTION participates in MAKES with (1,1)."),
    ("A LANDSCAPE photo must always have an associated COUNTRY attribute.", False, "LANDSCAPE participates in LOCATED with (0,1), so it may have no location."),
    ("A CUSTOMER can exist in the system without ever making a transaction.", True, "CUSTOMER participates in MAKES with (0,N).")]:
    TF(4, "Photo EER diagram: " + s, a, ["F25_3"], "worked", e + " (The exam photo is blurry, so double-check against your copy.)", img="photo_eer")

# ---------------------------------------------------------------- Chapter 5
M(5, "The cardinality of a relation is:",
  ["The number of tuples", "The number of attributes", "The maximum size of each tuple", "The type of data stored in each attribute"], 0,
  ["F24_1"], "slides", "Chapter 5, slide 5.")
M(5, "Degree of a relation is:",
  ["Number of attributes of its relation schema", "Number of tuples in its relation state", "Number of different domains of its relation schema"], 0,
  ["Q21"], "graded", "The student picked 'number of tuples' and it was marked wrong. Chapter 5, slide 5: degree = number of attributes.")
M(5, "What type of relational database constraint may be violated if the primary key attributes of each relation schema cannot have null values?",
  ["Domain", "Key", "Entity integrity", "Referential integrity"], 2, ["F24_1"], "slides")
M(5, "What type of relational database constraint may be violated if we attempt to update a non-key attribute value?",
  ["Key", "Entity integrity", "Referential integrity", "Domain"], 3, ["M25_3", "F23_1", "M24_2"], "key",
  "The Midterm 2nd 2024 answer key marks only Domain for this operation.")
_ops = ["Domain only", "Referential integrity only", "Domain and Referential integrity", "All four: Domain, Key, Entity integrity, Referential integrity"]
M(5, "Which constraints may be violated by a DELETION of one tuple?", _ops, 1, ["M24_2"], "key")
M(5, "Which constraints may be violated by an INSERTION of one tuple?", _ops, 3, ["M24_2"], "key")
M(5, "Which constraints may be violated by an UPDATE of a foreign key value?", _ops, 2, ["M24_2"], "key")
M(5, "Which constraints may be violated by an UPDATE of a non-key attribute value?", _ops, 0, ["M24_2"], "key")
M(5, "Keys involved in the relationship between tables to join them are called:",
  ["Primary keys", "Foreign keys", "Candidate keys", "Super keys"], 1, ["F23_1", "M25_3"], "slides")
M(5, "The referential integrity rule requires that:",
  ["It makes it possible for an attribute to have a corresponding value", "Every null foreign key value must reference an existing primary key value", "Every non-null foreign key value must reference an existing primary key value", "It makes it possible to delete a row in one table whose primary key does not have a matching foreign key value"], 2,
  ["M25_2"], "slides")
TF(5, "Person/SubjectArea diagram: Inserting the tuple <NULL, “Database management involves storing, organizing, retrieving…”> into SubjectArea, where NULL is assigned to Subject, violates the key constraint.", False,
   ["M24_1", "M25_3", "F25_2"], "worked", "Subject is the primary key, so a NULL there violates entity integrity, not the key constraint.", img="person_subject")
TF(5, "Person/SubjectArea diagram: Violating the referential integrity constraint occurs when a student is assigned a major in a subject that does not exist in the SubjectArea relation.", True,
   ["M24_1", "M25_3", "F25_2"], "worked", img="person_subject")
TF(5, "Person/SubjectArea diagram: Subject attribute is a primary key that cannot be null.", True, ["F25_2"], "slides", "Entity integrity constraint.", img="person_subject")

# ---------------------------------------------------------------- Chapter 6
M(6, "Which of the following is NOT a step in building a database for an application?",
  ["Understand the real-world domain", "Integration testing", "Create the schema using DDL", "Load data (DML)"], 1, ["M23S"], "key",
  "Chapter 6, slide 2 lists the design steps.")
M(6, "When mapping an N:M relationship from an ER model to a relational model, what is typically created?",
  ["A new table to represent the relationship", "A single table with combined attributes of both entities", "A foreign key in one of the participating tables", "A hierarchical structure combining both entities"], 0, ["F25_2"], "slides")
M(6, "When mapping a weak entity type to a relational schema, what is required?",
  ["A separate table with no foreign key", "A primary key that includes the primary key of its owner entity", "A new column that stores multivalued attributes", "A direct mapping to the owner entity's table"], 1, ["F25_2"], "slides")
for s, a, e in [
    ("The Order entity will be mapped into a relation with attributes (OrderID, TotalAmount, Date, CustomerID).", True, "1:N Places: the FK CustomerID and the relationship attribute Date go to the N side (Order)."),
    ("The Manages relationship is mapped into a relation whose primary key is the combination of EmployeeID and OrderID.", True, "M:N relationships get their own relation keyed by both FKs."),
    ("The Customer entity is mapped into a relation with attributes (CustomerID, Name, Email, Phone).", False, "Phone is multivalued (double oval) so it goes to its own relation CUSTOMER_PHONE(CustomerID, Phone)."),
    ("OrderItem primary key is LineItemID.", False, "OrderItem is weak: its key is the owner's key plus the partial key, (OrderID, LineItemID)."),
    ("Product entity is mapped into (ProductID, Name, Price, TaxPrice).", False, "TaxPrice is derived (dashed oval) and is not stored.")]:
    TF(6, "Product/Order/Employee diagram: " + s, a, ["F24_1"], "worked", e, img="customer_order_employee")
TF(6, "Person/SubjectArea diagram: Employee entity is mapped into (EmpID, {Position}, salary, Name).", False, ["F25_2"], "worked",
   "Position is single-valued, so it is not written in braces or split out, and the subclass relation also needs the superclass key ID.", img="person_subject")
TF(6, "Athlete diagram: The Champion entity will be mapped into Champion(Year, Medal).", False, ["F23_1"], "worked",
   "Champion is weak, so it must include the owner's key: Champion(SSN, Year, Medal) with key (SSN, Year).", img="athlete")
TF(6, "Athlete diagram: The name attribute of an Athlete will appear in the mapped relation as First and Last attributes.", True, ["F23_1"], "worked",
   "Composite attributes are mapped to their simple components.", img="athlete")
R(6, "Apply the ER-to-relational mapping to this medical-centres ER diagram (show PKs and FKs).",
  "PATIENT(<u>pID</u>)<br>PATIENT_PHONE(<u>pID, phone</u>) — pID → PATIENT<br>SERVICE(<u>number</u>, serviceTyp, pID) — pID → PATIENT (1:N Visit)<br>MEDICAL_CENTRE(<u>MCnumber</u>) — 'No worker' is derived, not stored<br>MEDICAL_WORKER(<u>mwID</u>, type, MCnumber) — MCnumber → MEDICAL_CENTRE (N:1 Work-in)<br>PROVIDE(<u>number, MCnumber</u>, startTime, endTime) — number → SERVICE, MCnumber → MEDICAL_CENTRE (M:N)",
  ["Q22"], "slides", "The graded paper got 3 marks; this answer follows the Chapter 6 mapping steps.", img="medical")

# ---------------------------------------------------------------- Chapter 7
users_ctx = """<div class="tables"><table><caption>USER</caption><tr><th>Id</th><th>Name</th><th>Age</th><th>Gender</th><th>OccupationId</th><th>CityId</th></tr>
<tr><td>1</td><td>John</td><td>25</td><td>Male</td><td>1</td><td>3</td></tr><tr><td>2</td><td>Sara</td><td>20</td><td>Female</td><td>3</td><td>4</td></tr>
<tr><td>3</td><td>Victor</td><td>31</td><td>Male</td><td>2</td><td>5</td></tr><tr><td>4</td><td>Jane</td><td>27</td><td>Female</td><td>1</td><td>3</td></tr></table>
<table><caption>OCCUPATION</caption><tr><th>OccupationId</th><th>OccupationName</th></tr><tr><td>1</td><td>Software Engineer</td></tr><tr><td>2</td><td>Accountant</td></tr><tr><td>3</td><td>Pharmacist</td></tr><tr><td>4</td><td>Library Assistant</td></tr></table>
<table><caption>CITY</caption><tr><th>CityId</th><th>CityName</th></tr><tr><td>1</td><td>Halifax</td></tr><tr><td>2</td><td>Calgary</td></tr><tr><td>3</td><td>Boston</td></tr><tr><td>4</td><td>New York</td></tr><tr><td>5</td><td>Toronto</td></tr></table></div>"""
M(7, "What is the result of π<sub>Name</sub>(σ<sub>Age&gt;25</sub>(USER))?",
  ["Name, Age: (Victor, 31), (Jane, 27)", "Name, Age: (John, 25)", "Id, Name: (3, Victor), (4, Jane)", "Name: Victor, Jane"], 3, ["Q23_2"], "marked",
  "Age > 25 keeps Victor and Jane (John is exactly 25), then only Name is projected.", ctx=users_ctx)
M(7, "How many tuples does σ<sub>Id&gt;2 OR Age≠31</sub>(USER) return?",
  ["2 (rows 1 and 2)", "4 (all rows)", "2 (rows 1 and 4)", "2 (rows 3 and 4)"], 1, ["Q23_2"], "marked",
  "Rows 1, 2, 4 have Age ≠ 31; row 3 has Id > 2. So every row qualifies.", ctx=users_ctx)
M(7, "What does σ<sub>USER.OccupationId = OCCUPATION.OccupationId</sub>(USER × OCCUPATION) return?",
  ["Only the 4 USER rows with USER's columns", "Only the OccupationId values 1, 3, 2", "USER's columns plus OccupationName, with a single OccupationId column", "All columns of both relations (both OccupationId columns kept), for the 4 matching rows"], 3,
  ["Q23_2"], "marked", "A selection over a Cartesian product (a theta/equi-join) keeps both OccupationId columns. Only a natural join removes the duplicate.", ctx=users_ctx)
M(7, "What does USER * OCCUPATION * CITY (natural join) return?",
  ["4 rows with CityId, OccupationId, Id, Name, Age, Gender, OccupationName, CityName", "Only Id, OccupationName, CityName", "Only CityId, OccupationId, Id", "No result"], 0,
  ["Q23_2"], "marked", "Every user has a matching occupation and city, and natural join keeps each common attribute once.", ctx=users_ctx)
M(7, "What is the result of π<sub>Name, Gender</sub>(σ<sub>CityName='Boston'</sub>(USER * CITY))?",
  ["(3, Victor, 31, Male, 2)", "Name, CityName: (John, Boston), (Jane, Boston)", "Full rows for John and Jane", "Name, Gender: (John, Male), (Jane, Female)"], 3,
  ["Q23_2"], "marked", "John and Jane live in CityId 3 = Boston.", ctx=users_ctx)
ra_ctx = "<pre>STUDENT (<u>Snum</u>, Sname, Major, Level, Age)\nCLASS (<u>Cname</u>, Cday, Ctime, Croom, Instructor_name)\nENROLLED (<u>Snum, Cname</u>)\nINSTRUCTOR (<u>Instructor_name</u>, Specialty, Dept_num)</pre>"
R(7, "Write the relational algebra: retrieve the name of all computer science students who are in level 5.",
  "π<sub>Sname</sub>(σ<sub>Major='CS' AND Level=5</sub>(STUDENT))", ["Q22"], "graded", ctx=ra_ctx)
R(7, "Write the relational algebra: retrieve the name of all instructors who give a class in room R24.",
  "π<sub>Instructor_name</sub>(σ<sub>Croom='R24'</sub>(CLASS))", ["Q22"], "graded",
  "The student used ENROLLED and lost 0.25; the grader corrected it to CLASS, which holds Croom.", ctx=ra_ctx)

# ---------------------------------------------------------------- Chapter 8
TF(8, "If there are two relations specified in the FROM-clause and there is no join condition, then the CARTESIAN PRODUCT of tuples of both relations will be retrieved.", True, ["Q25_3b"], "slides",
   "Chapter 8 DML slides. (The red mark on this item in the scan is a redaction, not an answer.)")
TF(8, "VARCHAR(n) is an attribute datatype where it is a fixed length string and n is the number of characters.", False, ["Q25_3b"], "slides", "CHAR(n) is fixed length; VARCHAR(n) is varying length (Chapter 8 DDL).")
TF(8, "UNIQUE clause specifies alternate secondary keys in the relations.", True, ["Q25_3b"], "slides", "Chapter 8 DDL: 'UNIQUE clause: specifies alternate secondary keys'.")
TF(8, "A missing WHERE-clause means all tuples of the relations in the FROM-clause are selected.", True, ["Q25_3b"], "slides")
TF(8, "The DELETE statement removes all rows from a table, and the table structure is also deleted.", False, ["F25_2"], "slides", "DELETE removes tuples only; DROP TABLE removes the structure.")
TF(8, "You can use the ALTER TABLE statement to add, modify, or delete columns in an existing table.", True, ["F25_2"], "slides")
TF(8, "The IN operator in SQL is used to check if a value matches any value in a list.", True, ["F25_2"], "slides")
TF(8, "Foreign keys are used basically to define referential integrity constraints.", True, ["Q24_1b"], "slides")
M(8, "Which clause should you use to exclude group results?",
  ["WHERE", "HAVING", "RESTRICT", "GROUP BY"], 1, ["Q24_1b"], "slides")
M(8, "To display the last names including upper or lowercase letter 'a' or 'A' as the second character, which SQL statement is correct?",
  ["SELECT last_name FROM employees WHERE UPPER(last_name) LIKE '_A%';", "SELECT last_name FROM employees WHERE UPPER(last_name) = '%A_';", "SELECT last_name FROM employees WHERE LOWER(last_name) = '_%a%';", "SELECT last_name FROM employees WHERE LOWER(last_name) LIKE '%A_';"], 0, ["Q24_1b"], "worked",
  "'_' matches exactly one character and '%' any sequence. The '=' options do no pattern matching, and LOWER(...) can never contain 'A'.")
M(8, "EMPLOYEE table: EMPLOYEE_ID NUMBER Primary Key, FIRST_NAME VARCHAR2(25), LAST_NAME VARCHAR2(25). Which statement inserts a row into the table?",
  ["INSERT INTO employees VALUES (NULL, 'John', 'Smith');", "INSERT INTO employees (first_name, last_name) VALUES ('John', 'Smith');", "INSERT INTO employees VALUES (1000, 'John', NULL);", "INSERT INTO employees (first_name, last_name, employee_id) VALUES (1000, 'John', 'Smith');"], 2,
  ["Q24_1b"], "worked", "A and B leave the primary key NULL; D puts 'Smith' into the NUMBER column.")
M(8, "CREATE TABLE Airport (Airport_Code char(4) NOT NULL, Name varchar(50), City varchar(20), PRIMARY KEY (Airport_Code)); Which table matches this definition?",
  ["Codes like 101, 102 with Airport_Code as key", "Codes like 1001 with both Airport_Code and Name underlined as key", "Codes like 1001 with only Airport_Code underlined as key", "A column called AirName instead of Name"], 2, ["Q23_2"], "marked",
  "This is the answer selected on the Blackboard screenshot, and it is the intended one: 4-character codes, only the primary key underlined. Strictly, 3-character codes like '101' would also fit in char(4), so option (a) is a trick.")
M(8, "CREATE TABLE Seat_Reservation (Flight_No varchar(6) NOT NULL, Seat_No char(3) NOT NULL, Seat_class varchar(12), customer_Name varchar(50), Amount float(8) CHECK (Amount <= 15000), PRIMARY KEY (Flight_No, Seat_No), FOREIGN KEY (Flight_No) REFERENCES Flight); Which table matches?",
  ["Named Reservation, only Flight_No underlined", "Named Seat_Reservation, with Flight_No, Seat_No and customer_Name underlined", "Named Seat_Reservation, with Flight_No and Seat_No underlined", "Named Reservation, with Flight_No and Seat_No underlined"], 2, ["Q23_2"], "marked")

emp1_ctx = """<div class="tables"><table><caption>EMP</caption><tr><th>ID</th><th>ENAME</th><th>JOB</th><th>DNO</th><th>SALARY</th><th>COMM</th></tr>
<tr><td>100</td><td>AMR</td><td>SALESMAN</td><td>10</td><td>300</td><td>50</td></tr><tr><td>101</td><td>SAMY</td><td>ENGINEER</td><td>20</td><td>400</td><td>NULL</td></tr>
<tr><td>102</td><td>ALI</td><td>MANAGER</td><td>10</td><td>400</td><td>100</td></tr><tr><td>103</td><td>AMANY</td><td>SALESMAN</td><td>30</td><td>300</td><td>NULL</td></tr>
<tr><td>104</td><td>FADY</td><td>ENGINEER</td><td>NULL</td><td>600</td><td>NULL</td></tr><tr><td>105</td><td>HANY</td><td>TSUPPORT</td><td>30</td><td>550</td><td>200</td></tr></table>
<table><caption>DEPT</caption><tr><th>DNO</th><th>DNAME</th><th>LOC</th></tr><tr><td>10</td><td>MARKETING</td><td>GIZA</td></tr><tr><td>20</td><td>SUPPORT</td><td>CAIRO</td></tr><tr><td>30</td><td>MANAGEMENT</td><td>ASWAN</td></tr><tr><td>40</td><td>PRODUCTION</td><td>ALEX</td></tr><tr><td>50</td><td>IT</td><td>CAIRO</td></tr></table></div>"""
F3 = ["F25_3"]
M(8, "SELECT MAX(salary) FROM emp WHERE job NOT IN ('ENGINEER', 'MANAGER');", ["300", "400", "550", "600"], 2, F3, "worked",
  "Remaining rows: AMR 300, AMANY 300, HANY 550.", ctx=emp1_ctx)
M(8, "SELECT ename, dname FROM emp NATURAL JOIN dept WHERE salary BETWEEN 500 AND 600;",
  ["HANY, MANAGEMENT", "HANY, MANAGEMENT and FADY, NULL", "FADY, PRODUCTION", "No rows"], 0, F3, "worked",
  "FADY (600) has DNO NULL, so he has no matching DEPT row and drops out of the join.", ctx=emp1_ctx)
M(8, "SELECT ename FROM emp WHERE ename LIKE '%N_';", ["AMANY, HANY", "HANY only", "AMANY only", "SAMY, AMANY, HANY"], 0, F3, "worked",
  "'%N_' means N is the second-to-last letter: AMA<b>N</b>Y, HA<b>N</b>Y.", ctx=emp1_ctx)
M(8, "DELETE FROM emp WHERE job = (SELECT job FROM emp WHERE id = 103); How many rows will be deleted?", ["1", "2", "3", "0"], 1, F3, "worked",
  "Employee 103 is a SALESMAN; AMR and AMANY are salesmen.", ctx=emp1_ctx)
M(8, "INSERT INTO emp(id, ename, job, dno, salary) VALUES (110, 'RAMY', 'TEACHER', 70, 4500); What will happen?",
  ["The row is inserted with COMM = NULL", "Rejected: referential integrity violation (no department 70)", "Rejected: primary key violation", "Rejected: domain violation on salary"], 1, F3, "worked", ctx=emp1_ctx)
M(8, "SELECT ename, salary FROM emp WHERE comm IS NOT NULL INTERSECT SELECT ename, salary FROM emp WHERE salary < 400;",
  ["AMR 300", "AMR 300, AMANY 300", "AMR 300, ALI 400, HANY 550", "No rows"], 0, F3, "worked",
  "COMM not null: AMR, ALI, HANY. Salary < 400: AMR, AMANY. Common: AMR.", ctx=emp1_ctx)

emp2_ctx = """<div class="tables"><table><caption>EMP</caption><tr><th>ID</th><th>ENAME</th><th>JOB</th><th>DNO</th><th>SALARY</th><th>COMM</th></tr>
<tr><td>100</td><td>AMR</td><td>SALESMAN</td><td>10</td><td>300</td><td>50</td></tr><tr><td>101</td><td>SAMY</td><td>ENGINEER</td><td>20</td><td>400</td><td>NULL</td></tr>
<tr><td>102</td><td>ALI</td><td>MANAGER</td><td>50</td><td>400</td><td>100</td></tr><tr><td>103</td><td>AMANY</td><td>SALESMAN</td><td>30</td><td>300</td><td>NULL</td></tr>
<tr><td>104</td><td>FADY</td><td>ENGINEER</td><td>40</td><td>600</td><td>NULL</td></tr><tr><td>105</td><td>HANY</td><td>TSUPPORT</td><td>50</td><td>550</td><td>50</td></tr></table>
<table><caption>DEPT</caption><tr><th>DNO</th><th>DNAME</th><th>LOC</th></tr><tr><td>10</td><td>MARKETING</td><td>Riyadh</td></tr><tr><td>20</td><td>SUPPORT</td><td>Jeddah</td></tr><tr><td>30</td><td>MANAGEMENT</td><td>Dammam</td></tr><tr><td>40</td><td>PRODUCTION</td><td>Hael</td></tr><tr><td>50</td><td>IT</td><td>Jeddah</td></tr></table></div>"""
F4 = ["Q24_1b"]
M(8, "SELECT MAX(salary) FROM emp WHERE dno IN (SELECT dno FROM dept WHERE dname = 'IT');", ["400", "550", "600", "950"], 1, F4, "worked", "IT is DNO 50: ALI 400, HANY 550.", ctx=emp2_ctx)
M(8, "SELECT ename, id FROM emp WHERE ename LIKE '_M%';", ["AMR 100, AMANY 103", "AMR 100 only", "SAMY 101", "No rows"], 0, F4, "worked",
  "Second letter M: A<b>M</b>R, A<b>M</b>ANY.", ctx=emp2_ctx)
M(8, "SELECT LOWER(ENAME), UPPER(ENAME) FROM EMP WHERE ID IN (100, 103);", ["amr AMR; amany AMANY", "AMR amr; AMANY amany", "amr AMR only", "Every row in EMP"], 0, F4, "worked", ctx=emp2_ctx)
M(8, "INSERT INTO emp(id, name, job, dno, salary) VALUES (110, 'RAMY', 'TEACHER', 60, 4500); What will happen?",
  ["The row is inserted", "It is rejected with an error", "The row is inserted with DNO NULL", "The row is inserted and department 60 is created"], 1, F4, "worked",
  "Two problems, either of which rejects it: EMP has no column called NAME (it is ENAME), and department 60 does not exist in DEPT, which violates referential integrity.", ctx=emp2_ctx)
M(8, "SELECT ename, salary FROM emp WHERE comm IS NULL UNION SELECT ename, salary FROM emp WHERE salary > 400;",
  ["SAMY 400, AMANY 300, FADY 600, HANY 550", "SAMY 400, AMANY 300, FADY 600", "FADY 600, HANY 550", "SAMY, AMANY, FADY, FADY, HANY"], 0, F4, "worked",
  "COMM null: SAMY, AMANY, FADY. Salary > 400: FADY, HANY. UNION removes the duplicate FADY.", ctx=emp2_ctx)

reg_ctx = """<div class="tables"><table><caption>STUDENT</caption><tr><th>SID</th><th>Sname</th><th>City</th><th>Gender</th></tr>
<tr><td>4401</td><td>Ahmed</td><td>Riyadh</td><td>Male</td></tr><tr><td>4402</td><td>Sara</td><td>Jeddah</td><td>Fmale</td></tr><tr><td>4403</td><td>Fatimah</td><td>Makkah</td><td>Fmale</td></tr></table>
<table><caption>REGISTER</caption><tr><th>Rno</th><th>CNo</th><th>SID</th><th>Register_Date</th><th>Registrant_Name</th><th>Registrant_City</th></tr>
<tr><td>341103</td><td>101</td><td>4401</td><td>13-01-2024</td><td>Ali</td><td>Riyath</td></tr><tr><td>231190</td><td>103</td><td>4402</td><td>02-03-2024</td><td>Hind</td><td>Jeddah</td></tr></table>
<table><caption>COURSE</caption><tr><th>Cno</th><th>Cname</th><th>Description</th><th>No_Of_Hours</th></tr>
<tr><td>101</td><td>Java</td><td>Introduction to java program</td><td>4</td></tr><tr><td>102</td><td>Data Base</td><td>Data base design and implementation</td><td>3</td></tr>
<tr><td>103</td><td>Networks</td><td>Network design</td><td>3</td></tr><tr><td>104</td><td>Security</td><td>Security Fundmentals</td><td>2</td></tr></table>
<p class="note">The exam spells the value 'Fmale' in the table. REGISTER.SID → STUDENT, REGISTER.CNo → COURSE, and a student or course cannot be removed while it appears in REGISTER.</p></div>"""
F2 = ["F25_2"]
M(8, "How many tuples are returned by: SELECT * FROM COURSE, REGISTER, STUDENT;", ["9", "12", "24", "2"], 2, F2, "worked", "Cartesian product: 4 × 2 × 3 = 24.", ctx=reg_ctx)
M(8, "How many tuples are returned by: SELECT DISTINCT Gender FROM STUDENT;", ["1", "2", "3", "0"], 1, F2, "worked", ctx=reg_ctx)
M(8, "How many tuples are returned by: SELECT * FROM COURSE WHERE Description LIKE 'N%';", ["0", "1", "2", "4"], 1, F2, "worked", "Only 'Network design' starts with N.", ctx=reg_ctx)
M(8, "How many tuples are returned by: SELECT COUNT(*) FROM REGISTER, STUDENT WHERE REGISTER.SID = STUDENT.SID AND Gender = 'Female';", ["0", "1", "2", "3"], 1, F2, "worked",
  "An aggregate with no GROUP BY always returns exactly one tuple (holding the count).", ctx=reg_ctx)
M(8, "How many tuples will be deleted from REGISTER if DELETE FROM STUDENT WHERE SID = 4401; is executed?", ["0", "1", "2", "3"], 0, F2, "worked",
  "The delete is rejected because student 4401 is referenced in REGISTER (deletion not allowed), so nothing is deleted.", ctx=reg_ctx)
R(8, "Write the SQL statement that creates the table REGISTER, knowing that (1) it is not allowed to remove a student or a course if they appear in REGISTER, and (2) none of the attributes accepts a NULL value.",
  "<pre>CREATE TABLE REGISTER (\n  Rno             INT         NOT NULL,\n  CNo             INT         NOT NULL,\n  SID             INT         NOT NULL,\n  Register_Date   DATE        NOT NULL,\n  Registrant_Name VARCHAR(30) NOT NULL,\n  Registrant_City VARCHAR(30) NOT NULL,\n  PRIMARY KEY (Rno),\n  FOREIGN KEY (SID) REFERENCES STUDENT(SID) ON DELETE RESTRICT,\n  FOREIGN KEY (CNo) REFERENCES COURSE(Cno)  ON DELETE RESTRICT\n);</pre>",
  F2, "slides", "Chapter 8 DDL: RESTRICT (the default, 'no action') blocks the delete.", ctx=reg_ctx)
R(8, "Write an SQL query that retrieves all REGISTER rows that include courses with No_Of_Hours over 2. You must use EXISTS.",
  "<pre>SELECT *\nFROM REGISTER R\nWHERE EXISTS (SELECT *\n              FROM COURSE C\n              WHERE C.Cno = R.CNo\n                AND C.No_Of_Hours > 2);</pre>", F2, "slides", ctx=reg_ctx)
R(8, "Write a SQL statement that deletes the student whose SID is 4401.", "<pre>DELETE FROM STUDENT WHERE SID = 4401;</pre>", F2, "slides", ctx=reg_ctx)
R(8, "Rewrite using a set operation: SELECT Cno FROM COURSE WHERE Cname = 'Java' OR No_Of_Hours &lt; 4;",
  "<pre>SELECT Cno FROM COURSE WHERE Cname = 'Java'\nUNION\nSELECT Cno FROM COURSE WHERE No_Of_Hours < 4;</pre>", F2, "slides", "OR becomes UNION (AND would become INTERSECT).")

pat_ctx = """<div class="tables"><table><caption>PATIENT</caption><tr><th>patient_id</th><th>first_name</th><th>date_of_birth</th><th>address</th></tr>
<tr><td>1</td><td>Ahmad</td><td>15-06-1985</td><td>Riyadh, Al Olaya St</td></tr><tr><td>2</td><td>Fatimah</td><td>20-11-1990</td><td>Jeddah</td></tr><tr><td>3</td><td>Sara</td><td>28-02-1975</td><td>Dammam</td></tr><tr><td>4</td><td>Khalid</td><td>09-08-1988</td><td>Mecca</td></tr></table>
<table><caption>APPOINTMENT</caption><tr><th>appointment_id</th><th>patient_id</th><th>doctor_id</th><th>appointment_date</th><th>reason</th></tr>
<tr><td>1</td><td>1</td><td>101</td><td>22-10-2024</td><td>Heart checkup</td></tr><tr><td>2</td><td>2</td><td>102</td><td>23-10-2024</td><td>Knee pain</td></tr><tr><td>3</td><td>3</td><td>103</td><td>24-10-2024</td><td>Child wellness</td></tr><tr><td>4</td><td>4</td><td>104</td><td>25-10-2024</td><td>Post-surgery follow-up</td></tr></table>
<table><caption>DOCTOR</caption><tr><th>doctor_id</th><th>first_name</th><th>Specialty</th></tr><tr><td>1</td><td>Abdullah</td><td>Cardiology</td></tr><tr><td>2</td><td>Noura</td><td>Orthopedics</td></tr><tr><td>3</td><td>Layla</td><td>Pediatrics</td></tr><tr><td>4</td><td>Faisal</td><td>General Surgery</td></tr></table>
<p class="note">Phone and time columns omitted. As printed in the exam, APPOINTMENT.doctor_id values (101–104) do not match DOCTOR ids (1–4).</p></div>"""
F1 = ["F24_1"]
M(8, "How many tuples will be returned by: SELECT first_name FROM APPOINTMENT A, DOCTOR D WHERE A.doctor_id = D.doctor_id AND first_name = 'Nora';", ["0", "1", "4", "16"], 0, F1, "worked",
  "No doctor is called 'Nora' (the table has 'Noura'), and the doctor ids don't match anyway.", ctx=pat_ctx)
M(8, "How many tuples will be returned from: SELECT first_name FROM APPOINTMENT NATURAL JOIN PATIENT;", ["0", "4", "8", "16"], 1, F1, "worked",
  "The intended common attribute is patient_id, and every appointment's patient exists, so 4. Watch out: the exam's table spells the APPOINTMENT column 'pathient_id'. Taken literally there would be no common column, and a natural join with no common column is a Cartesian product (16). 4 is almost certainly the intended answer.", ctx=pat_ctx)
M(8, "How many tuples will be returned from: SELECT first_name FROM APPOINTMENT, PATIENT;", ["4", "8", "16", "0"], 2, F1, "worked", "Cartesian product: 4 × 4.", ctx=pat_ctx)
M(8, "Given the CREATE statement from Q1 (a patient can't be removed while they have an appointment), how many tuples will be deleted from PATIENT by: DELETE FROM PATIENT WHERE address LIKE 'Riyadh%';", ["0", "1", "4", "2"], 0, F1, "worked",
  "Patient 1 lives in Riyadh but has appointment 1, so the delete is rejected.", ctx=pat_ctx)
R(8, "Write an SQL statement that retrieves the doctor_id and the number of appointments for each doctor who has more than three appointments, sorting the results by the number of appointments from high to low.",
  "<pre>SELECT doctor_id, COUNT(*) AS num_appointments\nFROM APPOINTMENT\nGROUP BY doctor_id\nHAVING COUNT(*) > 3\nORDER BY COUNT(*) DESC;</pre>", F1, "slides", ctx=pat_ctx)
R(8, "Rewrite using one of the set operations: SELECT doctor_id FROM DOCTOR WHERE specialty = 'Pediatrics' OR first_name = 'Abdullah';",
  "<pre>SELECT doctor_id FROM DOCTOR WHERE specialty = 'Pediatrics'\nUNION\nSELECT doctor_id FROM DOCTOR WHERE first_name = 'Abdullah';</pre>", F1, "slides", ctx=pat_ctx)
R(8, "Write an SQL statement that updates the date of the appointment with appointment_id 2 to be 3-11-2024.",
  "<pre>UPDATE APPOINTMENT\nSET appointment_date = '3-11-2024'\nWHERE appointment_id = 2;</pre>", F1, "slides", ctx=pat_ctx)
R(8, "Create the APPOINTMENT table so that a doctor or patient cannot be deleted while they have an appointment, and every attribute except reason is NOT NULL.",
  "<pre>CREATE TABLE APPOINTMENT (\n  appointment_id   INT NOT NULL,\n  patient_id       INT NOT NULL,\n  doctor_id        INT NOT NULL,\n  appointment_date DATE NOT NULL,\n  appoint_time     TIME NOT NULL,\n  reason           VARCHAR(100),\n  PRIMARY KEY (appointment_id),\n  FOREIGN KEY (patient_id) REFERENCES PATIENT(patient_id) ON DELETE RESTRICT,\n  FOREIGN KEY (doctor_id)  REFERENCES DOCTOR(doctor_id)   ON DELETE RESTRICT\n);</pre>",
  F1, "slides", ctx=pat_ctx)
R(8, "Write a query that lists the doctors who have no appointments (use NOT EXISTS).",
  "<pre>SELECT *\nFROM DOCTOR D\nWHERE NOT EXISTS (SELECT *\n                  FROM APPOINTMENT A\n                  WHERE A.doctor_id = D.doctor_id);</pre>", F1, "slides", ctx=pat_ctx)
R(8, "Delete the patient(s) who live in Riyadh.", "<pre>DELETE FROM PATIENT WHERE address LIKE 'Riyadh%';</pre>",
  F1, "slides", "With the RESTRICT rule from the CREATE statement this delete is rejected, because patient 1 has an appointment.", ctx=pat_ctx)

company_ctx = "<pre>EMPLOYEE (FNAME, MINIT, LNAME, <u>SSN</u>, BDATE, ADDRESS, SEX, SALARY, SUPERSSN, DNO)\nDEPARTMENT (DNAME, <u>DNUMBER</u>, MGRSSN, MGRSTARTDATE)\nDEPT_LOCATIONS (<u>DNUMBER, DLOCATION</u>)\nPROJECT (PNAME, <u>PNUMBER</u>, PLOCATION, DNUM)\nWORKS_ON (<u>ESSN, PNO</u>, HOURS)\nDEPENDENT (<u>ESSN, DEPENDENT_NAME</u>, SEX, BDATE, RELATIONSHIP)</pre>"
R(8, "Assuming the employee and department tables exist, write a DDL statement to create WORKS_ON with appropriate data types and constraints.",
  "<pre>CREATE TABLE WORKS_ON (\n  ESSN  CHAR(9)      NOT NULL,\n  PNO   INT          NOT NULL,\n  HOURS DECIMAL(3,1),\n  PRIMARY KEY (ESSN, PNO),\n  FOREIGN KEY (ESSN) REFERENCES EMPLOYEE(SSN),\n  FOREIGN KEY (PNO)  REFERENCES PROJECT(PNUMBER)\n);</pre>", F3, "slides", ctx=company_ctx)
R(8, "Add a foreign key constraint on DNO in EMPLOYEE referencing DNUMBER in DEPARTMENT, with SET NULL on deletion.",
  "<pre>ALTER TABLE EMPLOYEE\n  ADD CONSTRAINT Employee_Dno_FK\n  FOREIGN KEY (DNO) REFERENCES DEPARTMENT(DNUMBER)\n  ON DELETE SET NULL;</pre>", F3, "slides", ctx=company_ctx)
R(8, "Delete the FK constraint named Employee_Dno_FK defined on DNO in EMPLOYEE.",
  "<pre>ALTER TABLE EMPLOYEE DROP CONSTRAINT Employee_Dno_FK;</pre>", F3, "slides", ctx=company_ctx)
R(8, "Retrieve the first name, department name, and salary of each employee who works on any project located in \"Jeddah\", sorted by SALARY descending.",
  "<pre>SELECT DISTINCT E.FNAME, D.DNAME, E.SALARY\nFROM EMPLOYEE E, DEPARTMENT D, WORKS_ON W, PROJECT P\nWHERE E.DNO = D.DNUMBER\n  AND E.SSN = W.ESSN\n  AND W.PNO = P.PNUMBER\n  AND P.PLOCATION = 'Jeddah'\nORDER BY E.SALARY DESC;</pre>", F3, "slides", ctx=company_ctx)
R(8, "Create a view DEPT_TOTALS showing each department's name, count of employees, and total monthly salaries.",
  "<pre>CREATE VIEW DEPT_TOTALS (DEPT_NAME, NO_OF_EMPS, TOTAL_SAL) AS\nSELECT D.DNAME, COUNT(*), SUM(E.SALARY)\nFROM DEPARTMENT D, EMPLOYEE E\nWHERE D.DNUMBER = E.DNO\nGROUP BY D.DNAME;</pre>", F3, "slides", ctx=company_ctx)
R(8, "Remove the existing view named Dept_Totals.", "<pre>DROP VIEW Dept_Totals;</pre>", F3, "slides")

eds_ctx = """<div class="tables"><table><caption>EmployeeDetails</caption><tr><th>EmpId</th><th>FullName</th><th>ManagerId</th><th>DateOfJoining</th><th>City</th></tr>
<tr><td>121</td><td>John Snow</td><td>321</td><td>01/31/2014</td><td>Toronto</td></tr><tr><td>321</td><td>Walter White</td><td>986</td><td>01/30/2015</td><td>California</td></tr><tr><td>421</td><td>Kuldeep Rana</td><td>876</td><td>27/11/2016</td><td>New Delhi</td></tr></table>
<table><caption>EmployeeSalary</caption><tr><th>EmpId</th><th>Project</th><th>Salary</th><th>Variable</th></tr><tr><td>121</td><td>P1</td><td>8000</td><td>500</td></tr><tr><td>321</td><td>P2</td><td>10000</td><td>1000</td></tr><tr><td>421</td><td>P1</td><td>12000</td><td>0</td></tr></table></div>"""
Q5 = ["Q25_3b"]
R(8, "Fetch the EmpId and FullName of all employees working under the manager with id 876.", "<pre>SELECT EmpId, FullName FROM EmployeeDetails WHERE ManagerId = 876;</pre>", Q5, "slides", ctx=eds_ctx)
R(8, "Fetch the number of employees working in project 'P1'.", "<pre>SELECT COUNT(*) FROM EmployeeSalary WHERE Project = 'P1';</pre>", Q5, "slides", "Result: 2.", ctx=eds_ctx)
R(8, "Fetch the names of employees whose name has any two characters, followed by 'h', followed by anything.", "<pre>SELECT FullName FROM EmployeeDetails WHERE FullName LIKE '__h%';</pre>", Q5, "slides", "Result: John Snow.", ctx=eds_ctx)
R(8, "Fetch the employees who are not working on any project.",
  "<pre>SELECT *\nFROM EmployeeDetails\nWHERE EmpId NOT IN (SELECT EmpId FROM EmployeeSalary);</pre>", Q5, "slides", "With this data the result is empty: all three employees have a project.", ctx=eds_ctx)

# ---------------------------------------------------------------- Chapter 9
M(9, "Redundant information in tuples may cause:",
  ["Update anomalies", "Domain constraint", "Enhanced query speed", "Reduced storage requirements"], 0, ["F24_1"], "slides", "Chapter 9, slide 10.")
M(9, "The reason for nulls in a database is:",
  ["Attribute not applicable or invalid", "Attribute value unknown", "Value known to exist, but unavailable", "All the above answers are correct"], 3, ["F24_1", "F25_2"], "slides")
M(9, "Informal measures of quality for relation schema design:",
  ["Semantics of the relation attributes", "Redundant information in tuples", "Disallowing the generation of spurious tuples", "All the above"], 3, ["F24_1"], "slides", "Chapter 9, slide 5.")
M(9, "A table that is in 2NF and includes no transitive dependencies is said to be in:",
  ["1NF", "2NF", "3NF", "BCNF"], 2, ["F24_1", "F25_2"], "slides")
TF(9, "Normalization is the process of decomposing 'bad' relations by breaking up their attributes into smaller relations.", True, ["F25_2"], "slides")
TF(9, "A prime attribute is an attribute that is a member of the primary key K.", True, ["F25_2"], "slides", "Chapter 9, slide 31 uses this exact definition.")
TF(9, "If a relation has a multivalued attribute then it will be in first normal form.", False, ["F25_3"], "slides", "1NF forbids multivalued and composite attributes.")
TF(9, "If a relation has only one candidate key consisting of one attribute (i.e., no partial dependencies), it is automatically in Second Normal Form (2NF).", True, ["F25_3"], "slides")
fl_ctx = "<pre>FLIGHT_RESERVATION (<u>Flight#, Date, Cust_name</u>, Plane_type, Seat#, Plane_capacity)\nFlight# → Plane_type\nPlane_type → Plane_capacity</pre>"
M(9, "Each reservation is for one customer and assigns a unique Seat#. What normal form is FLIGHT_RESERVATION in?",
  ["1NF", "2NF", "3NF", "BCNF"], 0, ["Q22"], "graded", "Flight# → Plane_type is a partial dependency on part of the key, so it is not in 2NF.", ctx=fl_ctx)
R(9, "Normalize FLIGHT_RESERVATION until the relations cannot be decomposed further.",
  "<b>2NF</b>: FLIGHT(<u>Flight#</u>, Plane_type, Plane_capacity); RESERVATION(<u>Flight#, Date, Cust_name</u>, Seat#)<br><b>3NF</b>: FLIGHT(<u>Flight#</u>, Plane_type); PLANE(<u>Plane_type</u>, Plane_capacity); RESERVATION(<u>Flight#, Date, Cust_name</u>, Seat#)",
  ["Q22"], "graded", ctx=fl_ctx)
club_ctx = "<pre>CLUB_PARTICIPATION (<u>StudentID</u>, StudentName, {PhoneNo}, <u>EventID</u>, Score, EventDate, VenueName, VenueID, VenueCity)\n1. StudentID → StudentName\n2. EventID → EventDate, VenueID, VenueName\n3. VenueID → VenueCity\n4. StudentName → StudentID, {PhoneNo}\n5. StudentName, EventID → Score</pre>"
R(9, "Normalize CLUB_PARTICIPATION up to 3NF (PhoneNo is multivalued). Write the relations after each step.",
  "<b>1NF</b> (remove the multivalued attribute): PARTICIPATION(<u>StudentID, EventID</u>, StudentName, Score, EventDate, VenueID, VenueName, VenueCity); STUDENT_PHONE(<u>StudentID, PhoneNo</u>)<br><b>2NF</b> (remove partial dependencies): STUDENT(<u>StudentID</u>, StudentName); EVENT(<u>EventID</u>, EventDate, VenueID, VenueName, VenueCity); PARTICIPATION(<u>StudentID, EventID</u>, Score); STUDENT_PHONE(<u>StudentID, PhoneNo</u>)<br><b>3NF</b> (remove the transitive VenueID → VenueCity): EVENT(<u>EventID</u>, EventDate, VenueID, VenueName); VENUE(<u>VenueID</u>, VenueCity); plus STUDENT, PARTICIPATION, STUDENT_PHONE unchanged.",
  ["F25_3"], "slides", "Model answer written from the Chapter 9 steps; the exam paper has no key.", ctx=club_ctx)
race_ctx = "<pre>RACING_GROUP (Gnumber, <u>Gname</u>, {PhoneNo}, Point, <u>Rnumber</u>, Date, PlaygroundCity, PlaygroundNo)\nGname, Rnumber → Point\nGnumber → Gname   (and Gname → Gnumber)\nRnumber → Date, PlaygroundNo, PlaygroundCity\nGname → Gnumber, {PhoneNo}\nPlaygroundNo → PlaygroundCity</pre>"
R(9, "Apply normalization up to BCNF on RACING_GROUP (PhoneNo is multivalued).",
  "<b>1NF</b>: RACING_GROUP(<u>Gname, Rnumber</u>, Gnumber, Point, Date, PlaygroundNo, PlaygroundCity); GROUP_PHONE(<u>Gname, PhoneNo</u>)<br><b>2NF</b>: GROUP(<u>Gname</u>, Gnumber); RACE(<u>Rnumber</u>, Date, PlaygroundNo, PlaygroundCity); RESULT(<u>Gname, Rnumber</u>, Point); GROUP_PHONE(<u>Gname, PhoneNo</u>)<br><b>3NF</b>: RACE(<u>Rnumber</u>, Date, PlaygroundNo); PLAYGROUND(<u>PlaygroundNo</u>, PlaygroundCity); others unchanged<br><b>BCNF</b>: already satisfied. In GROUP, Gnumber → Gname holds but Gnumber is also a candidate key.",
  ["F25_2"], "slides", "Model answer written from the Chapter 9 steps; the exam paper has no key.", ctx=race_ctx)
