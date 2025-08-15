import requests
import time

retry_urls = []

# Fonction pour lire les URLs depuis un fichier texte
def load_urls_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]

# Fonction pour filtrer les URLs contenant le mot "psion"
def filter_urls_by_keyword(url_list, keyword="psion"):
    valid_urls = []

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }

    for url in url_list:
        try:
            response = requests.get(url, headers=headers, timeout=30)
            if response.status_code == 200:
                content = response.text.lower()

                if "psion" in content or "epoc" in content:
                    valid_urls.append(url)
                    print("Psion Website : ", url)
                else:
                    print("Not Psion Website : ", url)
                time.sleep(15)
        except requests.RequestException as e:
            print(f"Erreur lors de la requête pour {url} : {e}")
            retry_urls.append(url)
            print(retry_urls)
            print("Attente 60 sec")
            time.sleep(60)
    return valid_urls

# Charger les URLs depuis le fichier
input_file = r"S:\Developpement\PsionTimeMachine\psion_url3.txt"
urls = load_urls_from_file(input_file)

# Filtrer les URLs
filtered_urls = filter_urls_by_keyword(urls)

# Sauvegarder les URLs filtrées dans un fichier
output_file = r"S:\Developpement\PsionTimeMachine\filtered_psion_url3.txt"
with open(output_file, "w", encoding="utf-8") as file:
    for url in filtered_urls:
        file.write(url + "\n")

output_file = r"S:\Developpement\PsionTimeMachine\retry_psion_url.txt"
with open(output_file, "w", encoding="utf-8") as file:
    for url in retry_urls:
        file.write(url + "\n")

print(f"{len(filtered_urls)} URL(s) contenant 'psion' ont été enregistrées dans '{output_file}'.")
