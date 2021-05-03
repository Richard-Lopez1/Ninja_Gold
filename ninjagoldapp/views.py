from django.shortcuts import render, redirect
import random

MAP = {
    'form-1': [10,20],
    'form-2': [5,10],
    'form-3': [0,50],
    'form-4': [2,5]
}

# Create your views here.
def index(request):
    if not 'money' in request.session or 'activities' not in request.session: 
        request.session['money'] = 0
        request.session['activities'] = []
    return render(request, 'index.html') 

#  clears data
def reset(request):
    request.session.flush()
    return redirect('/')

def process(request):
    if request.method == 'GET':
        return redirect('/')
    
    print(request.POST)
    box_name = request.POST['form_name']
    print('box_name:', box_name)

    box = MAP[box_name]
    print('MAP VALUES:', box)

    curr_money = random.randint(box[0], box[1])
    # 10,20 
    print(curr_money)

    result = 'earn'
    message = f'Earned ${curr_money} from the {box_name}'

    # Check if a deduction is needed
    if box_name == 'form-3':
        if random.randint(0, 1) > 0:
            result = 'lose'
            message = f'{curr_money} darn it, losing money'
            curr_money = curr_money * -1

    request.session['money'] += curr_money

    request.session['activities'].append({ 'message': message, 'result': result})


    return redirect('/')

