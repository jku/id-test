import id
import jwt 


token = id.detect_credential("sigstore")
assert token

header, payload, sig = id.decode_oidc_token(token)
print("HEADER", header)
print("PAYLOAD", payload)
print("SIG", sig)
print("---")
claims = jwt.decode(
  token,
  options={
    "verify_signature": False,
    "verify_aud": True,
    "verify_iat": True,
    "verify_exp": True,
    "require": ["aud", "sub", "iat", "exp", "iss"],
  },
  audience="sigstore",
  leeway=5,
)
print(claims)
