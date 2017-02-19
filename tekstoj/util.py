import base64
import hmac
import time
from hashlib import sha1

from urllib.parse import urlencode
from six import iteritems, PY3


class RequestValidator(object):

    def __init__(self, token):
        self.token = token.encode("utf-8")

    def compute_signature(self, uri, params, utf=PY3):
        """Compute the signature for a given request

        :param uri: full URI that Twilio requested on your server
        :param params: post vars that Twilio sent with the request
        :param utf: whether return should be bytestring or unicode (python3)

        :returns: The computed signature
        """
        s = uri
        if len(params) > 0:
            for k, v in sorted(params.items()):
                s += k + v

        # compute signature and compare signatures
        mac = hmac.new(self.token, s.encode("utf-8"), sha1)
        computed = base64.b64encode(mac.digest())
        if utf:
            computed = computed.decode('utf-8')

        return computed.strip()

    def validate(self, uri, params, signature):
        """Validate a request from Twilio

        :param uri: full URI that Twilio requested on your server
        :param params: post vars that Twilio sent with the request
        :param signature: expected signature in HTTP X-Twilio-Signature header

        :returns: True if the request passes validation, False if not
        """
        return secure_compare(self.compute_signature(uri, params), signature)


def secure_compare(string1, string2):
    if len(string1) != len(string2):
        return False
    result = True
    for c1, c2 in zip(string1, string2):
        result &= c1 == c2
    return result

