from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm



def news_list(request):
    object_list= News.objects.all()
    paginator= Paginator(object_list, 2)
    current_page_number= request.GET.get('page')
    try:
        newss= paginator.page(current_page_number)
    except PageNotAnInteger:
        newss= paginator.page(1)
    except EmptyPage:
        newss= paginator.page(paginator.num_pages)
    return render(request, 'website1/news/list.html', {'newss':newss})

def news_detail(request, year, month, day, news):
    news= get_object_or_404(News, slug= news,
                                  status= 'published',
                                  created__year= year,
                                  created__month= month,
                                  created__day= day)

    comments= news.comments.filter(active= True)
    new_comment= None
    if request.method=='POST':
        comment_form= CommentForm(data= request.POST)
        if comment_form.is_valid():
            new_comment= comment_form.save(commit= False)
            new_comment.news= news
            new_comment.save()
    else:
         comment_form= CommentForm()
    return render(request, 'website1/news/detail.html', {'news':news, 'comments': comments, 'comment_form': comment_form})


