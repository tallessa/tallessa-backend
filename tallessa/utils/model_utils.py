import re


SLUGIFY_CHAR_MAP = {
  ' ': '-',
  '.': '-',
  '_': '-',
  'à': 'a',
  'á': 'a',
  'ä': 'a',
  'å': 'a',
  'è': 'e',
  'é': 'e',
  'ö': 'o',
  'ü': '',
}
SLUGIFY_FORBANNAD_RE = re.compile(r'[^a-z0-9-]', re.UNICODE)
SLUGIFY_MULTIDASH_RE = re.compile(r'-+', re.UNICODE)


def slugify(ustr):
    ustr = ustr.lower()
    ustr = ''.join(SLUGIFY_CHAR_MAP.get(c, c) for c in ustr)
    ustr = SLUGIFY_FORBANNAD_RE.sub('', ustr)
    ustr = SLUGIFY_MULTIDASH_RE.sub('-', ustr)
    return ustr
