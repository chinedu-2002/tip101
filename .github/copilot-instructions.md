# Copilot Instructions for TIP101

## Project Overview
**TIP101 (Technical Interview Prep)** practice repository—Python coding exercises organized by week/topic. Each file contains multiple problems with docstrings explaining requirements and expected outputs.

## Structure & Naming
```
week_1_list/    # Lists: iteration, indexing, comprehensions
week_2_dict/    # Dictionaries: key-value mapping, frequency counting
week_3_str/     # Strings: slicing, reversals, pattern matching
```
**File naming**: `unit{week}_s{session}_problem{num}.py` (e.g., `unit2_s1_problem1.py` = Week 2, Session 1)

## Problem Format (Critical)
Every problem follows this exact structure—**preserve it when adding/editing**:
```python
"""
Problem N: Title
Description...

def function_name(params):
    pass
Example Input: ...
Example Output: ...
"""
# def function_name(params):
#     solution code
# print(function_name(test_input))
```

## Solution Conventions
1. **Keep solutions commented out** after testing (preserves learning exercise format)
2. **Include test call** (`print()`) immediately after each solution
3. **Use list comprehensions** for transformations—see [unit1_s2_problem1.py#L34](week_1_list/unit1_s2_problem1.py#L34): `[x * 2 for x in lst]`
4. **Use `dict.get(key, default)`** for safe access—see [unit2_s2_problem1.py#L81](week_2_dict/unit2_s2_problem1.py#L81): `mapping.get(val, 0) + 1`
5. **No external dependencies**—standard library only

## Windows Emoji Support
Week 1 files require this UTF-8 config at top (copy when creating new week_1 files):
```python
import sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    import io as _io
    sys.stdout = _io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
```

## Running Code
- Each file is standalone—run directly: `python week_1_list/unit1_s1_problem1.py`
- To test a solution: uncomment the solution block, run file, re-comment

## When Helping with Problems
1. **Explain approach first** (this is interview prep—understanding matters)
2. **State time/space complexity** (e.g., O(n) time, O(1) space)
3. **Match the commented-out style** exactly
4. **Suggest alternatives** when multiple valid approaches exist (e.g., iterative vs comprehension)
