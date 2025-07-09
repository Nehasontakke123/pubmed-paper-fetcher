# pubmed-paper-fetcher
Use Git for version control. The code must be hosted on GitHub.



# PubMed Paper Fetcher 📄🔍

A command-line tool to fetch PubMed research papers that include **non-academic authors** affiliated with pharmaceutical or biotech companies.

---

## ✨ Features

- 🔍 Search PubMed using any valid query.
- 🧪 Filters out academic authors (based on affiliation).
- 🏢 Identifies authors from **biotech/pharma companies**.
- 📧 Extracts corresponding author email (if available).
- 📥 Save results to **CSV** or print to console.
- ✅ Built using **typed Python** with proper error handling.
- ⚙️ Packaged and managed using **Poetry**.

---

## 📦 Project Structure

pubmed-paper-fetcher/
├── pubmed_fetcher/
│ ├── init.py
│ ├── main.py # Command-line entry point
│ └── utils.py # Core logic and helper functions
├── pyproject.toml # Poetry configuration
├── README.md # You’re reading this!
---

## 🛠 Installation

1. **Clone the Repository:**

```bash
git clone https://github.com/your-username/pubmed-paper-fetcher.git
cd pubmed-paper-fetcher


Install Dependencies using Poetry:
poetry install


🚀 Usage
poetry run get-papers-list "COVID-19 vaccine"


Optional Flags
Flag	Description
-d, --debug	Print debug information
-f, --file	Save output to CSV file (e.g., out.csv)

Example:
poetry run get-papers-list "SARS-CoV-2" -d -f results.csv

Output CSV Format

| PubmedID | Title               | Publication Date | Non-academic Author(s) | Company Affiliation(s) | Corresponding Author Email                    |
| -------- | ------------------- | ---------------- | ---------------------- | ---------------------- | --------------------------------------------- |
| 40631743 | Some Research Title | 2025             | Smith                  | Biotech Inc.           | [smith@biotech.com](mailto:smith@biotech.com) |


🔍 How It Works
Uses NCBI PubMed API via esearch + efetch.

For each article:

Parses title, authors, affiliations, publication date.

Uses keyword-based filtering to identify non-academic affiliations:

Excludes: university, college, institute, school, etc.

Includes: hospital, clinic, labs, biotech, inc., etc.

Extracts first valid email using regex.

📚 Tools & Libraries Used
Poetry – For packaging and dependency management

Requests – For making HTTP requests

ElementTree – For XML parsing

Regex – For extracting emails

🧠 Author
👩‍💻 Neha Sontakke

📧 nehasontakke1880@gmail.com

📝 License
This project is licensed under the MIT License.

🏆 Bonus (Optional for Extra Credit)
 Publish this package on TestPyPI (can be added later)

✅ Example CSV Output (Snippet)

PubmedID,Title,Publication Date,Non-academic Author(s),Company Affiliation(s),Corresponding Author Email
40631953,Vogt-Koyanagi-Harada syndrome potentially associated with COVID-19 vaccination: a case report and literature review.,2025,Luo,"Department of Reproductive Genetics, Hebei General Hospital, Shijiazhuang, Hebei, China.",
40631743,Decoding the transcriptome from bulk RNA of infection-naïve versus imprinted patients with SARS-CoV-2 Omicron B.1.1.529.,2025,Sonnleitner; Walder,"Dr. Gernot Walder GmbH, Austria.",info@walderlab.at
...
