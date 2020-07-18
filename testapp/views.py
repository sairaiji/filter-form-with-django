from django.db.models import Q
from django.shortcuts import render
from .forms import ProfileSearchFormSet
from .models import Profile


def search(request):
    profile_list = Profile.objects.all()
    formset = ProfileSearchFormSet(request.POST or None)
    if request.method == 'POST':
        # 全ての入力欄はrequired=Falseなので、必ずTrueになる。
        formset.is_valid()

        # Qオブジェクトを格納するリスト
        queries = []

        # 各フォームの入力をもとに、Qオブジェクトとして検索条件を作っていく
        for form in formset:
            # Qオブジェクトの引数になる。
            # {gender: 1, height__gte: 170} → Q(gender=1, height__gte=170)
            q_kwargs = {}
            gender = form.cleaned_data.get('gender')
            if gender:
                q_kwargs['gender'] = gender

            from_age = form.cleaned_data.get('from_age')
            if from_age:
                q_kwargs['age__gte'] = from_age

            to_age = form.cleaned_data.get('to_age')
            if to_age:
                q_kwargs['age__lte'] = to_age

            from_height = form.cleaned_data.get('from_height')
            if from_height:
                q_kwargs['height__gte'] = from_height

            to_height = form.cleaned_data.get('to_height')
            if to_height:
                q_kwargs['height__lte'] = to_height
            
            from_shape = form.cleaned_data.get('from_shape')
            if from_shape:
                q_kwargs['body_shape__gte'] = from_shape

            to_shape = form.cleaned_data.get('to_shape')
            if to_shape:
                q_kwargs['body_shape__lte'] = to_shape

            job = form.cleaned_data.get('job')
            if job:
                q_kwargs['job'] = job

            from_income = form.cleaned_data.get('from_income')
            if from_income:
                q_kwargs['yearly_income__gte'] = from_income

            to_income = form.cleaned_data.get('to_income')
            if to_income:
                q_kwargs['yearly_income__lte'] = to_income

            holidays = form.cleaned_data.get('holidays')
            if holidays:
                q_kwargs['holidays'] = holidays

            education = form.cleaned_data.get('education')
            if education:
                q_kwargs['education'] = education

            living_in = form.cleaned_data.get('living_in')
            if living_in:
                q_kwargs['living_in'] = living_in
            
            alcohol = form.cleaned_data.get('alcohol')
            if education:
                q_kwargs['alcohol'] = alcohol
            
            cigarette = form.cleaned_data.get('cigarette')
            if cigarette:
                q_kwargs['cigarette'] = cigarette 

            # ここは、そのフォームに入力があった場合にのみ入る。
            # フォームが空なら、q_kwargsは空のままです。
            if q_kwargs:
                q = Q(**q_kwargs)
                queries.append(q)

        if queries:
            # filter(Q(...) | Q(...) | Q(...))を動的に行っている。
            base_query = queries.pop()
            for query in queries:
                base_query |= query
            profile_list = profile_list.filter(base_query)

    context = {
        'profile_list': profile_list,
        'formset': formset,
    }
    return render(request, 'profile_list.html', context)