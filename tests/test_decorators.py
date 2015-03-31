import unittest
from mock import Mock
from valipede import *
from valipede.decorators import validate


class TestDecorators(unittest.TestCase):
	
	def test_validate(self):
		foo = Mock(return_value=23)
		foo.__name__ = 'foo'
		wrapped_foo = validate(Schema(things=Text(), stuff=Integer(default=5)))(foo)
		
		result = wrapped_foo(things="Hi there")
		
		self.assertEquals(result, 23)
		foo.assert_called_once_with({'things':'Hi there', 'stuff':5})
		