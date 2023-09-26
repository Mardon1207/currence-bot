import currencyapicom
API_KEY="cur_live_9SV4BxZHyszCHWGgrvRgk8Z8VNSBXtfXcJiPPiAi"

client = currencyapicom.Client(API_KEY)


def converter(c: str, cs: list):
    result = client.latest(c, currencies=cs)
    
    return result