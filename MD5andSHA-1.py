import hashlib


def hash_demo(message: str):
    data = message.encode("utf-8")

    md5 = hashlib.md5(data).hexdigest()
    sha1 = hashlib.sha1(data).hexdigest()
    sha256 = hashlib.sha256(data).hexdigest()

    print(f"Message : {message}")
    print(f"MD5    : {md5} ({len(md5) * 4} bits)")
    print(f"SHA-1  : {sha1} ({len(sha1) * 4} bits)")
    print(f"SHA-256: {sha256} ({len(sha256) * 4} bits)")


def verify_integrity(file_content: str):
    original_hash = hashlib.md5(file_content.encode()).hexdigest()

    print("\nFile integrity check:")
    print(f"Original MD5 : {original_hash}")

    tampered = file_content + " (modified)"
    tampered_hash = hashlib.md5(tampered.encode()).hexdigest()

    print(f"Tampered MD5 : {tampered_hash}")
    print(f"Integrity OK : {original_hash == tampered_hash}")


def avalanche_effect():
    print("\nAvalanche Effect (tiny change → huge hash change):")

    m1 = "Hello"
    m2 = "hello"

    print(f"SHA1('{m1}') = {hashlib.sha1(m1.encode()).hexdigest()}")
    print(f"SHA1('{m2}') = {hashlib.sha1(m2.encode()).hexdigest()}")


hash_demo("SCSVMV University")
verify_integrity("Sensitive Document Content")
avalanche_effect()
