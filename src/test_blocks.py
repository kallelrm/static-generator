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
if __name__ == '__main__':
    unittest.main()
