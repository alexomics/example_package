#!/usr/bin/env python

"""Tests for `example_package` package."""

import pytest


from example_package import example_package


def test_content():
    assert example_package.prime(5)
    assert not example_package.prime(10)
