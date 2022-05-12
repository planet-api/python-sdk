import tests.type_transformation.test_athena as type_transformation_athena
import tests.type_transformation.test_pandas as type_transformation_pandas
import tests.type_transformation.test_big_query as type_transformation_big_query


all_modules = [
    type_transformation_athena,
    type_transformation_pandas,
    type_transformation_big_query
]


def run_all_tests():
    """
    Run all the test functions in all the testing modules
    """

    # Loop over each testing module
    for module in all_modules:
        for attributes in dir(module):

            # Check that the attributes start by 't'
            # Filter only test functions
            if attributes.startswith('t'):

                # Execute the test functions
                item = getattr(module, attributes)
                if callable(item):
                    item()


if __name__ == '__main__':
    run_all_tests()
