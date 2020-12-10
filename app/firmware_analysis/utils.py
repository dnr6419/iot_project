import hashlib

def Hash256(firmware):
  return hashlib.sha256(firmware.open('rb').read()).hexdigest()