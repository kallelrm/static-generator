import unittest
import textwrap
from blocks import *

class TestBlock(unittest.TestCase):
    def test_markdown_to_blocks(self):
            md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
           )
    
    def test_block_to_blocktype_code(self):
        md = """```
        code
        code
        code
        ```"""
        blocktype = block_to_blocktype(md)
        self.assertEqual(BlockType.CODE, blocktype)

    def test_block_to_blocktype_heading1(self):
        md = textwrap.dedent("""
        # a
        """).strip()
        blocktype = block_to_blocktype(md)
        self.assertEqual(BlockType.HEADING, blocktype)
    
    def test_block_to_blocktype_heading2(self):
        md = textwrap.dedent("""
        ## a
        """).strip()
        blocktype = block_to_blocktype(md)
        self.assertEqual(BlockType.HEADING, blocktype)

    def test_block_to_blocktype_heading3(self):
        md = textwrap.dedent("""
        ### a
        """).strip()
        blocktype = block_to_blocktype(md)
        self.assertEqual(BlockType.HEADING, blocktype)

    def test_block_to_blocktype_heading4(self):
        md = textwrap.dedent("""
        #### a
        """).strip()
        blocktype = block_to_blocktype(md)
        self.assertEqual(BlockType.HEADING, blocktype)

    def test_block_to_blocktype_heading5(self):
        md = textwrap.dedent("""
        ##### a
        """).strip()
        blocktype = block_to_blocktype(md)
        self.assertEqual(BlockType.HEADING, blocktype)

    def test_block_to_blocktype_heading6(self):
        md = textwrap.dedent("""
        ###### a
        """).strip()
        blocktype = block_to_blocktype(md)
        self.assertEqual(BlockType.HEADING, blocktype)

    def test_block_to_blocktype_quote(self):
        md = textwrap.dedent("""
        > quote1
        > quote2
        > quote3
        """).strip()
        blocktype = block_to_blocktype(md)
        self.assertEqual(BlockType.QUOTE, blocktype)

    def test_block_to_blocktype_unordered(self):
        md = textwrap.dedent("""
        - lista
        - lista
        - lista 
        """).strip()
        blocktype = block_to_blocktype(md)
        self.assertEqual(BlockType.UNORDERED, blocktype)
    
    def test_block_to_blocktype_ordered(self):
        md = textwrap.dedent("""
        1. lista
        2. lista
        3. lista 
        """).strip()
        blocktype = block_to_blocktype(md)
        self.assertEqual(BlockType.ORDERED, blocktype)

    def test_block_to_blocktype_paragraph(self):
        md = textwrap.dedent("""
        um paragrafo qualquer sobre
        uma pessoa que eu amo muito
        e todo meu amor há de transbordar
        pelo mundo
        """).strip()

        blocktype = block_to_blocktype(md)
        self.assertEqual(BlockType.PARAGRAPH, blocktype)

    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here
    
    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_headers(self):
        # Different header levels
        header1 = "# This is a heading 1"
        header2 = "## This is a heading 2 with **bold** text"
        header3 = "### This is a heading 3 with _italic_ text"
        header6 = "###### This is a heading 6"

        # Edge cases you might want to consider
        not_a_header = "This is just a paragraph with # in the middle"
        also_not_header = "#No space after hash"

        node1 = markdown_to_html_node(header1)
        node2 = markdown_to_html_node(header2)
        node3 = markdown_to_html_node(header3)
        node6 = markdown_to_html_node(header6)
        node_not_header = markdown_to_html_node(also_not_header)

    def test_quotes(self):
        quotes1 = """
        > First Paragraph
        > Teste Teste
        > Teste
        >
        > Second Paragraph 
        > Teste TEste
        > Teste 2
        > 
        > Third paragraph
        > not alone
        """

        node = markdown_to_html_node(quotes1)
        self.assertEqual(
            node.to_html(),
            "<div><blockquote><p>First Paragraph Teste Teste Teste</p><p>Second Paragraph Teste TEste Teste 2</p><p>Third paragraph not alone</p></blockquote></div>"
        )

    def test_unordered(self):
        u_list = """
        - _a_
        - b
        - c
        - d
        """

        node = markdown_to_html_node(u_list)
        self.assertEqual(
            "<div><ul><li><i>a</i></li><li>b</li><li>c</li><li>d</li></ul></div>",
            node.to_html(),
        )

    def test_ordered(self):
        o_list = """
        1. item 1
        2. item 2
        3. item 3
        """

        node = markdown_to_html_node(o_list)
        self.assertEqual(
            "<div><ol><li>item 1</li><li>item 2</li><li>item 3</li></ol></div>",
            node.to_html()
        )

    def test_codeblock(self):
        md = textwrap.dedent("""
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """)

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff</code></pre></div>",
            html,
        )
        
if __name__ == '__main__':
    unittest.main()
