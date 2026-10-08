import os
import json
from eml_parser import parse_eml
from ioc_extractor import extract_iocs

def main():
    # Directorios del laboratorio
    raw_emails_dir = "raw_emails/"
    artifacts_dir = "artifacts/"
    
    # Crea la carpeta de artefactos si no existe
    if not os.path.exists(artifacts_dir):
        os.makedirs(artifacts_dir)
        
    # Comprueba que la carpeta raw_emails exista
    if not os.path.exists(raw_emails_dir):
        print(f"[-] Error: La carpeta '{raw_emails_dir}' no existe. Créala y mete tus .eml ahí.")
        return
        
    # Busca todos los correos en la carpeta
    email_files = [f for f in os.listdir(raw_emails_dir) if f.endswith('.eml')]
    
    if not email_files:
        print(f"[-] No se encontraron archivos .eml en {raw_emails_dir}.")
        return
    
    print(f"[*] STARTING BULK TRIAGE: {len(email_files)} emails in queue...\n")
    
    # Diccionario maestro para guardar todo
    master_report = {}

    for file_name in email_files:
        file_path = os.path.join(raw_emails_dir, file_name)
        print(f">>> Processing: {file_name}")
        
        # 1. Parsear el correo
        email_data = parse_eml(file_path)
        
        if email_data:
            # Juntar todo el texto para analizarlo
            full_text = str(email_data["headers"]) + email_data["body"]
            
            # 2. Extraer los IoCs
            extracted_iocs = extract_iocs(full_text)
            
            # 3. Guardar los resultados
            master_report[file_name] = {
                "metadata": email_data["headers"],
                "attachments": email_data["attachments"],
                "iocs": extracted_iocs
            }
            
    # 4. Exportar el JSON final
    report_path = os.path.join(artifacts_dir, "triage_report.json")
    
    with open(report_path, "w", encoding="utf-8") as json_file:
        json.dump(master_report, json_file, indent=4, ensure_ascii=False)
        
    print(f"\n[+] TRIAGE COMPLETE! Report successfully saved to: {report_path}")

if __name__ == "__main__":
    main()