from django.shortcuts import render, get_object_or_404, redirect

from .models import AskTeam
from .forms import askTeamForm

from taggit.models import Tag
from django.template.defaultfilters import slugify

# Create your views here.
def recruit_view(request):
    posts = AskTeam.objects.all()
    common_tags = AskTeam.tags.most_common()[:4]
    form = askTeamForm(request.POST)
    if form.is_valid():
        newpost = form.save(commit=False)
        newpost.slug = slugify(newpost.title)
        newpost.save()
        form.save_m2m()

        return redirect('/askforteam/req-for-team')
    context = {
        'posts':posts,
        'common_tags':common_tags,
        'form':form,
    }
    return render(request, 'recruit_team/request_team.html', context)

def index(request):
    req = AskTeam.objects.all()
    return render(request, 'recruit_team/index.html', {'requests':req})

def detail_view(request, slug):
    post = get_object_or_404(AskTeam, slug=slug)
    context = {
        'post':post,
    }
    return render(request, 'recruit_team/detail_req.html', context)

def tagged(request, slug):
    tag = get_object_or_404(AskTeam, slug=slug)
    common_tags = AskTeam.tags.most_common()[:4]
    posts = AskTeam.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'common_tags':common_tags,
        'posts':posts,
    }
    return render(request, 'recruit_team/home.html', context)
