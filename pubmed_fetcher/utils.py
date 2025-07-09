# pubmed_fetcher/utils.py

from typing import List, Dict, Optional
import requests
import csv
import xml.etree.ElementTree as ET
import re

def fetch_pubmed_articles(query: str, debug: bool = False) -> List[Dict]:
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": "20",
        "retmode": "json"
    }
    res = requests.get(base_url, params=params)
    res.raise_for_status()
    ids = res.json()["esearchresult"].get("idlist", [])
    
    if debug:
        print(f"[DEBUG] Retrieved PubMed IDs: {ids}")

    articles = []
    for pmid in ids:
        fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
        fetch_params = {
            "db": "pubmed",
            "id": pmid,
            "retmode": "xml"
        }
        fetch_res = requests.get(fetch_url, params=fetch_params)
        fetch_res.raise_for_status()
        root = ET.fromstring(fetch_res.text)
        articles.append(root)

    return articles

def is_non_academic_affiliation(affiliation: str) -> bool:
    academic_keywords = ["university", "institute", "college", "school", "faculty", "dept"]
    return not any(word in affiliation.lower() for word in academic_keywords)

def extract_relevant_info(article: ET.Element) -> Optional[Dict]:
    try:
        article_data = article.find(".//PubmedArticle")
        pmid = article_data.findtext(".//PMID")
        title = article_data.findtext(".//ArticleTitle")
        pub_date = article_data.findtext(".//PubDate/Year") or "N/A"

        authors_info = []
        non_academic_authors = []
        companies = []
        email = ""

        for author in article_data.findall(".//Author"):
            name = author.findtext("LastName") or "Unknown"
            affiliation_info = author.findtext("AffiliationInfo/Affiliation") or ""

            if is_non_academic_affiliation(affiliation_info):
                non_academic_authors.append(name)
                companies.append(affiliation_info)

            if not email:
                email_match = re.search(r"[\w\.-]+@[\w\.-]+", affiliation_info)
                if email_match:
                    email = email_match.group(0)

        if not non_academic_authors:
            return None

        return {
            "PubmedID": pmid,
            "Title": title,
            "Publication Date": pub_date,
            "Non-academic Author(s)": "; ".join(non_academic_authors),
            "Company Affiliation(s)": "; ".join(companies),
            "Corresponding Author Email": email
        }
    except Exception as e:
        return None

def save_to_csv(data: List[Dict], filename: str) -> None:
    if not data:
        raise ValueError("No data to save.")

    with open(filename, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
