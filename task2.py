import os
import sys
import subprocess

try:
    import rdflib
except ImportError:
    print("Бібліотеку rdflib не знайдено. Встановлюємо в системний Python...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rdflib"])
    import rdflib

def verify_ontology():
    g = rdflib.Graph()
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    file_path = os.path.join(current_dir, "onto.owl")
    if not os.path.exists(file_path):
        file_path = os.path.join(current_dir, "models", "onto.owl")
    
    if not os.path.exists(file_path):
        print(f"Помилка: файл 'onto.owl' не знайдено ні в поточній папці, ні в 'models/onto.owl'!")
        return

    try:
        g.parse(file_path, format="turtle")
        print(f"Успіх! Файл '{os.path.basename(file_path)}' розпарсено без синтаксичних помилок.")
        print(f"Загальна кількість синтаксичних триплетів в онтології: {len(g)}")
    except Exception as e:
        print(f"Помилка парсингу файлу: {e}")

if __name__ == "__main__":
    verify_ontology()