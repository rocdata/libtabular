CSV data formats
================

The Comma-Separated Values (CSV) data format is in widespread use in many domains
(education, research, business, finance, etc.).

Any spreadsheet program (LibreOffice, OpenOffice, GoogleSheets, Excel, etc.) can
produce CSV files using the "Save As.." function by starting from a spreadsheet sheet.
This makes the CSV a very interesting format for data creation, editing, and exchange
between non-technical users (teachers, admins, office workers, analysts, etc.).

At the same time, the CSV format can be easily loaded and parsed by programmers,
integrations specialists, database administrators, and machine learning experts
since it is a "structured" format (with the structure being defined by a 
"headers row", which is usually the first row of the tabular data).



Users
-----

- Teacher: good familiarity with spreadsheets, can benefit from accessing data
  as spreadsheets and also act as reviewers, and upload new data.
- Curriculum experts: easily create standards, content collections, and
  curriculum alignment data as a non-technical user.
- Administrators: easy to handle lots of data (access, share by email, review, etc.)
- Platform developers: easy to parse CSV data and store in DB; easy to generate CSV data from DB
- Machine learning practitioners: can use any machine-readable data for training algorithms



Use cases
---------

Repository of Organized Curriculums (ROC) project use cases:

- Upload curriculum standards document spreadsheet
- Download curriculum standards data as spreadsheet
- Upload content correlations spreadsheet
- Upload standards crosswalk spreadsheet


Ricecooker and Kolibri Studio use cases:

- Ricecooker channel from spreadsheet of links
- Studio upload channel from spreadsheet of links
- Studio channel corrections/edits/enhancements from spreadsheet of commands
- Studio channel remixing based on a spreadsheet of "include" statements (include topic and include node)
