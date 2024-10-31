from django.shortcuts import render
import time

def karatsuba_algorithm(x, y, steps):
    """Performs Karatsuba multiplication and appends each calculation step to 'steps' list."""
    # Base case for recursion
    if x < 10 or y < 10:
        steps.append({'type': 'base', 'text': f"Base multiplication: {x} * {y} = {x * y}"})
        return x * y

    # Calculate the size of the numbers
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Split the digit sequences in the middle
    high1, low1 = divmod(x, 10**m)
    high2, low2 = divmod(y, 10**m)

    steps.append({'type': 'split', 'text': f"Split numbers: x = {x} as ({high1}, {low1}), y = {y} as ({high2}, {low2})"})

    # Recursively calculate three products
    z0 = karatsuba_algorithm(low1, low2, steps)
    z1 = karatsuba_algorithm((low1 + high1), (low2 + high2), steps)
    z2 = karatsuba_algorithm(high1, high2, steps)

    # Combine the results
    result = (z2 * 10**(2 * m)) + ((z1 - z2 - z0) * 10**m) + z0
    steps.append({'type': 'combine', 'text': f"Combine results: ({z2} * 10^{2 * m}) + (({z1} - {z2} - {z0}) * 10^{m}) + {z0} = {result}"})

    return result


def visualize_karatsuba(request):
    if request.method == 'POST':
        # Get numbers from the form
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2') or 0

        # Check if numbers are provided, else show an error
        if not num1 or (not num2 and 'square' not in request.POST):
            error_message = "Please enter values for both numbers, or select 'Square' to calculate the square."
            return render(request, 'karatsuba.html', {'error_message': error_message})

        # Convert inputs to integers
        num1 = int(num1)
        if num2:
            num2 = int(num2)
        else:
            num2 = num1  # Calculate the square if 'square' option is selected

        # Initialize steps list to track each step in the calculation
        steps = []
        result = karatsuba_algorithm(num1, num2, steps)

        # Render the result page with the steps for visualization
        return render(request, 'karatsuba_result.html', {
            'steps': steps,
            'result': result
        })

    # Render the initial form page if it's a GET request
    return render(request, 'karatsuba.html')
