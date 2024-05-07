#!/usr/bin/env python3
"""Insert all documents"""
import pymongo


def insert_all(collection, **kwargs):
	"""Insert doc function"""
	if len(kwargs) == 0:
		return None
	return collection.insert(kwargs)
