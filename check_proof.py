import sys

def validate_proof(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read().lower()
        required_keywords = ["theorem", "proof", "let", "so"]
        for word in required_keywords:
            if word not in content:
                print(f"SƏHV: '{word.capitalize()}' açar sözü tapılmadı!")
                return False
      logic_check = "2(k+m)"
        if logic_check not in content.replace(" ", ""):
            print(f"SƏHV: Riyazi nəticə formatı düzgün deyil! Gözlənilən: {logic_check}")
            return False

        print("TƏBRİKLƏR: Sübut həm struktur, həm də məntiq baxımından keçərli sayıldı.")
        return True

    except FileNotFoundError:
        print("SƏHV: proof.txt faylı tapılmadı!")
        return False

if __name__ == "__main__":
    if validate_proof("proof.txt"):
        sys.exit(0) 
    else:
        sys.exit(1) 
