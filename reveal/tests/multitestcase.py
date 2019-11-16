from django.test import TestCase


class MultiTestCase(TestCase):
    def _test(self, test_function, tests):
        """Test a function using given tests.
        Tests consist of function arguments and expected results.
        Tuple of arguments will be passed as multiple args.
        """
        for test in tests:
            test_func_args, expected_result = test
            if isinstance(test_func_args, str):
                result = test_function(test_func_args)
            else:
                try:
                    result = test_function(*test_func_args)
                except ValueError:
                    result = 'ValueError'
            if result == 'SKIP':
                break
            returned_result = str(result)
            expected_result = str(expected_result)
            if returned_result != expected_result:
                print('RETURNED:', returned_result)
                print('EXPECTED:', expected_result)
            self.assertEqual(returned_result, expected_result, test_func_args)
