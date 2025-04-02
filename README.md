
# Blood donation portal for an organization
Blood Donation Management System - Documentation
# Overview
This Django-based web application is designed to manage blood donation activities for organizations, hospitals, and donors. The system provides role-based access control with different functionalities for administrators, superusers, privileged users, and regular users.

# Features
User Roles and Access Control
Admin: Manages organizations and superusers

SuperUser (SU): Manages users, areas, hospitals, donors, and donations within their organization

Privileged User (PU): Manages hospitals, donors, and donations

User: Registers donors and manages donations

# Core Functionalities
Organization Management

Add/delete organizations

Manage organization details (name, address, contact)

User Management

Add/delete users with different roles

User authentication and session management

Donor Management

Register new donors with complete details

Search donors by name, phone, blood group, or area

Edit donor information

View donor lists

Blood Donation Tracking

Record blood donations

Track donation status (Donated/Not Donated)

Automatically update donor eligibility (90-day cooldown period)

Hospital Management

Add/delete hospitals

View hospital lists

Area Management

Add/delete areas

View area lists

Reporting

Generate donation reports by date range

Export reports to Excel format

Dashboard Analytics

Monthly donation statistics

Year-to-date donation counts

Comparison with previous month

# Technical Details
 ## Models
organizationMaster: Stores organization information

userMaster: Stores user details and roles

loginMaster: Handles authentication credentials

AreaMaster: Manages geographical areas

hospitalMaster: Stores hospital information

donorMaster: Maintains donor records

donationDetails: Tracks donation history

Dependencies
Django

openpyxl (for Excel report generation)

Python datetime utilities

Security Features
Session-based authentication

Role-based access control

Password protection (using phone number as default password)
