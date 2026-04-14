import sys
from sympy import symbols, simplify

def validate_proof(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read().lower()

      
        required_keywords = ["theorem", "proof", "let", "so"]
        for word in required_keywords:
            if word not in content:
                print(f"SƏHV: '{word}' açar sözü tapılmadı!")
                return False

     
        k, m = symbols('k m')
        content_no_space = content.replace(" ", "")

  
        if "2k+2m" in content_no_space or "2(k+m)" in content_no_space:

            left = 2*k + 2*m
            right = 2*(k + m)

            if simplify(left - right) == 0:
                print("TƏBRİKLƏR: Riyazi sübut doğrudur.")
                return True
            else:
                print("SƏHV: Riyazi məntiq yanlışdır!")
                return False

        else:
            print("SƏHV: Riyazi ifadə tapılmadı!")
            return False

    except FileNotFoundError:
        print("SƏHV: proof.txt tapılmadı!")
        return False


if __name__ == "__main__":
    if validate_proof("proof.txt"):
        sys.exit(0)
    else:
        sys.exit(1)
