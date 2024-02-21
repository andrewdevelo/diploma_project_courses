**Assignment 4: Online courses**                                                                          

**Project Goal**: Create a Django-based online learning web application that                                                                          
allows users to browse, enroll and take courses online.                                                                          

**Target audience**: Students, professionals, self-learners interested                                                                           
in online education.                                                                          

1) **General requirements**                                                                          
* `Platform`: Web application.                                                                          
* `Stack`: Django, Django REST Framework for API                                                                          
* `DataBases`: **PostgreSQL** \ **MySQL** (and \ or other non-relational DB).                                                                                                                                                                                                                                        
* `Security`: User authentication, data protection.                                                                          

2) **Data Models**                                                                          
**Course**:                                                                          
* `Title`: CharField                                                                          
* `Description`: TextField                                                                          
* `Start_date`: DateTimeField                                                                          
* `End_date`: DateTimeField                                                                          
* `Instructor`: ForeignKey (link to user model)                                                                          
**Module**:                                                                          
* `Title` (title): CharField                                                                          
* `Description`: TextField                                                                          
* `Course`: ForeignKey (link to course model)                                                                          
**Material**:                                                                          
* `Title`: CharField                                                                          
* `Type`: CharField (e.g. video, text, PDF)                                                                          
* `Content`: TextField/FileField                                                                          
* `Module`: ForeignKey (link to module model)                                                                          
**Enrollment**                                                                           
`ID`: PrimaryKey (automatically generated)                                                                          
`User`:ForeignKey (link to user model)                                                                          
`Course`: ForeignKey (link to course model)                                                                          
`Enrollment_date`: DateTimeField (date and time of course enrollment)                                                                          
`Status`: CharField (e.g. 'active', 'completed', 'canceled')                                                                          
**UserProgress**                                                                          
* `ID`: PrimaryKey (automatically generated)                                                                          
* `User`:ForeignKey (link to user model)Course: ForeignKey (link to course model)                                                                          
* `Module`: ForeignKey (link to module model)                                                                          
* `Progress`: IntegerField (percentage of module or course completion)                                                                          
* `Last_updated`: DateTimeField (date and time of the last progress update)                                                                          

---

## **Functional Requirements**                                                                           

**CRUD**:                                                                          

1) **User**                                                                          
* Create user (**POST**)                                                                          
* Get all users (**GET**)                                                                          
* Get user by ID (**GET**)                                                                          
* Update User (**PUT**/**PATCH**)                                                                          
* Delete User (**DELETE**)                                                                          
* Log in (**POST**)                                                                          
* Log out (**POST**)                                                                          
* Change password (**POST**)                                                                          
* Reset password (**POST**)                                                                          
2) **Course**                                                                          
* Create a course (**POST**)                                                                          
* Get all courses (**GET**)                                                                          
* Get course by ID (**GET**)                                                                          
* Update course (**PUT**/**PATCH**)                                                                          
* Delete a course (**DELETE**)                                                                          
* Enroll in a course (**POST**)                                                                          
* Unsubscribe from a course (**DELETE**)                                                                          
3) **Module**                                                                          
* Create a module (**POST**)                                                                          
* Get all modules (**GET**)                                                                          
* Get module by ID (**GET**)                                                                          
* Update module (**PUT**/**PATCH**)                                                                          
* Delete module (**DELETE**)                                                                          
4) **Training Material**                                                                          
* Create training material (**POST**)                                                                          
* Get all training materials (**GET**)                                                                          
* Get training material by ID (**GET**)                                                                          
* Update training material (**PUT**/**PATCH**)                                                                          
* Delete training material (**DELETE**)                                                                          
5) **Course Enrollment** (**Enrollment**)                                                                          
* Create course enrollment (**POST**)                                                                          
* Get all course enrollments (**GET**)                                                                          
* Get course enrollment by ID (**GET**)                                                                          
* Update course record (**PUT**/**PATCH**)                                                                          
* Delete a course record (**DELETE**)                                                                          
6) **UserProgress**                                                                                                                                                    
* Create a progress record (**POST**)                                                                          
* Get all user progress (**GET**)                                                                          
* Get user progress by ID (**GET**)                                                                          
* Update User Progress (**PUT**/**PATCH**)                                                                          
* Delete user progress record (**DELETE**)                                                                          

# **Permissions**                                                                                                                                                         
1) **Admin**:                                                                                                                                                         
* Managing all courses                                                                                                                                                                                                                                        
* Managing all users                                                                                                                                                       
2) **User**:                                                                                                                                                         
* Managing only himself profile                                                                                                                                                         
* Have possibility to enroll in courses                                                                                                                                                         
---

## **Security**                                                                                                                                                         

1) **Authentication**:                                                                                                                                                                                                                                        
* Consider implementing an authentication system (e.g. **Token Authentication**).                                                                                                                                                                                                                                        

2) **Data Validation**:                                                                                                                                                                                                                                        
* Check for correct input data for all operations.                                                                                                                                                         

---

## **Testing**                                                                                                                                                         
1) **Unit tests**:                                                                                                                                                         
* Writing tests to verify the functionality of all **CRUD** operations.                                                                               
2) **Integration tests**:                                                                               
* Testing the interaction of system components.                                                                               

---

## **Documentation**                                                                               

1) **README**:                                                                               
Project Description.                                                                               
List of technologies used to write the project.                                                                               
Instructions on how to install and run the application: commands one                                                                                                                                    
by one. How to run the project.                                                                                                                                     
2) **API documentation**:                                                                               
Description of endpoints, request and response formats. Examples of                                                                                                                                     
data that must be passed to process requests.                                                                                                                                       

---

# **User Flow \ User Journey**                                                                             

**For the Administrator**:                                                                          

* **As an administrator, I want to** be able to create courses to offer users                                                                           
a variety of educational programs.                                                                          
This includes providing a course title, description, start and end date.                                                                          

* **As an administrator, I want to** add and edit modules and learning materials                                                                           
in courses to shape the content of each course.                                                                          
Ability to select the type of learning material (video, text, PDF).                                                                          

* **As an administrator, I want to be able to** edit and delete courses, modules                                                                           
and learning materials to correct errors or update information.                                                                          

* **As an administrator, I want to** see statistics on courses and users to                                                                           
analyze training data.                                                                          

* **As an administrator, I want to be able to** manage users (create, edit, delete)                                                                           
to provide administration of the platform.                                                                          

**For the User**                                                                          
* **As a user, I want to be able to** browse through the list of available and active                                                                           
courses to select the courses I am interested in learning.                                                                          

* **As a user, I want to** enroll in courses and complete training modules to gain                                                                           
new knowledge and skills.                                                                          

* **As a user, I want to be able to** view learning materials within courses to explore                                                                           
the educational content provided.                                                                          

* **As a user, I want to be able to** see my progress through courses and modules to                                                                           
understand my learning achievements.                                                                          

* **As a user, I want to be able to** register and log in so that my results and                                                                           
progress can be linked to my account.                                                                          

* **As a user, I want to be able to** change my personal details and manage my                                                                           
account to keep my information up to date.                                                                          

---
### **Rules for working with **Git** for thesis writing and development. Branch organization**                                                                               
`One task - one branch`: You should create a separate branch from the                                                                                
main for each new task or functionality.                                                                                
The name of the branch should reflect the nature of the task.                                                                               

`Prohibit direct changes to the main`: All changes should be pushed into                                                                                
the main via **Pull Requests (PR)** after review and approval by other team members.                                                                               


**Commits**                                                                               
* `Many commits`: Make commits frequently to track progress and facilitate                                                                               
possible debugging.                                                                               
* `Informative commits`: Each commit should contain a clear and concise                                                                               
description of the changes made.                                                                               
* `Prefix commit system`:                                                                               
    * `doc`: To add or modify documentation.                                                                               
    * `feat`: To add new functionality.                                                                               
    * `fix`: For bug fixes or debugging.                                                                               

**Working with Pull Requests (PR)**                                                                                                                                                              
* `PR Description`: Each PR should contain a detailed description of the                                                                                
changes made and references to relevant tasks or requirements.                                                                               
* `Code-review`: Prior to merging with the main, the PR should be                                                                               
code-reviewed by at least one other team member.                                                                               
* `Testing`: Before creating a PR, make sure your code passes all                                                                                
tests and meets coding standards.                                                                               

**Regular updates**                                                                               
`Synchronize with main`: Regularly update your working branches by                                                                                
synchronizing them with the main branch of main to avoid merge conflicts.   