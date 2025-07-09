from pubmed_fetcher.utils import fetch_pubmed_articles, extract_relevant_info, save_to_csv
from typing import Optional
import argparse

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with non-academic authors.")
    parser.add_argument("query", type=str, help="PubMed search query.")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode.")
    parser.add_argument("-f", "--file", type=str, help="CSV output filename. If not provided, prints to console.")
    args = parser.parse_args()

    if args.debug:
        print(f"[DEBUG] Query: {args.query}")

    try:
        articles = fetch_pubmed_articles(args.query, debug=args.debug)
        if args.debug:
            print(f"[DEBUG] Fetched {len(articles)} articles.")

        filtered_results = [extract_relevant_info(article) for article in articles]
        filtered_results = [res for res in filtered_results if res]

        if args.file:
            save_to_csv(filtered_results, args.file)
            print(f"Results saved to {args.file}")
        else:
            for res in filtered_results:
                print(res)
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    main()
