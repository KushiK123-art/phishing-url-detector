from urllib.parse import urlparse


def extract_features(url):
    parsed = urlparse(url)

    features = {
        'url_length': len(url),
        'has_https': 1 if parsed.scheme == 'https' else 0,
        'num_dots': url.count('.'),
        'num_hyphens': url.count('-'),
        'num_slashes': url.count('/'),
        'has_ip': 1 if any(char.isdigit() for char in parsed.netloc) else 0,
        'has_at_symbol': 1 if '@' in url else 0,
    }

    return list(features.values())