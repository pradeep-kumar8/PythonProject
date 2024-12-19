# PMS Dashboard Automation Script
This project automates the data analysis and visualization processes for the Performance Management System (PMS) dashboard, with specific integration to the Summit Tool data columns. The automation aims to streamline the extraction, processing, and visualization of PMS incident data for enhanced decision-making, reducing manual effort, and ensuring that dashboards are updated with accurate insights based on fixed organization-specific data fields.

## Project Overview
The primary goal of this automation script is to optimize and automate the workflow for analyzing PMS data, ensuring accuracy and efficiency in generating dashboards and reports. The script processes the fixed data fields provided by the Summit Tool and produces valuable insights for performance managers and decision-makers.

## Key Features
### Data Extraction and Preprocessing:

The script processes data provided in the fixed columns of the Summit Tool, which include incident details, status, resolution times, and other key metrics.
Automatically filters and processes the PMS data, removing unnecessary columns, handling missing values, and converting data into suitable formats for analysis.
Key Metrics Calculation:

### Automatically computes key metrics such as:
Number of incidents resolved by each analyst.
Percentage of incidents meeting the Time to Resolution (TTR) target.
Average resolution time (TTO) per incident and analyst.
Incident trends by categories, teams, and dates.
Identifies outliers or incidents that may require further investigation (e.g., excessive resolution times or unresolved issues).
Dashboard Generation:

Generates visualizations of key performance metrics, including bar charts, line graphs, and pie charts.
Visualizations are saved in a ready-to-use format (e.g., PNG, JPEG) and can be incorporated into the dashboard or reports.
### Automated Report Generation:

The script can generate summary reports in Excel or CSV format with detailed insights on the incident status, resolution time, analyst performance, and other relevant metrics.
Optionally, the report can be emailed automatically to the stakeholders, ensuring that team leads, managers, and other decision-makers have timely updates.
### Summit Tool Integration:

The data fields are fixed and aligned with the organization’s Summit Tool data structure. These fields include:
1. Incident ID: Unique identifier for each incident.
2. Status: Current status of the incident (e.g., 'Closed', 'Pending').
3. Category: Incident category (e.g., 'Hardware', 'Software').
4. Analyst: Name of the analyst responsible for resolving the issue.
5. Time to Outcome (TTO): The time taken to resolve the issue.
6. Time to Resolution (TTR): The actual resolution time.
7. Resolution Type: The nature of the resolution provided (e.g., 'Workaround', 'Permanent Fix').
8. Incident Description: A brief description of the issue raised.
### Task Automation:

The entire analysis can be automated and scheduled to run at specific times (e.g., daily, weekly) via cron jobs (Linux) or Task Scheduler (Windows), ensuring that the dashboard is always up-to-date.
Dataset Description
#### The dataset used in this automation script comes from the Summit Tool and contains the following key columns:

1. Incident ID: Unique identifier for each incident.
2. Status: Indicates whether the incident is still open, in progress, or resolved.
3. Category: Categorizes the incident (e.g., 'Hardware', 'Network', 'Software').
4. Analyst: The analyst assigned to resolve the incident.
5. Time to Outcome (TTO): The time taken to resolve the issue.
6. Time to Resolution (TTR): The resolution time, indicating whether the SLA was met.
7. Resolution Type: Type of resolution provided (e.g., 'Workaround', 'Permanent Fix').
8. Incident Description: A brief description of the issue.
9. Location: Location associated with the incident (optional, if required by the organization).
Dependencies
#### To run this project, ensure that you have the following Python libraries installed:

Python 3.x
Pandas
NumPy
Matplotlib
Openpyxl (for report generation in Excel format)
Smtplib (for emailing reports)
