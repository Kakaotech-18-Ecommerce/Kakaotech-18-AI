# search_engine/__init__.py

from .config import INDEX_DIR, DEFAULT_SEARCH_FIELDS
from .search_engine import search
from .utils import setup_logging, validate_query, format_results, print_results
