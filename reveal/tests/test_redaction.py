import re
from reveal.templatetags.reveal_tags import EMAIL_RE, PHONE_RE, URL_RE
from reveal.tests.multitestcase import MultiTestCase


class RedactionTestCase(MultiTestCase):
    def check_re(self, val, regex):
        s = re.sub(regex, '', val)
        if s == '':
            return True
        return False

    def test_email_re(self):
        tests = (
            ('TEST@mail.COM', True),
            ('test@mail.com', True),
            ('test at mail dot com', True),
            ('test [at] mail.com', True),
            ('test[at]mail dot com', True),
            ('test [at] mail [dot] com', True),

            ('testATmail.com', False),  # satisfy case rottentomAToes.com
            ('stayed at home anecdotally', False),
            ('finish at 5 to the dot and go', False),
        )
        check_email_re = lambda x: self.check_re(x, EMAIL_RE)
        self._test(check_email_re, tests)

    def test_phone_re(self):
        tests = (
            ('+44.7902162632', True),
            ('+44 7902 162632', True),
            ('+44.7902.162.632', True),
            ('044 7902 162 632', True),
            ('044/7902 162 632', True),
            ('044-7902-162-632', True),
            ('+44 (0) 7902-162-632', True),
            ('0044 7902 162 632', True),
            ('0 7 9 0 2 1 6 2 6 3 2', True),
            ('07902162632', True),
            ('0044 436 435 21 32', True),
            ('O790III2632', True),

            ('2014', False),
            ('22/01/2014', False),
            ('22-01-2014', False),
            ('1-1-2014', False),
            ('£1000', False),
            ('23, 60, 80, 90D', False),
            ('£445, £465 & £490', False),
            ('3 min drive to m25 a2 and m20', False),
        )
        check_phone_re = lambda x: self.check_re(x, PHONE_RE)
        self._test(check_phone_re, tests)

    def test_url_re(self):
        tests = (
            ('twitter.com/handle', True),
            ('facebook.com/handle', True),
            ('zoopla.co.uk', True),
            ('http://rightmove.co.uk/test.html', True),

            ('Lorem ipsum.dolor/sit amet', False),
            ('Another. Compulsory test / finished.', False),
        )
        check_url_re = lambda x: self.check_re(x, URL_RE)
        self._test(check_url_re, tests)
