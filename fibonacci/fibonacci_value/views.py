from django.shortcuts import render
from datetime import datetime


def fibonacci(request):
    start_time = datetime.now()
    n = int(request.POST['number'])
    prev_fib = 0
    cur_fib = 1

    for i in range(1, n):
        prev_fib, cur_fib = cur_fib, cur_fib + prev_fib

    end_time = datetime.now()
    diff = end_time - start_time

    return render(request, 'fibonacci.html', {'result': cur_fib, 'time_taken': diff.microseconds})


def home(request):
    return render(request, 'fibonacci.html', {})