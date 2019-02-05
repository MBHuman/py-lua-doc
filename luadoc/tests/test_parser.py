import os
import unittest
from luadoc.parser import DocParser
from luadoc.printers import to_pretty_json


class ParserTestCase(unittest.TestCase):
    CURRENT_DIR: str = os.path.dirname(__file__)
    SOURCE_ROOT: str = os.path.join(CURRENT_DIR, "source")
    LUA_EXT: str = ".lua"
    JSON_EXT: str = ".json"

    def make_test_from_sources(self, test_name: str):
        lua_file = open(os.path.join(ParserTestCase.SOURCE_ROOT, test_name + ParserTestCase.LUA_EXT), 'r')
        tree_file = open(os.path.join(ParserTestCase.SOURCE_ROOT, test_name + ParserTestCase.JSON_EXT), 'r')

        lua_source = lua_file.read()
        exp_doc_tree = tree_file.read()

        module = DocParser().build_module_doc_model(lua_source)
        json_doc_tree = to_pretty_json(module)

        lua_file.close()
        tree_file.close()

        self.assertEqual(exp_doc_tree, json_doc_tree)

    def test_class(self):
        self.make_test_from_sources("class")

    def test_class_module(self):
        self.make_test_from_sources("class_module")

    def test_class_inheritance(self):
        self.make_test_from_sources("class_inheritance")

    def test_emmy_lua_params(self):
        self.make_test_from_sources("emmy_lua_params")

    def test_luadoc_tparam(self):
        self.make_test_from_sources("luadoc_tparam")
