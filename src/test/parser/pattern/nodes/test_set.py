from test.parser.pattern.nodes.base import PatternTestBaseClass
from programy.parser.pattern.nodes.set import PatternSetNode
from programy.dialog import Sentence

class PatternSetNodeTests(PatternTestBaseClass):

    def test_init(self):
        self.bot.brain.sets.add_set("TEST1", {"VALUE1": [["VALUE1"]], "VALUE2": [["VALUE2"]], "VALUE3": [["VALUE3"]]})

        node = PatternSetNode("test1")
        self.assertIsNotNone(node)

        self.assertFalse(node.is_root())
        self.assertFalse(node.is_priority())
        self.assertFalse(node.is_wildcard())
        self.assertFalse(node.is_zero_or_more())
        self.assertFalse(node.is_one_or_more())
        self.assertTrue(node.is_set())
        self.assertFalse(node.is_bot())
        self.assertFalse(node.is_template())
        self.assertFalse(node.is_that())
        self.assertFalse(node.is_topic())
        self.assertFalse(node.is_wildcard())

        self.assertIsNotNone(node.children)
        self.assertFalse(node.has_children())

        sentence = Sentence("VALUE1 VALUE2 VALUE3 VALUE4")

        self.assertTrue(node.equivalent(PatternSetNode("TEST1")))
        result = node.equals(self.bot, "testid", sentence, 0)
        self.assertTrue(result.matched)
        result = node.equals(self.bot, "testid", sentence, 1)
        self.assertTrue(result.matched)
        result = node.equals(self.bot, "testid", sentence, 2)
        self.assertTrue(result.matched)
        result = node.equals(self.bot, "testid", sentence, 3)
        self.assertFalse(result.matched)
        self.assertEqual(node.to_string(), "SET [P(0)^(0)#(0)C(0)_(0)*(0)To(0)Th(0)Te(0)] name=[TEST1]")

    def test_number(self):
        node = PatternSetNode("NUMBER")
        self.assertIsNotNone(node)

        sentence = Sentence("12 XY")

        result = node.equals(self.bot, "testid", sentence, 0)
        self.assertTrue(result.matched)
        result = node.equals(self.bot, "testid", sentence, 1)
        self.assertFalse(result.matched)

