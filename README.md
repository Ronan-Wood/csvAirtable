# csvAirtable

pipeline that syncs csv data from aflinx tables into airtable


## NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE

![nightmare](nightmare.jpg)

* ocr not working completely -- not all tables are in csv
* i manually put them in airtable
* halt on the project for now... will automate this process later


## prompt for chatgpt to create synthetic data:
### ASPNETUSERS
The attached file is a csv containing the following fields:
- Id (unique number)
- First_name (string)
- Last_name (string)
- Email (string)
- DoDId (number)
- CreatedDate (date MM/DD/YYYY)
- UpdatedDate (date MM/DD/YYYY)
- createdby (string)
- updatedby (string)
- EmailConfirmed ("checked" or blank)
- PasswordHash (string)
- SecurityStamp (string)
- PhoneNumber (string)
- PhoneNumberConfirmed ("checked" or blank)
- TwoFactorEnabled ("checked" or blank)
- LockoutEndDate (date MM/DD/YYYY)
- LockoutEnabled ("checked" or blank)
- AccessFailedCount (number)
- UserName (string)
- Name (string, concatenate First_name and Last_name)
- Location (string)
- Discriminator (string)
- IsDeleted ("checked" or blank)
- IsActive ("checked" or blank)
- ActivationEmail ("checked" or blank)
- EmailSent ("checked" or blank)
- MilitaryEmail (string)
- CivilianEmail (string)
- DefenseIDNumber (number)
- ProfilePicture (string, very short description)
- Speciality (string)
- EmailNotification ("checked" or blank)
- MobileNotification ("checked" or blank)
- WebNotification ("checked" or blank)
- AccountIsActive ("checked" or blank)

Please create 10 rows of synthetic data. The csv describes members of an airforce base.
The csv attached has one row of data for you to use as an example.
Output a csv
---
### EDUCATION
The attached file is a csv containing the following fields:

- EducationId (unique number starting from 1)
- UserId (blank)
- NameoftheAccreditedSchool (string)
- CertificateEarned (string)
- FieldofStudy (string)
- GraduationYear (date MM/DD/YYYY)
- FileName (string)
- createddate (date MM/DD/YYYY)
- updateddate (date MM/DD/YYYY)
- createdby (string)
- updatedby (string)
- IsDelete ("checked" or blank)
- SubCategoryId (blank)
- CategoryId (blank)D

Please create 10 rows of synthetic data. The csv describes members of an airforce base.
The csv attached has one row of data for you to use as an example.
Output a csv
--- 
### Designation
- DesignationID (Unique number stating from one)
- UserId (Blank)
- DesignationTitle (String)
- DesignationDate (Date MM/DD/YYYY)
- DesignationDescription (String)
- FileName (String)
- CreatedDate (Date MM/DD/YYYY)
- UpdatedDate (Date MM/DD/YYYY)
- CreatedBy (String)
- UpdatedBy (String)
- isDelete ("Checked" or Blank)
- SubCategoryID (Blank)
- CategoryID (Blank)
- GrantedBy (String)
- ExperationDate (Date MM/DD)
