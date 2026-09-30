"""AEAD seal and open, using OpenSSL's own libcrypto through ctypes."""
import ctypes
import ctypes.util

lib = ctypes.CDLL(ctypes.util.find_library("crypto"))
P, INT = ctypes.c_void_p, ctypes.c_int
lib.EVP_CIPHER_fetch.restype = P
lib.EVP_CIPHER_fetch.argtypes = [P, ctypes.c_char_p, ctypes.c_char_p]
lib.EVP_CIPHER_free.argtypes = [P]
lib.EVP_CIPHER_CTX_new.restype = P
lib.EVP_CIPHER_CTX_free.argtypes = [P]
lib.EVP_CipherInit_ex2.argtypes = [P, P, ctypes.c_char_p, ctypes.c_char_p,
                                   INT, P]
lib.EVP_CipherUpdate.argtypes = [P, P, ctypes.POINTER(INT),
                                 ctypes.c_char_p, INT]
lib.EVP_CipherFinal_ex.argtypes = [P, P, ctypes.POINTER(INT)]
lib.EVP_CIPHER_CTX_ctrl.argtypes = [P, INT, INT, P]
GET_TAG, SET_TAG = 0x10, 0x11  # EVP_CTRL_AEAD_GET_TAG / _SET_TAG


def _crypt(name, key, nonce, aad, data, encrypt, tag=None):
    if len(key) != 32 or len(nonce) != 12:
        raise ValueError("need a 32 byte key and a 12 byte nonce")
    cipher = lib.EVP_CIPHER_fetch(None, name.encode(), None)
    ctx = lib.EVP_CIPHER_CTX_new()
    try:
        if not lib.EVP_CipherInit_ex2(ctx, cipher, key, nonce, encrypt, None):
            raise ValueError(f"cannot initialise {name}")
        n = INT(0)
        lib.EVP_CipherUpdate(ctx, None, ctypes.byref(n), aad, len(aad))
        out = ctypes.create_string_buffer(len(data) + 16)
        lib.EVP_CipherUpdate(ctx, out, ctypes.byref(n), data, len(data))
        size = n.value
        tag_buf = ctypes.create_string_buffer(tag or bytes(16), 16)
        if not encrypt:
            lib.EVP_CIPHER_CTX_ctrl(ctx, SET_TAG, 16, tag_buf)
        if not lib.EVP_CipherFinal_ex(ctx, ctypes.byref(out, size),
                                      ctypes.byref(n)):
            raise ValueError("authentication failed, nothing released")
        if encrypt:
            lib.EVP_CIPHER_CTX_ctrl(ctx, GET_TAG, 16, tag_buf)
            return out.raw[:size], tag_buf.raw
        return out.raw[:size]
    finally:
        lib.EVP_CIPHER_CTX_free(ctx)
        lib.EVP_CIPHER_free(cipher)


def seal(name, key, nonce, aad, plaintext):
    """Encrypt and authenticate. Returns (ciphertext, 16 byte tag)."""
    return _crypt(name, key, nonce, aad, plaintext, 1)


def open_sealed(name, key, nonce, aad, ciphertext, tag):
    """Check the tag, then decrypt. Raises ValueError if anything changed."""
    return _crypt(name, key, nonce, aad, ciphertext, 0, tag)
