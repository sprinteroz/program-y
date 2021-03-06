import xml.etree.ElementTree as ET

from programy.parser.template.nodes.base import TemplateNode
from programy.parser.template.nodes.response import TemplateResponseNode
from programy.dialog import Question, Conversation

from test.parser.template.base import TemplateTestsBaseClass


class TemplateResponseNodeTests(TemplateTestsBaseClass):

    def test_to_str_defaults(self):
        node = TemplateResponseNode()
        self.assertEquals("RESPONSE", node.to_string())

    def test_to_str_no_defaults(self):
        node = TemplateResponseNode(index=2)
        self.assertEquals("RESPONSE index=2", node.to_string())

    def test_to_xml_defaults(self):
        root = TemplateNode()
        node = TemplateResponseNode()
        root.append(node)

        xml = root.xml_tree(self.bot, self.clientid)
        self.assertIsNotNone(xml)
        xml_str = ET.tostring(xml, "utf-8").decode("utf-8")
        self.assertEqual("<template><response /></template>", xml_str)

    def test_to_xml_no_defaults(self):
        root = TemplateNode()
        node = TemplateResponseNode(index=3)
        root.append(node)

        xml = root.xml_tree(self.bot, self.clientid)
        self.assertIsNotNone(xml)
        xml_str = ET.tostring(xml, "utf-8").decode("utf-8")
        self.assertEqual('<template><response index="3" /></template>', xml_str)

    def test_resolve_with_defaults(self):
        root = TemplateNode()
        self.assertIsNotNone(root)
        self.assertIsNotNone(root.children)
        self.assertEqual(len(root.children), 0)

        node = TemplateResponseNode()
        self.assertIsNotNone(node)
        self.assertEqual(1, node.index)

        root.append(node)
        self.assertEqual(len(root.children), 1)

        conversation = Conversation("testid", self.bot)

        question = Question.create_from_text("Hello1 question")
        question.current_sentence()._response = "Hello1 response"
        conversation.record_dialog(question)

        question = Question.create_from_text("Hello quesiton2")
        question.current_sentence()._response = "Hello2 response"
        conversation.record_dialog(question)

        self.bot._conversations["testid"] = conversation

        response = root.resolve(self.bot, "testid")
        self.assertIsNotNone(response)
        self.assertEqual(response, "Hello1 response")

    def test_resolve_with_no_defaults(self):
        root = TemplateNode()
        self.assertIsNotNone(root)
        self.assertIsNotNone(root.children)
        self.assertEqual(len(root.children), 0)

        node = TemplateResponseNode(index=1)
        self.assertIsNotNone(node)
        self.assertEqual(1, node.index)

        root.append(node)
        self.assertEqual(len(root.children), 1)

        conversation = Conversation("testid", self.bot)

        question = Question.create_from_text("Hello1 question")
        question.current_sentence()._response = "Hello1 response"
        conversation.record_dialog(question)

        question = Question.create_from_text("Hello quesiton2")
        question.current_sentence()._response = "Hello2 response"
        conversation.record_dialog(question)

        self.bot._conversations["testid"] = conversation

        response = root.resolve(self.bot, "testid")
        self.assertIsNotNone(response)
        self.assertEqual(response, "Hello1 response")

