# Python imports
import unittest
import configparser

# Local imports
from src import configreader
from src.errors import ConfigError


class ConfigReaderTestCase(unittest.TestCase):
    """
    These tests use the "test_config.ini" file as input to the
    configreader.ConfigReader() class methods and tests whether the return
    values are the same as in the mock configuration file
    """

    def setUp(self):
        self.Config = configparser.ConfigParser()
        self.Config.read("tests/test_config.ini")
        self.reader = configreader.ConfigReader("")

    def test_read_backup(self):
        purge, retries, backup_loc, directories = self.reader._read_backup(self.Config)
        self.assertEqual(purge, '1')
        self.assertEqual(retries, '10')
        self.assertEqual(backup_loc, "D:/")
        self.assertEqual(directories, ["C:/Sample_Dir1", "C:/Sample_Dir2"])

    def test_read_browse(self):
        urls = self.reader._read_browse(self.Config)
        self.assertEqual(urls, ["www.sampleweb1.com", "www.sampleweb2.com"])

    def test_read_manage(self):
        with self.assertRaises(ConfigError):
            self.reader._read_manage(self.Config)

    def test_read_music(self):
        result = self.reader._read_music(self.Config)
        self.assertEqual(result, [])

    def test_read_start(self):
        result = self.reader._read_start(self.Config)
        self.assertEqual(result, ["C:/Sample_Dir1/Sample_Prog1.exe"])

    def test_read_wallpaper(self):
        result = self.reader._read_wallpaper(self.Config)
        self.assertEqual(result, [])

    def test_read_word(self):
        files, editor = self.reader._read_work(self.Config)
        self.assertEqual(files, ["C:/Sample_Dir1"])
        self.assertEqual(editor, "C:/Sample_Editor1.exe")

if __name__ == '__main__':
    unittest.main()