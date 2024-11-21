import os
import unittest
from mmget.outputpathmetadata import OutputPathMetadata


class TestOutputPathValidator(unittest.TestCase):
    def test_default_path(self):
        metadata = OutputPathMetadata(None)
        self.assertEqual(metadata.absolute_path, os.path.abspath(os.getcwd()))
        self.assertTrue(metadata.is_valid)

    def test_valid_dist_type(self):
        metadata = OutputPathMetadata(".", dest_type="a1111")
        self.assertTrue(metadata.is_valid)
        self.assertEqual(metadata.dest_type, "a1111")

    def test_invalid_dist_type(self):
        metadata = OutputPathMetadata(".", dest_type="invalid")
        self.assertFalse(metadata.is_valid)

    def test_directory_check(self):
        metadata = OutputPathMetadata(".")
        self.assertTrue(metadata.is_directory)
        self.assertTrue(metadata.is_exists)

    def test_nonexistent_path(self):
        metadata = OutputPathMetadata("nonexistent_path")
        self.assertFalse(metadata.is_exists)
        self.assertFalse(metadata.is_directory)

    def test_dist_type_set_but_output_is_not_existed(self):
        metadata = OutputPathMetadata("file-not-existed", dest_type="a1111")
        self.assertFalse(metadata.is_exists)
        self.assertFalse(metadata.is_valid)

    def test_comfyui_prefix(self):
        metadata = OutputPathMetadata("comfyui:.")
        self.assertTrue(metadata.is_exists)
        self.assertTrue(metadata.is_valid)
        self.assertEqual(metadata.dest_type, "comfyui")

    def test_a1111_prefix(self):
        metadata = OutputPathMetadata("a1111:.")
        self.assertTrue(metadata.is_exists)
        self.assertTrue(metadata.is_valid)
        self.assertEqual(metadata.dest_type, "a1111")
