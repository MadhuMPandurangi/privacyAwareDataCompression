import base64
import tenseal as ts

#special object that holds different encryption keys and parameters
private_context = ts.context(ts.SCHEME_TYPE.BFV, poly_modulus_degree=4096, plain_modulus=1032193)


public_context = ts.context(ts.SCHEME_TYPE.BFV, poly_modulus_degree=4096, plain_modulus=1032193) 
# the context will drop the secret-key at this point
public_context.make_context_public()

lst = [60, 66, 73, 81, 90]
enc_lst = ts.bfv_vector(private_context, lst)

add_lst = enc_lst + [1, 1, 1, 1, 1]

print(add_lst.decrypt())