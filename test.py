import id
import jwt 


token = id.detect_credential()
assert token

print (token)

claims = jwt.decode(
  raw_token,
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
