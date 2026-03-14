"""SHA-512 content hash computation per draft-ietf-vcon-vcon-container Section 2.4.2."""

import base64
import hashlib


def compute_content_hash(file_path: str) -> str:
    """Compute SHA-512 content hash of a file in spec-required format.

    Returns string in format: sha512-<base64url-encoded-digest>
    Per the vCon spec, external references use SHA-512 with base64url encoding.
    """
    with open(file_path, "rb") as f:
        digest = hashlib.sha512(f.read()).digest()
    b64url = base64.urlsafe_b64encode(digest).rstrip(b"=").decode("ascii")
    return f"sha512-{b64url}"
