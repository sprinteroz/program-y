from test.parser.pattern.base import PatternTestBaseClass

from programy.parser.pattern.nodes.word import PatternWordNode
from programy.dialog import Sentence

class PatternWordNodeTests(PatternTestBaseClass):

    def test_init(self):
        node = PatternWordNode("test1")

        self.assertFalse(node.is_root())
        self.assertFalse(node.is_priority())
        self.assertFalse(node.is_wildcard())
        self.assertFalse(node.is_zero_or_more())
        self.assertFalse(node.is_one_or_more())
        self.assertFalse(node.is_set())
        self.assertFalse(node.is_bot())
        self.assertFalse(node.is_template())
        self.assertFalse(node.is_that())
        self.assertFalse(node.is_topic())
        self.assertFalse(node.is_wildcard())

        self.assertIsNotNone(node.children)
        self.assertFalse(node.has_children())

        sentence = Sentence("test1 test")

        self.assertTrue(node.equivalent(PatternWordNode("test1")))
        result = node.equals(self.bot, "testid", sentence, 0)
        self.assertTrue(result.matched)
        result = node.equals(self.bot, "testid", sentence, 1)
        self.assertFalse(result.matched)
        self.assertEqual(node.to_string(), "WORD [P(0)^(0)#(0)C(0)_(0)*(0)To(0)Th(0)Te(0)] word=[test1]")

        node.add_child(PatternWordNode("test2"))
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.to_string(), "WORD [P(0)^(0)#(0)C(1)_(0)*(0)To(0)Th(0)Te(0)] word=[test1]")
