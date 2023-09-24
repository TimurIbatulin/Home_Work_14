import pytest
from For_test import file_info

def test_for_test():
    assert file_info('/Users/timuribatulin/Downloads/images.png'), 'Не прошел'


if __name__ =='__main__':
    pytest.main()
