from django.shortcuts import render
from .models import poll
from .forms import pollForm


# Create your views here.
def index(request):
    polls = poll.objects.all()
    return render(request, 'poll/index.html', {'poll':polls} )

#post method , needs form
def newPoll(request):
    if request.method == 'POST':
        form = pollForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'poll/index.html', {})
        else:
            return render(request, 'poll/error.html', {'form':form})
    else:
        form = pollForm()
        return render(request,'poll/createPoll.html',{'form':form})

#test site
def testSite(request , pk):
    polls = poll.objects.get(id=pk)
    return render(request, 'poll/test.html', {'poll':polls} )


#vote

def vote(request , pk):
    polls = poll.objects.get(id=pk)
    polls.votes += 1
    polls.save()
    return render(request, 'poll/test.html', {'poll':polls} )

def downVote(request , pk):
    polls = poll.objects.get(id=pk)
    polls.votes -= 1
    polls.save()
    return render(request, 'poll/test.html', {'poll':polls} )
