#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import logging
import os
import sys
from pathlib import Path
from sasci360solworkflow.base import Base


current_file = __file__
real_path = os.path.realpath(current_file)
dir_path = os.path.dirname(real_path)
src_path = os.path.abspath(os.path.join(dir_path, os.pardir))
root_path = os.path.abspath(os.path.join(src_path, os.pardir))
pkg_path = os.path.abspath(os.path.join(root_path, os.pardir))
sys.path.append(dir_path)


class Workflow(Base):
	"""
	Planning Module
	"""

	def __init__(self) -> None:
		super().__init__()

		self._log_file = Path("{0}{1}{2}".format(pkg_path, "/logs/", "root.log"))
		self.logger = logging.getLogger(__name__)
		self.logger.setLevel(logging.INFO)
		handler = logging.FileHandler(self._log_file)
		handler.setLevel(logging.INFO)
		self.logger.addHandler(handler)

		result = self.root.get_root()

		# algorithm = self.algorithm
		# print("Planning-Result: {}".format(algorithm))

		# self.call_get_root()
		print("Result B: {0}".format(result.status_code))
		print("Result B: {0}".format(result.json()))

	# def call_get_root(self) -> requests.Response:
	# 	"""
	# 	Get the links for the API
	# 	:return: Returns the links to the top-level resources for the API.
	# 	:rtype: requests.Response
	# 	"""
	# 	result = None
	# 	try:
	# 		result = self.root.get_root()
	# 		# print("Result A: {0}".format(result.status_code))
	# 	except (AttributeError, Exception) as e:
	# 		self.logger.exception("Exception occurred: {}".format(str(e)))
	# 	finally:
	# 		return result


if __name__ == "__main__":
	Planning()
