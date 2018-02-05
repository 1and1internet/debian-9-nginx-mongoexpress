#!/usr/bin/env python3

import unittest
import os
import docker
from selenium import webdriver
from testpack_helper_library.unittests.dockertests import Test1and1Common


class Test1and1MongoImage(Test1and1Common):

    # <tests to run>

    def test_docker_logs(self):
        expected_log_lines = [
            "run-parts: executing /hooks/entrypoint-pre.d",
        ]
        container_logs = self.container.logs().decode('utf-8')
        for expected_log_line in expected_log_lines:
            self.assertTrue(
                container_logs.find(expected_log_line) > -1,
                msg="Docker log line missing: %s from (%s)" % (expected_log_line, container_logs)
            )

    def test_mongo_express_package(self):
        op = self.execRun("npm ls -g --depth=0 mongo-express")
        self.assertTrue(
            op.find("mongo-express") > -1,
            msg="mongo-express not installed"
        )

    # </tests to run>

if __name__ == '__main__':
    unittest.main(verbosity=1)
