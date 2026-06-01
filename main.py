import re

class DocGenerator:
    """
    Inline Code Docstring Parser
    Introspects Python classes and extracts docstrings into Markdown files.
    """
    def parse_class_docs(self, python_code):
        docstrings = re.findall(r'"""(.*?)"""', python_code, re.DOTALL)
        return [doc.strip() for doc in docstrings]

if __name__ == "__main__":
    gen = DocGenerator()
    code = """
class A:
    """This is sample documentation for Class A"""
    pass
"""
    print("Parsed Docstrings:")
    print(gen.parse_class_docs(code))
