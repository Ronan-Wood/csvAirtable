# csvAirtable

pipeline that syncs csv data from aflinx tables into airtable


## NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE

![nightmare](nightmare.jpg)

* ocr not working completely -- not all tables are in csv
* i manually put them in airtable
* halt on the project for now... will automate this process later
---



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
The csv attached has one row of data for you to use as an example. Output a csv.
--- 
### Designation
The attached file is a csv containing the following fields:

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
- ExperationDate (Date MM/DD/YY)

Please create 10 rows of synthetic data. The csv describes members of an airforce base.
The csv attached has one row of data for you to use as an example. Output a csv.
---
### Category
The attached file is a csv containing the following fields:

- CategoryID (Unique number stating from one)
- CategoryName (String)
- CreatedDate (Date MM/DD/YYYY)
- UpdatedDate (Date MM/DD/YYYY)
- CreatedBy (String)
- UpdatedBy (String)
- isDelete ("Checked" or Blank)
- WorkExperince (Blank)

Please create 10 rows of synthetic data. The csv describes members of an airforce base.
The csv attached has one row of data for you to use as an example. Output a csv.
---
### ASPNetRoles
The attached file is a csv containing the following fields:

- ID (Unique number stating from one)
- Name (String)
- Description (String)
- CreatedDate (MM/DD/YYYY)
- UpdatedDate (MM/DD/YYYY)
- createdBy (String - Pull from ASPNetUsers CSV)
- UpdatedBy (String - Same as "createdBy")
- ConcurruncyStanp (Number - Same as ID)
- NormalizedName (String - Same as Name)
- ShowinList ("Checked" or Blank)
- Permissions (String)

Please create 10 rows of synthetic data. The csv describes members of an airforce base.
The csv attached has one row of data for you to use as an example. Output a csv.
---
### WorkExperince
The attached file is a csv containing the following fields:

- WorkID (Unique number stating from one)
- UserID (Blank)
- JobTitle (String)
- WorkStartDate (Date MM/DD/YYYY)
- WorkEndDate (Date MM/DD?YYYY)
- WordDescription (String)
- CategoryId (Blank)
- WorkType (String)
- FileName (String)
- SubCategoryId (Blank)
- CompanyName (String)
- CreatedDate (Date MM/DD/YYYY)
- UpdatedDate (Date MM/DD/YYYY)
- CreatedBy (String - Combind First and Last Name from AspNetUsers)
- UpdatedBy (String - Same as CreatedBy)
- isDelete ("Checked" or Blank)

Please create 10 rows of synthetic data. The csv describes members of an airforce base.
The csv attached has one row of data for you to use as an example. Output a csv.
---
### AspNetUserRoles
The attached file is a csv containing the following fields:

- UserRoleId (Unique number stating from one)
- UserId (Blank)
- RoleId (Blank)
- createdDate (Date MM/DD/YYYY)
- UpdatedDate (Date MM/DD/YYYY)
- CreatedBy (String- Combind First and Last Name from AspNetUsers)
- UpdatedBy (String - Same as CreatedBy)
- isDelete ("Checked" or Blank)

Please create 10 rows of synthetic data. The csv describes members of an airforce base.
The csv attached has one row of data for you to use as an example. Output a csv.
---
### CheckList
The attached file is a csv containing the following fields:

- CheckListId (Unique number stating from one)
- CheckListName (String)
- CheckListType (String)
- createdDate (Date MM/DD/YYYY)
- UpdatedDate (Date MM/DD/YYYY)
- CreatedBy (String- Combind First and Last Name from AspNetUsers)
- UpdatedBy (String - Same as CreatedBy)
- isDelete ("Checked" or Blank)

Please create 10 rows of synthetic data. The csv describes members of an airforce base.
The csv attached has one row of data for you to use as an example. Output a csv.
---
### CheckListTaskResponse
The attached file is a csv containing the following fields:

- TaskResponseID (Unique number stating from one)
- TaskId (Blank)
- CheckListID (Blank)
- CheckListMessageId (Blank)
- CheckListUserId (Blank) 
- UserId (Blank)
- YesAnswer (String)
- NotesAnswer (String)
- UploadAnswer (String)
- CreatedDate (Date MM/DD/YYYY)
- UploadedDate (Date MM/DD/YYYY)
- CreatedBy (String - Combind First and Last Name from AspNetUsers)
- UpdatedBy (String - Same as CreatedBy)
- isDelete ("Checked" or Blank)

Please create 10 rows of synthetic data. The csv describes members of an airforce base.
The csv attached has one row of data for you to use as an example. Output a csv.
---
### CheckListTasks
The attached file is a csv containing the following fields:

- TaskId (Unique number stating from one)
- CheckListId (Blank)
- TaskName (String)
- TaskNote (String)
- CreatedDate (Date MM/DD/YYYY)
- UpdatedDate (Date MM/DD/YYYY)
- CreatedBy (String - Combind First and Last Name from AspNetUsers)
- UpdatedBy (String - Same as CreatedBy)
- isDelete ("Checked" or Blank)
- ShowYes ("Checked" or Blank)
- ShowNotes ("Checked" or Blank)
- Show Upload ("Checked" or Blank)

Please create 10 rows of synthetic data. The csv describes members of an airforce base.
The csv attached has one row of data for you to use as an example. Output a csv.
---
### Survey
The attached file is a csv containing the following fields:

- SurveyId (Unique number stating from one)
- SurveyName (String)
- SurveyDescription (String)
- SurveyType (String)
- CreatedDate (Date MM/DD/YYYY)
- UpdatedDate (Date MM/DD/YYYY)
- CreatedBy (String - Combind First and Last Name from AspNetUsers)
- UpdatedBy (String - Same as CreatedBy)
- isDelete ("Checked" or Blank)
- SurveyChoices (Blank)
- SurveyChoicesReponse (Blank)
- Communication (Blank)

Please create 10 rows of synthetic data. The csv describes members of an airforce base.
The csv attached has one row of data for you to use as an example. Output a csv.
---
### MessageGroups
The attached file is a csv containing the following fields:

- MessageGroupsId (Unique number stating from one)
- MessageGroupName (String)
- MessageGroupDescription (String)
- CreatedDate (Date MM/DD/YYYY)
- UpdatedDate (Date MM/DD/YYYY)
- CreatedBy (String - Combind First and Last Name from AspNetUsers)
- UpdatedBy (String - Same as CreatedBy)
- isDelete ("Checked" or Blank)
- Communication (Blank)
- MessageGroupUsers (Blank)
- AppMessageUsers (Blank)

Please create 10 rows of synthetic data. The csv describes members of an airforce base.
The csv attached has one row of data for you to use as an example. Output a csv.
---
### SurveyChoices
The attached file is a csv containing the following fields:

- ChoiceId (Unique number stating from one)
- SurveyId (Blank)
- Question (String)
- QuestionType (String)
- CreatedDate (Date MM/DD/YYYY)
- UpdatedDate (Date MM/DD/YYYY)
- CreatedBy (String - Combind First and Last Name from AspNetUsers)
- UpdatedBy (String - Same as CreatedBy)
- isDelete ("Checked" or Blank)
- QuestionNumber (Number)
- SurveyChoiceOptions (Blank)

Please create 10 rows of synthetic data. The csv describes members of an airforce base.
The csv attached has one row of data for you to use as an example. Output a csv.
---
### SurveyChoiceOptions
The attached file is a csv containing the following fields:

- ChoiceOptionId (Unique number stating from one)
- ChoiceId (Blank)
- ChoiceName (String)
- ChoiceTest (String)
- ChoiceImage (String)
- ChoiceStars (String)
- ChoiceType (String)
- ChoiceNote (String)
- CreatedDate (Date MM/DD/YYYY)
- UpdatedDate (Date MM/DD/YYYY)
- CreatedBy (String - Combind First and Last Name from AspNetUsers)
- UpdatedBy (String - Same as CreatedBy)
- isDelete ("Checked" or Blank)
- ChoiceNumber (Number)

Please create 10 rows of synthetic data. The csv describes members of an airforce base.
The csv attached has one row of data for you to use as an example. Output a csv.
---
### SurveyChoicesResponse
The attached file is a csv containing the following fields:

- ChoiceResponseId (Unique number stating from oneg)
- ChoiceId (Blank)
- SurveyId (Blank)
- SurveyMessageId (Blank)
- SurveyUserId (Blank) 
- UserId (Blank)
- UserResponse (String)
- CreatedDate (Date MM/DD/YYYY)
- UpdatedDate (Date MM/DD/YYYY)
- CreatedBy (String - Combind First and Last Name from AspNetUsers)
- UpdatedBy (String - Same as CreatedBy)
- isDelete ("Checked" or Blank)

Please create 10 rows of synthetic data. The csv describes members of an airforce base.
The csv attached has one row of data for you to use as an example. Output a csv.
---
### Communication
The attached file is a csv containing the following fields:

- CommunicationId (Unique number stating from one)
- CommunicationIdCategory (String)
- UserId (Blank)
- MessageGroupId (Blank)
- Title (String)
- CommunicationIdType (String)
- NudgeMessage (String)
- ReqId (Blank)
- ReqSlotId (Blank)
- CommunicationIdDate (Date MM/DD/YYYY)
- Link (String)
- SurveryId (Blank)
- CheckListId (Blank)
- Urgent (String)
- Status (String)
- CreatedDate (Date MM/DD/YYYY)
- UpdatedDate (Date MM/DD/YYYY)
- CreatedBy (String - Combind First and Last Name from AspNetUsers)
- UpdatedBy (String - Same as CreatedBy)
- isDelete ("Checked" or Blank)
- SendTo (String)
- ScheduleMessage (String)
- CommunicationDocument (String)

Please create 10 rows of synthetic data. The csv describes members of an airforce base.
The csv attached has one row of data for you to use as an example. Output a csv.
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

Please create 10 rows of synthetic data. The csv describes members of an airforce base.
The csv attached has one row of data for you to use as an example. Output a csv.
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

Please create 10 rows of synthetic data. The csv describes certificates that members of an airforce base have. The csv attached has one row of data for you to use as an example. Output a csv.
---
### TRAINING
The attached file is a csv containing the following fields:

- TrainingId (unique number starting from 2)
- UserId (blank)
- TrainingTitle (string, weapon name (M18, Grenade, Rifle, 240B, M249) concatenated with "Training" by a space)
- StartDate (date MM/DD/YYYY)
- EndDate (date MM/DD/YYYY, exactly 2 months ahead of StartDate)
- FileName (string, same as TrainingTitle)
- createddate (date MM/DD/YYYY)
- updateddate (date MM/DD/YYYY, same as createddate)
- createdby (blank)
- updatedby (blank)
- IsDelete ("checked" or blank)
- SubCategoryId (blank)
- CategoryId (blank)
- GrantedBy (blank)
- ExpirationDate (date MM/DD/YYYY, same MM/DD as EndDate but two years ahead)

Please create 10 rows of synthetic data. The csv describes training that members of an airforce base have. The csv attached has one row of data for you to use as an example. Output a csv.
---
### SubCategory
The attached file is a csv containing the following fields:

- SubCategoryId (unique number starting from 2)
- CategoryId (Blank)
- SubCategoryName (String - Categories related to big Categories (Operations, Medical, Mecanical, Etc.))
- createddate (date MM/DD/YYYY)
- updateddate (date MM/DD/YYYY, same as createddate)
- createdby (String - Combind First and Last Name from AspNetUsers)
- UpdatedBy (String - Same as CreatedBy)
- IsDelete ("checked" or blank)
- WorkExperience (Blank)
- Education (Blank)
- Designation (Blank)
- Certificate (Blank)
- Training_AFLINX (Blank)
- License (Blank)

Please create 10 rows of synthetic data. The csv describes training that members of an airforce base have. The csv attached has one row of data for you to use as an example. Output a csv.
---
### MessagePollOptions
The attached file is a csv containing the following fields:

- PollOptionId (unique number starting from 2)
- MessageDetailId (Blank)
- PollOptionName (String)
- createddate (date MM/DD/YYYY)
- updateddate (date MM/DD/YYYY, same as createddate)
- createdby (String - Combind First and Last Name from AspNetUsers)
- UpdatedBy (String - Same as CreatedBy)
- IsDelete ("checked" or blank)

Please create 10 rows of synthetic data. The csv describes training that members of an airforce base have. The csv attached has one row of data for you to use as an example. Output a csv.
---
### CheckListMessage
The attached file is a csv containing the following fields:

- Id (unique number starting from 2)
- SendTo (String - String - Combind First and Last Name from AspNetUsers)
- MessageText (String - What they are to do.)
- ScheduleMessage ("checked" or blank)
- SendDate (Date MM/DD/YYYY)
- CheckListId (Blank)
- createddate (date MM/DD/YYYY)
- updateddate (date MM/DD/YYYY, same as createddate)
- createdby (String - Combind First and Last Name from AspNetUsers - Diffrent than SentTo)
- UpdatedBy (String - Same as CreatedBy)
- IsDelete ("checked" or blank)
- Status (Single Select - Read or Unread)
- MessageTitle (String - Related to MessageText)
- CheckListTaskResponse (Blank)

Please create 10 rows of synthetic data. The csv describes training that members of an airforce base have. The csv attached has one row of data for you to use as an example. Output a csv.
---
### License
The attached file is a csv containing the following fields:

- LicensesId (unique number starting from 2)
- UserId (Blank)
- LicenseTitle (String)
- LicenseDate (Date MM/DD/YYYY)
- LicenseExpireDate (Date MM/DD/YYYY)
- File Name (String)
- createddate (date MM/DD/YYYY)
- updateddate (date MM/DD/YYYY, same as createddate)
- createdby (String - Combind First and Last Name from AspNetUsers - Diffrent than SentTo)
- UpdatedBy (String - Same as CreatedBy)
- IsDelete ("checked" or blank)
- SubCategoryId (Blank)
- CategoryId (Blank)
- GrantedBy (String - Name from AspNextUser - Diffrent from CreatedBy)

Please create 10 rows of synthetic data. The csv describes training that members of an airforce base have. The csv attached has one row of data for you to use as an example. Output a csv.
---
### MessageUsers
The attached file is a csv containing the following fields:

- MessageUserId (unique number starting from 2)
- MessageDetailId (Blank)
- MessageGroupId (Blank)
- UserId (Blank)
- createddate (date MM/DD/YYYY)
- updateddate (date MM/DD/YYYY, same as createddate)
- createdby (String - Combind First and Last Name from AspNetUsers - Diffrent than SentTo)
- UpdatedBy (String - Same as CreatedBy)
- IsDelete ("checked" or blank)
- isSent ("checked" or blank)
- SentTime (date MM/DD/YYYY)
- isError ("checked" or blank)
- ErrorDetail (String)
- Status (String)
- UserResponse (String)
- ReadCount (Number)
- PollAnswer (String)
- MessageStatus (String)
- AppMessageUser (Blank)

Please create 10 rows of synthetic data. The csv describes training that members of an airforce base have. The csv attached has one row of data for you to use as an example. Output a csv.
---
### Speciality
The attached file is a csv containing the following fields:

- Id (unique number starting from 2)
- Name (String)
- createddate (date MM/DD/YYYY)
- updateddate (date MM/DD/YYYY, same as createddate)
- createdby (String - Combind First and Last Name from AspNetUsers - Diffrent than SentTo)
- UpdatedBy (String - Same as CreatedBy)
- IsDelete ("checked" or blank)

Please create 10 rows of synthetic data. The csv describes training that members of an airforce base have. The csv attached has one row of data for you to use as an example. Output a csv.
---
### SurveyMessageUsers
The attached file is a csv containing the following fields:

- SurveyUserId (unique number starting from 2)
- SurveyMessageId (Blank)
- GroupId (Blank)
- UserId (Blank)
- createddate (date MM/DD/YYYY)
- updateddate (date MM/DD/YYYY)
- createdby (String - Combind First and Last Name from AspNetUsers - Diffrent than SentTo)
- UpdatedBy (String - Same as CreatedBy)
- IsDelete ("checked" or blank)
- isSent ("checked" or blank)
- SentTime (date MM/DD/YYYY)
- isError ("checked" or blank)
- ErrorDetail (String)
- Status (String)
- UserResponse (String)
- Readcount (Number)
- MessageStatus (String)
- SurveyChoicesResponse (Blank)

Please create 10 rows of synthetic data. The csv describes training that members of an airforce base have. The csv attached has one row of data for you to use as an example. Output a csv.
---
### Appointment Type
The attached file is a csv containing the following fields:

- Id (Name of the Appoinment Type)
- ATId (Blank)
- createddate (date MM/DD/YYYY)
- updateddate (date MM/DD/YYYY)
- createdby (String - Combind First and Last Name from AspNetUsers - Diffrent than SentTo)
- UpdatedBy (String - Same as CreatedBy)
- IsDelete ("checked" or blank)
- Requirments_Aflinx (Blank)

Please create 10 total rows of synthetic data. The csv describes training that members of an airforce base have. The csv attached has one row of data for you to use as an example. Output a csv.