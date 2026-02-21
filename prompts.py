def generate_code(language, task, level):
    return f"""
You are an expert {language} programmer.

Write a COMPLETE and EXECUTABLE {language} program.

Difficulty level: {level}

RULES:
- Do not stop midway
- Include all methods fully
- Include closing braces
- Code must compile and run
- Output ONLY code, no explanation

Task:
{task}
"""


def explain_code(code):
    return f"""
You are a programming tutor.

Explain the following code step by step in clear and simple language.

Code:
{code}
"""


def explain_code_simple(code):
    return f"""
Explain the following code as if teaching a beginner with no programming background.
Use very simple words and examples.

Code:
{code}
"""


def debug_code(code, error):
    return f"""
You are a debugging expert.

The following code has an error.

Code:
{code}

Error:
{error}

Tasks:
- Identify the mistake
- Provide corrected code
- Explain what was wrong
"""


def explain_concept(concept):
    return f"""
Explain the following programming concept clearly with examples.

Concept:
{concept}
"""