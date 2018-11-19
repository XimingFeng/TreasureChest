*****************************************
Software Requirement Specification (SRS)
*****************************************
 


###############
Introduction
###############

========
Purpose
========
This project is being undertaken by the Pima County Consolidated Justice Court 
(PCCJC) IT Department. The project is to develop IT device management system. 

====================
Document Conventions
====================
This document follows the standard IEEE, 1998 guidelines and conventions[1].

=========================================
Intended Audience and Reading Suggestions
=========================================
This document should be legible and understandable to all IT department 
employee.

===============
Product Scope
===============
The project is to develop tool for user to register, edit and delete IT device 
information for management user and to view, request IT device for normal user.
The projects include full stack web development of the management system. 

Objective of the application includes:

* For non-IT users  
   * normal user should be able to 
      * view device that he/she has 
      * request devices
   * suporvisors should be able to 
      * have all permissions that normal user has
      * view all the equipments in different department 
* IT users should be able to 
   * have all permission that Non-IT user has
   * register, edit, and delete device information 

Objective of the application does not include:

* User management, all the user management are though django administration page
* Automatic network information update. 
