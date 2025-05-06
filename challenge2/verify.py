import hashlib

EXPECTED_HASH = "e0a427aef0300b87ccd26d73e29c426f6c04c298f952e05d735b2461ecd83208"

def check_flag(user_input):
    h = hashlib.sha256(user_input.encode()).hexdigest()
    return h == EXPECTED_HASH

if __name__ == "__main__":
    flag = input("Enter the flag: ").strip()
    if check_flag(flag):
        print("Correct! 🎉")
    else:
        print("Incorrect. Try again.")

