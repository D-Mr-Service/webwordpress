import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from src.app import setup_logger

logger = setup_logger()
language_codes = [
    'aa', 'ab', 'ae', 'af', 'ak', 'am', 'an', 'ar', 'as', 'av', 'ay', 'az',
    'ba', 'be', 'bg', 'bh', 'bi', 'bm', 'bn', 'bo', 'br', 'bs', 'ca', 'ce',
    'ch', 'co', 'cr', 'cs', 'cu', 'cv', 'cy', 'da', 'de', 'dv', 'dz', 'ee',
    'el', 'en', 'eo', 'es', 'et', 'eu', 'fa', 'ff', 'fi', 'fj', 'fo', 'fr',
    'fy', 'ga', 'gd', 'gl', 'gn', 'gu', 'gv', 'ha', 'he', 'hi', 'ho', 'hr',
    'ht', 'hu', 'hy', 'hz', 'ia', 'id', 'ie', 'ig', 'ii', 'ik', 'io', 'is',
    'it', 'iu', 'ja', 'jv', 'ka', 'kg', 'ki', 'kj', 'kk', 'kl', 'km', 'kn',
    'ko', 'kr', 'ks', 'ku', 'kv', 'kw', 'ky', 'la', 'lb', 'lg', 'li', 'ln',
    'lo', 'lt', 'lu', 'lv', 'mg', 'mh', 'mi', 'mk', 'ml', 'mn', 'mr', 'ms',
    'mt', 'my', 'na', 'nb', 'nd', 'ne', 'ng', 'nl', 'nn', 'no', 'nr', 'nv',
    'ny', 'oc', 'oj', 'om', 'or', 'os', 'pa', 'pi', 'pl', 'ps', 'pt', 'qu',
    'rm', 'rn', 'ro', 'ru', 'rw', 'sa', 'sc', 'sd', 'se', 'sg', 'si', 'sk',
    'sl', 'sm', 'sn', 'so', 'sq', 'sr', 'ss', 'st', 'su', 'sv', 'sw', 'ta',
    'te', 'tg', 'th', 'ti', 'tk', 'tl', 'tn', 'to', 'tr', 'ts', 'tt', 'tw',
    'ty', 'ug', 'uk', 'ur', 'uz', 've', 'vi', 'vo', 'wa', 'wo', 'xh', 'yi',
    'yo', 'za', 'zh', 'zu'
]

def check_hreflang(url):
    """检查HTML中的hreflang标签"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        hreflang_links = soup.find_all('link', {'rel': ['alternate', 'canonical'], 'hreflang': True})
        return {link['hreflang'].split('-')[0].lower() for link in hreflang_links if link['hreflang'].split('-')[0].lower() in language_codes}
    except:
        return set()

def check_links_for_lang_codes(url):
    """分析页面链接结构"""
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        base_domain = urlparse(response.url).hostname
        found_langs = set()

        # 检查所有链接
        for link in soup.find_all('a', href=True):
            href = urlparse(link['href'].lower())

            # 检查路径中的语言代码（如 /en/path）
            path_segments = [seg for seg in href.path.split('/') if seg]
            if path_segments and path_segments[0] in language_codes:
                found_langs.add(path_segments[0])

            # 检查子域名（如 en.example.com）
            if href.hostname and href.hostname != base_domain:
                subdomains = href.hostname.split('.')
                if subdomains[0] in language_codes:
                    found_langs.add(subdomains[0])

        return found_langs
    except:
        return set()

def quick_probe(url):
    """快速探测常见语言路径"""
    probes = {'/', '/en/', '/es/', '/fr/', '/de/', '/zh/', '/ja/'}  # 常见语言路径
    found = set()

    for path in probes:
        try:
            response = requests.head(urljoin(url, path), timeout=5, allow_redirects=True)
            if 200 <= response.status_code < 300:
                lang = urlparse(response.url).path.split('/')[1]
                if lang in language_codes:
                    found.add(lang)
                    if len(found) >= 2:  # 找到足够语言立即返回
                        return found
        except:
            continue
    return found

def check_multilingual(url):
    """优化版检查流程（满足条件立即返回）"""
    logger.info(f"\n🔍 开始检测多语言支持: {url}")

    # 第一层检查：hreflang标签
    if langs := check_hreflang(url):
        logger.info(f"✅ 通过hreflang发现语言: {langs}")
        if len(langs) >= 2:
            return langs

    # 第二层检查：页面链接分析
    if link_langs := check_links_for_lang_codes(url):
        logger.info(f"✅ 在页面链接中发现语言代码: {link_langs}")
        combined = langs.union(link_langs)
        if len(combined) >= 2:
            return combined
        langs = combined

    # 第三层检查：快速路径探测
    if probe_langs := quick_probe(url):
        logger.info(f"✅ 通过路径探测发现语言: {probe_langs}")
        combined = langs.union(probe_langs)
        if len(combined) >= 2:
            return combined

    # 最终结果
    final_langs = langs.union(probe_langs)
    logger.info("🌐 所有检测到的语言代码:" + (f" {final_langs}" if final_langs else " 无"))
    return final_langs

# 使用示例
def urlsweb(test_url):
    detected = check_multilingual(test_url)

    if len(detected) >= 2:

        result = ",".join(detected)
        logger.info(result)
        return result

