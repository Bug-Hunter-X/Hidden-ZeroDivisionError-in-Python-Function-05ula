# Hidden ZeroDivisionError in Python

This example demonstrates a `ZeroDivisionError` that's less immediately obvious than a simple `1/0`. The error is hidden within conditional logic, making it harder to spot during initial code review.

The `function_with_uncommon_error` appears functional, but under specific conditions, it throws a `ZeroDivisionError`.  The challenge is identifying and fixing the condition. The solution file provides a corrected implementation.