from django.shortcuts import render
from .solver import solve_n_queens_step_by_step

def n_queens_view(request):
    n = int(request.GET.get('n', 7))  # Default to 7 if no input is provided
    steps = []

    def capture_step(board_state):
        steps.append(board_state)

    solve_n_queens_step_by_step(n, capture_step)

    context = {
        'n': n,
        'steps': steps,
    }
    return render(request, 'n_queens.html', context)
