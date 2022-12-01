# __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from pkgutil import extend_path

__path__ = extend_path(__path__, __name__)
