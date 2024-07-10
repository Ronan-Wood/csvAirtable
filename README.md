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

- EducationId (unique number starting from 2)
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
- CategoryId (blank)

Please create 10 rows of synthetic data. The csv describes the education of members of an airforce base.
The csv attached has one row of data for you to use as an example.
Output a csv
---
### DOCUMENT
The attached file is a csv containing the following fields:

- DocumentId (unique number starting from 2)
- UserId (blank)
- TypeofDocument (string)
- DocumentTitle (string)
- DocumentDescription (string, a brief description of the document and how it pertains to a member)
- FileName (string, same as DocumentTitle)
- createddate (date MM/DD/YYYY)
- updateddate (date MM/DD/YYYY)
- createdby (blank)
- updatedby (blank)
- IsDelete ("checked" or blank)

Please create 10 rows of synthetic data. The csv describes documents assigned to members of an airforce base.
The csv attached has one row of data for you to use as an example.
Output a csv
---
### CERTIFICATE
The attached file is a csv containing the following fields:

- CertificateId (unique number starting from 2)
- UserId (blank)
- CategoryId (blank)
- TitleofLicense (string, weapon name (M18, Grenade, Rifle, 240B, M249) concatenated with "License" by a space)
- CertificateDate (date MM/DD/YYYY)
- ExpirationDate (date MM/DD/YYYY, same MM/DD as CertificateDate but two years in ahead)
- CertificationDocument (date MM/DD/YYYY, same as CertificateDate)
- createddate (date MM/DD/YYYY)
- updateddate (date MM/DD/YYYY, same as createddate)
- createdby (blank)
- updatedby (blank)
- IsDelete ("checked" or blank)
- SubCategoryId (blank)
- GrantedBy (blank)

Please create 10 rows of synthetic data. The csv describes certificates that members of an airforce base have.
The csv attached has one row of data for you to use as an example.
Output a csv