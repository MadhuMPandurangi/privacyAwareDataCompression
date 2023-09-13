import base64
import tenseal as ts

def write_data(file_name: str, data: bytes):
    data = base64.b64encode(data)
    with open(file_name, 'wb') as f: 
        f.write(data)
  
def read_data(file_name: str) -> bytes:
    with open(file_name, "rb") as f:
        data = f.read()
    return base64.b64decode(data)

context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree = 8192, coeff_mod_bit_sizes = [60, 40, 40, 60])
context.generate_galois_keys()
context.global_scale = 2**40

secret_context = context.serialize(save_secret_key = True)
write_data("secret.txt", secret_context)
  
context.make_context_public()
public_context = context.serialize()
write_data("public.txt", public_context)

