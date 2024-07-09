# csvAirtable

pipeline that syncs csv data from aflinx tables into airtable


## NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE

![nightmare](nightmare.jpg)

* ocr not working completely -- not all tables are in csv
* i manually put them in airtable
* halt on the project for now... will automate this process later


## prompt for chatgpt to create synthetic data:
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